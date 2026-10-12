import math
from typing import cast

from controller import Motor, PositionSensor, Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Get joint motor
motor = cast(Motor, robot.getDevice("forearm"))
motor_base = cast(Motor, robot.getDevice("base"))

# Get joint sensor
sensor = cast(PositionSensor, robot.getDevice("forearm_sensor"))
sensor.enable(timestep)

sensor_base = cast(PositionSensor, robot.getDevice("base_sensor"))
sensor_base.enable(timestep)

# Initial position command
motor.setPosition(1.2)
motor_base.setPosition(0.0)

sampleTime = 1 * timestep

# Main loop:
# Perform simulation steps until Webots is stopping the controller
while robot.step(sampleTime) != -1:
    # Read the sensor
    theta = sensor.getValue()
    time = robot.getTime()

    # Set actuator position command increasing linearly with time
    position = 1.2 + 0.2 * math.sin(time)

    motor.setPosition(position)
    print(f"arm position: {theta:.2f}")

    theta = sensor_base.getValue()

    position = 0.2 * time

    motor_base.setPosition(position)
    print(f"base position: {theta:.2f}")
