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
        # inits the camera
        self.cameraserver = wp.CameraServer()
        self.cameraserver.launch("vision.py:main")

        # allows us to use the self.robot term to controll the robot functions
        self.robot: RobotConfig = RobotConfig()

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        # set all motors to BRAKE
        self.robot.setDriveIdleMode(BRAKE)

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        # set all motors to COAST
        self.robot.setDriveIdleMode(COAST)
        
    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        
        # drive code for teleop
        self.robot.drive.arcadeDrive(-self.robot.hunter.getLeftY() * 0.75, self.robot.hunter.getRightX() * 0.75)

        # elevator code  

        # if the left joysticks is moved up and down then the elevator goes up or down
        self.elevatorMove(self.robot.august.getLeftY() * 0.375)

        # hold the elevator and elevator follower in the correct pos if the pos is not being changed
        if self.robot.august.getLeftY() == 0:self.elevatorMove(.20)
        
        # intake code
        self.robot.intake.set((self.robot.august.getLeftTriggerAxis() *.75) - (self.robot.august.getRightTriggerAxis()))
            
        # arm code
        self.robot.arm.set(self.robot.august.getRightY()*.50)

    # moves the elevator and elevator_follower motors
    def elevatorMove(self, power):
        self.robot.elevator.set(power)
        self.robot.elevator_follower.set(power)

    def driveForwardForDistance(self, wantedDistance: float, speed: float):
        """
        Allows you to drive forward or backward with a six wheel

        wantedDistance is the distance you want to drive if you want backwards then you make the value negative

        speed is how fast the robot is driving. NOTE: if you want to go backwards then you apply the negative value to the wanted distance
        """
        # calculate power (negative or positive)
        if wantedDistance == -abs(wantedDistance): # if wantedDistance is negative then next
            self.power: float = -speed
        else:
            self.power: float = speed

        # if the speed is negative set the power to negative
        if speed == -abs(speed):
            self.power = -speed

             
