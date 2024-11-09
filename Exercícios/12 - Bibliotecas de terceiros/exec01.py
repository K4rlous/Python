# Biblioteca Requests

"Util para fazer requisições HTTP. Ela simplifica a interação com APIs e servidores web, permitindo que você envie e receba dados"

# Instalamos ela usando o gerenciador de pacotes pip com o comando:
# pip install requests

import requests

# Os outputs de cada operação foram "individualizados"

"Fazendo uma Requisição GET: A requisição GET é usada para recuperar dados de um servidor."

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)  # Código de status da resposta (200, 404, etc.)
print(response.json())       # Conteúdo da resposta em formato JSON


"Fazendo uma Requisição POST: A requisição POST é usada para enviar dados ao servidor."

payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(response.status_code)  # Código de status da resposta (201, etc.)
print(response.json())       # Conteúdo da resposta em formato JSON


"Passando Parâmetros em uma Requisição GET: Você pode passar parâmetros na URL da requisição GET."

params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.status_code)  # Código de status da resposta
print(response.json())       # Conteúdo da resposta filtrado por userId


"Enviando Cabeçalhos em Requisições: Você pode adicionar cabeçalhos às suas requisições para personalizar o comportamento do servidor."

headers = {'Authorization': 'Bearer seu_token'}
response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
print(response.status_code)  # Código de status da resposta
print(response.json())       # Conteúdo da resposta


"Tratamento de Erros: Requests facilita o tratamento de erros através de exceções."

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()  # Levanta exceção para códigos de status HTTP de erro
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
else:
    print(response.json())  # Conteúdo da resposta se não houve erro
