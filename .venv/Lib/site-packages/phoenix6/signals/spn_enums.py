"""
Copyright (C) Cross The Road Electronics.  All rights reserved.
License information can be found in CTRE_LICENSE.txt
For support and suggestions contact support@ctr-electronics.com or file
an issue tracker at https://github.com/CrossTheRoadElec/Phoenix-Releases
"""

from enum import Enum


class System_StateValue(Enum):
    """
    System state of the device.
    """
    BOOTUP_0 = 0
    BOOTUP_1 = 1
    BOOTUP_2 = 2
    BOOTUP_3 = 3
    BOOTUP_4 = 4
    BOOTUP_5 = 5
    BOOTUP_6 = 6
    BOOTUP_7 = 7
    BOOT_BEEP = 8
    CONTROL_DISABLED = 9
    CONTROL_ENABLED = 10
    CONTROL_ENABLED_11 = 11
    FAULT = 12
    RECOVER = 13
    NOT_LICENSED = 14
    PRODUCTION = 15


class IsPROLicensedValue(Enum):
    """
    Whether the device is Pro licensed.
    """
    NOT_LICENSED = 0
    LICENSED = 1


class Licensing_IsSeasonPassedValue(Enum):
    """
    Whether the device is Season Pass licensed.
    """
    NOT_LICENSED = 0
    LICENSED = 1


class SensorDirectionValue(Enum):
    """
    Direction of the sensor to determine positive rotation, as seen facing the LED
    side of the CANcoder.
    """
    COUNTER_CLOCKWISE_POSITIVE = 0
    """
    Counter-clockwise motion reports positive rotation.
    """
    CLOCKWISE_POSITIVE = 1
    """
    Clockwise motion reports positive rotation.
    """


class FrcLockValue(Enum):
    """
    Whether device is locked by FRC.
    """
    FRC_LOCKED = 1
    FRC_UNLOCKED = 0


class RobotEnableValue(Enum):
    """
    Whether the robot is enabled.
    """
    ENABLED = 1
    DISABLED = 0


class Led1OnColorValue(Enum):
    """
    The Color of LED1 when it's "On".
    """
    OFF = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    WHITE = 7


class Led1OffColorValue(Enum):
    """
    The Color of LED1 when it's "Off".
    """
    OFF = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    WHITE = 7


class Led2OnColorValue(Enum):
    """
    The Color of LED2 when it's "On".
    """
    OFF = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    WHITE = 7


class Led2OffColorValue(Enum):
    """
    The Color of LED2 when it's "Off".
    """
    OFF = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    WHITE = 7


class DeviceEnableValue(Enum):
    """
    Whether the device is enabled.
    """
    ENABLED = 1
    DISABLED = 0


class ForwardLimitValue(Enum):
    """
    Forward Limit Pin.
    """
    CLOSED_TO_GROUND = 0
    OPEN = 1


class ReverseLimitValue(Enum):
    """
    Reverse Limit Pin.
    """
    CLOSED_TO_GROUND = 0
    OPEN = 1


class AppliedRotorPolarityValue(Enum):
    """
    The applied rotor polarity as seen from the front of the motor.  This typically
    is determined by the Inverted config, but can be overridden if using Follower
    features.
    """
    POSITIVE_IS_COUNTER_CLOCKWISE = 0
    """
    Positive motor output results in counter-clockwise motion.
    """
    POSITIVE_IS_CLOCKWISE = 1
    """
    Positive motor output results in clockwise motion.
    """


