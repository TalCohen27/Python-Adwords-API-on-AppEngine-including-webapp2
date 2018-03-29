import webapp2


class HelloWorldApp(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


hello_world_app = webapp2.WSGIApplication([
    ('/', HelloWorldApp),
], debug=True)
