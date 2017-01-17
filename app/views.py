from app import app
from app import packages

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Rogue'}  # fake user
	return '''
<html>
  <head>
	<title>Home Page</title>
  </head>
  <body>
	<h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

@app.route('/test')
def index1():
	return "Hello, Test World!" + packages.print_fun()