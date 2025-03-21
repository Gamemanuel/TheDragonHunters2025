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
        self.drivetrainWheelDiameter: int = 6

        # every rotation of the motor the corresponding value is the distance traveled
        self.drivetrainMeters: float = (2 * 8.46 * 100 / 2.54 / self.drivetrainWheelDiameter) # 2 is radians to the gear ratio (8.46) to in (/6) to meters * 100
        self.armMeter: float = (2 * 216 * 100 / 33.857 / 2.54)
        self.intakeMeter: float = (2 * 9 * 100 / 4 / 2.54)
        self.elevatorMeter: float = (2 * 8 * 100 / 2.54 / 1.910)

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

    def targetElevatorPos(self, targetPos):
        pass
        # 1 motor rotation = distancevar
        # target pos = 

    def targetDrivetrainPos(self, targetPos):
        pass

    def targetArmPos(self, targetPos):
        pass

    def targetIntakePos(self, targetPos):
        pass
