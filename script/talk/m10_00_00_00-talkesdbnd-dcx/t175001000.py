# -*- coding: utf-8 -*-
def t175001000_1():
    """State 0,1"""
    t175001000_x2()
    Quit()

def t175001000_x0(actionbutton1=6000, flag1=6000, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag1) or GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5)
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag6)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not GetEventFlag(flag4)
            and not GetEventFlag(flag5)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t175001000_x1(z1=702, z2=1):
    """State 0,1"""
    c1_163(z1, z2)
    """State 2"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 3"""
    RequestSave(0)
    """State 9"""
    if f304(z1) == 1:
        """State 10,4"""
        SetEventFlag(10002040, FlagState.On)
        """State 5"""
        if f305():
            """State 6,8"""
            SetEventFlag(10002041, FlagState.On)
        elif not f305():
            """State 7"""
            pass
    else:
        """State 11"""
        pass
    """State 12"""
    return 0

def t175001000_x2():
    """State 0"""
    while True:
        """State 1"""
        # eventflag:6001:Flag to always be ON
        assert GetEventFlag(6001)
        """State 2,5"""
        # actionbutton:6000:"Talk"
        # eventflag:6000:Flag to always be OFF
        assert t175001000_x0(actionbutton1=6000, flag1=6000, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000)
        """State 3"""
        # eventflag:6001:Flag to always be ON
        SetEventFlag(6001, FlagState.On)
        """State 6"""
        assert t175001000_x1(z1=702, z2=1)
        """State 4"""
        assert GetCurrentStateElapsedTime() > 1
    """Unused"""
    """State 7"""
    return 0

