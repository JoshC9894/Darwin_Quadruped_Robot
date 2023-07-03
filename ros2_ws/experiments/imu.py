# import time
# import busio
# from board import SCL, SDA

# i2c = busio.I2C(SCL, SDA)
# mpu = imu.MPU6050(i2c)

# while True:
#     print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
#     print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
#     print("Temperature: %.2f C" % mpu.temperature)
#     print("")
#     time.sleep(1)

import adafruit_mpu6050 as imu
from typing import Tuple

class IMU():
    def __init__(self, i2c):
        self.mpu = imu.MPU6050(i2c)

    '''
    Returns the IMU Linear Acceleration value in m/s^2
    '''
    def acceleration(self) -> Tuple[float, float, float]:
        return self.mpu.acceleration
    
    '''
    Returns the IMU Angular Velocity value in rad/s
    '''
    def angular_velocity(self) -> Tuple[float, float, float]:
        return self.mpu.gyro
    
    '''
    Returns the IMU Angular Position value (Roll, Pitch, Roll) -> (X,Y,Z) in rad
    '''
    def angular_position(self) -> Tuple[float, float, float]:
        return (self.__roll_angle, self.__pitch_angle, self.__yaw_angle)

    '''
    Calculates Z-Axis rotation
    '''
    def __yaw_angle(self) -> float:
        return 0
    
    '''
    Calculates Y-Axis rotation
    '''
    def __pitch_angle(self) -> float:
        return 0
    
    '''
    Calculates X-Axis rotation
    '''
    def __roll_angle(self) -> float:
        return 0