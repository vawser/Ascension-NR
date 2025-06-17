# -*- coding: utf-8 -*-
def t609001000_1():
    """State 0,1"""
    t609001000_x2()
    Quit()

def t609001000_x0(actionbutton1=6907, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=10003045):
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
        # actionbutton:6907:"Change sparring settings"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t609001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t609001000_x2():
    """State 0"""
    while True:
        """State 4"""
        # actionbutton:6907:"Change sparring settings"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert t609001000_x0(actionbutton1=6907, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=10003045)
        """State 1,6"""
        call = t609001000_x3()
        if call.Done() and not (CheckSpecificPersonMenuIsOpen(42, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 7:
            """State 3,5"""
            assert t609001000_x1()
    """Unused"""
    """State 7"""
    return 0

def t609001000_x3():
    """State 0,1"""
    OpenSparringSettingsMenu()
    assert not (CheckSpecificPersonMenuIsOpen(46, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2,3"""
    return 0

