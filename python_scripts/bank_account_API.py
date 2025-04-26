import hashlib
from typing import Optional, Dict, Any
import psycopg2
from psycopg2 import OperationalError, sql


class DB:
    def __init__(self, db_string: str):
        self.db_string = db_string
        self.conn = None
        self.connect()

    def connect(self) -> None:
        """Устанавливает соединение с базой данных."""
        try:
            self.conn = psycopg2.connect(self.db_string)
            print(f"Connected to database")
        except OperationalError as e:
            print(f"Connection error: {e}")
            raise

    def execute_query(self, query: str, params: tuple = None) -> Optional[Dict[str, Any]]:
        """Выполняет SQL-запрос и возвращает результат."""
        if not self.conn:
            raise ConnectionError("Database connection is not established")

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                if cursor.description:  # Для SELECT запросов
                    columns = [desc[0] for desc in cursor.description]
                    result = cursor.fetchone()
                    return dict(zip(columns, result)) if result else None
                self.conn.commit()
                return None
        except OperationalError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return None

    def close(self) -> None:
        """Закрывает соединение с базой данных."""
        if self.conn:
            self.conn.close()
            print("Database connection closed")


class BankAccount:
    def __init__(self, db: DB, pin: str):
        self.db = db
        self._pin = pin
        self.user_data = self._authenticate_user()

        if not self.user_data:
            raise ValueError("Authentication failed")

        self._currency = self.user_data.get('currency', 'USD')
        self._current_deposit = float(self.user_data.get('current_deposit', 0.0))
        self._max_deposit = float(self.user_data.get('max_deposit', 100000))
        self._max_withdrawal = float(self.user_data.get('max_withdrawal', 50000))

    def _authenticate_user(self) -> Optional[Dict[str, Any]]:
        """Аутентификация пользователя по PIN-коду."""
        try:
            hashed_pin = hashlib.sha3_256(self._pin.encode()).hexdigest()
            query = sql.SQL("SELECT * FROM users WHERE password_hash = %s")
            return self.db.execute_query(query, (hashed_pin,))
        except Exception as e:
            print(f"Authentication error: {e}")
            return None

    def _validate_amount(self, amount: float, operation_type: str) -> None:
        """Общая валидация для операций."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if operation_type == 'deposit' and amount > self._max_deposit:
            raise ValueError(f"Cannot deposit more than {self._max_deposit} {self._currency}.")

        if operation_type == 'withdraw':
            if amount > self._max_withdrawal:
                raise ValueError(f"Cannot withdraw more than {self._max_withdrawal} {self._currency}.")
            if amount > self._current_deposit:
                raise ValueError(f"Insufficient funds. Current balance: {self._current_deposit}")

    def _execute_operation(self, amount: float, operation: str) -> bool:
        """Общая логика выполнения операций."""
        try:
            self._validate_amount(amount, operation)

            if operation == 'deposit':
                self._current_deposit += amount
            else:
                self._current_deposit -= amount

            # Обновляем баланс в базе данных
            update_query = sql.SQL("""
                UPDATE accounts 
                SET current_deposit = %s 
                WHERE user_id = %s
            """)
            params = (self._current_deposit, self.user_data['user_id'])

            if not self.db.execute_query(update_query, params):
                raise RuntimeError("Failed to update account balance")

            print(f"{operation.capitalize()} of {amount} {self._currency} successful. "
                  f"New balance: {self._current_deposit}")
            return True

        except (ValueError, RuntimeError) as e:
            print(f"Operation failed: {e}")
            return False

    def deposit(self, amount: float) -> bool:
        """Депозит средств на счет."""
        return self._execute_operation(amount, 'deposit')

    def withdraw(self, amount: float) -> bool:
        """Снятие средств со счета."""
        return self._execute_operation(amount, 'withdraw')

    def get_balance(self) -> float:
        """Возвращает текущий баланс."""
        return self._current_deposit


if __name__ == "__main__":
    try:
        # Инициализация подключения к БД
        db = DB('postgresql://user:password@localhost/bank')

        # Создание банковского аккаунта
        account = BankAccount(db, "1234")

        # Операции с аккаунтом
        account.deposit(1000)
        account.withdraw(500)
        print(f"Current balance: {account.get_balance()} {account._currency}")

    except Exception as e:
        print(f"Application error: {e}")
    finally:
        if 'db' in locals():
            db.close()