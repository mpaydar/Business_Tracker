import requests

url = "https://api.yelp.com/v3/businesses/search"
token = "kNIRAZWPcyNLjG6XojNCSBZk1J6qZCAeA-4-jzBlpYKdVFUjydm5SVGFqVuTPSfkkYlidORZkcPVa8axsbM2ErZzQ9buHHlzgn4Q2viHQ4dcYPJqOKIaRHJFKRJzZnYx"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())