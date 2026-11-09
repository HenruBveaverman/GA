from machine import Pin, SoftI2C, ADC
import time, struct, logging, sys
from threading import Event
time.sleep(1)

P = Pin.PULL_UP

i2c = SoftI2C(sda=Pin(7, Pin.OPEN_DRAIN, P), scl=Pin(6, Pin.OPEN_DRAIN, P), freq=115200)

ADDR = i2c.scan()[0]  # 0x28 or 0x29

i2c.writeto_mem(ADDR, 0x3D, b'\x00')   # config mode

time.sleep_ms(30)

i2c.writeto_mem(ADDR, 0x3D, b'\x0C')   # NDOF fusion mode

time.sleep_ms(30)

z_vel, z_pos = 0, 0
s_time = time.time()
t_time = 0
print_all = 0
flex_sensor = ADC(Pin(1))
flex_sensor.atten(ADC.ATTN_11DB)

hand = Hand()


print("Started")
while True:
    e_time = time.ticks_us()
    d_time = (e_time-s_time) / (10**6)
            
    data = i2c.readfrom_mem(ADDR, 0x1A, 20)          # Euler angles
    h, r, p, qw, qx, qy, qz, ax, ay, az= struct.unpack('<10h', data)
    bend = flex_sensor.read()
    if abs(az/100) < 0.4:
        az = 0
    if abs(z_vel) < 0.01:
        z_vel = 0
    cal = i2c.readfrom_mem(ADDR, 0x35, 1)[0]        # calibration status
    z_pos += ((az) * (d_time**2)) / 2 + z_vel * d_time
    z_vel += (az)*d_time
    print_all += 1
    if print_all == 550:
        print(f"\x1B[0J\x1B[1;1H{hand.print_data()} \nZ_pos: {z_pos}                                             \nZ_vel: {z_vel}                                             \nBend: {bend}                                           ")
        print_all = 500
    if print_all == 499:
        z_vel, z_pos = 0, 0
    s_time = e_time

    hand.sensor_data = [[h, r, p], [ax, ay, az]]
    hand.update_velocity(elapsed_time = d_time)
    hand.update_position(elapsed_time = d_time)
    