from flask import Flask, request
from flask_caching import Cache

from twilio.twiml.messaging_response import MessagingResponse

import requests 
import menu

from repositories.disease_data_repository import DiseaseDataRepository

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

application = Flask(__name__)

application.config.from_mapping(config)
cache = Cache(application)

TAMIL = 3
SINHALA = 2
ENGLISH = 1

@application.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    
    
    

    if '1' == incoming_msg:
        msg.body(menu.get_english_menu())
        responded = True
    if '2' == incoming_msg:
        msg.body(menu.get_sinhala_menu())
        responded = True
    if '3' == incoming_msg:
        msg.body(menu.get_tamil_menu())
        responded = True

    if '4' == incoming_msg:
        msg.body(get_stats(ENGLISH))
        responded = True
    if '5' == incoming_msg:
        msg.body(get_news(ENGLISH))
        responded = True
    if '6' == incoming_msg:
        msg.media(get_graph(ENGLISH))
        responded = True

    if '7' == incoming_msg:
        msg.body(get_stats(SINHALA))
        responded = True
    if '8' == incoming_msg:
        msg.body(get_news(SINHALA))
        responded = True
    if '9' == incoming_msg:
        msg.media(get_graph(SINHALA))
        responded = True

    if '10' == incoming_msg:
        msg.body(get_stats(TAMIL))
        responded = True
    if '11' == incoming_msg:
        msg.body(get_news(TAMIL))
        responded = True
    if '12' == incoming_msg:
        msg.media(get_graph(TAMIL))
        responded = True

    if not responded:
        msg.body(menu.get_welcome_menu())
    return str(resp)

def get_stats(lang):
    data_repository = DiseaseDataRepository(cache= cache)
    data = data_repository.get_disease_data()
    stats = f"\n*Globally* \n{data['global_confirmed']} confirmed \n{data['global_deaths']} deaths \n\n*Sri Lanka* \n{data['sl_confirmed']} confirmed \n{data['sl_deaths']} deaths"
    return stats

def get_news(lang):
    news = str(lang) + '\n*Latest news* \n - 5 new cases reported since yesterday http://news.lk/news'
    return news

def get_graph(lang):
    graph_url= 'https://blog.watchdog.paladinanalytics.com/content/images/2020/03/image-5.png'
    return graph_url
    