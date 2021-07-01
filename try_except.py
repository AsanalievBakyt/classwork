
import requests

url = 'http://192.168.2.133:8000/api/products'

x = requests.get(url).json()
print(x)

def func1(data):
    from math import inf
    max_price_title = None
    min_price_title = None
    min_price = inf
    max_price = 0
    for value in x:
        price = value['price']
        if price > max_price:
            max_price = price
            max_price_title = value['title']
        elif 0 < price < min_price:
            min_price = price
            min_price_title = value['title']

    print(max_price_title,max_price, min_price_title, min_price)
print(func1(x))

d1 = {
    'title': 'bakyt',
    'image' : 'None',
    'price': 200000000
}

a = requests.post(url,d1)



