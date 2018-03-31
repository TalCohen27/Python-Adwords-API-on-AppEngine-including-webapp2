import webapp2
import os
import jinja2
import urllib

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HelloWorldApp(webapp2.RequestHandler):
    def get(self):
        # url = self.request.uri 'url': url
        template = JINJA_ENVIRONMENT.get_template('sp_frontend/dist/index.html')
        self.response.out.write(template.render({}))


hello_world_app = webapp2.WSGIApplication([
    ('/', HelloWorldApp),
], debug=True)

