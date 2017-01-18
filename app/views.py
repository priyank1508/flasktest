from flask import render_template
from app import app
from app import packages

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Rogue'}  # fake user
	# return render_template('index.html', title='Home', user=user)
	return render_template('index.html', user=user)
# 	return '''
# <html>
#   <head>
# 	<title>Home Page</title>
#   </head>
#   <body>
# 	<h1>Hello, ''' + user['nickname'] + '''</h1>
#   </body>
# </html>
# '''

@app.route('/test')
def index1():
	return "Hello, Test World!" + packages.print_fun()