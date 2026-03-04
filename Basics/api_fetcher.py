import requests

def fetch_users():
    url="https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    # print(response.json())
    if(response.status_code == 200):
        users=response.json()
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}, Company: {user['company']['name']}")
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")
def main():
    fetch_users()   

if __name__ == "__main__":
    main()