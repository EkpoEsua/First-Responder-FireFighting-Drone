# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This is the main entry point for run the autonomoous mission software module

"""
import time, sys, asyncio
from sensorListener import Listener
from utilities.parser import Parser

listen = Listener()

listen.runListener()

print('waiting for request!...')
#wait for first request so the Parser class can have a valid string payload
while not Listener._continue:
    continue

print('request recieved, continuing...')

time.sleep(10)

Listener.shutdown_server()

print('sure!' + Parser.payload)

input()

sys.exit()