class ControlModeValue(Enum):
    """
    The active control mode of the motor controller.
    """
    DISABLED_OUTPUT = 0
    NEUTRAL_OUT = 1
    STATIC_BRAKE = 2
    DUTY_CYCLE_OUT = 3
    POSITION_DUTY_CYCLE = 4
    VELOCITY_DUTY_CYCLE = 5
    MOTION_MAGIC_DUTY_CYCLE = 6
    DUTY_CYCLE_FOC = 7
    POSITION_DUTY_CYCLE_FOC = 8
    VELOCITY_DUTY_CYCLE_FOC = 9
    MOTION_MAGIC_DUTY_CYCLE_FOC = 10
    VOLTAGE_OUT = 11
    POSITION_VOLTAGE = 12
    VELOCITY_VOLTAGE = 13
    MOTION_MAGIC_VOLTAGE = 14
    VOLTAGE_FOC = 15
    POSITION_VOLTAGE_FOC = 16
    VELOCITY_VOLTAGE_FOC = 17
    MOTION_MAGIC_VOLTAGE_FOC = 18
    TORQUE_CURRENT_FOC = 19
    POSITION_TORQUE_CURRENT_FOC = 20
    VELOCITY_TORQUE_CURRENT_FOC = 21
    MOTION_MAGIC_TORQUE_CURRENT_FOC = 22
    FOLLOWER = 23
    RESERVED = 24
    COAST_OUT = 25
    UNAUTHORIZED_DEVICE = 26
    MUSIC_TONE = 27
    MOTION_MAGIC_VELOCITY_DUTY_CYCLE = 28
    MOTION_MAGIC_VELOCITY_DUTY_CYCLE_FOC = 29
    MOTION_MAGIC_VELOCITY_VOLTAGE = 30
    MOTION_MAGIC_VELOCITY_VOLTAGE_FOC = 31
    MOTION_MAGIC_VELOCITY_TORQUE_CURRENT_FOC = 32
    MOTION_MAGIC_EXPO_DUTY_CYCLE = 33
    MOTION_MAGIC_EXPO_DUTY_CYCLE_FOC = 34
    MOTION_MAGIC_EXPO_VOLTAGE = 35
    MOTION_MAGIC_EXPO_VOLTAGE_FOC = 36
    MOTION_MAGIC_EXPO_TORQUE_CURRENT_FOC = 37


class MotionMagicIsRunningValue(Enum):
    """
    Check if Motion Magic® is running.  This is equivalent to checking that the
    reported control mode is a Motion Magic® based mode.
    """
    ENABLED = 1
    DISABLED = 0


class PIDRefPIDErr_ClosedLoopModeValue(Enum):
    """
    Whether the closed-loop is running on position or velocity.
    """
    POSITION = 0
    VELOCITY = 1


class PIDOutput_PIDOutputModeValue(Enum):
    """
    The output mode of the PID controller.
    """
    DUTY_CYCLE = 0
    VOLTAGE = 1
    TORQUE_CURRENT_FOC = 2


class PIDRefSlopeECUTime_ClosedLoopModeValue(Enum):
    """
    Whether the closed-loop is running on position or velocity.
    """
    POSITION = 0
    VELOCITY = 1


class MotorOutputStatusValue(Enum):
    """
    Assess the status of the motor output with respect to load and supply.
    
    This routine can be used to determine the general status of motor commutation.
    """
    UNKNOWN = 0
    """
    The status of motor output could not be determined.
    """
    OFF = 1
    """
    Motor output is disabled.
    """
    STATIC_BRAKING = 2
    """
    The motor is in neutral-brake.
    """
    MOTORING = 3
    """
    The motor is loaded in a typical fashion, drawing current from the supply, and
    successfully turning the rotor in the direction of applied voltage.
    """
    DISCORDANT_MOTORING = 4
    """
    The same as Motoring, except the rotor is being backdriven as the motor output
    is not enough to defeat load forces.
    """
    REGEN_BRAKING = 5
    """
    The motor is braking in such a way where motor current is traveling back to the
    supply (typically a battery).
    """


