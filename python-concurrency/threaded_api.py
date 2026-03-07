import requests
import threading
import time

urls=[
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

def fetch(url):
    response=requests.get(url)
    print(response.json()['title'])

threads=[]

start=time.time()

for url in urls:
    thread=threading.Thread(target=fetch, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
end=time.time()

print("Execution time:", end-start)