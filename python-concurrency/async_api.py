import asyncio
import aiohttp
import time

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def fetch(session,url):
    async with session.get(url) as response:
        data = await response.json()
        print(data['title'])

async def main():
    async with aiohttp.ClientSession() as session:
        tasks=[]
        for url in urls:
            tasks.append(fetch(session,url))
        await asyncio.gather(*tasks)

start=time.time()
asyncio.run(main())
end=time.time()
print("Execution time:", end-start)    