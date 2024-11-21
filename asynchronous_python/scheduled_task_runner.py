import asyncio


async def my_func(x,y):
    print(x + y)


async def job():
    task = asyncio.create_task(my_func(3,2))
    return await task

async def scheduler():
    while True:
        try:
            await job()
            print(f"Restarting in {delay} seconds")
            await asyncio.sleep(delay)
        except asyncio.CancelledError:
            print("Script terminated")
            break

delay = 3
asyncio.run(scheduler())



