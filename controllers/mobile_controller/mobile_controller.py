from typing import cast

from controller import Motor, PositionSensor, Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = cast(Motor, robot.getDevice("left wheel motor"))
left_sensor = cast(PositionSensor, robot.getDevice("left wheel sensor"))
left_sensor.enable(timestep)

right_motor = cast(Motor, robot.getDevice("right wheel motor"))
right_sensor = cast(PositionSensor, robot.getDevice("right wheel sensor"))
right_sensor.enable(timestep)

left_motor.setPosition(0)
right_motor.setPosition(0)

while robot.step(timestep) != -1:
    left_position = left_sensor.getValue()
    right_position = right_sensor.getValue()

    print(f"left position: {left_position:.2f}, right position: {right_position:.2f}")

    position = robot.getTime()
    left_motor.setPosition(position * 10)
    right_motor.setPosition(position * 10)
