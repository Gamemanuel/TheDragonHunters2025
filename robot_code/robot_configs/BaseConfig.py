import wpilib as wp
import navx
from ..robot_utils.REVSparkMax import REVSparkMax
from ..constants import REVIdleMode, NO_SAFE_RESET, NO_PERSIST, REVERSE


class BaseConfig:
    """
    Base configuration for the robot.

    Initializes and manages robot components like the power distribution panel, NavX, and drive motors.
    """
    def __init__(self):
        """
        Initializes the base configuration.

        Sets up the power distribution panel, NavX, and initializes some motor lists.
        """
        # CAN ID
        power_distribution: int = 1

        # Power Distribution
        self.pd : wp.PowerDistribution = wp.PowerDistribution(power_distribution, wp.PowerDistribution.ModuleType.kRev)

        # NavX
        self.navx: navx.AHRS = navx.AHRS(navx.AHRS.NavXComType.kMXP_SPI)

        # Motor Lists
        self.drive_motors: list[REVSparkMax] = []
        self.follower_motors: list[tuple[REVSparkMax, REVSparkMax]] = []
        self.reversed_motors: list[REVSparkMax] = []

    def clearStickyFaults(self) -> None:
        """
        Clears sticky faults from the power distribution panel.
        """
        self.pd.clearStickyFaults()

    def resetNavx(self) -> None:
        """
        Resets the NavX displacement.
        """
        self.navx.reset()
        self.navx.resetDisplacement()
        self.navx.zeroYaw()

    def addDriveMotor(self, drive_motor: REVSparkMax) -> REVSparkMax:
        """
        Adds a drive motor to the list of drive motors.

        Args:
            drive_motor: The drive motor to add.

        Returns:
            The added drive motor.
        """
        self.drive_motors.append(drive_motor)
        return drive_motor

    def addFollowerMotor(self, leader: REVSparkMax, follower: REVSparkMax) -> None:
        """
        Adds a follower motor to the list of follower motors.

        The follower motor will follow the leader motor's output.
        Args:
            leader: The leader motor.
            follower: The follower motor.

        Raises:
            ValueError: If the leader and follower have the same CAN ID.
        """
        if leader.getID() == follower.getID(): raise ValueError("CAN IDs must be different for leaders and followers")
        self.follower_motors.append((leader, follower))
        follower.setLeaderID(leader.getID())

    def addReversedMotor(self, reversed_motor: REVSparkMax) -> None:
        """
        Adds a reversed motor to the list of reversed motors.

        The reversed motor will have its direction inverted.
        Args:
            reversed_motor: The motor to reverse.
        """
        self.reversed_motors.append(reversed_motor)
        reversed_motor.setDirection(REVERSE)

    def setDriveIdleMode(self, idle_mode: REVIdleMode) -> None:
        """
        Sets the idle mode for all drive motors.

        Args:
            idle_mode: The idle mode to set.

        Raises:
            ValueError: If no drive motors are configured.
        """
        if len(self.drive_motors) == 0: raise ValueError("You have 0 drive motors configured")

        for motor in self.drive_motors:
            motor.setIdleMode(idle_mode)
            motor.setConfig(NO_SAFE_RESET, NO_PERSIST)
    