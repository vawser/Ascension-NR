# -*- coding: utf-8 -*-
def t121201000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t121201000_x7(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1, mode3=1)
    Quit()

def t121201000_1000():
    """State 0,2,3"""
    assert t121201000_x40()
    """State 1"""
    EndMachine(1000)
    Quit()

def t121201000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert t121201000_x0(actionbutton1=6000, flag7=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag6=6000)
    """State 1"""
    EndMachine(2000)
    Quit()

def t121201000_x0(actionbutton1=6000, flag7=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag7) or GetEventFlag(flag11) or GetEventFlag(flag12) or GetEventFlag(flag13) or
                GetEventFlag(flag14))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag6)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag7) and not GetEventFlag(flag11) and not GetEventFlag(flag12) and not GetEventFlag(flag13)
            and not GetEventFlag(flag14)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t121201000_x1():
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

def t121201000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t121201000_x3(action3=21071001):
    """State 0,1"""
    # action:21071001:"I cannot ignore a danger to the flock"
    OpenGenericDialog(DialogBoxType.CenterBottom1, action3, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t121201000_x4(z5=2):
    """State 0,2"""
    if not CompareRNGValue(CompareType.Equal, 0) != -1:
        """State 1,4"""
        ShuffleRNGSeed(z5)
    else:
        """State 3"""
        pass
    """State 5"""
    SetRNGSeed()
    """State 6"""
    return 0

def t121201000_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t121201000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t121201000_x1()
    else:
        """State 4,7"""
        call = t121201000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t121201000_x1()
    """State 9"""
    return 0

def t121201000_x6():
    """State 0,1"""
    assert t121201000_x1()
    """State 2"""
    return 0

def t121201000_x7(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t121201000_x24(flag3=flag3, flag4=flag4, flag5=flag5, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag6=flag6, flag7=flag7, flag8=flag8, flag9=flag9,
                              flag10=flag10, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t121201000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t121201000_x8(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag6=6000, flag7=6001, flag8=6000,
                  flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t121201000_x11(actionbutton1=actionbutton1, flag6=flag6, flag7=flag7, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t121201000_x15(val1=val1, z1=z1)
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
        elif GetEventFlag(flag10):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag8) and not GetEventFlag(flag9) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t121201000_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t121201000_x28() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t121201000_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t121201000_x9(val2=10, val3=12):
    """State 0,1"""
    call = t121201000_x19(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t121201000_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t121201000_x10(flag3=6000, val2=10, val3=12):
    """State 0,8"""
    assert t121201000_x36()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag3):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t121201000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t121201000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t121201000_x11(actionbutton1=6000, flag6=6000, flag7=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t121201000_x12(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t121201000_x0(actionbutton1=actionbutton1, flag7=flag7, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag6=flag6))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121201000_x12(machine1=_, val6=_):
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

def t121201000_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t121201000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t121201000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t121201000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t121201000_x14():
    """State 0,1"""
    assert t121201000_x12(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t121201000_x15(val1=5, z1=1):
    """State 0,4"""
    assert t121201000_x25()
    """State 3"""
    call = t121201000_x16()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t121201000_x27()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t121201000_x16():
    """State 0,1"""
    assert t121201000_x12(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t121201000_x17(val5=12):
    """State 0,2"""
    call = t121201000_x18()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t121201000_x28()
    """State 4"""
    return 0

def t121201000_x18():
    """State 0,1"""
    assert t121201000_x12(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t121201000_x19(val2=10, val3=12):
    """State 0,5"""
    assert t121201000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t121201000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t121201000_x30()
    """Unused"""
    """State 6"""
    return 0

def t121201000_x20():
    """State 0,2"""
    call = t121201000_x12(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t121201000_x21():
    """State 0,1"""
    assert t121201000_x12(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t121201000_x22():
    """State 0,1"""
    assert t121201000_x12(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t121201000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t121201000_x24(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                   mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t121201000_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag6=flag6, flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, z1=z1, z2=z2, z3=z3,
                             z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag3):
            """State 3"""
            Label('L0')
            call = t121201000_x10(flag3=flag3, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag4) or GetEventFlag(flag5):
            """State 2"""
            call = t121201000_x9(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag3):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag4) and not GetEventFlag(flag5):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t121201000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t121201000_x25():
    """State 0,1"""
    assert t121201000_x26()
    """State 2"""
    return 0

def t121201000_x26():
    """State 0,1"""
    assert t121201000_x12(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t121201000_x27():
    """State 0,1"""
    call = t121201000_x12(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t121201000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121201000_x28():
    """State 0,1"""
    call = t121201000_x12(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t121201000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121201000_x29():
    """State 0,1"""
    call = t121201000_x12(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t121201000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121201000_x30():
    """State 0,1"""
    call = t121201000_x12(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t121201000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121201000_x31(text1=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t121201000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode5 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag1, FlagState.On)
    """State 6"""
    return 0

def t121201000_x32(text3=_, mode4=1):
    """State 0,4"""
    assert t121201000_x33() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text3, -1, -1, True)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t121201000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t121201000_x34():
    """State 0,1"""
    assert t121201000_x12(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t121201000_x35():
    """State 0,1"""
    assert t121201000_x1()
    """State 2"""
    return 0

def t121201000_x36():
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

def t121201000_x37():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t121201000_x38(action1=23112000, action2=23112001):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:23112000:"Eliminate"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:23112001:"Leave alone"
    AddTalkListDataAlt(2, action2, -1, 0, False)
    """State 3"""
    OpenConversationChoicesMenu(0)
    """State 4"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    else:
        """State 7"""
        return 1

def t121201000_x39(text1=_, flag1=_, text2=_, flag2=_):
    """State 0,4"""
    assert t121201000_x4(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t121201000_x31(text1=text1, flag1=flag1, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t121201000_x31(text1=text2, flag1=flag2, mode5=1)
    """State 5"""
    return 0

def t121201000_x40():
    """State 0,1"""
    assert t121201000_x41()
    """State 2"""
    return 0

def t121201000_x41():
    """State 0"""
    if f302(-1) == 3 or f302(-1) == 3:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t121201000_x42()
    else:
        """State 1"""
        """State 2"""
        pass
    """State 4"""
    return 0

def t121201000_x42():
    """State 0"""
    if GetEventFlag(3215):
        """State 1,6"""
        # talk:31100700:"Well, well, you must be my saviour..."
        # talk:31100701:"It is a pleasure to meet you. I am but a humble merchant."
        # talk:31100702:"I must have strayed into this cheery place at some point, though I know not when or how..."
        # talk:31100703:"I believe you are attempting to rescue the Lands Between from its plight..."
        # talk:31100704:"Well, I can hardly stand by and do nothing! Allow me to aid you in your quest."
        # talk:31100705:"Even as one who leads a somewhat unusual existence, I'm sure I can be of use..."
        # talk:31100706:"Hee hee hee..."
        assert t121201000_x31(text1=31100700, flag1=1129100, mode5=1)
    elif GetEventFlag(3216):
        """State 2,7"""
        assert t121201000_x43()
    elif GetEventFlag(3217):
        """State 3,8"""
        assert t121201000_x44()
    elif GetEventFlag(3219):
        """State 4,9"""
        assert t121201000_x45()
    else:
        """State 5"""
        pass
    """State 10"""
    return 0

def t121201000_x43():
    """State 0"""
    if GetEventFlag(1129101):
        """State 2"""
        pass
    else:
        """State 3"""
        # talk:31100800:"Ah, pardon me."
        # talk:31100801:"Please, take this to mark the occasion of our acquaintance."
        assert t121201000_x31(text1=31100800, flag1=1129101, mode5=1)
        """State 1,5"""
        assert t121201000_x37() and f316() == 0
    """State 4"""
    # talk:31100810:"It might seem a little worse for wear, but trust me, it remains as potent as ever. It will protect you, my saviour."
    # talk:31100811:"I shall share them out amongst your comrades later."
    # talk:31100812:"Now please, do take a look at my wares."
    assert t121201000_x31(text1=31100810, flag1=1129102, mode5=1)
    """State 6"""
    return 0

def t121201000_x44():
    """State 0"""
    if not GetEventFlag(1129113):
        """State 1,10"""
        # talk:31100900:"Welcome, my saviour! Take as long as you need."
        # talk:31100902:"All you could ever need, at a fair price."
        assert t121201000_x39(text1=31100900, flag1=1129103, text2=31100902, flag2=1129104)
        """State 2"""
        OpenJarShop(12000, 12010)
        ClearTalkActionState()
        """State 7"""
        if not (CheckSpecificPersonMenuIsOpen(38, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
            """State 3"""
            if GetEventFlag(1129113):
                pass
            elif DidYouDoSomethingInTheMenu(9):
                """State 4,11"""
                # talk:31101000:"My utmost thanks... Hee hee..."
                # talk:31101002:"Very good. You have...exquisite taste... Hee..."
                assert t121201000_x39(text1=31101000, flag1=1129105, text2=31101002, flag2=1129106)
                Goto('L0')
            else:
                """State 5,12"""
                # talk:31101100:"Sometimes merely browsing is nice, isn't it... Hee hee..."
                # talk:31101102:"Come back at your convenience, I never stray far... Hee hee..."
                assert t121201000_x39(text1=31101100, flag1=1129107, text2=31101102, flag2=1129108)
                Goto('L0')
        elif GetEventFlag(1129113):
            """State 9"""
            assert GetCurrentStateElapsedTime() > 1 or not (CheckSpecificPersonMenuIsOpen(38, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            assert t121201000_x36()
        """State 8,13"""
        # talk:31101400:"Goodness gracious, I've sold through my entire stock!"
        # talk:31101401:"Thank you! You truly are a customer like no other..."
        # talk:31101402:"I hope to restock before long, please, do look forward to it! Heh heh heh..."
        assert t121201000_x31(text1=31101400, flag1=1129109, mode5=1)
    elif GetEventFlag(1129113):
        """State 6,14"""
        # talk:31101500:"I hope to restock before long, please, do look forward to it! Heh heh heh..."
        assert t121201000_x31(text1=31101500, flag1=1129110, mode5=1)
    """State 16"""
    Label('L0')
    return 0

def t121201000_x45():
    """State 0,8"""
    SetEventFlag(10003123, FlagState.On)
    """State 9"""
    # talk:31101200:"Ah, welcome, my saviour! What...what's the matter?"
    assert t121201000_x31(text1=31101200, flag1=1129111, mode5=1)
    while True:
        """State 11"""
        # action:23112000:"Eliminate"
        # action:23112001:"Leave alone"
        call = t121201000_x38(action1=23112000, action2=23112001)
        if call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 3,12"""
            # action:21071001:"I cannot ignore a danger to the flock"
            assert t121201000_x3(action3=21071001)
    """State 1"""
    SetEventFlag(10003111, FlagState.On)
    assert GetCurrentStateElapsedTime() > 2
    """State 14"""
    # talk:31101300:"Argh! What are you doing!?"
    assert t121201000_x32(text3=31101300, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
    """State 7"""
    SetEventFlag(10003121, FlagState.On)
    """State 5"""
    assert not GetEventFlag(10003121) and GetCurrentStateElapsedFrames() > 1
    """State 15"""
    # talk:31101310:"Why...my sav...iour?"
    # talk:31101311:"Tell me...why...?"
    # talk:31101312:"I don't want...to..."
    # talk:31101313:"..."
    assert t121201000_x32(text3=31101310, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
    """State 6"""
    SetEventFlag(1129112, FlagState.On)
    """State 2"""
    SetEventFlag(10003111, FlagState.Off)
    """State 4,16"""
    return 0
    """Unused"""
    """State 10"""
    # talk:31101300:"Argh! What are you doing!?"
    t121201000_x31(text1=31101300, flag1=10003121, mode5=1)
    Quit()
    """State 13"""
    # talk:31101310:"Why...my sav...iour?"
    # talk:31101311:"Tell me...why...?"
    # talk:31101312:"I don't want...to..."
    # talk:31101313:"..."
    t121201000_x31(text1=31101310, flag1=1129112, mode5=1)
    Quit()

