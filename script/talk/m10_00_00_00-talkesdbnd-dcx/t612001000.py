# -*- coding: utf-8 -*-
def t612001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t612001000_x5(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  z5=0, z6=0, mode1=0)
    Quit()

def t612001000_1000():
    """State 0,2"""
    assert t612001000_x33()
    """State 1"""
    EndMachine(1000)
    Quit()

def t612001000_2000():
    """State 0,2,3"""
    # actionbutton:6910:"Paint picture"
    # eventflag:6000:Flag to always be OFF
    assert (t612001000_x0(actionbutton1=6910, flag5=10009416, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=10009808))
    """State 1"""
    EndMachine(2000)
    Quit()

def t612001000_x0(actionbutton1=_, flag5=_, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag5) or GetEventFlag(flag9) or GetEventFlag(flag10) or GetEventFlag(flag11) or GetEventFlag(flag12)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag4) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not GetEventFlag(flag11)
            and not GetEventFlag(flag12))):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t612001000_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0):
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t612001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t612001000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t612001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t612001000_x1()
    else:
        """State 4,7"""
        call = t612001000_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t612001000_x1()
    """State 9"""
    return 0

def t612001000_x4():
    """State 0,1"""
    assert t612001000_x1()
    """State 2"""
    return 0

def t612001000_x5(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  z5=0, z6=0, mode1=0):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t612001000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7,
                              flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1)
        assert IsClientPlayer()
        """State 1"""
        call = t612001000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t612001000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001, flag6=6001,
                  flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, z5=0, z6=0, mode1=0):
    """State 0"""
    while True:
        """State 2"""
        call = t612001000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode1 == 1, 1000000)
            call = t612001000_x13(val1=val1, z1=z1)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                c1_172(1, 0, 9, 9, 9, 9, 9, 9, 9)
            def ExitPause():
                ChangeCamera(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif IsAttackedBySomeone() and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag8):
            Goto('L0')
        # eventflag:6001:Flag to always be ON
        elif GetEventFlag(flag6) and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t612001000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t612001000_x26() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t612001000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t612001000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t612001000_x17(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t612001000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t612001000_x8(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t612001000_x32()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t612001000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t612001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t612001000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t612001000_x10(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t612001000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t612001000_x10(machine1=_, val6=_):
    """State 0,1"""
    if MachineExists(machine1):
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            RunMachine(machine1)
        assert GetMachineResult() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t612001000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t612001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t612001000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t612001000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t612001000_x12():
    """State 0,1"""
    assert t612001000_x10(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t612001000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t612001000_x23()
    """State 1"""
    call = t612001000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t612001000_x25()
    """State 4"""
    return 0

def t612001000_x14():
    """State 0,1"""
    assert t612001000_x10(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t612001000_x15(val5=12):
    """State 0,1"""
    call = t612001000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t612001000_x26()
    """State 3"""
    return 0

def t612001000_x16():
    """State 0,1"""
    assert t612001000_x10(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t612001000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t612001000_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t612001000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t612001000_x28()
    """Unused"""
    """State 6"""
    return 0

def t612001000_x18():
    """State 0,2"""
    call = t612001000_x10(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t612001000_x19():
    """State 0,1"""
    assert t612001000_x10(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t612001000_x20():
    """State 0,1"""
    assert t612001000_x10(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t612001000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t612001000_x22(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                   z5=0, z6=0, mode1=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t612001000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag1):
            """State 3"""
            Label('L0')
            call = t612001000_x8(flag1=flag1, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag2) or GetEventFlag(flag3):
            """State 2"""
            call = t612001000_x7(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag1):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t612001000_x31() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t612001000_x23():
    """State 0,1"""
    assert t612001000_x24()
    """State 2"""
    return 0

def t612001000_x24():
    """State 0,1"""
    assert t612001000_x10(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t612001000_x25():
    """State 0,1"""
    call = t612001000_x10(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t612001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t612001000_x26():
    """State 0,1"""
    call = t612001000_x10(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t612001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t612001000_x27():
    """State 0,1"""
    call = t612001000_x10(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t612001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t612001000_x28():
    """State 0,1"""
    call = t612001000_x10(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t612001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t612001000_x29(text1=31300100, mode2=1):
    """State 0,4"""
    assert t612001000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:31300100:"What's done is done."
    # talk:31300101:"The Erdtree is no more."
    # talk:31300102:"What is lost...can never return."
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode2 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t612001000_x30():
    """State 0,1"""
    assert t612001000_x10(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t612001000_x31():
    """State 0,1"""
    assert t612001000_x1()
    """State 2"""
    return 0

def t612001000_x32():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0):
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t612001000_x33():
    """State 0,1,6"""
    SetEventFlag(10009818, FlagState.On)
    assert not GetEventFlag(10009818)
    """State 2"""
    SetEventFlag(10009815, FlagState.On)
    """State 3"""
    SetEventFlag(10009816, FlagState.On)
    """State 7"""
    # talk:31300100:"What's done is done."
    # talk:31300101:"The Erdtree is no more."
    # talk:31300102:"What is lost...can never return."
    assert t612001000_x29(text1=31300100, mode2=1) and CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    SetEventFlag(10009817, FlagState.On)
    SetEventFlag(10009805, FlagState.On)
    """State 5"""
    SetEventFlag(10009808, FlagState.On)
    """State 8"""
    return 0

