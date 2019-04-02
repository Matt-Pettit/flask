# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


from __future__ import print_function
import sys,os,datetime
from flask import Flask, render_template,request,url_for,redirect
import requests
import socket
import select

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
#LOGIN BEGIN
@app.route('/loginform')
def loginsite():
	return render_template('login.html')
#This is the thing that takes my request and sends it to ->$
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('hello',user = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('hello',user = user))
#->$here
@app.route('/hello/<user>')
def hello(user):
	return(render_template('hello.html',name = user))
#LOGIN END

if __name__ == "__main__":
    app.run(debug=True)
