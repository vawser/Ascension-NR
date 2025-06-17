# -*- coding: utf-8 -*-
def t200801000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t200801000_x7(flag7=6000, flag8=6000, flag9=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag10=6000, flag11=6001, flag12=6000, flag13=6000, flag14=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t200801000_1000():
    """State 0,2,6"""
    def WhilePaused():
        RequestAnimation(90300, -1)
        SetLookAtEntityForTalkIf(GetEventFlag(10003010), 10000731, 10000)
    assert t200801000_x41()
    """State 1"""
    Label('L0')
    EndMachine(1000)
    Quit()
    """Unused"""
    """State 3"""
    Goto('L1')
    """State 4"""
    ForceCloseGenericDialog()
    Quit()
    """State 5"""
    ForceCloseMenu()
    Quit()
    """State 7"""
    Label('L1')
    assert t200801000_x2()
    Goto('L0')

def t200801000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t200801000_x0(actionbutton1=6000, flag11=6001, flag15=6000, flag16=6000, flag17=6000, flag18=6000,
            flag10=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t200801000_x0(actionbutton1=6000, flag11=6001, flag15=6000, flag16=6000, flag17=6000, flag18=6000, flag10=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag11) or GetEventFlag(flag15) or GetEventFlag(flag16) or GetEventFlag(flag17) or
                GetEventFlag(flag18))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag10)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag10) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag11) and not GetEventFlag(flag15) and not GetEventFlag(flag16) and not GetEventFlag(flag17)
            and not GetEventFlag(flag18)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t200801000_x1():
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

