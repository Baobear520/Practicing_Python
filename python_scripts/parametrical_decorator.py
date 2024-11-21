import functools


def logcall(params=True, result=True):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Функция: {func.__name__}")
            if params:
                print(f"Параметры: {args}, {kwargs}")
        
            try:
                res = func(*args, **kwargs)
                if result:
                    print(f"Результат: {res}")
                return res
            except Exception as e:
                print(f"Исключение: {type(e).__name__}")
                raise 	     
        return wrapper
    return my_decorator

@logcall(result=False)
def div(x, y):
   return x // y
div(10, 0)