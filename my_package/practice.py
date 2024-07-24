import asyncio
from random import randint

async def hello():
    await asyncio.sleep(1)
    print("Hello",end=" ")

async def world():
    for char in "World":
        await asyncio.sleep(randint(3,4))
        print(char,end="",flush=True)

async def do_smth_else():
    print(sum(range(5)),end=" ")
    
async def main():
    await asyncio.gather(hello(), world(),do_smth_else())
    
if __name__ == '__main__':
    asyncio.run(main())