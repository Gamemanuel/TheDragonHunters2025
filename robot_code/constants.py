import rev
from typing import TypeAlias


Direction: TypeAlias = bool


REVMotorType   = rev.SparkBase.MotorType
REVResetMode   = rev.SparkBase.ResetMode
REVPersistMode = rev.SparkBase.PersistMode
REVIdleMode    = rev.SparkBaseConfig.IdleMode


BRUSHED      : REVMotorType   = REVMotorType.kBrushed
BRUSHLESS    : REVMotorType   = REVMotorType.kBrushless

SAFE_RESET   : REVResetMode   = REVResetMode.kResetSafeParameters
NO_SAFE_RESET: REVResetMode   = REVResetMode.kNoResetSafeParameters

PERSIST      : REVPersistMode = REVPersistMode.kPersistParameters
NO_PERSIST   : REVPersistMode = REVPersistMode.kNoPersistParameters

COAST        : REVIdleMode    = REVIdleMode.kCoast
BRAKE        : REVIdleMode    = REVIdleMode.kBrake

FORWARD      : Direction      = False
REVERSE      : Direction      = True