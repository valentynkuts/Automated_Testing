import requests

# ---- https://reqres.in ----

# Wrong request
# HTTP request method GET
users = 'elephants'
user_id = '88'
url0 = f"https://reqres.in/api/{users}/{user_id}"
response0 = requests.get(url0)
assert response0.status_code == 404, "Status code is not 404"

# HTTP request method GET
users1 = 'users'
user_id1 = '4'
url1 = f"https://reqres.in/api/{users1}/{user_id1}"
response1 = requests.get(url1)
json_res1 = response1.json()
assert response1.status_code == 200, "Status code is not 200"
assert json_res1['data']['id'] == 4
assert json_res1['data']['first_name'] == 'Eve'
assert (json_res1['support']['text']).endswith('costs are appreciated!'), 'Something wrong with text'

assert response1.headers['Content-Type'] == 'application/json; charset=utf-8'
assert response1.headers['Connection'] == 'keep-alive'
assert response1.encoding == 'utf-8'
assert response1.url == url1

# Update data
# HTTP request method PUT
response2 = requests.put(url1, data={"name": "Billy", "job": "Flutter developer"})
json_res2 = response2.json()
assert response2.status_code == 200, "Status code is not 200"

# To get list of keys
keys = list(json_res2)
assert keys[0] == 'name', 'Wrong key'
assert keys[1] == 'job', 'Wrong key'
assert json_res2['name'] == 'Billy', 'Something wrong'
assert json_res2['job'] == 'Flutter developer', 'Something wrong'

# Create data
# HTTP request method POST
url2 = 'https://reqres.in/api/users'
response3 = requests.post(url2, data={"name": "Hello", "job": "World"})
assert response3.status_code == 201, "Status code is not 201"
json_res3 = response3.json()
assert json_res3['name'] == 'Hello', 'Something wrong'
assert json_res3['job'] == 'World', 'Something wrong'
