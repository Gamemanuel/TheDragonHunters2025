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

    def robotPeriodic(self):
        sd.putNumber("Z", self.robot.navx.getDisplacementZ())
        sd.putNumber("X", self.robot.navx.getDisplacementX())
        sd.putNumber("Y", self.robot.navx.getDisplacementY())
        sd.putNumber("LEFT", self.robot.left_motor.getID())
        sd.putNumber("LEFT-FOLLOW", self.robot.left_motor_follower.getID())
        sd.putNumber("RIGHT", self.robot.right_motor.getID())
        sd.putNumber("RIGHT-FOLLOW", self.robot.right_motor_follower.getID())
        sd.putBoolean("left follow", self.robot.left_motor_follower.getIsFollower())
        sd.putBoolean("right follow", self.robot.right_motor_follower.getIsFollower())
        sd.putNumber("Rotation", self.robot.navx.getRotation2d().cos())

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.robot.setDriveIdleMode(BRAKE)
        self.robot.resetNavx()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.robot.setDisplacementY(0.5, 1)
        self.robot.setRotation(0.33, 0.25)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        self.robot.setDriveIdleMode(COAST)
        self.robot.resetNavx()

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        SPEED_MULT = ((-self.robot.driver.getThrottle()) * 0.25) + 0.75
        
        self.robot.drive.arcadeDrive(
            self.robot.driver.getY()  * SPEED_MULT, -self.robot.driver.getX() * SPEED_MULT, False
        )
    