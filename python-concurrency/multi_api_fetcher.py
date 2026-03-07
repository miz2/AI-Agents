import asyncio
import aiohttp
import time

# Generate 10 API URLs
urls = [
    f"https://jsonplaceholder.typicode.com/posts/{i}"
    for i in range(1, 11)
]

# Async function to fetch API data
async def fetch_post(session, url):
    async with session.get(url) as response:
        data = await response.json()

        post_id = data["id"]
        title = data["title"]

        print(f"Post ID: {post_id}")
        print(f"Title: {title}\n")


# Main async function
async def main():
    async with aiohttp.ClientSession() as session:

        tasks = []

        # Create tasks for each API
        for url in urls:
            task = fetch_post(session, url)
            tasks.append(task)

        # Run all tasks concurrently
        await asyncio.gather(*tasks)


# Measure execution time
start = time.time()

asyncio.run(main())

end = time.time()

print("Execution time:", end - start)