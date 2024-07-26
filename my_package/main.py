
def my_decorator(arg):
    def actual_decorator(function):
        def wrapper(*args,**kwargs):
            # здесь можно использовать arg
            result = function(*args,**kwargs)  # вызов оригинальной функции
            dec_res = arg * result
            print(f"Sum of integers from 0 to {args[0] - 1} multipled by {arg} is {dec_res}")
        return wrapper
        
    return actual_decorator

#multiplies the result
@my_decorator(3)
def sum_of_ints(x:int):
    return sum(range(x))

sum_of_ints(10)