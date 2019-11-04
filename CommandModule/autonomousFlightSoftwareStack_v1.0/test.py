#!/usr/bin/env python3

import asyncio
from mavsdk import System
# from mavsdk import (e)


async def run():

    # Init the drone
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyUSB1:57600")
    # await drone.connect(system_address="serial:///dev/ttyACM0:57600")
    # await drone.connect(system_address="udp://:14540")

    print("Waiting for drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # Start the tasks
    # asyncio.ensure_future(print_battery(drone))
    # asyncio.ensure_future(print_gps_info(drone))
    # asyncio.ensure_future(print_in_air(drone))
    # asyncio.ensure_future(print_position(drone))
    # asyncio.ensure_future(print_actuator_output_status(drone))
    # asyncio.ensure_future(print_armed(drone))
    asyncio.ensure_future(print_health(drone))
    # asyncio.ensure_future(print_home(drone))
    # asyncio.ensure_future(print_landed_state(drone))
    # asyncio.ensure_future(print_rc_status(drone))
    asyncio.ensure_future(print_flight_mode(drone))

    # forcefully arm the drone

    # await drone.core.connection_state()

    # Execute the maneuvers
    # print("-- Arming")

    await asyncio.sleep(30)

    await drone.action.arm()

    await asyncio.sleep(30)

    await drone.action.disarm()

async def print_battery(drone):
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery}")

async def print_home(drone):
    async for home in drone.telemetry.home():
        print(f"Home: {home}")
        
async def print_landed_state(drone):
    async for landed_state in drone.telemetry.landed_state():
        print(f"Landed State: {landed_state}")

async def print_armed(drone):
    async for armed in drone.telemetry.armed():
        print(f"Armed: {armed}")

async def print_flight_mode(drone):
    async for flight_mode in drone.telemetry.flight_mode():
        print(f"Flight Mode: {flight_mode}")

async def print_health(drone):
    async for health in drone.telemetry.health():
        print(f"Health: {health}")

async def print_rc_status(drone):
    async for rc_status in drone.telemetry.rc_status():
        print(f"RC Status: {rc_status}")

async def print_actuator_output_status(drone):
    async for actuator_output_status in drone.telemetry.actuator_output_status():
        print(f"Actuactor Output Status: {actuator_output_status}")


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def print_in_air(drone):
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_position(drone):
    async for position in drone.telemetry.position():
        print(position)


if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
