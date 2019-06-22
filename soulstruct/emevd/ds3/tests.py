from soulstruct.emevd.shared.tests import *
import soulstruct.emevd.ds3.instructions as instr


def __no_skip_or_negate_or_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, **kwargs)

    return decorated


def __negate_only(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrTerminateError
        if end_event or restart_event:
            raise NoSkipOrTerminateError
        if condition is None:
            raise ValueError("Condition index must be specified (-7 to 7).")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def __skip_and_negate_and_terminate(func):
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            if condition not in range(-7, 8):
                raise ValueError("Condition register index must be in range [-7, 7], inclusive.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


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

IN_OWN_WORLD = ConstantCondition(
    if_true_func=instr.IfPlayerInOwnWorld,
    if_false_func=instr.IfPlayerNotInOwnWorld,
    end_if_true_func=instr.EndIfPlayerInOwnWorld,
    end_if_false_func=instr.EndIfPlayerNotInOwnWorld,
    restart_if_true_func=instr.RestartIfPlayerInOwnWorld,
    restart_if_false_func=instr.RestartIfPlayerNotInOwnWorld,
)


@__no_skip_or_negate_or_terminate
def ActionButtonInRegion(action_button_id, region, condition):
    return instr.IfActionButtonInRegion(condition, action_button_id, region)


@__no_skip_or_negate_or_terminate
def IsAttackedWithDamageType(attacked_entity, attacking_character, damage_type, condition):
    return instr.IfDamageType(condition, attacked_entity, attacking_character, damage_type)


@__no_skip_or_negate_or_terminate
def CharacterDrawGroupActive(character, condition):
    return instr.IfCharacterDrawGroupActive(condition, character)


@__no_skip_or_negate_or_terminate
def CharacterDrawGroupInactive(character, condition):
    return instr.IfCharacterDrawGroupInactive(condition, character)
