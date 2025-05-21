import requests

# api_url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(api_url)
# print(response.headers)  # 200
# usuarios = response.json()
# print(usuarios[0:3])

# for usuario in usuarios:
#     print(usuario["id"], usuario["name"])
#     print(usuario["address"]["street"], usuario["address"]["city"])
#     print(usuario["company"]["name"])
#     print(usuario["email"])
#     print(usuario["phone"])
#     print(usuario["website"])
#     print(" ")

# api_url = "https://jsonplaceholder.typicode.com/users"
# user = {
#     "name": "Juan Perro"
# }
# response = requests.post(api_url, json=user)
# print(response.status_code)

## CABECERAS
api_url = "https://jsonplaceholder.typicode.com/users"
apikey = "tu_api_key_aqui"
headers = {
    "Authorization": f"Bearer {apikey}"
}
response = requests.get(api_url, headers=headers)
print(response.status_code)
