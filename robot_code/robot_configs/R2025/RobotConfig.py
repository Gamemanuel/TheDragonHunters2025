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
        left_motor_follower : int = 10
        right_motor         : int = 4
        right_motor_follower: int = 5
        elevator            : int = 6 
        elevator_follower   : int = 7 
        arm                 : int = 9 
        intake              : float = 8 
        #hang                : int = 10 #TODO: check the actual config on the bot for this motor / the robot does not have a hang so not nessisarry
        
        # Drive Motors
        self.left_motor          : REVSparkMax = self.addDriveMotor(REVSparkMax(left_motor, BRUSHLESS))
        self.left_motor_follower : REVSparkMax = self.addDriveMotor(REVSparkMax(left_motor_follower, BRUSHLESS))
        self.right_motor         : REVSparkMax = self.addDriveMotor(REVSparkMax(right_motor, BRUSHLESS))
        self.right_motor_follower: REVSparkMax = self.addDriveMotor(REVSparkMax(right_motor_follower, BRUSHLESS))
        self.elevator            : REVSparkMax = REVSparkMax(elevator, BRUSHLESS)
        self.elevator_follower   : REVSparkMax = REVSparkMax(elevator_follower, BRUSHLESS)
        self.arm                 : REVSparkMax = REVSparkMax(arm, BRUSHLESS)       
        self.intake              : REVSparkMax = REVSparkMax(intake, BRUSHLESS)   
        self.hang                : REVSparkMax = REVSparkMax(hang, BRUSHLESS)    

        # Follower Motors
        self.addFollowerMotor(self.left_motor, self.left_motor_follower)
        self.addFollowerMotor(self.right_motor, self.right_motor_follower)
        self.addFollowerMotor(self.elevator, self.elevator_follower)
        
        # Reversed Motors
        self.addReversedMotor(self.left_motor)
        self.addReversedMotor(self.left_motor_follower)
        
        # Differential Drive
        self.drive: wpd.DifferentialDrive = wpd.DifferentialDrive(self.left_motor, self.right_motor)
        
        # Controllers
        self.hunter: wp.XboxController = wp.XboxController(0)
        self.august: wp.XboxController = wp.XboxController(1)

        # set elevator as BRAKE
        self.elevator.setIdleMode(BRAKE)
        self.elevator_follower.setIdleMode(BRAKE)

    
    def setDisplacementZ(self, power: float, displacement: float) -> None:
        if -self.navx.getDisplacementZ() <= displacement:
            self.drive.tankDrive(-power, -power, False)

    def setDisplacementY(self, power: float, displacement: float) -> None:
        if -self.navx.getDisplacementY() <= displacement:
            self.drive.tankDrive(-power, -power, False)

    def setDisplacementX(self, power: float, displacement: float) -> None:
        if -self.navx.getDisplacementX() <= displacement:
            self.drive.tankDrive(-power, -power, False)
    
    def getDisplacementY(self) -> float:
        return self.navx.getDisplacementY()
    
        
    def setRotation(self, power: float, rotation: float) -> None:
        if self.navx.getRotation2d().cos() >= rotation:
            self.drive.tankDrive(power, -power, False)

    def getRotation(self) -> float:
        return self.navx.getRotation2d()
        