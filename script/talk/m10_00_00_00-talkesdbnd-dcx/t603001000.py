# -*- coding: utf-8 -*-
def t603001000_1():
    """State 0,1"""
    t603001000_x2(flag1=10002704)
    Quit()

def t603001000_x0(actionbutton1=6903, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045):
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
        # actionbutton:6903:"Open Visual Codex"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t603001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t603001000_x2(flag1=10002704):
    """State 0"""
    while True:
        """State 7"""
        # actionbutton:6903:"Open Visual Codex"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t603001000_x0(actionbutton1=6903, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045)
        if call.Done():
            """State 1"""
            pass
        elif GetEventFlag(flag1):
            """State 3"""
            assert GetDistanceToPlayer() < 6.9
        """State 6"""
        call = t603001000_x3()
        if call.Done() and not (CheckSpecificPersonMenuIsOpen(36, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 7:
            """State 5,8"""
            assert t603001000_x1()
        """State 4"""
        SetEventFlag(flag1, FlagState.Off)
    """Unused"""
    """State 9"""
    return 0

def t603001000_x3():
    """State 0,1"""
    OpenVisualCodex()
    assert not (CheckSpecificPersonMenuIsOpen(36, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2,3"""
    return 0

