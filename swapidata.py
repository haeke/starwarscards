import requests
class Swapidata():
    def __init__(self, data):
        self.data = data

    def get_data(self):
        #point to the URL
        api_url = 'http://swapi.co/api/people/'
        #get the information
        request_data = requests.get(api_url)
        #return the data in json format
        return request_data.json()
