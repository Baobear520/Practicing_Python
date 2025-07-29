"""
Task:
Build an async web scraper that uses threads for I/O (download) and processes for CPU-heavy parsing.

Key Concepts Tested:

Combining asyncio with executors (run_in_executor)

Knowing when to switch between paradigms
"""
import asyncio
import concurrent.futures
import time

import requests


def blocking_io(url):
    pass

async def scraper(urls):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, blocking_io, url) for url in urls]
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "https://www.avito.ru/all/nedvizhimost",
        "https://www.avito.ru/garage?utm_source=main_mini_menu",
        "https://www.avito.ru/sankt-peterburg/transport?cd=1"
    ]
    asyncio.run(scraper(urls))