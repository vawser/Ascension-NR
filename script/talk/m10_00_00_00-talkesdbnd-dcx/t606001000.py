# -*- coding: utf-8 -*-
def t606001000_1():
    """State 0,1"""
    t606001000_x2(flag1=10002705)
    Quit()

def t606001000_x0(actionbutton1=6904, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5) or GetEventFlag(flag6)
        """State 4"""
        assert not GetEventFlag(flag7)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag7) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag2) and not GetEventFlag(flag3) and not GetEventFlag(flag4) and not GetEventFlag(flag5)
            and not GetEventFlag(flag6)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6904:"Open journal"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t606001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t606001000_x2(flag1=10002705):
    """State 0"""
    while True:
        """State 8"""
        # actionbutton:6904:"Open journal"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t606001000_x0(actionbutton1=6904, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045)
        if call.Done():
            """State 1"""
            pass
        elif GetEventFlag(10009001) and not GetEventFlag(10002016):
            """State 6"""
            SetEventFlag(10002016, FlagState.On)
            assert GetCurrentStateElapsedTime() > 0.5
            continue
        elif GetEventFlag(10002705):
            """State 3"""
            assert GetDistanceToPlayer() < 6.9
        """State 7"""
        call = t606001000_x3()
        if call.Done() and not (CheckSpecificPersonMenuIsOpen(39, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 7:
            """State 5,9"""
            assert t606001000_x1()
        """State 4"""
        SetEventFlag(flag1, FlagState.Off)
        """State 10"""
        assert t606001000_x5()
    """Unused"""
    """State 11"""
    return 0

def t606001000_x3():
    """State 0,1"""
    OpenJournal()
    """State 3"""
    call = t606001000_x4()
    assert not (CheckSpecificPersonMenuIsOpen(39, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2,4"""
    return 0

def t606001000_x4():
    """State 0,5"""
    if not GetChrHero() == Hero.Recluse:
        """State 2"""
        """State 3"""
        pass
    elif GetChrHero() == Hero.Recluse:
        """State 1"""
        """State 4"""
        """State 7"""
        pass
    """State 15"""
    Label('L0')
    return 0
    """Unused"""
    """State 6"""
    assert f315(7) > 5
    """State 8"""
    SetEventFlag(10003350, FlagState.On)
    Goto('L0')
    """State 9"""
    assert f315(7) > 6
    """State 10"""
    SetEventFlag(1179100, FlagState.On)
    Goto('L0')
    """State 11"""
    assert f315(7) > 7
    """State 12"""
    SetEventFlag(1179101, FlagState.On)
    Goto('L0')
    """State 13,14"""
    SetEventFlag(-1, FlagState.On)
    Goto('L0')

def t606001000_x5():
    """State 0,1"""
    if not GetEventFlag(10003350):
        """State 3"""
        pass
    elif GetEventFlag(10003350):
        """State 2,4"""
        SetEventFlag(10003351, FlagState.On)
        """State 5"""
        SetEventFlag(10003350, FlagState.Off)
        """State 6"""
        SetEventFlag(10003045, FlagState.On)
    """State 7"""
    return 0

