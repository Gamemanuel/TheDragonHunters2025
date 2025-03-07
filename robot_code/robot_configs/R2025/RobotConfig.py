from ..BaseConfig import BaseConfig
from ...robot_utils.REVSparkMax import REVSparkMax
from ...constants import *
import wpilib.drive as wpd
import wpilib as wp
from ...robot_utils.Logitech_X3D_Joystick import LogitechX3D


class RobotConfig(BaseConfig):
    """
    Robot configuration for the 2025 robot.

    Initializes and configures robot-specific components and controllers.
    """
    def __init__(self):
        """
        Initializes the robot configuration.

        Sets up drive motors, controllers, and other robot-specific hardware.
        """
        super().__init__()
        
        # CAN ID
        left_motor          : int = 2
        left_motor_follower : int = 3
        right_motor         : int = 4
        right_motor_follower: int = 5
        
        # Drive Motors
        self.left_motor          : REVSparkMax = self.addDriveMotor(REVSparkMax(left_motor, BRUSHLESS))
        self.left_motor_follower : REVSparkMax = self.addDriveMotor(REVSparkMax(left_motor_follower, BRUSHLESS))
        self.right_motor         : REVSparkMax = self.addDriveMotor(REVSparkMax(right_motor, BRUSHLESS))
        self.right_motor_follower: REVSparkMax = self.addDriveMotor(REVSparkMax(right_motor_follower, BRUSHLESS))
        
        # Follower Motors
        self.addFollowerMotor(self.left_motor, self.left_motor_follower)
        self.addFollowerMotor(self.right_motor, self.right_motor_follower)
        
        # Reversed Motors
        self.addReversedMotor(self.left_motor)
        self.addReversedMotor(self.left_motor_follower)
        
        # Differential Drive
        self.drive: wpd.DifferentialDrive = wpd.DifferentialDrive(self.left_motor, self.right_motor)
        
        # Controllers
        self.driver: LogitechX3D = LogitechX3D(0)
    
    def setDisplacementY(self, power: float, displacement: float) -> None:
        if -self.navx.getDisplacementY() <= displacement:
            self.drive.tankDrive(-power, -power, False)
    
    def getDisplacementY(self) -> float:
        return self.navx.getDisplacementY()
    
        
    def setRotation(self, power: float, rotation: float) -> None:
        if self.navx.getRotation2d().cos() >= rotation:
            self.drive.tankDrive(power, -power, False)

    def getRotation(self) -> float:
        return self.navx.getRotation2d()
        