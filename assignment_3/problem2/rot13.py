import codecs
import webapp2

form = """
<form method="post">
<label>
Do a rot13 on these words:
<input type="text" name="rot13" value="%(rot13)s">
</label>
<input type="submit" value="Submit">
</form>
"""
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.write_form()

	def post(self):
		words = self.request.get("rot13")
		words = codecs.encode(words, 'rot_13')
		self.write_form(words)
	
	def write_form(self, rot13=""):
		self.response.out.write(form % {"rot13" : rot13})
		
application = webapp2.WSGIApplication([('/', MainPage)],
									   debug=True)
