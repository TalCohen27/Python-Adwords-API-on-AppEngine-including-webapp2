import webapp2
import os
import jinja2
import get_campaigns
import urllib
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HelloWorldApp(webapp2.RequestHandler):
    def get(self):
       campaings_list = get_campaigns.get_all_campaigns()
       template = JINJA_ENVIRONMENT.get_template('sp_frontend/dist/index.html')
       self.response.out.write(template.render({'campaigns' : campaings_list}))


hello_world_app = webapp2.WSGIApplication([
    ('/', HelloWorldApp),
], debug=True)

