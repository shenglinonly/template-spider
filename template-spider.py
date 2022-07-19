import requests

url = ''

headers = {

}

response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)
