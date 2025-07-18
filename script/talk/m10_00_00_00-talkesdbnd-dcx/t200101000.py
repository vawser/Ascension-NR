# -*- coding: utf-8 -*-
def t200101000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t200101000_x6(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t200101000_1000():
    """State 0,2,3"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t200101000_x46()
    """State 1"""
    EndMachine(1000)
    Quit()

def t200101000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t200101000_x0(actionbutton1=6000, flag32=6001, flag36=6000, flag37=6000, flag38=6000, flag39=6000,
            flag31=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t200101000_x0(actionbutton1=6000, flag32=6001, flag36=6000, flag37=6000, flag38=6000, flag39=6000, flag31=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag32) or GetEventFlag(flag36) or GetEventFlag(flag37) or GetEventFlag(flag38) or
                GetEventFlag(flag39))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag31)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag31) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag32) and not GetEventFlag(flag36) and not GetEventFlag(flag37) and not GetEventFlag(flag38)
            and not GetEventFlag(flag39)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t200101000_x1():
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

def t200101000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t200101000_x3(z5=_):
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

def t200101000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t200101000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t200101000_x1()
    else:
        """State 4,7"""
        call = t200101000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t200101000_x1()
    """State 9"""
    return 0

def t200101000_x5():
    """State 0,1"""
    assert t200101000_x1()
    """State 2"""
    return 0

def t200101000_x6(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t200101000_x23(flag28=flag28, flag29=flag29, flag30=flag30, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag31=flag31, flag32=flag32, flag33=flag33,
                              flag34=flag34, flag35=flag35, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t200101000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t200101000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag31=6000, flag32=6001, flag33=6000,
                  flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t200101000_x10(actionbutton1=actionbutton1, flag31=flag31, flag32=flag32, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t200101000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag35):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag33) and not GetEventFlag(flag34) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t200101000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t200101000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t200101000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t200101000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t200101000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t200101000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t200101000_x9(flag28=6000, val2=10, val3=12):
    """State 0,8"""
    assert t200101000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag28):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t200101000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200101000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t200101000_x10(actionbutton1=6000, flag31=6000, flag32=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t200101000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t200101000_x0(actionbutton1=actionbutton1, flag32=flag32, flag36=6000, flag37=6000, flag38=6000,
                flag39=6000, flag31=flag31))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200101000_x11(machine1=_, val6=_):
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

def t200101000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t200101000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t200101000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200101000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t200101000_x13():
    """State 0,1"""
    assert t200101000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t200101000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t200101000_x24()
    """State 3"""
    call = t200101000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t200101000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t200101000_x15():
    """State 0,1"""
    assert t200101000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t200101000_x16(val5=12):
    """State 0,2"""
    call = t200101000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t200101000_x27()
    """State 4"""
    return 0

def t200101000_x17():
    """State 0,1"""
    assert t200101000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t200101000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t200101000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t200101000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t200101000_x29()
    """Unused"""
    """State 6"""
    return 0

def t200101000_x19():
    """State 0,2"""
    call = t200101000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t200101000_x20():
    """State 0,1"""
    assert t200101000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t200101000_x21():
    """State 0,1"""
    assert t200101000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t200101000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t200101000_x23(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t200101000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag31=flag31, flag32=flag32, flag33=flag33, flag34=flag34, flag35=flag35, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag28):
            """State 3"""
            Label('L0')
            call = t200101000_x9(flag28=flag28, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag28):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag29) or GetEventFlag(flag30):
            """State 2"""
            call = t200101000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag28):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag29) and not GetEventFlag(flag30):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t200101000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t200101000_x24():
    """State 0,1"""
    assert t200101000_x25()
    """State 2"""
    return 0

def t200101000_x25():
    """State 0,1"""
    assert t200101000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t200101000_x26():
    """State 0,1"""
    call = t200101000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t200101000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200101000_x27():
    """State 0,1"""
    call = t200101000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t200101000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200101000_x28():
    """State 0,1"""
    call = t200101000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t200101000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200101000_x29():
    """State 0,1"""
    call = t200101000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t200101000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200101000_x30(text1=_, flag7=_, mode5=1):
    """State 0,5"""
    assert t200101000_x2() and CheckSpecificPersonTalkHasEnded(0)
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
    SetEventFlag(flag7, FlagState.On)
    """State 6"""
    return 0

def t200101000_x31(text16=10103100, mode4=1):
    """State 0,4"""
    assert t200101000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10103100:"When do we fight?"
    TalkToPlayer(text16, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t200101000_x32():
    """State 0,1"""
    assert t200101000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t200101000_x33():
    """State 0,1"""
    assert t200101000_x1()
    """State 2"""
    return 0

def t200101000_x34():
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

def t200101000_x35(text14=10102100, flag26=-1, text15=10103200, flag27=-1):
    """State 0,4"""
    assert t200101000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200101000_x30(text1=text14, flag7=flag26, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200101000_x30(text1=text15, flag7=flag27, mode5=1)
    """State 5"""
    return 0

def t200101000_x36(text14=10102100, flag24=1209006, text15=10103200, flag25=1209007):
    """State 0"""
    if not GetEventFlag(flag24):
        """State 1"""
        assert t200101000_x30(text1=text14, flag7=flag24, mode5=1)
    elif not GetEventFlag(flag25):
        """State 2"""
        assert t200101000_x30(text1=text15, flag7=flag25, mode5=1)
    else:
        """State 3"""
        assert t200101000_x35(text14=text14, flag26=-1, text15=text15, flag27=-1)
    """State 4"""
    return 0

def t200101000_x37(text11=10101600, flag21=1209003, text12=10101700, flag22=1209004, text13=10101800, flag23=1209005):
    """State 0"""
    if not GetEventFlag(flag21):
        """State 2"""
        Label('L0')
        assert t200101000_x30(text1=text11, flag7=flag21, mode5=1)
    elif not GetEventFlag(flag22):
        """State 3"""
        assert t200101000_x30(text1=text12, flag7=flag22, mode5=1)
    elif not GetEventFlag(flag23):
        """State 4"""
        assert t200101000_x30(text1=text13, flag7=flag23, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag21, FlagState.Off)
        SetEventFlag(flag22, FlagState.Off)
        SetEventFlag(flag23, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t200101000_x38(text7=10103200, flag13=1209007, text8=10102200, flag14=1209009, text9=10102300, flag15=1209010,
                   text10=10102400, flag16=1209011):
    """State 0"""
    if not GetEventFlag(flag13):
        """State 1"""
        assert t200101000_x30(text1=text7, flag7=flag13, mode5=1)
    elif not GetEventFlag(flag14):
        """State 2"""
        assert t200101000_x30(text1=text8, flag7=flag14, mode5=1)
    elif not GetEventFlag(flag15):
        """State 3"""
        assert t200101000_x30(text1=text9, flag7=flag15, mode5=1)
    elif not GetEventFlag(flag16):
        """State 4"""
        assert t200101000_x30(text1=text10, flag7=flag16, mode5=1)
    else:
        """State 5"""
        assert (t200101000_x40(text7=text7, flag17=-1, text8=text8, flag18=-1, text9=text9, flag19=-1, text10=text10,
                flag20=-1))
    """State 6"""
    return 0

def t200101000_x39(text1=10103200, flag1=1209007, text2=10102300, flag2=1209010, text3=10102400, flag3=1209011,
                   text4=10102500, flag4=1209012, text5=10102600, flag5=1209013, text6=10102700, flag6=1209014):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t200101000_x30(text1=text1, flag7=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t200101000_x30(text1=text2, flag7=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t200101000_x30(text1=text3, flag7=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t200101000_x30(text1=text4, flag7=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t200101000_x30(text1=text5, flag7=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 7"""
        assert t200101000_x30(text1=text6, flag7=flag6, mode5=1)
    else:
        """State 6"""
        assert (t200101000_x41(text1=text1, flag7=-1, text2=text2, flag8=-1, text3=text3, flag9=-1, text4=text4,
                flag10=-1, text5=text5, flag11=-1, text6=text6, flag12=-1))
    """State 8"""
    return 0

def t200101000_x40(text7=10103200, flag17=-1, text8=10102200, flag18=-1, text9=10102300, flag19=-1, text10=10102400,
                   flag20=-1):
    """State 0,5"""
    assert t200101000_x3(z5=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200101000_x30(text1=text7, flag7=flag17, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200101000_x30(text1=text8, flag7=flag18, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t200101000_x30(text1=text9, flag7=flag19, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t200101000_x30(text1=text10, flag7=flag20, mode5=1)
    """State 7"""
    return 0

def t200101000_x41(text1=10103200, flag7=-1, text2=10102300, flag8=-1, text3=10102400, flag9=-1, text4=10102500,
                   flag10=-1, text5=10102600, flag11=-1, text6=10102700, flag12=-1):
    """State 0,5"""
    assert t200101000_x3(z5=6)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200101000_x30(text1=text1, flag7=flag7, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200101000_x30(text1=text2, flag7=flag8, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t200101000_x30(text1=text3, flag7=flag9, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t200101000_x30(text1=text4, flag7=flag10, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t200101000_x30(text1=text5, flag7=flag11, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t200101000_x30(text1=text6, flag7=flag12, mode5=1)
    """State 9"""
    return 0

def t200101000_x42():
    """State 0"""
    if DoesSelfHaveSpEffect(9660):
        """State 1,6"""
        # talk:10101900:"This won't be easy. We face a true horror."
        # talk:10101901:"We can't know what's coming, but we can prepare."
        assert t200101000_x30(text1=10101900, flag7=1209000, mode5=1)
    elif DoesSelfHaveSpEffect(9661):
        """State 2,5"""
        Label('L0')
        # talk:10103100:"When do we fight?"
        assert t200101000_x30(text1=10103100, flag7=1209002, mode5=1)
    elif DoesSelfHaveSpEffect(9662):
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 7"""
    return 0

def t200101000_x43():
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

def t200101000_x44():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t200101000_x45():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,6"""
        assert t200101000_x47()
    elif GetTalkListEntryResult() == 99:
        """State 2,7"""
        Label('L0')
        # talk:10101600:"..."
        # talk:10101700:"Hmm."
        # talk:10101800:"Fine."
        assert (t200101000_x37(text11=10101600, flag21=1209003, text12=10101700, flag22=1209004, text13=10101800,
                flag23=1209005))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t200101000_x46():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t200101000_x48()
    else:
        """State 2"""
        assert t200101000_x42()
        """State 4"""
        assert t200101000_x43()
        """State 5"""
        assert t200101000_x44()
        """State 3"""
        assert t200101000_x45()
    """State 7"""
    return 0

def t200101000_x47():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10103200:"The Night could swallow us at any moment."
        # talk:10103201:"Don't expect me to show the fiends any mercy."
        # talk:10102300:"The land here is cursed. Alongside every creature that walks it."
        # talk:10102301:"I suppose it's fitting... as a place to bury that abomination."
        # talk:10102400:"We've seen our share of sacrifice. But we always knew there would be a cost."
        # talk:10102401:"I ask myself how I’m still alive...and all I can think is "sheer luck"."
        # talk:10102500:"The time has come."
        # talk:10102501:"Let's finish this."
        # talk:10102600:"My instincts are telling me—this battle will be the last."
        # talk:10102601:"One thing... I couldn't have done it alone."
        # talk:10102602:"Thank you."
        # talk:10102700:"The stakes have risen. But I am as calm as I've ever been. Calmer, perhaps."
        # talk:10102701:"Makes no sense, but it's true."
        assert (t200101000_x39(text1=10103200, flag1=1209007, text2=10102300, flag2=1209010, text3=10102400, flag3=1209011,
                text4=10102500, flag4=1209012, text5=10102600, flag5=1209013, text6=10102700, flag6=1209014))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10103200:"The Night could swallow us at any moment."
        # talk:10103201:"Don't expect me to show the fiends any mercy."
        # talk:10102200:"So there's more than one Lord? That explains it. They have the same scent."
        # talk:10102201:"Fine. We track them down, and kill them all."
        # talk:10102300:"The land here is cursed. Alongside every creature that walks it."
        # talk:10102301:"I suppose it's fitting... as a place to bury that abomination."
        # talk:10102400:"We've seen our share of sacrifice. But we always knew there would be a cost."
        # talk:10102401:"I ask myself how I’m still alive...and all I can think is "sheer luck"."
        assert (t200101000_x38(text7=10103200, flag13=1209007, text8=10102200, flag14=1209009, text9=10102300,
                flag15=1209010, text10=10102400, flag16=1209011))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10102100:"That beast... Was that the Nightlord?"
        # talk:10103200:"The Night could swallow us at any moment."
        # talk:10103201:"Don't expect me to show the fiends any mercy."
        assert t200101000_x36(text14=10102100, flag24=1209006, text15=10103200, flag25=1209007)
    """State 7"""
    return 0

def t200101000_x48():
    """State 0,1"""
    # talk:10103100:"When do we fight?"
    assert t200101000_x31(text16=10103100, mode4=1)
    """State 2"""
    return 0

