import time
import busio
import RPi.GPIO as GPIO

from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

class Leg():
    def __init__(
        self,
        ankle_servo: servo.Servo,
        knee_servo: servo.Servo,
        hip_servo: servo.Servo
    ):
        self.ankleJoint = ankle_servo; self.ankleJoint.angle = 90
        self.kneeJoint = knee_servo; self.kneeJoint.angle = 90
        self.hipJoint = hip_servo; self.hipJoint.angle = 90
        time.sleep(0.1)

i2c = busio.I2C(SCL, SDA)

pca_1 = PCA9685(i2c, address=0x40); pca_1.frequency = 50
pca_2 = PCA9685(i2c, address=0x41); pca_2.frequency = 50

# Rear Left Leg
rl_leg = Leg(
    ankle_servo=servo.Servo(pca_1.channels[8], min_pulse=650, max_pulse=2600),
    knee_servo=servo.Servo(pca_1.channels[11], min_pulse=400, max_pulse=2250),
    hip_servo=servo.Servo(pca_1.channels[15], min_pulse=650, max_pulse=2400)
)

# Front Left Leg
fl_leg = Leg(
    ankle_servo=servo.Servo(pca_2.channels[5], min_pulse=600, max_pulse=2600),
    knee_servo=servo.Servo(pca_2.channels[3], min_pulse=400, max_pulse=2350),
    hip_servo=servo.Servo(pca_2.channels[1], min_pulse=650, max_pulse=2450)
)

# Rear Right Leg
rr_leg = Leg(
    ankle_servo=servo.Servo(pca_1.channels[7], min_pulse=650, max_pulse=2650),
    knee_servo=servo.Servo(pca_1.channels[4], min_pulse=500, max_pulse=2350),
    hip_servo=servo.Servo(pca_1.channels[0], min_pulse=650, max_pulse=2400)
)

# Front Right Leg
fr_leg = Leg(
    ankle_servo=servo.Servo(pca_2.channels[7], min_pulse=600, max_pulse=2500),
    knee_servo=servo.Servo(pca_2.channels[8], min_pulse=600, max_pulse=2550),
    hip_servo=servo.Servo(pca_2.channels[15], min_pulse=650, max_pulse=2600)
)

# Headlights
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)

# while True:
#     GPIO.output(11, GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(11, GPIO.LOW)
#     time.sleep(0.5)