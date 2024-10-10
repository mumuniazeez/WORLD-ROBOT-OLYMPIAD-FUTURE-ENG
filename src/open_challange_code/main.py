#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

left_ultrasonic = UltrasonicSensor(Port.S1)
right_ultrasonic = UltrasonicSensor(Port.S2)
bottom_color = ColorSensor(Port.S3)

steering = Motor(Port.A)
left_motor = Motor(Port.B, gears=[20, 12])
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=[20, 12])


# Write your program here.
ev3.speaker.beep()

steering.run_time(-500, 500, Stop.HOLD)
wait(100)
steering.run_angle(5000, 90)
wait(100)
steering.reset_angle(0)


# wait(2000000)

# right_ultrasonic.distance() < 1000


while True:
    while not bottom_color.rgb()[0] < 10:

        if right_ultrasonic.distance() > 0 and right_ultrasonic.distance() < 200:
            steering.run_angle(500, -65 - steering.angle())
            print("very close")

        elif right_ultrasonic.distance() < 400:
            steering.run_angle(500, -40 - steering.angle())
            print("Too close")

        if right_ultrasonic.distance() > 460 and right_ultrasonic.distance() < 3000:
            steering.run_angle(500, 65 - steering.angle())
            print("very far")

        elif right_ultrasonic.distance() > 450:
            steering.run_angle(500, 40 - steering.angle())
            print("Too far")

        
        if right_ultrasonic.distance() > 400 and right_ultrasonic.distance() < 450:
            steering.run_angle(500, 0 - steering.angle())
            print("good")
        

        left_motor.run(1000)
        right_motor.run(1000)
        
    ev3.speaker.beep()