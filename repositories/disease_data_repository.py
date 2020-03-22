import yaml
import requests

class DiseaseDataRepository:
  DATA_SOURCE = 'hpb'
  COVID_DATA_URL = 'covid_data_url'

  url_collection = {}
  cache = None
  def __init__(self, cache):
    self.cache = cache

    with open("config.yml", 'r') as stream:
      try:
        self.url_collection = yaml.safe_load(stream)[self.DATA_SOURCE]
        print(self.url_collection)
      except yaml.YAMLError as exc:
        print(exc)


  
  def get_disease_data(self):
    cached_data = self.cache.get(self.COVID_DATA_URL)
    
    if cached_data == None:
      response = requests.get(url= self.url_collection[self.COVID_DATA_URL])
      response_data = response.json()
      self.cache.set(self.COVID_DATA_URL, response_data, timeout = 30)
    else:
      response_data = cached_data
    
    print(response_data)
    return "ok"



