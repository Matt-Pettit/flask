# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


from flask import Flask, render_template,request,url_for,redirect
import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def input():
	return render_template('input.html')



@app.route('/command',methods = ['POST', 'GET'])
def input1():
    if request.method == 'POST':
        command = request.form['command']
        #return redirect(url_for('page',command = command))
    else:
        command = request.args.get('command')
        #return redirect(url_for('page',command = command))
	list1 = []
	c = os.popen(command)
	for item in c.readlines():
		list1.append(item)
	return render_template('output.html', your_list=list1)


@app.route('/output/<command>')
def page(command):
	list1 = []
	c = os.popen(command)
	for item in c.readlines():
		list1.append(item)
	return render_template('output.html', your_list=list1)

@app.errorhandler(404)
def page_not_found(error):
	return("Error 404, Page not found.")

if __name__ == "__main__":
    app.run(debug=True)
