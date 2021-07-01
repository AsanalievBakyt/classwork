

import requests


class MyRequests():

    def __init__(self,url):
        self.url = url

    def get(self):
        responce = requests.get(self.url).json()
        print(responce)

    def post(self, data):
        responce = requests.post(self.url, data)
        print(responce)

    def put(self, data, id):
        url = self.url + str(id) +'/'
        responce = requests.put(url,data)
        print(responce.json())

    def delete(self, id):
        url = self.url + str(id) + '/'
        responce = requests.delete(url)
        print(responce.json())
a = MyRequests('http://192.168.2.133:8000/api/v1/magnit/')

# a.get()
data = {'name':'cap', 'price': 120, 'score': 5, 'author': 'Nike', 'owner': '7'}
# a.post(data)
# a.put(data,5)
a.delete(7)
a.delete(8)
a.delete(9)