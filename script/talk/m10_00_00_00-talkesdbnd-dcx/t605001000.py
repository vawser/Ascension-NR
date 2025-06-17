# -*- coding: utf-8 -*-
def t605001000_1():
    """State 0,1"""
    t605001000_x2(flag1=10002706)
    Quit()

def t605001000_x0(actionbutton1=6909, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045):
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
        # actionbutton:6909:"Purchase"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t605001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t605001000_x2(flag1=10002706):
    """State 0"""
    while True:
        """State 7"""
        # actionbutton:6909:"Purchase"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t605001000_x0(actionbutton1=6909, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=10003045)
        if call.Done():
            """State 1"""
            def WhilePaused():
                RequestAnimation(20030, -1)
        elif GetEventFlag(flag1):
            """State 3"""
            def WhilePaused():
                RequestAnimation(20030, -1)
            assert GetDistanceToPlayer() < 6.9
        """State 6"""
        call = t605001000_x3()
        if call.Done() and not (CheckSpecificPersonMenuIsOpen(38, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 7:
            """State 5,8"""
            assert t605001000_x1()
        """State 4"""
        SetEventFlag(flag1, FlagState.Off)
    """Unused"""
    """State 9"""
    return 0

def t605001000_x3():
    """State 0,7"""
    SetEventFlag(10001915, FlagState.On)
    """State 1"""
    OpenJarShop(10000, 10199)
    assert not (CheckSpecificPersonMenuIsOpen(38, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if DidYouDoSomethingInTheMenu(9):
        """State 3,8"""
        assert t605001000_x4(z1=9790, z2=9791, z3=9792, z4=9793, z5=9794)
        """State 5"""
        ClearTalkActionState()
        def WhilePaused():
            RequestAnimation(20026, -1)
    else:
        """State 4,9"""
        assert t605001000_x4(z1=9795, z2=9796, z3=9797, z4=9798, z5=9799)
        """State 6"""
        def WhilePaused():
            RequestAnimation(20028, -1)
    """State 10"""
    return 0

def t605001000_x4(z1=_, z2=_, z3=_, z4=_, z5=_):
    """State 0,1"""
    if CompareRNGValue(CompareType.Equal, 0) != -1:
        """State 2"""
        pass
    else:
        """State 3"""
        ShuffleRNGSeed(5)
    """State 4"""
    SetRNGSeed()
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 5"""
        GiveSpEffectToSelf(z1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 6"""
        GiveSpEffectToSelf(z2)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 7"""
        GiveSpEffectToSelf(z3)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 8"""
        GiveSpEffectToSelf(z4)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 9"""
        GiveSpEffectToSelf(z5)
    """State 10"""
    return 0

