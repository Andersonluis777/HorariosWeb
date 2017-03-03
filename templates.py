import webapp2

form_html = '''
<form>
<h2>Adicione uma comida</h2>
<input type="text" name="food">
<button>Adicionar</button>
</form>
'''

class Handler(webapp2.RequestHandler):
	def write(selt, *a, **kw):
		self.response.out.write(*a, **kw)

class MainHandler(Handler):
	def get(self):
		self.write(form_html)

app = webapp2.WSGIApplication([
	('/',MainHandler)
], debug=True)
