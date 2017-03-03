import webapp2

form=open("form.html").read()

class MainHandler(Handler):
	def get(self):
		self.write(form)

class CursosHandler(Handler):
	def get(self):
		self.write(form)
		
class ProfessorHandler(Handler):
	def get(self):
		self.write(form)

app = webapp2.WSGIApplication([
	('/',MainHandler)
	('/cursos',CursosHandler),
	('/professor',ProfessorHandler)
], debug=True)
