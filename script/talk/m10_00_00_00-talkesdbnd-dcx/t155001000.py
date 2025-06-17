# -*- coding: utf-8 -*-
def t155001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t155001000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                  mode1=1, mode2=1, mode3=0)
    Quit()

def t155001000_1000():
    """State 0,2,3"""
    assert t155001000_x34()
    """State 1"""
    EndMachine(1000)
    Quit()

def t155001000_2000():
    """State 0,2,3"""
    # actionbutton:6970:"Touch monument"
    # eventflag:6000:Flag to always be OFF
    assert (t155001000_x1(actionbutton1=6970, flag5=1159070, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=10003257))
    """State 1"""
    EndMachine(2000)
    Quit()

def t155001000_x0(action3=21031001):
    """State 0,1"""
    # action:21031001:"Travel to the battlegrounds?"
    OpenGenericDialog(DialogBoxType.CenterBottom2, action3, DialogResult.Leave, DialogBoxStyle.Unk, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t155001000_x1(actionbutton1=_, flag5=_, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag5) or GetEventFlag(flag9) or GetEventFlag(flag10) or GetEventFlag(flag11) or GetEventFlag(flag12)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag4) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not GetEventFlag(flag11)
            and not GetEventFlag(flag12)) or DoesPlayerHaveSpEffect(9640)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t155001000_x2():
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

