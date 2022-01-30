from urllib.request import urlopen
import json

class Apidata:
    
    def __init__(self,stock):
        self.stock=stock
        self.Apikey=''
        self.url='https://financialmodelingprep.com/api/v3/historical-price-full/'+self.stock+'?apikey='+self.Apikey
        
    def apiJsonResponse(self):
        response = urlopen(self.url)
        data_json = json.loads(response.read())
        return data_json
        
        

