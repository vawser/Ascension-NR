# -*- coding: utf-8 -*-
def t171101000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t171101000_x5(flag1=6000, flag2=6000, flag3=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1, mode3=1)
    Quit()

def t171101000_1000():
    """State 0,2,3"""
    assert t171101000_x34()
    """State 1"""
    EndMachine(1000)
    Quit()

def t171101000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t171101000_x0(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag4=10003361)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif f302(-1) == 3:
        pass
    while True:
        """State 5"""
        call = t171101000_x42()
        assert DoesSelfHaveSpEffect(10124)
        """State 3"""
        assert not DoesSelfHaveSpEffect(10124) and GetCurrentStateElapsedFrames() > 1

def t171101000_x0(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag4=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag5) or GetEventFlag(flag10) or GetEventFlag(flag11) or GetEventFlag(flag12) or
                GetEventFlag(flag13))
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag4) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag5) and not GetEventFlag(flag10) and not GetEventFlag(flag11) and not GetEventFlag(flag12)
            and not GetEventFlag(flag13)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t171101000_x1():
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

def t171101000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t171101000_x3(val2=100, val3=100):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t171101000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t171101000_x1()
    else:
        """State 4,7"""
        call = t171101000_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t171101000_x1()
    """State 9"""
    return 0

def t171101000_x4():
    """State 0,1"""
    assert t171101000_x1()
    """State 2"""
    return 0

