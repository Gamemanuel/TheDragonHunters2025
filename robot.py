import wpilib as wp # type: ignore
from wpilib import SmartDashboard as sd # type: ignore
from robot_code.robot_configs.R2025.RobotConfig import RobotConfig
from robot_code.constants import *


class MyRobot(wp.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.cameraserver = wp.CameraServer()
        self.cameraserver.launch("testVision.py:main")
        self.TURN_MULT: float = 0.5

        self.robot: RobotConfig = RobotConfig()
        self.robot.resetNavx()

        self.elevatorPos: int = 0
        self.armPos: int = 0
        self.intakeSpeed: float = 0
        self.drivetrainWheelDiameter: int = 6

        # every rotation of the motor the corresponding value is the distance traveled
        self.drivetrainMeters: float = inch_to_meter(self.robot.DRIVETRAIN_WHEEL_DIAMATER, self.robot.DRIVETRAIN_GEAR_RATIO) # 2 is radians to the gear ratio (8.46) to in (/6) to meters * 100
        self.armMeter: float = inch_to_meter(self.robot.ARM_WHEEL_DIAMATER, self.robot.ARM_GEAR_RATIO)  
        self.intakeMeter: float = inch_to_meter(self.robot.INTAKE_WHEEL_DIAMATER, self.robot.INTAKE_GEAR_RATIO)
        self.elevatorMeter: float = inch_to_meter(self.robot.ELEVATOR_WHEEL_DIAMATER, self.robot.ELEVATOR_GEAR_RATIO)

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.robot.setDriveIdleMode(BRAKE)
        self.robot.resetNavx()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.robot.drive.arcadeDrive(
            .5, 0
        )
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
        """ this function allows you to run the ELEVATOR to a specific distance UP in METERS
        targetPos = Distance that you want to travel
        power = power of ELEVAROR"""
        pass
        # 1 motor rotation = distancevar
        # rotations =  targetpos / distancevar
        # 4092 encoder ticks = 1 rotation

    def targetDrivetrainPos(self, targetPos, power):
        """ this function allows you to run the DRIVETRAIN to a specific distance FORWARD in METERS
        targetPos = Distance that you want to travel
        power = power of DRIVETRAIN"""
        #  
        # while 
        pass

    def targetArmPos(self, targetPos, power):
        """ this function allows you to turn the ARM to a specific distance in METERS
        targetPos = Distance that you want to the arm rotate
        power = power of ARM"""
        pass

    def targetIntakePos(self, targetPos, power):
        """ this function allows you to spin the INTAKE to a specific distance in METERS
        power = power of INTAKE"""
        pass

    def targetIntakeRotation(self, targetRotation, power):
        """ this function allows you to spin the INTAKE forward for a specific # of rotations
        power = power of INTAKE"""
        # target rotation is in rotations and is the wanted acutal rotation
        # ticks in a rotation is 4096
        # theoretical rotations * gear ratio = actual rotations
        self.actualRotation: float = (targetRotation * (1/self.robot.INTAKE_GEAR_RATIO))
        # wheel spin roation = wheel distance in meters/ circumphrence in meters
        while self.actualRotation <= targetRotation: # if we have not hit the rotation amount continue
            self.robot.intake.set(power)
        self.robot.intake.set(0) # else stop the motors

def inch_to_meter(diamater: float, gear_ratio: float):
    return (2.0 * gear_ratio * 100 * (1/diamater) * (1/2.54))