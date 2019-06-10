import requests
url = "https://www.youtube.com/watch?v=hNbv1EIUW6g&list=PLpOqH6AE0tNguX5SG8HpcD3lfmzWrIn9n&index=5"
if __name__ == "__main__":
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        response_json = response.json()
