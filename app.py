# import Flask class
# render_template is for html partials
# request is for form methods
from flask import Flask, render_template, request
import datetime

# by convention need to type this line
# __name__ just saying the current file is the flask app
# create a variable app tying it to the current app instance
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return f"<h1>Hello, {name}</h1>"

# render a template
# find template files in templates > xyz.html
@app.route("/template")
def temp():
	return render_template("template_partial.html")

# using dynamic variables in html template
# html templating
@app.route('/dynamic')
def dynamic():
	headline = "hello, world 2020"
	return render_template("dynamic_partial.html", headline=headline) #headline is the variable in html, second headline is the python variable

# demo control flow in jinja and in python
# useful if want to display or hide a full section of webpage based on condition
@app.route("/christmas")
def is_christmas():
	now = datetime.datetime.now()
	new_year = now.month == 1 and now.day == 1
	#new_year = True
	return render_template("christmas.html", headline=new_year)

# dynamically generate <li> items in html
# using jinja loops
@app.route("/each")
def each():
	names = ["Kathleen", "Sandra", "Adriana"]
	return render_template("each.html", names=names)

# detail page and go back
# figure out what is the more function url
# even if it changes later
# {{url_for('more')}}
@app.route("/product")
def product():
	return render_template("product.html")

@app.route("/more")
def more():
	return render_template("product_detail.html")

# template inheritance example
# the python route, controller side doesn't change much
# now the HTML contains a base layout and modified layout
# in layout directory there are now three files
# layout.html
# iindex.html
# imore.html
# previously no layout.html
# any change in layout html will change the other partials that inherit it
@app.route("/inherit_index")
def i_index():
	return render_template('iindex.html')

@app.route("/inherit_more")
def i_more():
	return render_template('imore.html')


# forms
@app.route("/forms")
def forms():
	return render_template("forms.html")

# must specify method
# else Method Not Allowed error
# default method is GET 
@app.route("/forms_submit", methods=["GET","POST"]) #just need the post method
def forms_submit():
	'''
	# first name is the python variable
	# second name is the form variable
	name = request.form.get("name")
	# pass the python variable name to the html
	return render_template("forms_submit.html", name=name)
	'''

	# even safer way to write it
	if request.method == 'GET':
		return "Please submit the form instead"
	else:
		name = request.form.get("name")
		return render_template("forms_submit.html", name=name)