import asyncio



async def future_func(fut,delay, value):
    print(f"I am {future_func().__name__} ")
    await asyncio.sleep(delay)
    print(f"{future_func().__name__} is done")
    fut.set_result(delay*value)


async def my_func(delay):
    print(f"I am {my_func.__name__} ")
    await asyncio.sleep(delay)
    print(f"{my_func.__name__} is done")
    return delay // 2

async def i_need_future(fut):
    print(f"Result is {fut}!")


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(my_func(2))
        print(task1.result())




    # loop = asyncio.get_running_loop()
    # fut = loop.create_future()
    # await loop.create_task(f1(fut,5, 2))
    #
    # print(await fut+10)
        #asyncio.Task.cancel(task2)




if __name__=="__main__":
    asyncio.run(main())

