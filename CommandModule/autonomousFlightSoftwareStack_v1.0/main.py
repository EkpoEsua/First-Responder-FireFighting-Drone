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

time.sleep(10)

Listener.stop = True
print('stop initiated!')

time.sleep(10)

print('sure!' + Parser.payload)

sys.exit()