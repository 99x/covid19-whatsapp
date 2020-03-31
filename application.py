from flask import Flask, request
from flask_caching import Cache
import i18n
from twilio.twiml.messaging_response import MessagingResponse

import requests 
import menu
import info
from covid_stats import Stats
from repositories.analytics_repository import AnalyticsRepository


application = Flask(__name__)


# Caching related configurations
config = {
    "DEBUG": True,          
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 300
}
application.config.from_mapping(config)
cache = Cache(application)
stats = Stats(cache)

# Setting i18n file format
i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append('translations')

# Google Analytics
analytics_repo = AnalyticsRepository()

TAMIL = 'tm'
SINHALA = 'sl'
ENGLISH = 'en'

@application.route('/redirect', methods=['POST'])
def redirect():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(info.get_redirect_msg())
    return str(resp)

@application.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    print(request.values)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    

    if '1' == incoming_msg:
        msg.body(menu.get_main_menu(ENGLISH))
        responded = True
    if '2' == incoming_msg:
        msg.body(menu.get_main_menu(SINHALA))
        responded = True
    if '3' == incoming_msg:
        msg.body(menu.get_main_menu(TAMIL))
        responded = True

    if '4' == incoming_msg:
        msg.body(stats.get_numbers(ENGLISH))
        responded = True
    if '5' == incoming_msg:
        msg.body(info.get_protect_info(ENGLISH))
        responded = True
    if '6' == incoming_msg:
        msg.body(info.get_travel_info(ENGLISH))
        responded = True
    if '7' == incoming_msg:
        msg.body(info.get_questions_info(ENGLISH))
        responded = True
    if '8' == incoming_msg:
        msg.body(info.get_latest_news(ENGLISH))
        responded = True


    if '9' == incoming_msg:
        msg.body(stats.get_numbers(SINHALA))
        responded = True
    if '10' == incoming_msg:
        msg.body(info.get_protect_info(SINHALA))
        responded = True
    if '11' == incoming_msg:
        msg.body(info.get_travel_info(SINHALA))
        responded = True
    if '12' == incoming_msg:
        msg.body(info.get_questions_info(SINHALA))
        responded = True
    if '13' == incoming_msg:
        msg.body(info.get_latest_news(SINHALA))
        responded = True

    if '14' == incoming_msg:
        msg.body(stats.get_numbers(TAMIL))
        responded = True
    if '15' == incoming_msg:
        msg.body(info.get_protect_info(TAMIL))
        responded = True
    if '16' == incoming_msg:
        msg.body(info.get_travel_info(TAMIL))
        responded = True
    if '17' == incoming_msg:
        msg.body(info.get_questions_info(TAMIL))
        responded = True
    if '18' == incoming_msg:
        msg.body(info.get_latest_news(TAMIL))
        responded = True

    if not responded:
        msg.body(menu.get_welcome_menu())
        analytics_repo.add_event(request.values['From'])

    return str(resp)

