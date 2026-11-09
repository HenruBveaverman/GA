import math, time

class Hand:

    def __init__(self):
        self.sensor_data = [[0, 0, 0], [0, 0, 0]] # Will change to actual sensor data later
        self.position_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Pos, velocity, rotation

    def update_velocity(self, elapsed_time):
        # TODO # ADD Y_ROT, Z_ROT # TODO #
        z_rot = 2
        y_rot = 1
        #=========================== UPDATE VELOCITY FROM ACCELERATION AND TIME ===========================#
        self.position_data[1][0] += self.sensor_data[0][0]*elapsed_time*math.cos(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))
        self.position_data[1][0] += self.sensor_data[0][1]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))
        self.position_data[1][0] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))

        self.position_data[1][1] += self.sensor_data[0][0]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))
        self.position_data[1][1] += self.sensor_data[0][1]*elapsed_time*math.cos(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))
        self.position_data[1][1] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))

        self.position_data[1][2] += self.sensor_data[0][0]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))
        self.position_data[1][2] += self.sensor_data[0][1]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))
        self.position_data[1][2] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))
        return

    def update_position(self, elapsed_time):
        z_rot = 2
        y_rot = 1
        #=========================== UPDATE POSITION FROM VELOCITY, ACCELERATION AND TIME ===========================#
        self.position_data[0][0] += self.position_data[1][0]*elapsed_time
        self.position_data[0][0] += self.sensor_data[0][0]*elapsed_time*math.cos(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))/2
        self.position_data[0][0] += self.sensor_data[0][1]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))/2
        self.position_data[0][0] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))/2
    
        self.position_data[0][1] += self.position_data[1][1]*elapsed_time
        self.position_data[0][1] += self.sensor_data[0][0]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))/2
        self.position_data[0][1] += self.sensor_data[0][1]*elapsed_time*math.cos(math.radians(self.sensor_data[1][z_rot]))*math.cos(math.radians(self.sensor_data[1][y_rot]))/2
        self.position_data[0][1] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))/2
    
        self.position_data[0][2] += self.position_data[1][2]*elapsed_time
        self.position_data[0][2] += self.sensor_data[0][0]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))/2
        self.position_data[0][2] += self.sensor_data[0][1]*elapsed_time*math.sin(math.radians(self.sensor_data[1][z_rot]))/2
        self.position_data[0][2] += self.sensor_data[0][2]*elapsed_time*math.sin(math.radians(self.sensor_data[1][y_rot]))/2
        return

    def print_data(self):
        return f"""Rotation :                                       
        h: {self.sensor_data[0][0]}                                      
        r: {self.sensor_data[0][1]}                                      
        p: {self.sensor_data[0][2]}                                      
        Acceleration :                                      
        ax: {self.sensor_data[1][0]}                                      
        ay: {self.sensor_data[1][1]}                                      
        az: {self.sensor_data[1][2]}                                      
        """