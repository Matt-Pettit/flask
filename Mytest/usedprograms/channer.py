# credits to Anarov for improved example - (used to find basic syntax of wrapper)

#"THE BEER-WARE LICENSE" (Revision 42):
#<pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return. Matt Pettit

from __future__ import print_function
import basc_py4chan
import sys
import os






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
        mainlist.append('------------------------------------------------------')
    return(mainlist)

    #except:
        #print('There was an error(check your boardname)')


def threader(board,thread):

    mainlist = []
    board = basc_py4chan.Board(str(board))
    thread_id = thread
    print(thread_id)
    thread = board.get_thread(thread_id)
    print(thread)
    for i in range(len(thread.replies)):
        mainlist.append(thread.replies[i].text_comment)
    return(mainlist)




print(threader('g','67675328'))
