import requests

api_key = "21eaf0f3ddae403e94624fbcc6007664"

url = 'https://newsapi.org/v2/top-headlines?' \
       'country=us&sortBy=publishedAt' \
       'apiKey=21eaf0f3ddae403e94624fbcc6007664'

r = requests.get(url)

content = r.text

print(content)