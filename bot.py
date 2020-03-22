from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from repositories.disease_data_repository import DiseaseDataRepository

app = Flask(__name__)

TAMIL = 3
SINHALA = 2
ENGLISH = 1

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    data_repository = DiseaseDataRepository()
    print(data_repository.get_disease_data(data=1))
    if '1' in incoming_msg:
        msg.body(get_stats(ENGLISH))
        responded = True
    if '2' in incoming_msg:
        msg.body(get_news(ENGLISH))
        responded = True
    if '3' in incoming_msg:
        msg.media(get_graph(ENGLISH))
        responded = True

    if '4' in incoming_msg:
        msg.body(get_stats(SINHALA))
        responded = True
    if '5' in incoming_msg:
        msg.body(get_news(SINHALA))
        responded = True
    if '6' in incoming_msg:
        msg.media(get_graph(SINHALA))
        responded = True

    if '7' in incoming_msg:
        msg.body(get_stats(TAMIL))
        responded = True
    if '8' in incoming_msg:
        msg.body(get_news(TAMIL))
        responded = True
    if '9' in incoming_msg:
        msg.media(get_graph(TAMIL))
        responded = True

    if not responded:
        msg.body(get_menu())
    return str(resp)

def get_stats(lang):
    stats = '*Globally* \n266 073 confirmed \n11 184 deaths \n\n*Sri Lanka* \n80 confirmed \n0 deaths'
    return stats

def get_news(lang):
    news = '*Latest news* \n - 5 new cases reported since yesterday http://news.lk/news'
    return news

def get_graph(lang):
    graph_url= 'https://blog.watchdog.paladinanalytics.com/content/images/2020/03/image-5.png'
    return graph_url

def get_menu():
    menu = '''*A project by UNDP and 99X*

        You can get latest Sri Lankan covid-19 information here. 
        Reply with the number: 

        *in English*
        1. Latest numbers
        2. Related news
        3. Case graph
        
        *සිංහලෙන්*
        4. අලුත්ම සංක්‍යා 
        5. නවතම පුවත් 
        6. ප්‍රස්ථාර දත්ත

        *தமிழில்*
        7. சமீபத்திய எண்கள்
        8. சமீபத்திய செய்தி
        9. வரைபடத் தரவு
        
        '''
    return menu