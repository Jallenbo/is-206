import codecs
import webapp2

form = """
<form method="post">
Do a rot13 on these words: <br />
<textarea name="text" value="%(text)s">%(text)s</textarea> <br />
<input type="submit" value="Submit">

</form>

"""
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.write_form()

	def post(self):
		words = self.request.get("text")
		words = codecs.encode(words, 'rot_13')
		self.write_form(words)
	
	def write_form(self, text=""):
		self.response.out.write(form % {"text" : text})
		
application = webapp2.WSGIApplication([('/', MainPage)],
									   debug=True)
