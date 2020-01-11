from soulstruct.events.internal import ConstantCondition
from soulstruct.events.shared.tests import *
import soulstruct.events.darksouls1.instructions as instr

__all__ = [
    # Names processed directly by EVS parser
    "NeverRestart", "RestartOnRest", "UnknownRestart", "EVENTS", "Condition", "END", "RESTART", "Await",

    # Shared tests
    "THIS_FLAG", "THIS_SLOT_FLAG",
    "ONLINE", "OFFLINE", "DLC_OWNED", "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY", "BLACK_WORLD_TENDENCY", "NEW_GAME_CYCLE", "SOUL_LEVEL",
    "FlagEnabled", "FlagDisabled",
    "SecondsElapsed", "FramesElapsed",
    "CharacterInsideRegion", "CharacterOutsideRegion",
    "PlayerInsideRegion", "PlayerOutsideRegion", "AllPlayersInsideRegion", "AllPlayersOutsideRegion",
    "InsideMap", "OutsideMap",
    "EntityWithinDistance", "EntityBeyondDistance", "PlayerWithinDistance", "PlayerBeyondDistance",
    "HasItem", "HasWeapon", "HasArmor", "HasRing", "HasGood",
    "DialogPromptActivated",
    "MultiplayerEvent", "TrueFlagCount", "EventValue", "EventFlagValue",
    "AnyItemDroppedInRegion", "ItemDropped",
    "OwnsItem", "OwnsWeapon", "OwnsArmor", "OwnsRing", "OwnsGood",
    "IsAlive", "IsDead", "IsAttacked",
    "HealthRatio", "HealthValue", "PartHealthValue",
    "IsCharacterType", "IsHollow", "IsHuman", "IsInvader", "IsBlackPhantom", "IsWhitePhantom",
    "HasSpecialEffect",
    "BackreadEnabled", "BackreadDisabled",
    "HasTaeEvent",
    "IsTargeting", "HasAiStatus", "AiStatusIsNormal", "AiStatusIsRecognition", "AiStatusIsAlert", "AiStatusIsBattle",
    "PlayerIsClass", "PlayerInCovenant",
    "IsDamaged", "IsDestroyed", "IsActivated",
    "PlayerStandingOnCollision", "PlayerMovingOnCollision", "PlayerRunningOnCollision",

    # Dark Souls 1 specific tests
    "HOST", "CLIENT", "SINGLEPLAYER", "MULTIPLAYER",
]


HOST = ConstantCondition(
    if_true_func=instr.IfHost,
    skip_if_true_func=instr.SkipLinesIfHost,
    end_if_true_func=instr.EndIfHost,
    restart_if_true_func=instr.RestartIfHost,
)

CLIENT = ConstantCondition(
    if_true_func=instr.IfClient,
    skip_if_true_func=instr.SkipLinesIfClient,
    end_if_true_func=instr.EndIfClient,
    restart_if_true_func=instr.RestartIfClient,
)

SINGLEPLAYER = ConstantCondition(
    if_true_func=instr.IfSingleplayer,
    skip_if_true_func=instr.SkipLinesIfSingleplayer,
    end_if_true_func=instr.EndIfSingleplayer,
    restart_if_true_func=instr.RestartIfSingleplayer,
)

MULTIPLAYER = ConstantCondition(
    if_true_func=instr.IfMultiplayer,
    skip_if_true_func=instr.SkipLinesIfMultiplayer,
    end_if_true_func=instr.EndIfMultiplayer,
    restart_if_true_func=instr.RestartIfMultiplayer,
)
