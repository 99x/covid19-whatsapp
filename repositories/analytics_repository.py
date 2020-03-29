from pyga.requests import Tracker
from pyga.entities import Event, Session, Visitor
from random import random

class AnalyticsRepository:

  def add_event(self,user_source):
    ga_tracker = Tracker(account_id='UA-162032901-2', domain_name='test.picasix.com')
    event = Event(category='UserEvents',action='Visit',label= 'User' + str(user_source), value=1)
    session = Session()
    visitor = Visitor()
    ga_tracker.track_event(event= event, session= session, visitor= visitor)
    return "event added"

