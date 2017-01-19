from flask import render_template
from app import app
from app import packages

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Rogue'}  # fake user
	posts = [  # fake array of posts
		{ 
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!' 
		},
		{ 
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template('index.html', title='Home', user=user, posts = posts)
	# return render_template('index.html', user=user) #used to test the else condition in index.html
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