def t171101000_x5(flag1=6000, flag2=6000, flag3=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t171101000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7,
                              flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t171101000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t171101000_x6(val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1,
                  mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t171101000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t171101000_x13(val1=val1, z1=z1)
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
            call = t171101000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t171101000_x26() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t171101000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t171101000_x7(val2=100, val3=100):
    """State 0,1"""
    call = t171101000_x17(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t171101000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t171101000_x8(flag1=6000, val2=100, val3=100):
    """State 0,8"""
    assert t171101000_x32()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t171101000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t171101000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t171101000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t171101000_x10(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t171101000_x0(actionbutton1=actionbutton1, flag5=flag5, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171101000_x10(machine1=_, val6=_):
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

def t171101000_x11(val2=100, val3=100):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t171101000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t171101000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t171101000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t171101000_x12():
    """State 0,1"""
    assert t171101000_x10(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t171101000_x13(val1=100, z1=1):
    """State 0,4"""
    assert t171101000_x23()
    """State 3"""
    call = t171101000_x14()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t171101000_x25()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t171101000_x14():
    """State 0,1"""
    assert t171101000_x10(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t171101000_x15(val5=100):
    """State 0,2"""
    call = t171101000_x16()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t171101000_x26()
    """State 4"""
    return 0

def t171101000_x16():
    """State 0,1"""
    assert t171101000_x10(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t171101000_x17(val2=100, val3=100):
    """State 0,5"""
    assert t171101000_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t171101000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t171101000_x28()
    """Unused"""
    """State 6"""
    return 0

def t171101000_x18():
    """State 0,2"""
    call = t171101000_x10(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t171101000_x19():
    """State 0,1"""
    assert t171101000_x10(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t171101000_x20():
    """State 0,1"""
    assert t171101000_x10(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t171101000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t171101000_x22(flag1=6000, flag2=6000, flag3=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                   mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t171101000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3,
                             z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag1):
            """State 3"""
            Label('L0')
            call = t171101000_x8(flag1=flag1, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag2) or GetEventFlag(flag3):
            """State 2"""
            call = t171101000_x7(val2=val2, val3=val3)
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
        assert t171101000_x31() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t171101000_x23():
    """State 0,1"""
    assert t171101000_x24()
    """State 2"""
    return 0

def t171101000_x24():
    """State 0,1"""
    assert t171101000_x10(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t171101000_x25():
    """State 0,1"""
    call = t171101000_x10(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t171101000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171101000_x26():
    """State 0,1"""
    call = t171101000_x10(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t171101000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171101000_x27():
    """State 0,1"""
    call = t171101000_x10(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t171101000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171101000_x28():
    """State 0,1"""
    call = t171101000_x10(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t171101000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171101000_x29(text1=_, flag9=_, mode4=1):
    """State 0,5"""
    assert t171101000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode4 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag9, FlagState.On)
    """State 6"""
    return 0

def t171101000_x30():
    """State 0,1"""
    assert t171101000_x10(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t171101000_x31():
    """State 0,1"""
    assert t171101000_x1()
    """State 2"""
    return 0

def t171101000_x32():
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

def t171101000_x33():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t171101000_x34():
    """State 0,1"""
    assert t171101000_x35()
    """State 2"""
    return 0

def t171101000_x35():
    """State 0"""
    if f302(-1) == 3:
        """State 6"""
        call = t171101000_x36()
        if call.Get() == 1:
            """State 3"""
            Label('L0')
            """State 2"""
            Label('L1')
        elif call.Done():
            pass
        elif GetDistanceToPlayer() > 6:
            """State 4,8"""
            assert t171101000_x2()
    elif True:
        """State 7"""
        call = t171101000_x37()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
        elif GetDistanceToPlayer() > 6:
            """State 5"""
            SetEventFlagIf(not DoesSelfHaveSpEffect(9935), 10003361, FlagState.Off)
            """State 9"""
            assert t171101000_x2()
    else:
        """State 1"""
        Goto('L1')
    """State 10"""
    return 0

def t171101000_x36():
    """State 0"""
    if GetEventFlag(3712):
        """State 1"""
        """State 2"""
        pass
    elif GetEventFlag(3713):
        """State 7,13"""
        # talk:31200200:"It hath been long indeed, fellow spellcaster."
        # talk:31200201:"How pleasant it is, to see thy feathers ruffled for a change."
        # talk:31200202:"Understandable though, as thou sawest me battle-slain and buried—"
        # talk:31200203:"The Nightlord saw fit to return me to life."
        # talk:31200204:"Now we're reunited, perhaps we ought take this chance to speak?"
        assert t171101000_x29(text1=31200200, flag9=1179061, mode4=1)
    elif GetEventFlag(3714):
        """State 3,9"""
        assert t171101000_x38()
    elif GetEventFlag(3715):
        """State 4,10"""
        # talk:31200600:"...As events conspired, neither of us should have survived."
        # talk:31200601:"Yet thou still drawest breath, while I..."
        # talk:31200602:"Why? In what measure did I not stand equal to thee?"
        # talk:31200603:"Yet. Unlike thee, ever heedless, free of spirit, I am the one who will succeed."
        # talk:31200604:"I hope thou takest my meaning, fellow spellcaster..."
        # talk:31200605:"Cease thy foolish conduct, following in the Nightlord's very steps."
        # talk:31200606:"Indeed, how should I put this..."
        # talk:31200607:"Canst thou thine own child slay?"
        assert t171101000_x29(text1=31200600, flag9=1179065, mode4=1)
    elif GetEventFlag(3716):
        """State 5,11"""
        # talk:31200700:"If thou seekest the mechanical menial, I merely needed his momentary silence..."
        # talk:31200701:"Take a good look inside the mausoleum."
        assert t171101000_x29(text1=31200700, flag9=1179066, mode4=1)
        """State 8"""
        SetEventFlag(10003365, FlagState.On)
        SetEventFlag(10003361, FlagState.On)
        ChangeCamera(-1)
        assert GetEventFlag(10003366)
    elif GetEventFlag(3717):
        """State 6,12"""
        assert t171101000_x40()
    else:
        """State 15"""
        return 1
    """State 14"""
    return 0

def t171101000_x37():
    """State 0"""
    if GetEventFlag(3724):
        """State 1,2"""
        SetEventFlag(10003357, FlagState.On)
        SetEventFlag(10003361, FlagState.On)
        """State 6"""
        # talk:31201200:"My fellow spellcaster..."
        # talk:31201201:"I thank thee, for bestowing thy love upon our Night."
        assert t171101000_x29(text1=31201200, flag9=1179067, mode4=1) and not GetEventFlag(10003357)
        """State 8"""
        Label('L0')
        return 0
    else:
        """State 9"""
        return 1
    """Unused"""
    """State 3"""
    UnlockGarb(105030)
    """State 4"""
    SetEventFlag(1179070, FlagState.On)
    """State 5,7"""
    assert t171101000_x33()
    Goto('L0')

def t171101000_x38():
    """State 0,4"""
    # talk:31200300:"Pray, speak thy mind."
    assert t171101000_x29(text1=31200300, flag9=1179062, mode4=1)
    """State 5"""
    assert t171101000_x39()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,6"""
        # talk:31200500:"Remembrest thou not?"
        # talk:31200501:"The monster to which thou gavest rise. The devourer of shadow. The weapon unleashed by thee upon the world entire."
        # talk:31200502:"I was subsumed by the infant, but clung to life in this form."
        # talk:31200503:"Granted now the chance to act upon mine own desires..."
        assert t171101000_x29(text1=31200500, flag9=1179064, mode4=1)
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t171101000_x39():
    """State 0,3"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 1"""
    # action:23120000:"About your resurrection"
    AddTalkListDataAlt(1, 23120000, -1, 0, False)
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    return 0

def t171101000_x40():
    """State 0,4"""
    # talk:31200700:"If thou seekest the mechanical menial, I merely needed his momentary silence..."
    # talk:31200701:"Take a good look inside the mausoleum."
    assert t171101000_x29(text1=31200700, flag9=1179066, mode4=1)
    """State 5"""
    assert t171101000_x39()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,6"""
        # talk:31200500:"Remembrest thou not?"
        # talk:31200501:"The monster to which thou gavest rise. The devourer of shadow. The weapon unleashed by thee upon the world entire."
        # talk:31200502:"I was subsumed by the infant, but clung to life in this form."
        # talk:31200503:"Granted now the chance to act upon mine own desires..."
        assert t171101000_x29(text1=31200500, flag9=1179064, mode4=1)
    else:
        """State 3"""
        pass
    """State 7"""
    return 0

def t171101000_x41():
    """State 0,1"""
    assert GetEventFlag(10003354)
    """State 5"""
    if GetCurrentStateElapsedTime() > 2.5:
        """State 6"""
        # talk:31200100:"What gave me away?"
        call = t171101000_x29(text1=31200100, flag9=1179060, mode4=1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 20:
            """State 3"""
            Label('L0')
            """State 7"""
            assert t171101000_x2()
            """State 4"""
            SetEventFlag(1179060, FlagState.On)
    elif GetDistanceToPlayer() > 20:
        Goto('L0')
    """State 2"""
    SetEventFlag(10003354, FlagState.Off)
    """State 8"""
    return 0

def t171101000_x42():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t171101000_x0(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                             flag4=10003361)
        if call.Done():
            break
        elif GetEventFlag(10003353):
            """State 4"""
            def WhilePaused():
                GiveSpEffectToSelf(9625)
            assert t171101000_x41()
            """State 1"""
            assert not GetEventFlag(10003353)
    """State 2"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 5"""
    return 0

