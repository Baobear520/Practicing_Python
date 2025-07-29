"""
Multithreading for I/O-bound Tasks
Task:
*Download 10 images from URLs concurrently using threads, ensuring thread-safe error handling.*

Key Concepts Tested:

threading module or concurrent.futures.ThreadPoolExecutor

Thread safety (e.g., shared resources, locks)

I/O-bound vs CPU-bound tasks
"""

import threading
from asyncio import timeout

import requests
from queue import Queue
from requests import HTTPError
from requests.exceptions import ConnectionError

from concurrent.futures import ThreadPoolExecutor, as_completed


def crawler(url,timeout):
    try:
        response = requests.get(url,timeout=timeout)
        print(f"{url}: response status {response.status_code}")
        if response.status_code != '200':
            response.raise_for_status()
        print(f"Connected to {url}.")
        return response.text[0]
    except ConnectionError:
        print(f"Couldn't connect to {url}")
    except HTTPError:
        print(f"Error parsing data from {url}")

def producer(q: Queue, data: list):
    for el in data:
        q.put(el)
        print(f"Put {el} in the queue.")

def consumer(q: Queue):
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

def main():
    links = [
        "https://python.org",
        "https://docs.python.org",
        "https://peps.python.org",
    ]
    q = Queue()
    threading.Thread(target=producer, args=(q,links)).start()
    threading.Thread(target=consumer, args=(q,), daemon=True).start()
    q.join()  # Ждём завершения всех задач



def run_in_threads_pool(task):
    links = [
        "https://python.org",
        "https://docs.python.org",
        "https://peps.python.org",
        "https://www.google.com/"
    ]

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(task, url, timeout): url for url in links}
        for num, future in enumerate(as_completed(futures),start=1):
            data = future.result()
            print(f"Done task {num}")


if __name__ == "__main__":
    timeout = 5
    main()




