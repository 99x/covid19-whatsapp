import yaml
import requests

class DiseaseDataRepository:
  DATA_SOURCE = 'hpb'
  API_RESPONSE_CACHE_KEY = 'api_response_cache_key'
  API_RESPONSE_SUCCESS_CACHE_KEY = 'api_response_success_cache_key'
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
    cached_data = self.cache.get(self.API_RESPONSE_CACHE_KEY)
    errorResponse = False

    if cached_data == None:

      try:
        response =  requests.get(url= self.url_collection[self.COVID_DATA_URL])
        response.raise_for_status()
        response_data = response.json()['data']
        self.cache.set(self.API_RESPONSE_CACHE_KEY, response_data, timeout = 60)
        self.cache.set(self.API_RESPONSE_SUCCESS_CACHE_KEY, response_data, timeout = 3600)    
      except requests.exceptions.HTTPError as errh:
        errorResponse = True
        print ("Error in getting data from health.gov.lk API: Type Http:",errh)
      except requests.exceptions.ConnectionError as errc:
        errorResponse = True
        print ("Error in getting data from health.gov.lk API: Type Connection:",errc)
      except requests.exceptions.Timeout as errt:
        errorResponse = True
        print ("Error in getting data from health.gov.lk API: Type Timeout:",errt)
      except requests.exceptions.SSLError as errs:
        errorResponse = True
        print ("Error in getting data from health.gov.lk API: Type SSLError:",errs)
      except requests.exceptions.RequestException as err:
        errorResponse = True
        print ("Error in getting data from health.gov.lk API: Type RequestException:",err)
        
      if errorResponse == True:
        response_data = self.cache.get(self.API_RESPONSE_SUCCESS_CACHE_KEY)
        print ("Responding from last succesful response")

    else:
      response_data = cached_data
    
    formatted_object = {
      'global_new_cases': response_data['global_new_cases'], 
      'global_confirmed': response_data['global_total_cases'], 
      'global_deaths': response_data['global_deaths'],
      'global_new_deaths': response_data['global_new_deaths'],
      'global_recovered': response_data['global_recovered'],
      'sl_confirmed': response_data['local_total_cases'],
      'sl_deaths': response_data['local_deaths'],
      'sl_new_deaths': response_data['local_new_deaths'],
      'sl_new': response_data['local_new_cases'],
      'sl_hospitals': response_data['local_total_number_of_individuals_in_hospitals'],
      'sl_recovered': response_data['local_recovered'],
      'last_updated': response_data['update_date_time']
    }
    return formatted_object



