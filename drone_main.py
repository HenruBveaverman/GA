# Drone commands - Main

import random, sys, os, math, time, serial
from hand import Hand
from drone import Drone
from Adafruit_BNO055 import BNO055
import machine

#imu  = BNO055.BNO055()

#serial.Serial(port="COM9", baudrate=115200)
#print(serial)


s_time = time.time()

running = True

def main():
    hand = Hand()
    s_time = time.time()
    t_time = 0
    while running:
        e_time = time.time()
        d_time = e_time-s_time
        t_time += d_time
        print(f"\x1B[1;1H\x1B[0JTsl: {d_time}s  \x1B[1;40HTttl: {t_time}s")
        s_time = time.time()
        for i in range(len(hand.position_data[2])): # Update rotation
            hand.position_data[2][i] += hand.sensor_data[1][i]*(d_time)

        hand.update_position(elapsed_time=d_time)
        hand.update_velocity(elapsed_time=d_time)

        
main()