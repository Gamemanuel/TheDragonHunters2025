from __future__ import annotations

# import constants
    # every rotation of the motor the corresponding value is the distance traveled
drivetrainMeters: float = rotationToInch(robot.DRIVETRAIN_WHEEL_DIAMATER, robot.DRIVETRAIN_GEAR_RATIO) # 2 is radians to the gear ratio (8.46) to in (/6) to meters * 100
armMeter: float = rotationToInch(robot.ARM_WHEEL_DIAMATER, robot.ARM_GEAR_RATIO)  
intakeMeter: float = rotationToInch(robot.INTAKE_WHEEL_DIAMATER, robot.INTAKE_GEAR_RATIO)
elevatorMeter: float = rotationToInch(robot.ELEVATOR_WHEEL_DIAMATER, robot.ELEVATOR_GEAR_RATIO)

def targetElevatorPos(targetPos, power, currentPos: float):
    """
    this function allows you to run the ELEVATOR to a specific distance UP in METERS
    targetPos = Distance that you want to travel
    power = power of ELEVAROR
    """

    # the actual motor rotations = targetPos / elevatorMeters
    actualRotation: float = targetPos / elevatorMeter

    # convert the motor rotations into ticks
    actualTicks: float = (actualRotation * robot.TPR)

    # wait untill the encoder ticks on the robot == the wanted encoder ticks
    while actualTicks >= encoderTicksTraveled(currentPos, robot.elevator.getEncoder().getPosition()):

        # make the elevator move up
        robot.elevator.set(power)
        robot.elevator_follower.set(power)
    
    # after the correct ticks are hit kill the elevator
    robot.elevator.set(0)
    robot.elevator_follower.set(0)


def targetDrivetrainPos(self, targetPos, power):
    """
    this function allows you to run the DRIVETRAIN to a specific distance FORWARD in METERS
    targetPos = Distance that you want to travel
    power = power of DRIVETRAIN
    """
    # starting rotation
    startingEncoderTicks: float = robot.left_motor.getEncoder().getPosition()

    # the actual motor rotations = targetPos / drivetrainMeters
    actualRotation: float = (targetPos / drivetrainMeters)
    
    # convert the motor rotations into ticks
    actualTicks: float = (actualRotation * robot.TPR)

    # wait untill the encoder ticks on the robot == the wanted encoder ticks
    while actualTicks >= encoderTicksTraveled(startingEncoderTicks, robot.left_motor.getEncoder().getPosition()): 

        # make the drivetrain drive forward
        robot.drive.arcadeDrive (power, 0)

    # after the correct ticks are hit kill the drivetrain
    robot.drive.arcadeDrive(0,0)

def targetArmPos(self, targetPos, power):
    """
    this function allows you to turn the ARM to a specific distance in METERS
    targetPos = Distance that you want to the arm rotate
    power = power of ARM
    """
    # starting rotation
    startingEncoderTicks: float = robot.arm.getEncoder().getPosition()

    # the actual motor rotations = targetPos / armMeter
    actualRotation: float = (targetPos / armMeter)
    
    # convert the motor rotations into ticks
    actualTicks: float = (actualRotation * robot.TPR)

    # wait untill the encoder ticks on the robot == the wanted encoder ticks
    while actualTicks >= encoderTicksTraveled(startingEncoderTicks, robot.arm.getEncoder().getPosition()): 

        # make the drivetrain drive forward
        robot.arm.set(power)

    # after the correct ticks are hit kill the drivetrain
    robot.arm.set(0)
    
def targetIntakeRotation(self, targetRotation, power):

    # description of the function
    """ 
    this function allows you to spin the INTAKE forward for a specific # of rotations

    power = power of INTAKE. 
    
    targetRotations is the amount of turns you want the intake wheel to make
    """
    # starting rotation
    startingEncoderTicks: float = robot.intake.getEncoder().getPosition()

    # theoretical rotations * gear ratio = actual rotations
    actualRotation: float = (targetRotation * (1/robot.INTAKE_GEAR_RATIO))

    # convert actual rotations to actual Ticks of the encoder
    actualTicks: float = actualRotation * robot.TPR # NOTE: ticks in a rotation is 4096 this is according to the rev hardware manager

    # if we have not hit the rotation amount continue untill we are (loop untill we hit the amount)
    while actualRotation >= encoderTicksTraveled(startingEncoderTicks, robot.intake.getEncoder().getPosition()):

        # drives the robot forward at the POWER that you define in the call of the function
        robot.intake.set(power) 

    # after the while loop exits (IE the INTAKE has spun the correct amount of rotations) stop the intake
    robot.intake.set(0)

def rotationToInch(diamater: float, gear_ratio: float):
    return (2.0 * gear_ratio * (1/diamater))

def encoderTicksTraveled(startingTick: float, currentTick: float):
    """
    this function allows you to find the amount of encoder ticks that have encured after the startingTick

    startingTick = the tick at the begining of the function

    currentTick = the tick at the time of function call "robot.motor.getEncoder"
    """
    # takes the current tick and minses the starting tick to find the tricks that are traveled 
    ticksTraveled: float = (currentTick - startingTick)

    # returns the ticksTravleled variable to be used
    return ticksTraveled