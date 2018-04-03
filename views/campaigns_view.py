import os
import webapp2
import get_campaigns
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class ShowCampaigns(webapp2.RequestHandler):
    def get(self):
       campaings_list = get_campaigns.get_all_campaigns()
       path = os.path.join(os.path.dirname(__file__),
                          '../templates/show_campaigns.html')
       template = JINJA_ENVIRONMENT.get_template(path)
       self.response.out.write(template.render({'campaigns': campaings_list}))