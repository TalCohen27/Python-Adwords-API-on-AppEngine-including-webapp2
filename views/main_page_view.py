import webapp2
import jinja2
import os

# Use the App Engine Requests adapter. This makes sure that Requests uses URLFetch.

class SetMain(webapp2.RequestHandler):
    def get(self):
        JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
                           'templates')),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True)

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render({}))


