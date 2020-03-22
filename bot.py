from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

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

    if '1' == incoming_msg:
        msg.body(get_english_menu())
        responded = True
    if '2' == incoming_msg:
        msg.body(get_sinhala_menu())
        responded = True
    if '3' == incoming_msg:
        msg.body(get_tamil_menu())
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
        msg.body(get_welcome_menu())
    return str(resp)

def get_stats(lang):
    stats = str(lang) + '\n*Globally* \n266 073 confirmed \n11 184 deaths \n\n*Sri Lanka* \n80 confirmed \n0 deaths'
    return stats

def get_news(lang):
    news = str(lang) + '\n*Latest news* \n - 5 new cases reported since yesterday http://news.lk/news'
    return news

def get_graph(lang):
    graph_url= 'https://blog.watchdog.paladinanalytics.com/content/images/2020/03/image-5.png'
    return graph_url

def get_welcome_menu():
    menu = '''
    *Welcome to COVID-19 bot made by UNDP, ICTA and 99X*
    
    * You can get information regarding the current outbreak of coronavirus in Sri Lanka.
    * ශ්‍රී ලංකාවේ වර්තමාන COVID-19 වෛරසය පැතිරීම පිළිබඳ තොරතුරු මෙතැනින් ලබා ගත හැකිය.
    * இலங்கையில் கோவிட் -19 வெடித்தது குறித்த தகவல்களை இங்கே பெறலாம்.

    1. Provide data in English
    2. සිංහල භාෂාවෙන් දත්ත දෙන්න 
    3. தரவை தமிழில் கொடுங்கள்
    
    .
        '''
    return menu

def get_english_menu():
    menu = '''
    *Enter the menu number of the information you require*\n
    4. Latest numbers
    5. Related news
    6. Graph data
    '''
    return menu

def get_sinhala_menu():
    menu = '''
    *ඔබට අවශ්‍ය තොරතුරු වල මෙනු අංකය ඇතුළත් කරන්න*\n
    7. අලුත්ම සංක්‍යා 
    8. නවතම පුවත් 
    9. ප්‍රස්ථාර දත්ත
    '''
    return menu

def get_tamil_menu():
    menu = '''
    *உங்களுக்குத் தேவையான தகவலின் மெனு எண்ணை உள்ளிடவும்*\n
    10. சமீபத்திய எண்கள்
    11. சமீபத்திய செய்தி
    12. வரைபடத் தரவு
    '''
    return menu