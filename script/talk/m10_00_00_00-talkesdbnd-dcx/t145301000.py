# -*- coding: utf-8 -*-
def t145301000_1():
    """State 0,1"""
    SetUpdateDistance(100)
    while True:
        """State 7"""
        # actionbutton:6961:"Bless iron coin"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert t145301000_x0(actionbutton1=6961, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=1149110)
        """State 2,3"""
        SetEventFlag(10003213, FlagState.On)
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        assert not GetEventFlag(10003213)
        """State 6"""
        SetEventFlag(1149110, FlagState.On)
        """State 5"""
        UnlockGarb(102021)
        assert not IsMenuOpen(MenuType.Bonfire) and GetCurrentStateElapsedFrames() > 1

def t145301000_x0(actionbutton1=6961, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=1149110):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag1) or GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not GetEventFlag(flag4)
            and not GetEventFlag(flag5)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6961:"Bless iron coin"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

