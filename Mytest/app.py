#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
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
import basc_py4chan
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('home.html')#render template takes  html file and renders it to here
	print(currenttime())
app.add_url_rule('/home','/', index)# rule to send '/home' to '/' in the url

@app.route('/about')
def about():
	return render_template('about.html')#render template takes  html file and renders it to here


@app.route('/slashdot')
def slashdot():
	listofitems = []
	listofitems = slashdotMain()
	return render_template('slashdot.html', your_list=listofitems)




@app.route('/articles')
def articles():
	return render_template('articles.html')#render template takes  html file and renders it to here

#chan BEGIN
@app.route('/gchanboard')
def board():
	listofitems = []
	listofitems = boarder('g',1)
	return render_template('boardshow.html', your_list=listofitems)
#end of board show, begin thread
@app.route('/gchanform')
def gchanform():
	return render_template('gchan.html')

@app.route('/gchanthread',methods = ['POST', 'GET'])
def gchanthread():
   if request.method == 'POST':
	   id = request.form['thread']
	   return redirect(url_for('thread',thread = str(id)))
   else:
	   id = request.args.get('thread')
	   return redirect(url_for('thread',thread = str(id)))

@app.route('/thread/<thread>')
def thread(thread):
	listofitems = []
	listofitems = threader('g',thread)
	return render_template('boardshow.html', your_list=listofitems)



#chan END

#server BEGIN
@app.route('/serverform')
def serversite():
	return render_template('server.html')
#This is the thing that takes my request and sends it to ->$
@app.route('/server',methods = ['POST', 'GET'])
def server():
   if request.method == 'POST':
      command = request.form['command']
      return redirect(url_for('sc',command = command))
   else:
      command = request.args.get('command')
      return redirect(url_for('sc',command = command))
#->$here
@app.route('/sc/<command>')
def sc(command):
	command = servermain(command)
	return(render_template('sc.html',command = command))
#server END

#CALC BEGIN
@app.route('/calcform')
def calcform():
	return render_template('calc.html')
#This is the thing that takes my request and sends it to ->$
@app.route('/calc',methods = ['POST', 'GET'])
def calcenter():
   if request.method == 'POST':
	   val = int(request.form['numberval'])
	   val = str(val*2)
	   return redirect(url_for('calcdone',num = val))
   else:
	   val = int(request.args.get('numberval'))
	   val = str(val*2)
	   return redirect(url_for('calcdone',num = val))
#->$here
@app.route('/calcdone/<num>')
def calcdone(num):
	return('The answer is %s') % num
	flash(num, info)
#CALC END

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



@app.context_processor
def get_legacy_var():
    return dict(get_legacy_var=currenttime())

def currenttime():
	time = datetime.datetime.now()
	return(time)




#put slashdot thing here
def multifind(string, value, start = 0, stop = None):
	    values = []
	    while True:
	        found = string.find(value, start, stop)
	        if found == -1:
	            break
	        values.append(found)
	        start = found + 1
	    return values


def valfinder(string,xmldata):
	return(multifind(xmldata, string))

def printer(titles,descs,links):
	for i in range(len(links)):
		print(titles[i])
		print('='*len(titles[i])+'\n')
		print(descs[i]+'\n')
		print(links[i]+'\n')

def finder(xmldata, string1,string2):
	list1 = []
	wordbegvalstr = string1
	wordendvalstr = string2
	wordbegval = valfinder(wordbegvalstr,xmldata)
	wordendval = valfinder(wordendvalstr,xmldata)
	for i in range(len(wordbegval)):
		mainstring = (xmldata[wordbegval[i]+(len(wordbegvalstr)):wordendval[i]])
		if string1 == '<title>':
			list1.append(mainstring+':')
		else:
			list1.append(mainstring)
	if string1 == '<description>':
		descsfinal= []
		list1.remove(list1[0])
		for word in list1:
		#currentdesc = descs[i]
			loc = (word.find('&lt;p&gt;&lt;div'))
			currentdesc = word[0:loc]
			descsfinal.append(currentdesc)
		return(descsfinal)
	else:
		list1.remove(list1[0])
		list1.remove(list1[0])
		list1.remove(list1[len(list1)-1])
		return(list1)



def slashdotMain():
	url = 'http://rss.slashdot.org/Slashdot/slashdotMain'
	headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
	response = requests.get(url, headers=headers)
	xmldata = response.text
	titles = finder(xmldata,'<title>','</title>')
	links = finder(xmldata,'<link>','</link>')
	descs = finder(xmldata, '<description>', '</description>')
	finalprint = []
	#print(titles)
	#print(links)
	#print(descs)
	for i in range(len(titles)):
		finalprint.append(titles[i])
		finalprint.append(descs[i])
		finalprint.append(links[i])
		finalprint.append('='*(len(links[i])))

	return(finalprint)

def boarder(board,page):
    #try:
	board = basc_py4chan.Board(str(board))
    # select the first thread on the board
	all_thread_ids = board.get_all_thread_ids()
	mainlist = []

	for i in range(page*15):
		thread_id = all_thread_ids[i]
		thread = board.get_thread(thread_id)
		topic = thread.topic
		mainlist.append('Subject:'+str(topic.subject))
		mainlist.append('Comment:'+str(topic.text_comment))
		mainlist.append('Replies:'+str(len(thread.replies)))
		mainlist.append('Thread ID:'+str(thread_id))
		mainlist.append(str('='*204))
	return(mainlist)

def threader(board,thread):
	thread = str(int(thread))
	mainlist = []
	board = basc_py4chan.Board(str(board))
	thread_id = thread
	print(thread_id)
	thread = board.get_thread(thread_id)
	print(thread)
	for i in range(len(thread.replies)):
		mainlist.append(thread.replies[i].text_comment)
		mainlist.append('='*len(thread.replies[i].text_comment))
	return(mainlist)

def servermain(message):
	def sendmessage(message):
		sockets_list = [sys.stdin, server]
		server.sendall(message.encode('utf-8'))
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	IP_address = '127.0.0.1'
	Port = int(1235)
	server.connect((IP_address, Port))
	sendmessage(message)
	server.close()
	return(message)


#checks for main and runs
if __name__ == '__main__':
	app.run(debug = True) #runs app in debug mode(allows for on the fly changes)
