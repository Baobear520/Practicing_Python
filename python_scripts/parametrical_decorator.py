import functools

def my_decor(param: int):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            for _ in range(param):
                func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


def say_my_name(name: str)-> None:
    print(name.upper(), end=' ')

my_decor(3)(say_my_name)('dima') # outer_wrapper(say_my_name) inner_wrapper('dima')


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