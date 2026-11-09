import logging, sys, time, math
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper
from cflib.crazyflie.commander import Commander

class Drone():

    def __init__(self, id : int = 0):
        self.id = id
        self.BASE_THRUST = 0.43 * 100 # Approximate thrust percentage needed to hover with a naked drone.  

    def update_command(self, roll : float, pitch: float, yawrate):
        """
        Updates the command that is being sent to the drone. 

        r : float
        Stands for roll. 
        Degrees
        
        p : float
        Stands for pitch 
        Degrees
        
        yawrate : float
        Degrees per second
        """
        self.y_velocity += math.tan(pitch)*9.82
        self.x_velocity += math.tan(roll)*9.82