class DifferentialControlModeValue(Enum):
    """
    The active control mode of the differential controller.
    """
    DISABLED_OUTPUT = 0
    NEUTRAL_OUT = 1
    STATIC_BRAKE = 2
    DUTY_CYCLE_OUT = 3
    POSITION_DUTY_CYCLE = 4
    VELOCITY_DUTY_CYCLE = 5
    MOTION_MAGIC_DUTY_CYCLE = 6
    DUTY_CYCLE_FOC = 7
    POSITION_DUTY_CYCLE_FOC = 8
    VELOCITY_DUTY_CYCLE_FOC = 9
    MOTION_MAGIC_DUTY_CYCLE_FOC = 10
    VOLTAGE_OUT = 11
    POSITION_VOLTAGE = 12
    VELOCITY_VOLTAGE = 13
    MOTION_MAGIC_VOLTAGE = 14
    VOLTAGE_FOC = 15
    POSITION_VOLTAGE_FOC = 16
    VELOCITY_VOLTAGE_FOC = 17
    MOTION_MAGIC_VOLTAGE_FOC = 18
    TORQUE_CURRENT_FOC = 19
    POSITION_TORQUE_CURRENT_FOC = 20
    VELOCITY_TORQUE_CURRENT_FOC = 21
    MOTION_MAGIC_TORQUE_CURRENT_FOC = 22
    FOLLOWER = 23
    RESERVED = 24
    COAST_OUT = 25


class DiffPIDRefPIDErr_ClosedLoopModeValue(Enum):
    """
    Whether the closed-loop is running on position or velocity.
    """
    POSITION = 0
    VELOCITY = 1


class DiffPIDOutput_PIDOutputModeValue(Enum):
    """
    The output mode of the differential PID controller.
    """
    DUTY_CYCLE = 0
    VOLTAGE = 1
    TORQUE_CURRENT_FOC = 2


class DiffPIDRefSlopeECUTime_ClosedLoopModeValue(Enum):
    """
    Whether the closed-loop is running on position or velocity.
    """
    POSITION = 0
    VELOCITY = 1


class GravityTypeValue(Enum):
    """
    Gravity Feedforward/Feedback Type.
    
    This determines the type of the gravity feedforward/feedback.
    
    Choose Elevator_Static for systems where the gravity feedforward is constant,
    such as an elevator. The gravity feedforward output will always have the same
    sign.
    
    Choose Arm_Cosine for systems where the gravity feedback is dependent on the
    angular position of the mechanism, such as an arm. The gravity feedback output
    will vary depending on the mechanism angular position. Note that the sensor
    offset and ratios must be configured so that the sensor reports a position of 0
    when the mechanism is horizonal (parallel to the ground), and the reported
    sensor position is 1:1 with the mechanism.
    """
    ELEVATOR_STATIC = 0
    """
    The system's gravity feedforward is constant, such as an elevator. The gravity
    feedforward output will always have the same sign.
    """
    ARM_COSINE = 1
    """
    The system's gravity feedback is dependent on the angular position of the
    mechanism, such as an arm. The gravity feedback output will vary depending on
    the mechanism angular position. Note that the sensor offset and ratios must be
    configured so that the sensor reports a position of 0 when the mechanism is
    horizonal (parallel to the ground), and the reported sensor position is 1:1 with
    the mechanism.
    """


class InvertedValue(Enum):
    """
    Invert state of the device as seen from the front of the motor.
    """
    COUNTER_CLOCKWISE_POSITIVE = 0
    """
    Positive motor output results in clockwise motion.
    """
    CLOCKWISE_POSITIVE = 1
    """
    Positive motor output results in counter-clockwise motion.
    """


class NeutralModeValue(Enum):
    """
    The state of the motor controller bridge when output is neutral or disabled.
    """
    COAST = 0
    BRAKE = 1


