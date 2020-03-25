from flask import Flask, request
from flask_caching import Cache
import i18n
from twilio.twiml.messaging_response import MessagingResponse

import requests 
import menu
import info
from covid_stats import Stats


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

TAMIL = 'tm'
SINHALA = 'sl'
ENGLISH = 'en'


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
        msg.body(stats.get_numbers(SINHALA))
        responded = True
    if '7' == incoming_msg:
        msg.body(info.get_protect_info(SINHALA))
        responded = True

    if '8' == incoming_msg:
        msg.body(stats.get_numbers(TAMIL))
        responded = True
    if '9' == incoming_msg:
        msg.body(info.get_protect_info(TAMIL))
        responded = True

    if not responded:
        msg.body(menu.get_welcome_menu())
    return str(resp)

