#coding=utf-8

import webapp2
import string
import codecs


#Render the form in HTML
form = """
<form method="post">
Do a rot13 on these words: <br />
<textarea name="text" value="%(text)s">%(text)s</textarea> <br />
<input type="submit" value="Submit">

</form>

"""

#Check if input is ASCII
#This function returns False if there's spaces in input, and is not used here
def isAscii(self, s):
	for c in s:
		if c not in string.ascii_letters:
			return False
	return True
	

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.write_form()

#Use encode to perform rot13
	def post(self):
		words = self.request.get("text")
		words = codecs.encode(words, 'rot_13')
		self.write_form(words)
			
#Function to write the form, without losing the content in textarea
	def write_form(self, text=""):
		self.response.out.write(form % {"text" : text})
		
application = webapp2.WSGIApplication([('/', MainPage)],
									   debug=True)
