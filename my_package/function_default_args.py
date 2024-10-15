x = 4

def some_func(el,lst=[]):
    lst.append(el)

my_list = [1]
some_func(5)
some_func(5)
some_func(5, lst=my_list)
some_func(5)
print(my_list)