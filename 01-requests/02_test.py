import requests

response = requests.get('https://www.sina.com.cn/')

with open('files/sina.html', 'wb') as f:
    f.write(response.content)