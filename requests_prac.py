import requests

params = {
    "name": "Himanshu",
    "age": 21
}

# res = requests.get("https://httpbin.org/get", params = params)
# print(res.url)

#To handle status codes
# res = requests.get("https://httpbin.org/status/404")
# if res.status_code == 404:
#     print("Not FOund")
# else:
#     print(res.status_code)

res = requests.get("https://httpbin.org/get", params = params)
print()

# print(res.text)