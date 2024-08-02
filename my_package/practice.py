my_list = [1,2,3]
my_tuple = 1,2,3
my_dict = {'a':1,'b':2}
my_set = {1,2,3}
my_string = "abc"

def my_gen(limit:int):
    count = 0
    while count <= limit:
        yield ("woo"*(count+1))
        count += 1

gen_obj = my_gen(5)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))