import wpilib as wp # type: ignore
from wpilib import SmartDashboard as sd # type: ignore
from robot_code.robot_configs.R2025.RobotConfig import RobotConfig
from robot_code.constants import *
import math


class MyRobot(wp.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.cameraserver = wp.CameraServer()
        self.cameraserver.launch("vision.py:main")
        self.TURN_MULT: float = 0.5

        self.robot: RobotConfig = RobotConfig()
        self.robot.resetNavx()

        self.elevatorPos: int = 0
        self.armPos: int = 0
        self.intakeSpeed: float = 0
        self.drivetrainWheelDiameter: int = 6

        # every rotation of the motor the corresponding value is the distance traveled
        self.drivetrainMeters: float = rotationToInch(self.robot.DRIVETRAIN_WHEEL_DIAMATER, self.robot.DRIVETRAIN_GEAR_RATIO) # 2 is radians to the gear ratio (8.46) to in (/6) to meters * 100
        self.armMeter: float = rotationToInch(self.robot.ARM_WHEEL_DIAMATER, self.robot.ARM_GEAR_RATIO)  
        self.intakeMeter: float = rotationToInch(self.robot.INTAKE_WHEEL_DIAMATER, self.robot.INTAKE_GEAR_RATIO)
        self.elevatorMeter: float = rotationToInch(self.robot.ELEVATOR_WHEEL_DIAMATER, self.robot.ELEVATOR_GEAR_RATIO)

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.robot.setDriveIdleMode(BRAKE)
        self.robot.resetNavx()
        # TODO: make all the motors set to BRAKE during auto init

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.robot.drive.arcadeDrive(.5, 0)
        #if self.isAutonomousEnabled() == True: 
        #    self.targetDrivetrainPos(5,.5)


    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        self.robot.setDriveIdleMode(COAST)
        self.robot.resetNavx()
        
    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        
        self.robot.drive.arcadeDrive(
            -self.robot.hunter.getLeftY() * 0.75, self.robot.hunter.getRightX() * 0.75
        )

        # if the left joysticks is moved up and down then the elevator goes up or down
        self.robot.elevator.set(self.robot.august.getLeftY() * 0.375)
        self.robot.elevator_follower.set(self.robot.august.getLeftY() * 0.375)

        # hold the elevator and elevator follower in the correct pos if the pos is not being changed
        if self.robot.august.getLeftY() == 0:
            self.robot.elevator.set(.20)
            self.robot.elevator_follower.set(.20)

        # intake code
        self.robot.intake.set((self.robot.august.getLeftTriggerAxis() *.75) - (self.robot.august.getRightTriggerAxis()))
            
        # arm code
        self.robot.arm.set(self.robot.august.getRightY()*.50)

    def targetElevatorPos(self, targetPos, power):
        """
        this function allows you to run the ELEVATOR to a specific distance UP in METERS
        targetPos = Distance that you want to travel
        power = power of ELEVAROR
        """
        # starting rotation
        startingEncoderTicks: float = self.robot.elevator.getEncoder().getPosition()

        # the actual motor rotations = targetPos / elevatorMeters
        self.actualRotation: float = targetPos / self.elevatorMeter

        # convert the motor rotations into ticks
        self.actualTicks: float = (self.actualRotation * self.robot.TPR)

        # wait untill the encoder ticks on the robot == the wanted encoder ticks
        while self.actualTicks >= encoderTicksTraveled(startingEncoderTicks, self.robot.elevator.getEncoder().getPosition()):

            # make the elevator move up
            self.robot.elevator.set(power)
            self.robot.elevator_follower.set(power)
        
        # after the correct ticks are hit kill the elevator
        self.robot.elevator.set(0)
        self.robot.elevator_follower.set(0)


    def targetDrivetrainPos(self, targetPos, power):
        """
        this function allows you to run the DRIVETRAIN to a specific distance FORWARD in METERS
        targetPos = Distance that you want to travel
        power = power of DRIVETRAIN
        """
        # starting rotation
        startingEncoderTicks: float = self.robot.left_motor.getEncoder().getPosition()

        # the actual motor rotations = targetPos / drivetrainMeters
        self.actualRotation: float = (targetPos / self.drivetrainMeters)
        
        # convert the motor rotations into ticks
        self.actualTicks: float = (self.actualRotation * self.robot.TPR)

        # wait untill the encoder ticks on the robot == the wanted encoder ticks
        while self.actualTicks >= encoderTicksTraveled(startingEncoderTicks, self.robot.left_motor.getEncoder().getPosition()): 

            # make the drivetrain drive forward
            self.robot.drive.arcadeDrive (power, 0)

        # after the correct ticks are hit kill the drivetrain
        self.robot.drive.arcadeDrive(0,0)

    def targetArmPos(self, targetPos, power):
        """
        this function allows you to turn the ARM to a specific distance in METERS
        targetPos = Distance that you want to the arm rotate
        power = power of ARM
        """
        # starting rotation
        startingEncoderTicks: float = self.robot.arm.getEncoder().getPosition()

        # the actual motor rotations = targetPos / armMeter
        self.actualRotation: float = (targetPos / self.armMeter)
        
        # convert the motor rotations into ticks
        self.actualTicks: float = (self.actualRotation * self.robot.TPR)

        # wait untill the encoder ticks on the robot == the wanted encoder ticks
        while self.actualTicks >= encoderTicksTraveled(startingEncoderTicks, self.robot.arm.getEncoder().getPosition()): 

            # make the drivetrain drive forward
            self.robot.arm.set(power)

        # after the correct ticks are hit kill the drivetrain
        self.robot.arm.set(0)
        
    def targetIntakeRotation(self, targetRotation, power):

        # description of the function
        """ 
        this function allows you to spin the INTAKE forward for a specific # of rotations

        power = power of INTAKE. 
        
        targetRotations is the amount of turns you want the intake wheel to make
        """
        # starting rotation
        startingEncoderTicks: float = self.robot.intake.getEncoder().getPosition()

        # theoretical rotations * gear ratio = actual rotations
        self.actualRotation: float = (targetRotation * (1/self.robot.INTAKE_GEAR_RATIO))

        # convert actual rotations to actual Ticks of the encoder
        self.actualTicks: float = self.actualRotation * self.robot.TPR # NOTE: ticks in a rotation is 4096 this is according to the rev hardware manager

        # if we have not hit the rotation amount continue untill we are (loop untill we hit the amount)
        while self.actualRotation >= encoderTicksTraveled(startingEncoderTicks, self.robot.intake.getEncoder().getPosition()):
    
            # drives the robot forward at the POWER that you define in the call of the function
            self.robot.intake.set(power) 

        # after the while loop exits (IE the INTAKE has spun the correct amount of rotations) stop the intake
        self.robot.intake.set(0)

def rotationToInch(diamater: float, gear_ratio: float):
    return (2.0 * gear_ratio * (1/diamater))

def encoderTicksTraveled(startingTick: float, currentTick: float):
    """
    this function allows you to find the amount of encoder ticks that have encured after the startingTick

    startingTick = the tick at the begining of the function

    currentTick = the tick at the time of function call "self.robot.motor.getEncoder"
    """
    # takes the current tick and minses the starting tick to find the tricks that are traveled 
    ticksTraveled: float = (currentTick - startingTick)

    # returns the ticksTravleled variable to be used
    return ticksTraveled