
# #GPIO Mode (BOARD / BCM)
# GPIO.setmode(GPIO.BCM)
 
# #set GPIO Pins
# # GPIO_TRIGGER = 17
# # GPIO_ECHO = 27

# GPIO_TRIGGER = 9
# GPIO_ECHO = 10
 
# #set GPIO direction (IN / OUT)
# # GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# # GPIO.setup(GPIO_ECHO, GPIO.IN)
 
# # def distance():
# #     # set Trigger to HIGH
# #     GPIO.output(GPIO_TRIGGER, True)
 
# #     # set Trigger after 0.01ms to LOW
# #     time.sleep(0.00001)
# #     GPIO.output(GPIO_TRIGGER, False)
 
# #     StartTime = time.time()
# #     StopTime = time.time()
 
# #     # save StartTime
# #     while GPIO.input(GPIO_ECHO) == 0:
# #         StartTime = time.time()
 
# #     # save time of arrival
    # while GPIO.input(GPIO_ECHO) == 1:
    #     StopTime = time.time()
 
# #     # time difference between start and arrival
# #     TimeElapsed = StopTime - StartTime
# #     # multiply with the sonic speed (34300 cm/s)
# #     # and divide by 2, because there and back
# #     distance = (TimeElapsed * 34300) / 2
 
# #     return distance

# StartTime, StopTime = time.time(), time.time()

# def echo_callback(callback):
#     StopTime = time.time()
#     TimeElapsed = StopTime - StartTime
#     distance = (TimeElapsed * 34300) / 2
#     print('Echo... %0.4f cm' % distance)


# def test():
#     GPIO.add_event_detect(GPIO_ECHO, GPIO.RISING, callback=echo_callback, bouncetime=100)

#     while(True):
#         print('Pulse...')
#         GPIO.output(GPIO_TRIGGER, True)
#         StartTime = time.time()
#         time.sleep(0.00001)
#         GPIO.output(GPIO_TRIGGER, False)
#         time.sleep(5)

#     return
import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 9
GPIO_ECHO = 10

class UltrasonicSensor():
    def __init__(self, trigger, echo):
        self.triggerPin = trigger; GPIO.setup(trigger, GPIO.OUT),
        self.echoPin = echo; GPIO.setup(echo, GPIO.IN)
        # GPIO.add_event_detect(echo, GPIO.RISING, callback=self.echoCallback, bouncetime=100)

        self.startTime = time.time()
        self.endTime = time.time()

    # def echoCallback(self, _):
    #     self.endTime = time.time()
    #     TimeElapsed = self.endTime - self.startTime
    #     distance = (TimeElapsed * 34300) / 2
    #     print('Echo... %0.4f cm' % distance)

    def scan(self):
        print('Pulse...')
        GPIO.output(self.triggerPin, True)
        # self.startTime = time.time()
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, False)

        self.startTime = time.time()
        self.endTime = time.time()
    
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            self.startTime = time.time()
    
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            self.endTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = self.endTime - self.startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        print ("Measured Distance = %.1f cm" % distance)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    sensor = UltrasonicSensor(
        trigger=GPIO_TRIGGER,
        echo=GPIO_ECHO
    )

    try:
        while True:
            sensor.scan()
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()