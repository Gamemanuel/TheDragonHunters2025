import wpilib as wp
from wpilib import SmartDashboard as sd
from robot_code.robot_configs.R2025.RobotConfig import RobotConfig
from robot_code.constants import *


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
        self.intakeSpeed: int = 0

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.robot.setDriveIdleMode(BRAKE)
        self.robot.resetNavx()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.robot.setDisplacementY(0.5, 1)
        # self.robot.setRotation(0.33, 0.25)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        self.robot.setDriveIdleMode(COAST)
        self.robot.resetNavx()
    

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        #SPEED_MULT = ((-self.robot.driver.getThrottle()) * 0.25) + 0.75
        
        self.robot.drive.arcadeDrive(
            -self.robot.hunter.getLeftY(), self.robot.hunter.getRightX()
        )

        # if the left joysticks is moved up and down then the elevator goes up or down
        if self.robot.august.getLeftY() != 0:
            self.elevatorPos = self.elevatorPos + self.robot.august.getLeftY()
            self.robot.elevator.set(self.elevatorPos)

        # if the right joystick is moved up and down the arm that holds the intake moves up or down
        if self.robot.august.getRightY() != 0:
            self.armPos = self.armPos + self.robot.august.getRightY()
            self.robot.arm.set(self.armPos)

        # if the left trigger is pressed then the intake spins in reverse
        if self.robot.august.getLeftTriggerAxis() != 0:
            self.intakeSpeed = self.intakeSpeed - self.robot.august.getLeftTriggerAxis()
        else: 
            self.intakeSpeed = 0

        # if the right trigger is pressed the intake spins forwards
        if self.robot.august.getRightTriggerAxis() != 0:
            self.intakeSpeed = self.intakeSpeed + self.robot.august.getRightTriggerAxis()
        else: 
            self.intakeSpeed = 0   