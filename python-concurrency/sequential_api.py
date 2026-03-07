import requests
import time 

urls=[
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

start=time.time()
for url in urls:
    response=requests.get(url)
    print(response.json()['title'])

end=time.time()

print("Execution time:", end-start)