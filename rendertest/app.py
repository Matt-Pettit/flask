# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


from flask import Flask, render_template,request,url_for,redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def jumbo():
	list1 = ["word","word2","word3"]
	p1 = "hi ther ewats asdjjdfdj ajsdnwaiw aisas saskia"
	return render_template('jumbo.html', list = list1)#render template takes  html file and renders it to here

@app.route('/index')
def index():
	return render_template('index.html')#render template takes  html file and renders it to here

@app.route('/login')
def login():
	return render_template('login.html')#render template takes  html file and renders it to here

@app.route('/test')
def test():
	return render_template('complianceauditlog2.html')

#checks for main and runs
if __name__ == '__main__':
	app.run(debug = True) #runs app in debug mode(allows for on the fly changes)