def t200801000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t200801000_x3(action1=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action1, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t200801000_x4(z5=3):
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

def t200801000_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t200801000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t200801000_x1()
    else:
        """State 4,7"""
        call = t200801000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t200801000_x1()
    """State 9"""
    return 0

def t200801000_x6():
    """State 0,1"""
    assert t200801000_x1()
    """State 2"""
    return 0

def t200801000_x7(flag7=6000, flag8=6000, flag9=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag10=6000, flag11=6001, flag12=6000, flag13=6000, flag14=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t200801000_x24(flag7=flag7, flag8=flag8, flag9=flag9, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag10=flag10, flag11=flag11, flag12=flag12,
                              flag13=flag13, flag14=flag14, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t200801000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t200801000_x8(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag10=6000, flag11=6001, flag12=6000,
                  flag13=6000, flag14=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t200801000_x11(actionbutton1=actionbutton1, flag10=flag10, flag11=flag11, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t200801000_x15(val1=val1, z1=z1)
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
        elif GetEventFlag(flag14):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag12) and not GetEventFlag(flag13) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t200801000_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t200801000_x28() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t200801000_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t200801000_x9(val2=10, val3=12):
    """State 0,1"""
    call = t200801000_x19(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t200801000_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t200801000_x10(flag7=6000, val2=10, val3=12):
    """State 0,8"""
    assert t200801000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag7):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t200801000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200801000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t200801000_x11(actionbutton1=6000, flag10=6000, flag11=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t200801000_x12(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t200801000_x0(actionbutton1=actionbutton1, flag11=flag11, flag15=6000, flag16=6000, flag17=6000,
                flag18=6000, flag10=flag10))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200801000_x12(machine1=_, val6=_):
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

def t200801000_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t200801000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t200801000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200801000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t200801000_x14():
    """State 0,1"""
    assert t200801000_x12(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t200801000_x15(val1=5, z1=1):
    """State 0,4"""
    assert t200801000_x25()
    """State 3"""
    call = t200801000_x16()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t200801000_x27()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t200801000_x16():
    """State 0,1"""
    assert t200801000_x12(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t200801000_x17(val5=12):
    """State 0,2"""
    call = t200801000_x18()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t200801000_x28()
    """State 4"""
    return 0

def t200801000_x18():
    """State 0,1"""
    assert t200801000_x12(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t200801000_x19(val2=10, val3=12):
    """State 0,5"""
    assert t200801000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t200801000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t200801000_x30()
    """Unused"""
    """State 6"""
    return 0

def t200801000_x20():
    """State 0,2"""
    call = t200801000_x12(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t200801000_x21():
    """State 0,1"""
    assert t200801000_x12(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t200801000_x22():
    """State 0,1"""
    assert t200801000_x12(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t200801000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t200801000_x24(flag7=6000, flag8=6000, flag9=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag10=6000, flag11=6001, flag12=6000, flag13=6000, flag14=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t200801000_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag10=flag10, flag11=flag11, flag12=flag12, flag13=flag13, flag14=flag14, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag7):
            """State 3"""
            Label('L0')
            call = t200801000_x10(flag7=flag7, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag7):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag8) or GetEventFlag(flag9):
            """State 2"""
            call = t200801000_x9(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag7):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag8) and not GetEventFlag(flag9):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t200801000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t200801000_x25():
    """State 0,1"""
    assert t200801000_x26()
    """State 2"""
    return 0

def t200801000_x26():
    """State 0,1"""
    assert t200801000_x12(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t200801000_x27():
    """State 0,1"""
    call = t200801000_x12(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t200801000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200801000_x28():
    """State 0,1"""
    call = t200801000_x12(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t200801000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200801000_x29():
    """State 0,1"""
    call = t200801000_x12(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t200801000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200801000_x30():
    """State 0,1"""
    call = t200801000_x12(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t200801000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200801000_x31(text1=_, flag4=_, mode4=1):
    """State 0,5"""
    assert t200801000_x2() and CheckSpecificPersonTalkHasEnded(0)
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
    SetEventFlag(flag4, FlagState.On)
    """State 6"""
    return 0

def t200801000_x32():
    """State 0,1"""
    assert t200801000_x12(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t200801000_x33():
    """State 0,1"""
    assert t200801000_x1()
    """State 2"""
    return 0

def t200801000_x34():
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

def t200801000_x35(text1=10400100, flag4=1209350, text2=10400200, flag5=1209351, text3=10400300, flag6=1209352):
    """State 0"""
    if not GetEventFlag(flag4):
        """State 2"""
        Label('L0')
        assert t200801000_x31(text1=text1, flag4=flag4, mode4=1)
    elif not GetEventFlag(flag5):
        """State 3"""
        assert t200801000_x31(text1=text2, flag4=flag5, mode4=1)
    elif not GetEventFlag(flag6):
        """State 4"""
        assert t200801000_x31(text1=text3, flag4=flag6, mode4=1)
    else:
        """State 1"""
        SetEventFlag(flag4, FlagState.Off)
        SetEventFlag(flag5, FlagState.Off)
        SetEventFlag(flag6, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t200801000_x36(action1=_, flag1=_):
    """State 0,1"""
    SetEventFlag(flag1, FlagState.On)
    """State 2"""
    assert t200801000_x3(action1=action1)
    """State 3"""
    return 0

def t200801000_x37():
    """State 0,1"""
    # talk:10400100:"..."
    # talk:10400200:"..."
    # talk:10400300:"..."
    assert t200801000_x35(text1=10400100, flag4=1209350, text2=10400200, flag5=1209351, text3=10400300, flag6=1209352)
    """State 2"""
    return 0

def t200801000_x38():
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAlt(98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 3"""
    return 0

def t200801000_x39():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t200801000_x40():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,6"""
        assert t200801000_x42()
    elif GetTalkListEntryResult() == 99:
        """State 2"""
        pass
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        pass
    else:
        """State 4"""
        pass
    """State 7"""
    return 0

def t200801000_x41():
    """State 0,1"""
    assert t200801000_x37()
    """State 3"""
    assert t200801000_x38()
    """State 4"""
    assert t200801000_x39()
    """State 2"""
    assert t200801000_x40()
    """State 5"""
    return 0

def t200801000_x42():
    """State 0,1"""
    if DoesSelfHaveSpEffect(9695):
        """State 2"""
        if not GetEventFlag(3832):
            """State 5,15"""
            # action:21041010:"He paints a depiction of the Erdtree. It does not yet look finished."
            # action:21041008:"The Executor faces his canvas with purpose"
            # action:21041009:"The Executor makes bold strokes with his brush"
            assert (t200801000_x43(action1=21041010, flag1=1209363, action2=21041008, flag2=1209361, action3=21041009,
                    flag3=1209362))
        elif GetEventFlag(3832):
            """State 6,16"""
            # action:21041011:"He paints a depiction of the Erdtree. He seems somewhat satisfied."
            # action:21041008:"The Executor faces his canvas with purpose"
            # action:21041009:"The Executor makes bold strokes with his brush"
            assert (t200801000_x43(action1=21041011, flag1=1209364, action2=21041008, flag2=1209361, action3=21041009,
                    flag3=1209362))
    elif DoesSelfHaveSpEffect(9696):
        """State 3"""
        if not GetEventFlag(3832):
            """State 7,13"""
            # action:21041006:"He appears to be thinking about a place far, far away"
            # action:21041004:"The Executor simply stares quietly up at the sky"
            # action:21041005:"The Executor gazes at the commingling of the clouds"
            assert (t200801000_x43(action1=21041006, flag1=1209359, action2=21041004, flag2=1209357, action3=21041005,
                    flag3=1209358))
        elif GetEventFlag(3832):
            """State 8,14"""
            # action:21041007:"He appears to be thinking about what lies beyond the Night's end"
            # action:21041004:"The Executor simply stares quietly up at the sky"
            # action:21041005:"The Executor gazes at the commingling of the clouds"
            assert (t200801000_x43(action1=21041007, flag1=1209360, action2=21041004, flag2=1209357, action3=21041005,
                    flag3=1209358))
    elif DoesSelfHaveSpEffect(9697):
        """State 4"""
        Label('L0')
        if not GetEventFlag(3832):
            """State 9,11"""
            # action:21041000:"The Executor focuses solely upon his painting"
            # action:21041001:"The Executor appears to be facing his inner self"
            # action:21041002:"He appears to be sharpening his spirit. From his stance a certain tension can be perceived, like a blade drawn from its sheathe."
            assert (t200801000_x43(action1=21041000, flag1=1209353, action2=21041001, flag2=1209354, action3=21041002,
                    flag3=1209355))
        elif GetEventFlag(3832):
            """State 10,12"""
            # action:21041003:"There is a tenderness that was not apparent before, as he focuses upon his painting"
            # action:21041001:"The Executor appears to be facing his inner self"
            # action:21041002:"He appears to be sharpening his spirit. From his stance a certain tension can be perceived, like a blade drawn from its sheathe."
            assert (t200801000_x43(action1=21041003, flag1=1209356, action2=21041001, flag2=1209354, action3=21041002,
                    flag3=1209355))
    else:
        Goto('L0')
    """State 17"""
    return 0

def t200801000_x43(action1=_, flag1=_, action2=_, flag2=_, action3=_, flag3=_):
    """State 0,1"""
    if not GetEventFlag(10002800) and not GetEventFlag(10002801) and not GetEventFlag(10002802):
        """State 2,12"""
        if not GetEventFlag(flag1):
            """State 6"""
            Label('L0')
            """State 9"""
            SetEventFlag(10002800, FlagState.On)
            """State 14"""
            assert t200801000_x36(action1=action1, flag1=flag1)
        elif not GetEventFlag(flag2):
            """State 7"""
            Label('L1')
            """State 10"""
            SetEventFlag(10002801, FlagState.On)
            """State 15"""
            assert t200801000_x36(action1=action2, flag1=flag2)
        elif not GetEventFlag(flag3):
            """State 8"""
            Label('L2')
            """State 11"""
            SetEventFlag(10002802, FlagState.On)
            """State 16"""
            assert t200801000_x36(action1=action3, flag1=flag3)
        else:
            """State 17"""
            assert t200801000_x4(z5=3)
            """State 4"""
            if CompareRNGValue(CompareType.Equal, 0) == True:
                Goto('L0')
            elif CompareRNGValue(CompareType.Equal, 1) == True:
                Goto('L1')
            elif CompareRNGValue(CompareType.Equal, 2) == True:
                Goto('L2')
    else:
        """State 3,5"""
        if GetEventFlag(10002800):
            Goto('L0')
        elif GetEventFlag(10002801):
            Goto('L1')
        elif GetEventFlag(10002802):
            Goto('L2')
        else:
            """State 13"""
            Goto('L2')
    """State 18"""
    return 0

