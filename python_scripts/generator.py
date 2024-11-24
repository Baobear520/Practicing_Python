def my_generator(iterable,return_even=True):
    for index,item in enumerate(iterable):
        if (index % 2 == 0) == return_even:
            yield item



gen = my_generator([1,2,3,4],return_even=False)
# print(next(gen))
# print(next(gen))
# print(next(gen))


def aggr_aver(iterable):
    total = 0
    for pos, num in enumerate(iterable,start=1):
        total = total + num
        yield total / pos



if __name__ == "__main__":
    gen_obj = aggr_aver([2, 3, 4, 5])
    for obj in gen_obj:
        print(obj)


