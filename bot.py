from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '1' in incoming_msg:
        msg.body(get_stats())
        responded = True
    if '2' in incoming_msg:
        msg.body(get_news())
        responded = True
    if '3' in incoming_msg:
        msg.media(get_graph())
        responded = True
    if not responded:
        msg.body('*A project by UNDP and 99X*\n\nYou can get latest Sri Lankan covid-19 information here. \nReply with the number: \n\n1. latest numbers\n2. related news\n3. case graph ')
    return str(resp)

def get_stats():
    stats = '*Globally* \n266 073 confirmed \n11 184 deaths \n\n*Sri Lanka* \n80 confirmed \n0 deaths'
    return stats

def get_news():
    news = '*Latest news* \n - 5 new cases reported since yesterday http://news.lk/news'
    return news

def get_graph():
    graph_url= 'https://blog.watchdog.paladinanalytics.com/content/images/2020/03/image-5.png'
    return graph_url