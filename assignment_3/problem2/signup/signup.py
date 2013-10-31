import webapp2
import re
		
form = """
<form method ="post">
<label> Username
	<input type="text" name="username">
</label>
<br />
<label> Password
	<input type="password" name="password">
</label>
<br />
<label> Re-type password
	<input type="password" name="verify">
</label>
<br />
<label> E-mail
	<input type="text" name="email">
</label>
<br />
<input type="submit">
<!--<div>%(error)s</div>-->
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
	return USER_RE.match(username)		
	
PASS_RE = re.compile(r"^.{3,20}$")	
def valid_password(password):
	return PASS_RE.match(password)
	
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return EMAIL_RE.match(email)
	
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.write_form()
		
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")
		
		error = False
		
		if not valid_username(username):
			error = True
			self.response.out.write("Error in username, ")
			
		if not valid_password(password):
			error = True
			self.response.out.write("Error in password, ")
		elif password != verify:
			error = True
			self.response.out.write("The password didn't match, ")
		
		if not valid_email(email):
			error = True
			self.response.out.write("Error in mail ")
			
		if error:
			self.response.out.write(form)
		else:
			self.redirect("/register")
			
	def write_form(self):
		self.response.out.write(form)
			
class Register(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Welcome")
		
application = webapp2.WSGIApplication([('/', MainPage),
									   ('/register', Register)],
									   debug=True)