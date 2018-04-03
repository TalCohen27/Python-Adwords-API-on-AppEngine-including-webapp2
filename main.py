from demo import DEBUG
from views import SetMain
from views import GetAllCampaigns
import webapp2
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()


app = webapp2.WSGIApplication([(r'/Campaigns', GetAllCampaigns)], debug=DEBUG)