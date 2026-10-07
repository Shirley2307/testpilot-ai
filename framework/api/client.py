import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint,headers=None):
        url = self.base_url + endpoint
        response = requests.get(url)
        return response

    def post(self, endpoint, data,headers=None):
        url = self.base_url + endpoint
        response = requests.post(url, json=data,headers=headers)
        return response

    def put(self, endpoint, data,headers=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=data,headers=headers)
        return response

    def delete(self,endpoint,headers=None):
        url = self.base_url + endpoint
        response = requests.delete(url,headers=headers)
        return response