def t155001000_x3(action2=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action2, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t155001000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t155001000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t155001000_x2()
    else:
        """State 4,7"""
        call = t155001000_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t155001000_x2()
    """State 9"""
    return 0

def t155001000_x5():
    """State 0,1"""
    assert t155001000_x2()
    """State 2"""
    return 0

def t155001000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                  mode1=1, mode2=1, mode3=0):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t155001000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7,
                              flag8=flag8, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t155001000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t155001000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000,
                  flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1, mode2=1, mode3=0):
    """State 0"""
    while True:
        """State 2"""
        call = t155001000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t155001000_x14(val1=val1, z3=z3)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                c5_172(mode1 == 1 and mode2 == 1, 1, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(mode1 == 1 and not mode2 == 1, 1, 9, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode1 == 1 and mode2 == 1, 9, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode1 == 1 and not mode2 == 1, 9, 9, 9, 9, 9, 9, 9, 9, 9)
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
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag6) and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t155001000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t155001000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t155001000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t155001000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t155001000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t155001000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t155001000_x9(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t155001000_x32()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t155001000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t155001000_x2()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t155001000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t155001000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t155001000_x1(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t155001000_x11(machine1=_, val6=_):
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

def t155001000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t155001000_x2()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t155001000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t155001000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t155001000_x13():
    """State 0,1"""
    assert t155001000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t155001000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t155001000_x24()
    """State 3"""
    call = t155001000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t155001000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t155001000_x15():
    """State 0,1"""
    assert t155001000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t155001000_x16(val5=12):
    """State 0,2"""
    call = t155001000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t155001000_x27()
    """State 4"""
    return 0

def t155001000_x17():
    """State 0,1"""
    assert t155001000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t155001000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t155001000_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t155001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t155001000_x29()
    """Unused"""
    """State 6"""
    return 0

def t155001000_x19():
    """State 0,2"""
    call = t155001000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t155001000_x20():
    """State 0,1"""
    assert t155001000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t155001000_x21():
    """State 0,1"""
    assert t155001000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t155001000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t155001000_x23(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                   mode1=1, mode2=1, mode3=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t155001000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5,
                             z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag1):
            """State 3"""
            Label('L0')
            call = t155001000_x9(flag1=flag1, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag2) or GetEventFlag(flag3):
            """State 2"""
            call = t155001000_x8(val2=val2, val3=val3)
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
        assert t155001000_x31() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t155001000_x24():
    """State 0,1"""
    assert t155001000_x25()
    """State 2"""
    return 0

def t155001000_x25():
    """State 0,1"""
    assert t155001000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t155001000_x26():
    """State 0,1"""
    call = t155001000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t155001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t155001000_x27():
    """State 0,1"""
    call = t155001000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t155001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t155001000_x28():
    """State 0,1"""
    call = t155001000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t155001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t155001000_x29():
    """State 0,1"""
    call = t155001000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t155001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t155001000_x30():
    """State 0,1"""
    assert t155001000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t155001000_x31():
    """State 0,1"""
    assert t155001000_x2()
    """State 2"""
    return 0

def t155001000_x32():
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

def t155001000_x33(action1=21031001, z1=21032001, z2=21032002):
    """State 0,1"""
    # action:21031001:"Travel to the battlegrounds?"
    OpenGenericDialog(DialogBoxType.CenterBottom2, action1, z1, z2, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t155001000_x34():
    """State 0"""
    if GetEventFlag(3519):
        """State 6,8"""
        SetEventFlag(1159076, FlagState.On)
        """State 18"""
        Label('L0')
        assert t155001000_x40()
    elif GetEventFlag(3518):
        """State 5,17"""
        assert t155001000_x39()
    elif GetEventFlag(3511) or GetEventFlag(3512):
        """State 4,16"""
        assert t155001000_x38()
    elif GetEventFlag(3506):
        """State 3,7"""
        SetEventFlag(1159073, FlagState.On)
        """State 15"""
        assert t155001000_x37()
    elif GetEventFlag(3504):
        """State 2,14"""
        assert t155001000_x36()
    elif GetEventFlag(3501):
        """State 1,13"""
        assert t155001000_x35()
    elif GetEventFlag(3520):
        """State 9"""
        Goto('L0')
    elif GetEventFlag(3521):
        """State 10"""
        Goto('L0')
    elif GetEventFlag(3522):
        """State 11"""
        Goto('L0')
    else:
        """State 12,19"""
        assert t155001000_x37()
    """State 20"""
    return 0

def t155001000_x35():
    """State 0,1"""
    SetEventFlag(10002021, FlagState.On)
    SetEventFlag(10002020, FlagState.On)
    """State 2"""
    SetEventFlag(1159071, FlagState.On)
    SetEventFlag(10003257, FlagState.On)
    SetEventFlag(10003258, FlagState.On)
    """State 3"""
    return 0

def t155001000_x36():
    """State 0,3"""
    SetEventFlag(1159072, FlagState.On)
    """State 8"""
    # action:21031001:"Travel to the battlegrounds?"
    call = t155001000_x33(action1=21031001, z1=21032001, z2=21032002)
    if call.Get() == 0:
        """State 4,6"""
        c1_164()
        assert not f305()
        """State 1"""
        SetEventFlag(10003250, FlagState.On)
        """State 2"""
        assert GetCurrentStateElapsedTime() > 10
    elif call.Get() == 1:
        """State 5"""
        pass
    elif GetDistanceToPlayer() > 4:
        """State 7,10"""
        assert t155001000_x2()
    """State 11"""
    return 0
    """Unused"""
    """State 9"""
    # action:21031001:"Travel to the battlegrounds?"
    t155001000_x0(action3=21031001)
    Quit()

def t155001000_x37():
    """State 0,1"""
    # action:21031003:"No response"
    assert t155001000_x3(action2=21031003)
    """State 2"""
    return 0

def t155001000_x38():
    """State 0,3"""
    SetEventFlag(1159074, FlagState.On)
    """State 8"""
    # action:21031001:"Travel to the battlegrounds?"
    call = t155001000_x33(action1=21031001, z1=21032001, z2=21032002)
    if call.Get() == 0:
        """State 4,6"""
        c1_164()
        assert not f305()
        """State 1"""
        SetEventFlag(10003251, FlagState.On)
        """State 2"""
        assert GetCurrentStateElapsedTime() > 10
    elif call.Get() == 1:
        """State 5"""
        pass
    elif GetDistanceToPlayer() > 4:
        """State 7,9"""
        assert t155001000_x2()
    """State 10"""
    return 0

def t155001000_x39():
    """State 0,3"""
    SetEventFlag(1159075, FlagState.On)
    """State 8"""
    # action:21031001:"Travel to the battlegrounds?"
    call = t155001000_x33(action1=21031001, z1=21032001, z2=21032002)
    if call.Get() == 0:
        """State 4,6"""
        c1_164()
        assert not f305()
        """State 1"""
        SetEventFlag(10003252, FlagState.On)
        """State 2"""
        assert GetCurrentStateElapsedTime() > 10
    elif call.Get() == 1:
        """State 5"""
        pass
    elif GetDistanceToPlayer() > 4:
        """State 7,9"""
        assert t155001000_x2()
    """State 10"""
    return 0

def t155001000_x40():
    """State 0,1"""
    # action:21031006:"Engraved with names of challengers and their records\n"The Black Claw defeated the White Horn to achieve victory"\n"Ye souls felled in battle, be proud of thine exploits""
    assert t155001000_x3(action2=21031006)
    """State 2"""
    return 0

