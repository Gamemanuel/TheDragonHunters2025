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
        self.cameraserver.launch("vision.py:main")
        self.TURN_MULT: float = 0.5

        self.robot: RobotConfig = RobotConfig()
        self.robot.resetNavx()

        self.elevatorPos: int = 0
        self.armPos: int = 0
        self.intakeSpeed: float = 0
        # self.HangPos: int = 0 

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.robot.setDriveIdleMode(BRAKE)
        self.robot.resetNavx()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.robot.setDisplacementZ(-0.25, .001) 
        # self.robot.setRotation(0.33, 0.25)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        self.robot.setDriveIdleMode(COAST)
        self.robot.resetNavx()
        
    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        
        # TODO: add a toogle for speed 

        self.robot.drive.arcadeDrive(
            -self.robot.hunter.getLeftY() * 0.70, self.robot.hunter.getRightX() * 0.70
        )

        # if the left joysticks is moved up and down then the elevator goes up or down
        self.robot.elevator.set(self.robot.august.getLeftY() * 0.375)
        self.robot.elevator_follower.set(self.robot.august.getLeftY() * 0.375)
        # TODO: add it slower going down bu .50 going up
        elevatorEncoder: float = self.robot.elevator.getEncoder

        # hold the elevator and elevator follower in the correct pos if the pos is not being changed

        # zack's terrible method
        if self.robot.august.getLeftY() == 0:
            self.robot.elevator.set(.20)
            self.robot.elevator_follower.set(.20)

        # gavin's better method
        #TODO: add the better method ie make the code "motor break"
