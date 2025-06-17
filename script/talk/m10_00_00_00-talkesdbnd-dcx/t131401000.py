# -*- coding: utf-8 -*-
def t131401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t131401000_x5(flag1=1139047, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                  mode1=1, mode2=1, mode3=1)
    Quit()

def t131401000_1000():
    """State 0,2,3"""
    assert t131401000_x34()
    """State 1"""
    EndMachine(1000)
    Quit()

def t131401000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert t131401000_x0(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag4=6000)
    """State 1"""
    EndMachine(2000)
    Quit()

def t131401000_x0(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag4=6000):
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
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag4)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag4) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag5) and not GetEventFlag(flag10) and not GetEventFlag(flag11) and not GetEventFlag(flag12)
            and not GetEventFlag(flag13)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t131401000_x1():
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

def t131401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t131401000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t131401000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t131401000_x1()
    else:
        """State 4,7"""
        call = t131401000_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t131401000_x1()
    """State 9"""
    return 0

def t131401000_x4():
    """State 0,1"""
    assert t131401000_x1()
    """State 2"""
    return 0

def t131401000_x5(flag1=1139047, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                  mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t131401000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7,
                              flag8=flag8, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t131401000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t131401000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000,
                  flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t131401000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t131401000_x13(val1=val1, z3=z3)
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
            call = t131401000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t131401000_x26() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t131401000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t131401000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t131401000_x17(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t131401000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t131401000_x8(flag1=1139047, val2=10, val3=12):
    """State 0,8"""
    assert t131401000_x32()
    """State 1"""
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t131401000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t131401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t131401000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t131401000_x10(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t131401000_x0(actionbutton1=actionbutton1, flag5=flag5, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t131401000_x10(machine1=_, val6=_):
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

def t131401000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t131401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t131401000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t131401000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t131401000_x12():
    """State 0,1"""
    assert t131401000_x10(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t131401000_x13(val1=5, z3=1):
    """State 0,4"""
    assert t131401000_x23()
    """State 3"""
    call = t131401000_x14()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t131401000_x25()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t131401000_x14():
    """State 0,1"""
    assert t131401000_x10(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t131401000_x15(val5=12):
    """State 0,2"""
    call = t131401000_x16()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t131401000_x26()
    """State 4"""
    return 0

def t131401000_x16():
    """State 0,1"""
    assert t131401000_x10(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t131401000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t131401000_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t131401000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t131401000_x28()
    """Unused"""
    """State 6"""
    return 0

def t131401000_x18():
    """State 0,2"""
    call = t131401000_x10(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t131401000_x19():
    """State 0,1"""
    assert t131401000_x10(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t131401000_x20():
    """State 0,1"""
    assert t131401000_x10(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t131401000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t131401000_x22(flag1=1139047, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000,
                   mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t131401000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5,
                             z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        if CheckSelfDeath() or GetEventFlag(flag1):
            """State 3"""
            Label('L0')
            call = t131401000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag2) or GetEventFlag(flag3):
            """State 2"""
            call = t131401000_x7(val2=val2, val3=val3)
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
        assert t131401000_x31() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t131401000_x23():
    """State 0,1"""
    assert t131401000_x24()
    """State 2"""
    return 0

def t131401000_x24():
    """State 0,1"""
    assert t131401000_x10(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t131401000_x25():
    """State 0,1"""
    call = t131401000_x10(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t131401000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t131401000_x26():
    """State 0,1"""
    call = t131401000_x10(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t131401000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t131401000_x27():
    """State 0,1"""
    call = t131401000_x10(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t131401000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t131401000_x28():
    """State 0,1"""
    call = t131401000_x10(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t131401000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t131401000_x29(text1=_, flag9=_, mode4=1):
    """State 0,5"""
    assert t131401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t131401000_x30():
    """State 0,1"""
    assert t131401000_x10(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t131401000_x31():
    """State 0,1"""
    assert t131401000_x1()
    """State 2"""
    return 0

def t131401000_x32():
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

def t131401000_x33(z1=303, z2=_):
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

def t131401000_x34():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t131401000_x35()
    """State 2"""
    return 0

def t131401000_x35():
    """State 0"""
    if f302(-1) == 2:
        """State 3"""
        call = t131401000_x36()
        if call.Get() == 1:
            """State 4"""
            call = t131401000_x37()
            if call.Get() == 1:
                """State 2"""
                Label('L0')
            elif call.Done():
                pass
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L0')
    """State 5"""
    return 0

def t131401000_x36():
    """State 0"""
    if GetEventFlag(3311):
        """State 1,3"""
        assert t131401000_x38()
    elif GetEventFlag(3312):
        """State 2,4"""
        assert t131401000_x40()
    else:
        """State 6"""
        return 1
    """State 5"""
    return 0

def t131401000_x37():
    """State 0"""
    if GetEventFlag(3313):
        """State 1,5"""
        assert t131401000_x39()
    elif GetEventFlag(3314):
        """State 2,4"""
        Label('L0')
    elif GetEventFlag(3315):
        """State 3"""
        Goto('L0')
    else:
        """State 7"""
        return 1
    """State 6"""
    return 0

def t131401000_x38():
    """State 0,12"""
    # talk:31400100:"Well met, comrade."
    # talk:31400101:"It pains me to see you like this, but yes...I am the traitor."
    # talk:31400102:"You've come to hurry me to my end, haven't you? I've been waiting."
    # talk:31400103:"Well. You'd best get on with it."
    assert t131401000_x29(text1=31400100, flag9=1139040, mode4=1)
    """State 6"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 7"""
    # action:23142001:"Execute him"
    AddTalkListData(1, 23142001, -1)
    """State 8"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 9"""
    if GetTalkListEntryResult() == 1:
        """State 1"""
        SetEventFlag(10003150, FlagState.On)
        """State 3"""
        SetEventFlag(10003151, FlagState.On)
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        if not GetEventFlag(10003151):
            """State 13"""
            # talk:31400200:"Agh..."
            # talk:31400201:"..."
            assert t131401000_x29(text1=31400200, flag9=10003157, mode4=1)
            """State 11"""
            assert not GetEventFlag(10003157) and GetCurrentStateElapsedFrames() > 1
            """State 15"""
            # talk:31400210:"...Didn't quite manage it, did we..."
            # talk:31400211:"You should know as well as anyone, we can't be killed so easily..."
            # talk:31400212:"Find an Edge of Order..."
            # talk:31400213:"And I'll let you in on a little secret."
            assert t131401000_x29(text1=31400210, flag9=1139041, mode4=1)
            """State 2"""
            SetEventFlag(10003150, FlagState.Off)
            """State 14"""
            assert t131401000_x33(z1=303, z2=1)
        elif GetEventFlag(10003154):
            """State 5"""
            pass
    else:
        """State 10"""
        pass
    """State 16"""
    return 0

def t131401000_x39():
    """State 0,14"""
    # talk:31400600:"You have it."
    # talk:31400601:"Then please, strike true."
    assert t131401000_x29(text1=31400600, flag9=1139045, mode4=1)
    """State 5"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 6"""
    # action:23142001:"Execute him"
    AddTalkListData(1, 23142001, -1)
    """State 7"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 8"""
    if GetTalkListEntryResult() == 1:
        """State 1"""
        SetEventFlag(10003152, FlagState.On)
        """State 3"""
        SetEventFlag(10003153, FlagState.On)
        assert GetCurrentStateElapsedFrames() > 1
        """State 10"""
        if not GetEventFlag(10003153):
            """State 15"""
            # talk:31400700:"Agh..."
            # talk:31400701:"..."
            assert t131401000_x29(text1=31400700, flag9=10003158, mode4=1)
            """State 13"""
            assert not GetEventFlag(10003158) and GetCurrentStateElapsedFrames() > 1
            """State 17"""
            # talk:31400710:"I-I can feel it... I'm certain...this is the real thing."
            # talk:31400711:"I'll tell you what you want to know..."
            # talk:31400712:"You and I...all of us...are already dead. But our curse does not allow us...to rest."
            # talk:31400713:"As Those Who Live in Death... We could not rest until the Nightlord was defeated..."
            # talk:31400714:"Battle...was not suffering...but pleasure...until..."
            # talk:31400715:"You have undergone...the same... You have...the same eyes."
            # talk:31400716:"What...will you do?"
            # talk:31400717:"My heart...I finally feel...it beat...its last..."
            # talk:31400718:"..."
            assert t131401000_x29(text1=31400710, flag9=1139046, mode4=1)
            """State 2"""
            SetEventFlag(10003152, FlagState.Off)
            """State 4"""
            SetEventFlag(1139047, FlagState.On)
            """State 12,16"""
            assert t131401000_x33(z1=303, z2=3)
        elif GetEventFlag(10003155):
            """State 11"""
            pass
    else:
        """State 9"""
        pass
    """State 18"""
    return 0

def t131401000_x40():
    """State 0,5"""
    # talk:31400300:"Feeling talkative, are we?"
    assert t131401000_x29(text1=31400300, flag9=1139042, mode4=1)
    """State 6"""
    assert t131401000_x41()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,7"""
        # talk:31400400:"Find an Edge of Order."
        # talk:31400401:"A blade of unique make. It has, layered within, the weight of the Night."
        # talk:31400402:"Find one, and I'll talk."
        assert t131401000_x29(text1=31400400, flag9=1139043, mode4=1)
    elif GetTalkListEntryResult() == 2:
        """State 3,8"""
        # talk:31400500:"Of course the Fellowship would send someone after me."
        # talk:31400501:"They kill anything and everything that stands in their way."
        # talk:31400502:"This is no different."
        assert t131401000_x29(text1=31400500, flag9=1139044, mode4=1)
    else:
        """State 4"""
        pass
    """State 9"""
    return 0

def t131401000_x41():
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 2"""
    # action:23140001:"About the secret"
    AddTalkListDataAlt(1, 23140001, -1, 1, False)
    # action:23140002:"About the traitor"
    AddTalkListDataAlt(2, 23140002, -1, 2, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 3"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    return 0

