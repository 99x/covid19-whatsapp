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
      response_data = response.json()['data']
      self.cache.set(self.COVID_DATA_URL, response_data, timeout = 60)
    else:
      response_data = cached_data
    
    formatted_object = {
      'global_confirmed': response_data['global_total_cases'], 
      'global_deaths': response_data['global_deaths'],
      'sl_confirmed': response_data['local_total_cases'],
      'sl_deaths': response_data['local_deaths'],
      'sl_new': response_data['local_new_cases'],
      'sl_hospitals': response_data['local_total_number_of_individuals_in_hospitals'],
      'sl_recovered': response_data['local_recovered']
    }
    return formatted_object



