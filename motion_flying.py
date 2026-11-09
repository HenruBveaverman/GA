import logging, sys, time, math
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper
from cflib.crazyflie.commander import Commander

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

DEFAULT_HEIGHT = 0.5
BASE_THRUST = (0.5) * 100 # Trial and error found that the thrust needed to hover was between 40% and 45% 
LAND_TIME = 5

deck_attached_event = Event()

logging.basicConfig(level=logging.ERROR)

def init_drone(scf):
    drone_cmd = Commander(scf.cf)
    time.sleep(1)
    print("Commander initialized. ")
    return drone_cmd

def set_drone_instructions(cmnd : Commander, roll: float, pitch : float, yawrate : float, thrust : float):
    cmnd.send_setpoint_manual(roll=roll, pitch=pitch, yawrate=yawrate, thrust_percentage=thrust, rate=False)

def land_drone(cmnd : Commander, land_time : float, thrust : float):
    start_thrust = thrust
    while thrust >= 1:
        set_drone_instructions(cmnd = cmnd, roll=0, pitch=0, yawrate=0, thrust=thrust)
        time.sleep(land_time/100)
        thrust -= start_thrust/(100*land_time)
    return
    

if __name__ == '__main__':
    print("Program started")
    cflib.crtp.init_drivers()
    
    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        # Arm the Crazyflie
        scf.cf.supervisor.send_arming_request(True)
        time.sleep(1.0)
        drone_cmd = init_drone(scf=scf)

        thrust = BASE_THRUST
        if input("Start? ") != " ":
            set_drone_instructions(cmnd=drone_cmd, roll=0, pitch=0, yawrate=0, thrust=thrust+5)
            time.sleep(1)
            
            for i in range(200):
                r = 0
                p = 0
                y = 0
                new_thrust = BASE_THRUST*math.cos(math.radians(r))*math.cos(math.radians(p))
                thrust = min(max(new_thrust, 0), 100)
                set_drone_instructions(cmnd=drone_cmd, roll=r, pitch=p, yawrate=y, thrust=thrust)
                time.sleep(0.004) # Ca 4 ms to not clog everything too much. 
        set_drone_instructions(cmnd=drone_cmd, roll = 0, pitch = 10, yawrate=0, thrust=(BASE_THRUST*math.cos(math.radians(10))))
        time.sleep(2)
        land_drone(cmnd=drone_cmd, land_time=LAND_TIME, thrust=BASE_THRUST)