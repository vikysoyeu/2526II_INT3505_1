import requests

BASE_URL = "http://127.0.0.1:5000"


# GET all users
response = requests.get(BASE_URL + "/users")
print("All users:", response.json())


# GET single user
response = requests.get(BASE_URL + "/users/1")
print("User 1:", response.json())


# CREATE user
new_user = {"name": "David"}

response = requests.post(BASE_URL + "/users", json=new_user)
print("Created:", response.json())


# DELETE user
response = requests.delete(BASE_URL + "/users/2")
print("Delete result:", response.json())