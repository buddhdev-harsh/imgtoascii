import urllib.request
import requests
from bs4 import BeautifulSoup

# url = ''
headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
url = 'https://www.myntra.com/tshirts/difference-of-opinion/difference-of-opinion-men-mustard-yellow-solid-round-neck-t-shirt-with-printed-detailing/10005885/buy'
req = requests.get(url) 
bsobj = BeautifulSoup(req.text , 'html.parser')


find_title = bsobj.find("h1",{"class":"pdp-name"})
print(find_title)