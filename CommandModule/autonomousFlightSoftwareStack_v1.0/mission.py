#!/usr/bin/env python3

import asyncio, time
from mavsdk import System
from mavsdk import (MissionItem)

# MISSION_LAT = 47.398039859999997
# MISSION_LON = 8.5455725400000002
MISSION_HEIGHT = 5.0
MISSION_SPEED = 3.0
# ACTION_HEIGHT = 2.0

# This is the time it takes for the drone to discharge its content
ACTION_TIME_SECS = 10

async def runMission(MISSION_LAT, MISSION_LON, ACTION_HEIGHT):
    """
    This is the "main" function.
    It first creates the drone object and initializes it.

    Then it registers tasks to be run in parallel (one can think of them as threads):
       
    Finally, it goes to the actual works: arm the drone, initiate a takeoff
    and finally land.

    Note that "observe_is_in_air" is not necessary, but it ensures that the
    script waits until the drone is actually landed, so that we receive feedback
    during the landing as well.

    Parameters
    ----------
    MISSION_LAT : float
        - This is the latitude of the mission location point

    MISSION_LON : float
        - This is the longitude of the mission location point

    ACTION_HEIGHT : float
        - This is the height of the point to be extinguished, relative to the
        the home altitude in meters.

    """

    # Initialize the drone
    drone = System()
    # use serial:///dev/ttyUSB0:57600 when connecting to mavlink over usb
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # Set up mission parameters
    await set_mission_params(drone)

    # Get mission parameters
    await get_mission_params(drone)

    # await drone.action.reboot()

    # Start parallel tasks
    asyncio.ensure_future(print_altitude(drone))
    asyncio.ensure_future(print_flight_mode(drone))
    asyncio.ensure_future(print_status(drone))
    asyncio.ensure_future(print_mission_progress(drone))
    termination_task = asyncio.ensure_future(observe_is_in_air(drone))

    # create actuator controls

    # Create Mission and get mission items
    mission_items = await initialize_mission(drone, MISSION_LAT, MISSION_LON, ACTION_HEIGHT)

    # Upload mission to the drone
    print("-- Uploading mission")
    await drone.mission.upload_mission(mission_items)

    # Execute the maneuvers
    print("-- Arming")
    await drone.action.arm()

    # Print drone home position
    await print_drone_home_position(drone)

    # print("-- Taking off")
    await drone.action.takeoff()

    # print("-- Starting mission")
    # await drone.mission.start_mission()

    # await asyncio.sleep(10)

    # print("-- Landing")
    # await drone.action.land()

    # Wait until the drone is landed (instead of returning after 'land' is sent)
    await termination_task



# Helper Functions

async def print_drone_home_position(drone):
    """ Prints the drone's position """

    async for position in drone.telemetry.home():
        print(f"HOME --- {position}")
        return

async def print_altitude(drone):
    """ Prints the altitude when it changes """

    previous_altitude = None

    async for position in drone.telemetry.position():
        altitude = round(position.relative_altitude_m)
        if altitude != previous_altitude:
            previous_altitude = altitude
            print(f"Altitude: {altitude}")


async def print_flight_mode(drone):
    """ Prints the flight mode when it changes """

    previous_flight_mode = None

    async for flight_mode in drone.telemetry.flight_mode():
        if flight_mode is not previous_flight_mode:
            previous_flight_mode = flight_mode
            print(f"Flight mode: {flight_mode}")

async def print_status(drone):
    """ prints the current position of the drone """

    previous_status = None

    async for status in drone.telemetry.status_text():
        if status is not previous_status:
            previous_status = status
            print(status)


async def print_mission_progress(drone):
    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: {mission_progress.current_item_index}/{mission_progress.mission_count}")


async def set_mission_params(drone):
    """ set mission parameters for the mission """

    # Set takeoff altitude
    await drone.param.set_float_param("MIS_TAKEOFF_ALT", MISSION_HEIGHT)

    # Set action after takeoff, set to mission mode if any
    await drone.param.set_int_param("COM_TAKEOFF_ACT", 1)

    # Maximum horizontal velocity in mission
    await drone.param.set_float_param("MPC_XY_CRUISE", MISSION_SPEED)

    # Maximum horizontal velocity
    await drone.param.set_float_param("MPC_XY_VEL_MAX", MISSION_SPEED)

    # Return mode loiter altitude
    await drone.param.set_float_param("RTL_DESCEND_ALT", MISSION_HEIGHT)

    # RTL altitude
    await drone.param.set_float_param("RTL_RETURN_ALT", MISSION_HEIGHT)


async def initialize_mission(drone, MISSION_LAT, MISSION_LON, ACTION_HEIGHT):
    """ intialize the mission items for the mission """

    mission_items = []
    mission_items.append(MissionItem(MISSION_LAT,
                                     MISSION_LON,
                                     MISSION_HEIGHT,
                                     MISSION_SPEED,
                                     True,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.NONE,
                                     float('nan'),
                                     float('nan')))

    # ADD ACTION (EXTINGUISHING) POINT AS A MISSION ITEM
    mission_items.append(MissionItem(MISSION_LAT,
                                     MISSION_LON,
                                     ACTION_HEIGHT,
                                     0,
                                     False,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.NONE,
                                     ACTION_TIME_SECS,
                                     float('nan')))
    
    for mission in mission_items:
        print(mission)

    await drone.mission.set_return_to_launch_after_mission(True)

    return mission_items


async def get_mission_params(drone):
    """ get/print mission parameters """

    print(await drone.param.get_float_param("MIS_TAKEOFF_ALT"))


async def observe_is_in_air(drone):
    """ Monitors whether the drone is flying or not and
    returns after landing """

    was_in_air = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            was_in_air = is_in_air

        if was_in_air and not is_in_air:
            await asyncio.get_event_loop().shutdown_asyncgens()
            return


# Main external entry point function
def run(MISSION_LAT, MISSION_LON, ACTION_HEIGHT):
    asyncio.get_event_loop().run_until_complete(runMission(MISSION_LAT, MISSION_LON, ACTION_HEIGHT))

