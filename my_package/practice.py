import asyncio
from random import randint

async def hello():
    await asyncio.sleep(3)
    print("Hello",end=" ")

async def world():

    for char in "World":
        await asyncio.sleep(randint(1,2))
        print(char,end="",flush=True)

async def do_smth_else():
    print(sum(range(5)),end=" ")
    
async def main():
    await hello()
    await world()
    await do_smth_else()
    
if __name__ == '__main__':
    asyncio.run(main())