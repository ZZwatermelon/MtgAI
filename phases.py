# Beginning
#    Untap
#    Upkeep
#    Draw
# Pre-Combat Main Phase
# Combat
#    Beginning of Combat
#    Declare Attackers
#    Declare Blockers
#    Assign Damage
#    End of Combat
# Post-Combat Main Phase
# End
#    End Step
#    Cleanup

from enum import Enum


class Phases(Enum):
    BEGINNING_PHASE = 1
    UNTAP_STEP = 2
    UPKEEP_STEP = 3
    DRAW_STEP = 4
    PRE_COMBAT_MAIN_PHASE = 5
    COMBAT_PHASE = 6
    BEGIN_COMBAT_STEP = 7
    DECLARE_ATTACKERS_STEP = 8
    DECLARE_BLOCKERS_STEP = 9
    ASSIGN_DAMAGE_STEP = 10
    END_COMBAT_STEP = 11
    POST_COMBAT_MAIN_PHASE = 12
    END_PHASE = 13
    END_STEP = 14
    CLEANUP_STEP = 15
