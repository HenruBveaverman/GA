# Drone commands - Main

import random, sys, os, math, time

s_time = time.time()

running = True
sensor_data = [[0, 0, 0], [0, 0, 0]]
pos_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Pos, velocity, rotation

def main(pos_data, sen_data):
    while running:
            e_time = time.time()
            d_time = e_time-s_time
            print(f"Time since last tick: {d_time} seconds")
            s_time = time.time()
            for i in range(len(pos_data[2])): # Update rotation
                pos_data[2][i] += sen_data[1][i]*(d_time)

            pos_data = update_velocity(position_data=pos_data, sensor_data=sen_data, elapsed_time=d_time)
            pos_data = update_position(position_data=pos_data, sensor_data=sen_data, elapsed_time=d_time)

        

def update_velocity(position_data, sensor_data, elapsed_time):
    # TODO # ADD Y_ROT, Z_ROT # TODO #

    # Update velocity
    position_data[1][0] += sensor_data[0][0]*elapsed_time*math.cos(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))
    position_data[1][0] += sensor_data[0][1]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))
    position_data[1][0] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))
     
    position_data[1][1] += sensor_data[0][0]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))
    position_data[1][1] += sensor_data[0][1]*elapsed_time*math.cos(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))
    position_data[1][1] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))
     
    position_data[1][2] += sensor_data[0][0]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))
    position_data[1][2] += sensor_data[0][1]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))
    position_data[1][2] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))

    return position_data

def update_position(position_data, sensor_data, elapsed_time):
    position_data[0][0] += pos_data[1][0]*elapsed_time
    position_data[0][0] += sensor_data[0][0]*elapsed_time*math.cos(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))/2
    position_data[0][0] += sensor_data[0][1]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))/2
    position_data[0][0] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))/2

    position_data[0][1] += pos_data[1][1]*elapsed_time
    position_data[0][1] += sensor_data[0][0]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))/2
    position_data[0][1] += sensor_data[0][1]*elapsed_time*math.cos(math.radians(sensor_data[1][z_rot]))*math.cos(math.radians(sensor_data[1][y_rot]))/2
    position_data[0][1] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))/2

    position_data[0][2] += pos_data[1][2]*elapsed_time
    position_data[0][2] += sensor_data[0][0]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))/2
    position_data[0][2] += sensor_data[0][1]*elapsed_time*math.sin(math.radians(sensor_data[1][z_rot]))/2
    position_data[0][2] += sensor_data[0][2]*elapsed_time*math.sin(math.radians(sensor_data[1][y_rot]))/2

    return position_data
        
main(pos_data=pos_data, sen_data=sensor_data)