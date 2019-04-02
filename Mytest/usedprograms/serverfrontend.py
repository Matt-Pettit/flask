#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chatfrontend.py
#
#  Copyright 2018 Matt Pettit <pettit.matt@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

# Python program to implement client side of chat room.
import socket
import select
import sys

def servermain(message):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_address = '127.0.0.1'
    Port = int(1237)
    server.connect((IP_address, Port))

    def sendmessage(message):

    # maintains a list of possible input streams
        sockets_list = [sys.stdin, server]
        server.sendall(message.encode('utf-8'))
    """ There are two possible input situations. Either the
    user wants to give  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""

    #read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])


    sendmessage(message)

    server.close()
servermain('echo "hi"')
