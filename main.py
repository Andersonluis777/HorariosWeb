import webapp2

form=open("form.html").read()

class MainHandler(Handler):
	def get(self):
		self.write(form)

app = webapp2.WSGIApplication([
	('/',MainHandler)
], debug=True)
