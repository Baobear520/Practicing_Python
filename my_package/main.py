# Что происходит при
# string = ‘foo’
# string = string + ‘bar’
    # Ссылка переменной string указывает на новое значение
    # Строка string изменяется
    # Строки не изменяются, поэтому вылетит ошибка
    # Нельзя создавать переменные с именем string - ошибка
#Когда срабатывает finally в блоке try/except
#Какой тип у  *args в аргументах функции?
#Что такое магические методы в Python?
    # Это методы класса
    # Это декораторы, которые декорируют методы внутри класса
    # Это методы, которые позволяют экземплярам класса взаимодействовать со встроенными функциями и операторами языка
    # Это облачные функции
#Что будет выведено при print(range(0, 2))
#Могут ли декораторы оборачивать декоратор?
#Что такое Meta?
    # Это родительский класс от которого можно наследоваться
    # Это классы, которые создают классы
    # Это класс наследник, который может наследоваться от родительского класса
    # Это экземпляры классов
#Garbage Collector в питоне:
    # Это алгоритм для подсчета ссылок
    # Это алгоритм,  который чистит память в питоне
    # Это процесс, для освобождения памяти, который выполняет два алгоритма
#Как написать свой класс работающий с контекстом with
    # Никак
    # Реализовать методы start/end
    # Реализовать методы enter/exit
    # В методе init открыть файл
#Каких из этих методов объекта string нет в Python?
# count
# find
# new
# index
# join
# zip
# split
# isalnum
# Correct answer
# new
# zip


def move_zeros(my_array: list):
    # list_of_zeroes = []
    # for num in my_array:
    #     if num == 0:
    #         my_array.remove(num)
    #         list_of_zeroes.append(0)
    # my_array.extend(list_of_zeroes)
    # return my_array
    for num in my_array[::-1]:
        if my_array[-1] == 0:
            pass
        if num == 0:
            my_array.remove(num)
            my_array.append(0)
    return my_array

if __name__ == "__main__":
    move_zeros([1,1,0,3,0,4,5,0])
