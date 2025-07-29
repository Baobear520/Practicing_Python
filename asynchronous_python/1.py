"""Task:
Write an async Python script that fetches data from 3 different mock API endpoints concurrently,
processes the results, and returns a combined output.
* run in on a schedule
"""


import asyncio
from asyncio import CancelledError

from aiohttp import ClientSession, ClientResponseError, ClientConnectorDNSError


async def fetch_data(url):
    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return response.host
        except ClientConnectorDNSError as e:
            print(f"DNS error occurred: {e}")
        except ClientResponseError as e:
            print(f"Error while parsing {url}: status {e.status}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


async def run_tasks(urls_lst: list, task):
    tasks = [task(url) for url in urls_lst]
    return await asyncio.gather(*tasks,return_exceptions=True)



async def scheduler(delay, job, *args, **kwargs):
    while True:
        try:
            print(f"Starting the script...")
            result = await job(*args,**kwargs)
            print(result)
            print(f"Restarting in {delay} sec")
            await asyncio.sleep(delay)
        except CancelledError:
            print(f"Job {job.__name__} has been cancelled")
            raise


if __name__ == "__main__":
    delay = 5
    urls = [
        "https://webscraper.io/test-sites/e-commerce/allinone",
        "https://webscraper.io/test-sites/e-commerce/static",
        "https://webscraper.io/test-sites/tables"
        ]
    try:
        asyncio.run(
            scheduler(delay,run_tasks,urls,fetch_data)
        )
    except KeyboardInterrupt:
        print("Script interrupted...")