class FeedbackSensorSourceValue(Enum):
    """
    Choose what sensor source is reported via API and used by closed-loop and limit
    features.  The default is RotorSensor, which uses the internal rotor sensor in
    the Talon.
    
    Choose RemoteCANcoder to use another CANcoder on the same CAN bus (this also
    requires setting FeedbackRemoteSensorID).  Talon will update its position and
    velocity whenever CANcoder publishes its information on CAN bus, and the Talon
    internal rotor will not be used.
    
    Choose FusedCANcoder (requires Phoenix Pro) and Talon will fuse another
    CANcoder's information with the internal rotor, which provides the best possible
    position and velocity for accuracy and bandwidth (this also requires setting
    FeedbackRemoteSensorID).  FusedCANcoder was developed for applications such as
    swerve-azimuth.
    
    Choose SyncCANcoder (requires Phoenix Pro) and Talon will synchronize its
    internal rotor position against another CANcoder, then continue to use the rotor
    sensor for closed loop control (this also requires setting
    FeedbackRemoteSensorID).  The Talon will report if its internal position differs
    significantly from the reported CANcoder position.  SyncCANcoder was developed
    for mechanisms where there is a risk of the CANcoder failing in such a way that
    it reports a position that does not match the mechanism, such as the sensor
    mounting assembly breaking off.
    
    Choose RemotePigeon2_Yaw, RemotePigeon2_Pitch, and RemotePigeon2_Roll to use
    another Pigeon2 on the same CAN bus (this also requires setting
    FeedbackRemoteSensorID).  Talon will update its position to match the selected
    value whenever Pigeon2 publishes its information on CAN bus. Note that the Talon
    position will be in rotations and not degrees.
    
    Note: When the feedback source is changed to FusedCANcoder or SyncCANcoder, the
    Talon needs a period of time to fuse before sensor-based (soft-limit, closed
    loop, etc.) features are used. This period of time is determined by the update
    frequency of the CANcoder's Position signal.
    """
    ROTOR_SENSOR = 0
    """
    Use the internal rotor sensor in the Talon.
    """
    REMOTE_CANCODER = 1
    """
    Use another CANcoder on the same CAN bus (this also requires setting
    FeedbackRemoteSensorID).  Talon will update its position and velocity whenever
    CANcoder publishes its information on CAN bus, and the Talon internal rotor will
    not be used.
    """
    REMOTE_PIGEON2_YAW = 2
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    FeedbackRemoteSensorID).  Talon will update its position to match the Pigeon2
    yaw whenever Pigeon2 publishes its information on CAN bus. Note that the Talon
    position will be in rotations and not degrees.
    """
    REMOTE_PIGEON2_PITCH = 3
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    FeedbackRemoteSensorID).  Talon will update its position to match the Pigeon2
    pitch whenever Pigeon2 publishes its information on CAN bus. Note that the Talon
    position will be in rotations and not degrees.
    """
    REMOTE_PIGEON2_ROLL = 4
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    FeedbackRemoteSensorID).  Talon will update its position to match the Pigeon2
    roll whenever Pigeon2 publishes its information on CAN bus. Note that the Talon
    position will be in rotations and not degrees.
    """
    FUSED_CANCODER = 5
    """
    Requires Phoenix Pro; Talon will fuse another CANcoder's information with the
    internal rotor, which provides the best possible position and velocity for
    accuracy and bandwidth (this also requires setting FeedbackRemoteSensorID). 
    FusedCANcoder was developed for applications such as swerve-azimuth.
    """
    SYNC_CANCODER = 6
    """
    Requires Phoenix Pro; Talon will synchronize its internal rotor position against
    another CANcoder, then continue to use the rotor sensor for closed loop control
    (this also requires setting FeedbackRemoteSensorID).  The Talon will report if
    its internal position differs significantly from the reported CANcoder position.
     SyncCANcoder was developed for mechanisms where there is a risk of the CANcoder
    failing in such a way that it reports a position that does not match the
    mechanism, such as the sensor mounting assembly breaking off.
    """


class ForwardLimitTypeValue(Enum):
    """
    Determines if the forward limit switch is normally-open (default) or
    normally-closed.
    """
    NORMALLY_OPEN = 0
    NORMALLY_CLOSED = 1


class ForwardLimitSourceValue(Enum):
    """
    Determines where to poll the forward limit switch.  This defaults to the forward
    limit switch pin on the limit switch connector.
    
    Choose RemoteTalonFX to use the forward limit switch attached to another Talon
    FX on the same CAN bus (this also requires setting ForwardLimitRemoteSensorID).
    
    Choose RemoteCANifier to use the forward limit switch attached to another
    CANifier on the same CAN bus (this also requires setting
    ForwardLimitRemoteSensorID).
    
    Choose RemoteCANcoder to use another CANcoder on the same CAN bus (this also
    requires setting ForwardLimitRemoteSensorID).  The forward limit will assert
    when the CANcoder magnet strength changes from BAD (red) to ADEQUATE (orange) or
    GOOD (green).
    """
    LIMIT_SWITCH_PIN = 0
    """
    Use the forward limit switch pin on the limit switch connector.
    """
    REMOTE_TALON_FX = 1
    """
    Use the forward limit switch attached to another Talon FX on the same CAN bus
    (this also requires setting ForwardLimitRemoteSensorID).
    """
    REMOTE_CANIFIER = 2
    """
    Use the forward limit switch attached to another CANifier on the same CAN bus
    (this also requires setting ForwardLimitRemoteSensorID).
    """
    REMOTE_CANCODER = 4
    """
    Use another CANcoder on the same CAN bus (this also requires setting
    ForwardLimitRemoteSensorID).  The forward limit will assert when the CANcoder
    magnet strength changes from BAD (red) to ADEQUATE (orange) or GOOD (green).
    """
    REMOTE_CANRANGE = 6
    """
    Use another CANrange on the same CAN bus (this also requires setting
    ForwardLimitRemoteSensorID).  The forward limit will assert when the CANrange
    proximity detect is tripped.
    """
    DISABLED = 3
    """
    Disable the forward limit switch.
    """


class ReverseLimitTypeValue(Enum):
    """
    Determines if the reverse limit switch is normally-open (default) or
    normally-closed.
    """
    NORMALLY_OPEN = 0
    NORMALLY_CLOSED = 1


class ReverseLimitSourceValue(Enum):
    """
    Determines where to poll the reverse limit switch.  This defaults to the reverse
    limit switch pin on the limit switch connector.
    
    Choose RemoteTalonFX to use the reverse limit switch attached to another Talon
    FX on the same CAN bus (this also requires setting ReverseLimitRemoteSensorID).
    
    Choose RemoteCANifier to use the reverse limit switch attached to another
    CANifier on the same CAN bus (this also requires setting
    ReverseLimitRemoteSensorID).
    
    Choose RemoteCANcoder to use another CANcoder on the same CAN bus (this also
    requires setting ReverseLimitRemoteSensorID).  The reverse limit will assert
    when the CANcoder magnet strength changes from BAD (red) to ADEQUATE (orange) or
    GOOD (green).
    """
    LIMIT_SWITCH_PIN = 0
    """
    Use the reverse limit switch pin on the limit switch connector.
    """
    REMOTE_TALON_FX = 1
    """
    Use the reverse limit switch attached to another Talon FX on the same CAN bus
    (this also requires setting ReverseLimitRemoteSensorID).
    """
    REMOTE_CANIFIER = 2
    """
    Use the reverse limit switch attached to another CANifier on the same CAN bus
    (this also requires setting ReverseLimitRemoteSensorID).
    """
    REMOTE_CANCODER = 4
    """
    Use another CANcoder on the same CAN bus (this also requires setting
    ReverseLimitRemoteSensorID).  The reverse limit will assert when the CANcoder
    magnet strength changes from BAD (red) to ADEQUATE (orange) or GOOD (green).
    """
    REMOTE_CANRANGE = 6
    """
    Use another CANrange on the same CAN bus (this also requires setting
    ReverseLimitRemoteSensorID).  The reverse limit will assert when the CANrange
    proximity detect is tripped.
    """
    DISABLED = 3
    """
    Disable the reverse limit switch.
    """


class MagnetHealthValue(Enum):
    """
    Magnet health as measured by CANcoder.
    
    Red indicates too close or too far, Orange is adequate but with reduced
    accuracy, green is ideal. Invalid means the accuracy cannot be determined.
    """
    MAGNET_RED = 1
    """
    The magnet is too close or too far from the CANcoder.
    """
    MAGNET_ORANGE = 2
    """
    Magnet health is adequate but with reduced accuracy.
    """
    MAGNET_GREEN = 3
    """
    Magnet health is ideal.
    """
    MAGNET_INVALID = 0
    """
    The accuracy cannot be determined.
    """


class BridgeOutputValue(Enum):
    """
    The applied output of the bridge.
    """
    BRIDGE_REQ_COAST = 0
    BRIDGE_REQ_BRAKE = 1
    BRIDGE_REQ_TRAPEZ = 6
    BRIDGE_REQ_FOCTORQUE = 7
    BRIDGE_REQ_MUSIC_TONE = 8
    BRIDGE_REQ_FOCEASY = 9
    BRIDGE_REQ_FAULT_BRAKE = 12
    BRIDGE_REQ_FAULT_COAST = 13
    BRIDGE_REQ_ACTIVE_BRAKE = 14


class DifferentialSensorSourceValue(Enum):
    """
    Choose what sensor source is used for differential control of a mechanism.  The
    default is Disabled.  All other options require setting the
    DifferentialTalonFXSensorID, as the average of this Talon FX's sensor and the
    remote TalonFX's sensor is used for the differential controller's primary
    targets.
    
    Choose RemoteTalonFX_Diff to use another TalonFX on the same CAN bus.  Talon FX
    will update its differential position and velocity whenever the remote TalonFX
    publishes its information on CAN bus.  The differential controller will use the
    difference between this TalonFX's sensor and the remote Talon FX's sensor for
    the differential component of the output.
    
    Choose RemotePigeon2_Yaw, RemotePigeon2_Pitch, and RemotePigeon2_Roll to use
    another Pigeon2 on the same CAN bus (this also requires setting
    DifferentialRemoteSensorID).  Talon FX will update its differential position to
    match the selected value whenever Pigeon2 publishes its information on CAN bus.
    Note that the Talon FX differential position will be in rotations and not
    degrees.
    
    Choose RemoteCANcoder to use another CANcoder on the same CAN bus (this also
    requires setting DifferentialRemoteSensorID).  Talon FX will update its
    differential position and velocity to match the CANcoder whenever CANcoder
    publishes its information on CAN bus.
    """
    DISABLED = 0
    """
    Disable differential control.
    """
    REMOTE_TALON_FX_DIFF = 1
    """
    Use another TalonFX on the same CAN bus.  Talon FX will update its differential
    position and velocity whenever the remote TalonFX publishes its information on
    CAN bus.  The differential controller will use the difference between this
    TalonFX's sensor and the remote Talon FX's sensor for the differential component
    of the output.
    """
    REMOTE_PIGEON2_YAW = 2
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    DifferentialRemoteSensorID).  Talon FX will update its differential position to
    match the Pigeon2 yaw whenever Pigeon2 publishes its information on CAN bus.
    Note that the Talon FX differential position will be in rotations and not
    degrees.
    """
    REMOTE_PIGEON2_PITCH = 3
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    DifferentialRemoteSensorID).  Talon FX will update its differential position to
    match the Pigeon2 pitch whenever Pigeon2 publishes its information on CAN bus.
    Note that the Talon FX differential position will be in rotations and not
    degrees.
    """
    REMOTE_PIGEON2_ROLL = 4
    """
    Use another Pigeon2 on the same CAN bus (this also requires setting
    DifferentialRemoteSensorID).  Talon FX will update its differential position to
    match the Pigeon2 roll whenever Pigeon2 publishes its information on CAN bus.
    Note that the Talon FX differential position will be in rotations and not
    degrees.
    """
    REMOTE_CANCODER = 5
    """
    Use another CANcoder on the same CAN bus (this also requires setting
    DifferentialRemoteSensorID).  Talon FX will update its differential position and
    velocity to match the CANcoder whenever CANcoder publishes its information on
    CAN bus.
    """


class StaticFeedforwardSignValue(Enum):
    """
    Static Feedforward Sign during position closed loop.
    
    This determines the sign of the applied kS during position closed-loop modes.
    The default behavior uses the velocity reference sign. This works well with
    velocity closed loop, Motion Magic® controls, and position closed loop when
    velocity reference is specified (motion profiling).
    
    However, when using position closed loop with zero velocity reference (no motion
    profiling), the application may want to apply static feedforward based on the
    sign of closed loop error instead. When doing so, we recommend using the minimal
    amount of kS, otherwise the motor output may dither when closed loop error is
    near zero.
    """
    USE_VELOCITY_SIGN = 0
    """
    Use the velocity reference sign. This works well with velocity closed loop,
    Motion Magic® controls, and position closed loop when velocity reference is
    specified (motion profiling).
    """
    USE_CLOSED_LOOP_SIGN = 1
    """
    Use the sign of closed loop error. This is useful when using position closed
    loop with zero velocity reference (no motion profiling). We recommend the
    minimal amount of kS, otherwise the motor output may dither when closed loop
    error is near zero.
    """


class ConnectedMotorValue(Enum):
    """
    The type of motor attached to the Talon.
    
    This can be used to determine what motor is attached to the Talon FX.  Return
    will be "Unknown" if firmware is too old or device is not present.
    """
    UNKNOWN = 0
    """
    Talon could not determine the type of motor attached.
    """
    FALCON500_INTEGRATED = 1
    """
    Talon is attached to an integrated Falcon motor.
    """
    KRAKENX60_INTEGRATED = 2
    """
    Talon is attached to an integrated Kraken X60 motor.
    """
    KRAKENX44_INTEGRATED = 3
    """
    Talon is attached to an integrated Kraken X44 motor.
    """
    MINION_JST = 4
    """
    Talon is connected to a CTR Electronics Minion® brushless three phase motor.
    """
    BRUSHED_AB = 5
    """
    Talon is connected to a third party brushed DC motor with leads A and B.
    """
    BRUSHED_AC = 6
    """
    Talon is connected to a third party brushed DC motor with leads A and C.
    """
    BRUSHED_BC = 7
    """
    Talon is connected to a third party brushed DC motor with leads B and C.
    """
    NEO_JST = 8
    """
    Talon is connected to a third party NEO brushless three phase motor.
    """
    NEO550_JST = 9
    """
    Talon is connected to a third party NEO550 brushless three phase motor.
    """
    VORTEX_JST = 10
    """
    Talon is connected to a third party VORTEX brushless three phase motor.
    """


class MeasurementHealthValue(Enum):
    """
    Health of the distance measurement.
    """
    GOOD = 0
    """
    Measurement is good.
    """
    LIMITED = 1
    """
    Measurement is likely okay, but the target is either very far away or moving
    very quickly.
    """
    BAD = 2
    """
    Measurement is compromised.
    """


class UpdateModeValue(Enum):
    """
    Update mode of the CANrange. The CANrange supports short-range and long-range
    detection at various update frequencies.
    """
    SHORT_RANGE100_HZ = 0
    """
    Updates distance/proximity at 100hz using short-range detection mode.
    """
    SHORT_RANGE_USER_FREQ = 1
    """
    Uses short-range detection mode for improved detection under high ambient
    infrared light conditions. Uses user-specified update frequency.
    """
    LONG_RANGE_USER_FREQ = 2
    """
    Uses long-range detection mode and user-specified update frequency.
    """

