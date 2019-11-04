from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative


# Connect to the Vehicle (in this case a simulator running the same computer)
vehicle = connect('/dev/ttyUSB0', wait_ready=True)

print("--- Connected to Link ---")

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print ("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print (" Waiting for vehicle to initialise...")
        time.sleep(1)

    print ("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print (" Waiting for arming...")
        time.sleep(1)

    
arm_and_takeoff(20)