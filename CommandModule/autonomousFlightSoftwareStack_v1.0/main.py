# -*- coding: utf-8 -*-
"""
Created on Mon September 23 11:14:45 2019

@author: EsuaEkpo

@decription: This is the main entry point for run the autonomoous mission software module

"""
import time, sys, asyncio
from sensorListener import Listener

listen = Listener()

listen.runListener()

time.sleep(10)

sys.exit()