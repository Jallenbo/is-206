import codecs
import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(codecs.encode("WHAT's UP", 'rot_13'))

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
