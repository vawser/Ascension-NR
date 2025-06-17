# -*- coding: utf-8 -*-
def t615001000_1():
    """State 0,1"""
    t615001000_x2()
    Quit()

def t615001000_x0(actionbutton1=6990, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=10003045):
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
        # actionbutton:6990:"Change garb"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t615001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t615001000_x2():
    """State 0"""
    while True:
        """State 6"""
        # actionbutton:6990:"Change garb"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t615001000_x0(actionbutton1=6990, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=10003045)
        if call.Done():
            """State 5"""
            pass
        elif GetEventFlag(10002702):
            """State 3"""
            pass
        """State 8"""
        call = t615001000_x3()
        if call.Done():
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 7:
            """State 1,7"""
            assert t615001000_x1()
        """State 4"""
        SetEventFlag(10002702, FlagState.Off)
    """Unused"""
    """State 9"""
    return 0

def t615001000_x3():
    """State 0,2"""
    ClearTalkActionState()
    """State 1"""
    OpenGarbShop(11000, 11999)
    while True:
        """State 4"""
        TurnCharacterToFaceEntity(61020, 20000, -1, -1)
        if not (CheckSpecificPersonMenuIsOpen(43, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            break
        elif DidYouDoSomethingInTheMenu(10):
            """State 5"""
            ClearTalkActionState()
            assert GetCurrentStateElapsedFrames() > 5
    """State 3,6"""
    return 0

