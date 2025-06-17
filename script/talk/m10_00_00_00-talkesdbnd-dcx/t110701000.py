# -*- coding: utf-8 -*-
def t110701000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t110701000_x6(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t110701000_1000():
    """State 0,2,3"""
    assert t110701000_x49()
    """State 1"""
    EndMachine(1000)
    Quit()

def t110701000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t110701000_x0(actionbutton1=6000, flag36=6001, flag40=6000, flag41=6000, flag42=6000, flag43=6000, flag35=6000)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif f301(-1) == Hero.Wylder and f302(-1) == 3:
        """State 3,5"""
        t110701000_x53()
        Quit()

def t110701000_x0(actionbutton1=6000, flag36=6001, flag40=6000, flag41=6000, flag42=6000, flag43=6000, flag35=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag36) or GetEventFlag(flag40) or GetEventFlag(flag41) or GetEventFlag(flag42) or
                GetEventFlag(flag43))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag35)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag35) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag36) and not GetEventFlag(flag40) and not GetEventFlag(flag41) and not GetEventFlag(flag42)
            and not GetEventFlag(flag43)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t110701000_x1():
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

def t110701000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t110701000_x3(z5=_):
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

def t110701000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t110701000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t110701000_x1()
    else:
        """State 4,7"""
        call = t110701000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t110701000_x1()
    """State 9"""
    return 0

def t110701000_x5():
    """State 0,1"""
    assert t110701000_x1()
    """State 2"""
    return 0

def t110701000_x6(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t110701000_x23(flag32=flag32, flag33=flag33, flag34=flag34, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag35=flag35, flag36=flag36, flag37=flag37,
                              flag38=flag38, flag39=flag39, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t110701000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t110701000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag35=6000, flag36=6001, flag37=6000,
                  flag38=6000, flag39=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t110701000_x10(actionbutton1=actionbutton1, flag35=flag35, flag36=flag36, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t110701000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag39):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag37) and not GetEventFlag(flag38) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t110701000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t110701000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t110701000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t110701000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t110701000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t110701000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t110701000_x9(flag32=6000, val2=10, val3=12):
    """State 0,8"""
    assert t110701000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag32):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t110701000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t110701000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t110701000_x10(actionbutton1=6000, flag35=6000, flag36=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t110701000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t110701000_x0(actionbutton1=actionbutton1, flag36=flag36, flag40=6000, flag41=6000, flag42=6000,
                flag43=6000, flag35=flag35))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110701000_x11(machine1=_, val6=_):
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

def t110701000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t110701000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t110701000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t110701000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t110701000_x13():
    """State 0,1"""
    assert t110701000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t110701000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t110701000_x24()
    """State 3"""
    call = t110701000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t110701000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t110701000_x15():
    """State 0,1"""
    assert t110701000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t110701000_x16(val5=12):
    """State 0,2"""
    call = t110701000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t110701000_x27()
    """State 4"""
    return 0

def t110701000_x17():
    """State 0,1"""
    assert t110701000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t110701000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t110701000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t110701000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t110701000_x29()
    """Unused"""
    """State 6"""
    return 0

def t110701000_x19():
    """State 0,2"""
    call = t110701000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t110701000_x20():
    """State 0,1"""
    assert t110701000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t110701000_x21():
    """State 0,1"""
    assert t110701000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t110701000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t110701000_x23(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t110701000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag35=flag35, flag36=flag36, flag37=flag37, flag38=flag38, flag39=flag39, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag32):
            """State 3"""
            Label('L0')
            call = t110701000_x9(flag32=flag32, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag32):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag33) or GetEventFlag(flag34):
            """State 2"""
            call = t110701000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag32):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag33) and not GetEventFlag(flag34):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t110701000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t110701000_x24():
    """State 0,1"""
    assert t110701000_x25()
    """State 2"""
    return 0

def t110701000_x25():
    """State 0,1"""
    assert t110701000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t110701000_x26():
    """State 0,1"""
    call = t110701000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t110701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110701000_x27():
    """State 0,1"""
    call = t110701000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t110701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110701000_x28():
    """State 0,1"""
    call = t110701000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t110701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110701000_x29():
    """State 0,1"""
    call = t110701000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t110701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110701000_x30(text1=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t110701000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t110701000_x31(text18=10505400, mode4=1):
    """State 0,4"""
    assert t110701000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10505400:"What is it?"
    TalkToPlayer(text18, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t110701000_x32():
    """State 0,1"""
    assert t110701000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t110701000_x33():
    """State 0,1"""
    assert t110701000_x1()
    """State 2"""
    return 0

def t110701000_x34():
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

def t110701000_x35(text16=10505800, flag30=-1, text17=10505900, flag31=-1):
    """State 0,4"""
    assert t110701000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110701000_x30(text1=text16, flag1=flag30, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110701000_x30(text1=text17, flag1=flag31, mode5=1)
    """State 5"""
    return 0

def t110701000_x36(text16=10505800, flag28=1209307, text17=10505900, flag29=1209308):
    """State 0"""
    if not GetEventFlag(flag28):
        """State 1"""
        assert t110701000_x30(text1=text16, flag1=flag28, mode5=1)
    elif not GetEventFlag(flag29):
        """State 2"""
        assert t110701000_x30(text1=text17, flag1=flag29, mode5=1)
    else:
        """State 3"""
        assert t110701000_x35(text16=text16, flag30=-1, text17=text17, flag31=-1)
    """State 4"""
    return 0

def t110701000_x37(text13=_, flag25=_, text14=_, flag26=_, text15=_, flag27=_):
    """State 0"""
    if not GetEventFlag(flag25):
        """State 2"""
        Label('L0')
        assert t110701000_x30(text1=text13, flag1=flag25, mode5=1)
    elif not GetEventFlag(flag26):
        """State 3"""
        assert t110701000_x30(text1=text14, flag1=flag26, mode5=1)
    elif not GetEventFlag(flag27):
        """State 4"""
        assert t110701000_x30(text1=text15, flag1=flag27, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag25, FlagState.Off)
        SetEventFlag(flag26, FlagState.Off)
        SetEventFlag(flag27, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t110701000_x38(text8=10505800, flag15=1209307, text9=10505900, flag16=1209308, text10=10506000, flag17=1209309,
                   text11=10506100, flag18=1209310, text12=10506200, flag19=1209311):
    """State 0"""
    if not GetEventFlag(flag15):
        """State 1"""
        assert t110701000_x30(text1=text8, flag1=flag15, mode5=1)
    elif not GetEventFlag(flag16):
        """State 2"""
        assert t110701000_x30(text1=text9, flag1=flag16, mode5=1)
    elif not GetEventFlag(flag17):
        """State 3"""
        assert t110701000_x30(text1=text10, flag1=flag17, mode5=1)
    elif not GetEventFlag(flag18):
        """State 4"""
        assert t110701000_x30(text1=text11, flag1=flag18, mode5=1)
    elif not GetEventFlag(flag19):
        """State 5"""
        assert t110701000_x30(text1=text12, flag1=flag19, mode5=1)
    else:
        """State 6"""
        assert (t110701000_x39(text8=text8, flag20=-1, text9=text9, flag21=-1, text10=text10, flag22=-1, text11=text11,
                flag23=-1, text12=text12, flag24=-1))
    """State 7"""
    return 0

def t110701000_x39(text8=10505800, flag20=-1, text9=10505900, flag21=-1, text10=10506000, flag22=-1, text11=10506100,
                   flag23=-1, text12=10506200, flag24=-1):
    """State 0,5"""
    assert t110701000_x3(z5=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110701000_x30(text1=text8, flag1=flag20, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110701000_x30(text1=text9, flag1=flag21, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t110701000_x30(text1=text10, flag1=flag22, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t110701000_x30(text1=text11, flag1=flag23, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t110701000_x30(text1=text12, flag1=flag24, mode5=1)
    """State 8"""
    return 0

def t110701000_x40(text1=10505800, flag8=-1, text2=10505900, flag9=-1, text3=10506100, flag10=-1, text4=10506200,
                   flag11=-1, text5=10506300, flag12=-1, text6=10506400, flag13=-1, text7=10506500, flag14=-1):
    """State 0,5"""
    assert t110701000_x3(z5=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110701000_x30(text1=text1, flag1=flag8, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110701000_x30(text1=text2, flag1=flag9, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t110701000_x30(text1=text3, flag1=flag10, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t110701000_x30(text1=text4, flag1=flag11, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t110701000_x30(text1=text5, flag1=flag12, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t110701000_x30(text1=text6, flag1=flag13, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t110701000_x30(text1=text7, flag1=flag14, mode5=1)
    """State 10"""
    return 0

def t110701000_x41(text1=10505800, flag1=1209307, text2=10505900, flag2=1209308, text3=10506100, flag3=1209310,
                   text4=10506200, flag4=1209311, text5=10506300, flag5=1209312, text6=10506400, flag6=1209313,
                   text7=10506500, flag7=1209314):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t110701000_x30(text1=text1, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t110701000_x30(text1=text2, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t110701000_x30(text1=text3, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t110701000_x30(text1=text4, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t110701000_x30(text1=text5, flag1=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t110701000_x30(text1=text6, flag1=flag6, mode5=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t110701000_x30(text1=text7, flag1=flag7, mode5=1)
    else:
        """State 8"""
        assert (t110701000_x40(text1=text1, flag8=-1, text2=text2, flag9=-1, text3=text3, flag10=-1, text4=text4,
                flag11=-1, text5=text5, flag12=-1, text6=text6, flag13=-1, text7=text7, flag14=-1))
    """State 9"""
    return 0

def t110701000_x42():
    """State 0"""
    if DoesSelfHaveSpEffect(9690):
        """State 3,9"""
        Label('L0')
        # talk:10505400:"What is it?"
        assert t110701000_x30(text1=10505400, flag1=1209300, mode5=1)
    elif DoesSelfHaveSpEffect(9691):
        """State 2"""
        # eventflag:102:First sortie completed
        if not GetEventFlag(102):
            """State 7,4"""
            Label('L1')
            Goto('L0')
        elif GetEventFlag(10002011) or GetEventFlag(10002012) or GetEventFlag(10002010):
            """State 5"""
            Goto('L1')
        else:
            """State 11"""
            # talk:10505600:"I fear I may succumb to sleep..."
            assert t110701000_x30(text1=10505600, flag1=1209302, mode5=1)
    elif DoesSelfHaveSpEffect(9692):
        """State 1"""
        if GetEventFlag(10002011) or GetEventFlag(10002012):
            """State 6"""
            Goto('L1')
        else:
            """State 10"""
            # talk:10505500:"Wishest thou to converse?"
            assert t110701000_x30(text1=10505500, flag1=1209301, mode5=1)
    else:
        Goto('L1')
    """State 12"""
    return 0
    """Unused"""
    """State 8"""
    # talk:10505400:"What is it?"
    # talk:10505500:"Wishest thou to converse?"
    # talk:10505600:"I fear I may succumb to sleep..."
    t110701000_x37(text13=10505400, flag25=1209301, text14=10505500, flag26=1209302, text15=10505600, flag27=1209303)
    Quit()

def t110701000_x43():
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

def t110701000_x44():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t110701000_x45():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,6"""
        assert t110701000_x47()
    elif GetTalkListEntryResult() == 99:
        """State 2,7"""
        Label('L0')
        # talk:10505100:"Till next we meet..."
        # talk:10505200:"I see."
        # talk:10505300:"Is our business concluded?"
        assert (t110701000_x37(text13=10505100, flag25=1209307, text14=10505200, flag26=1209308, text15=10505300,
                flag27=1209309))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t110701000_x46():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t110701000_x48()
    else:
        """State 2"""
        assert t110701000_x42()
        """State 4"""
        assert t110701000_x43()
        """State 5"""
        assert t110701000_x44()
        """State 3"""
        assert t110701000_x45()
    """State 7"""
    return 0

def t110701000_x47():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10505800:"We must put the night sky to rights, to see its beauty once more..."
        # talk:10505900:"I believe myself skilled...in my craft..."
        # talk:10506100:"There is much to be done..."
        # talk:10506200:"How it bustles here, now..."
        # talk:10506300:"Finally. The moment is come."
        # talk:10506400:"I can't help but be happy, amid all this novelty..."
        # talk:10506500:"We must both do our part...to see this matter settled."
        assert (t110701000_x41(text1=10505800, flag1=1209307, text2=10505900, flag2=1209308, text3=10506100, flag3=1209310,
                text4=10506200, flag4=1209311, text5=10506300, flag5=1209312, text6=10506400, flag6=1209313, text7=10506500,
                flag7=1209314))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10505800:"We must put the night sky to rights, to see its beauty once more..."
        # talk:10505900:"I believe myself skilled...in my craft..."
        # talk:10506000:"Can the hound be taught a new trick, I wonder?"
        # talk:10506100:"There is much to be done..."
        # talk:10506200:"How it bustles here, now..."
        assert (t110701000_x38(text8=10505800, flag15=1209307, text9=10505900, flag16=1209308, text10=10506000,
                flag17=1209309, text11=10506100, flag18=1209310, text12=10506200, flag19=1209311))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10505800:"We must put the night sky to rights, to see its beauty once more..."
        # talk:10505900:"I believe myself skilled...in my craft..."
        assert t110701000_x36(text16=10505800, flag28=1209307, text17=10505900, flag29=1209308)
    """State 7"""
    return 0

def t110701000_x48():
    """State 0,1"""
    # talk:10505400:"What is it?"
    assert t110701000_x31(text18=10505400, mode4=1)
    """State 2"""
    return 0

def t110701000_x49():
    """State 0,1"""
    assert t110701000_x50()
    """State 2"""
    return 0

def t110701000_x50():
    """State 0"""
    if f302(-1) == 4:
        """State 2"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110701000_x51()
    elif f302(-1) == 5:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110701000_x55()
    else:
        """State 1,3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110701000_x42()
    """State 5"""
    return 0

def t110701000_x51():
    """State 0"""
    if GetEventFlag(3122):
        """State 2,10"""
        Label('L0')
        # talk:10506800:"..."
        assert t110701000_x30(text1=10506800, flag1=1119018, mode5=1)
    elif GetEventFlag(3123):
        """State 6"""
        Goto('L0')
    elif GetEventFlag(3114):
        """State 3,11"""
        assert t110701000_x56()
    elif GetEventFlag(3115):
        """State 4,8"""
        # talk:10502200:"Seek thee a tear of silver."
        # talk:10502201:"But the road will be one of hardship..."
        # talk:10502202:"All the same, I wish thee good fortune..."
        # talk:10502203:"For the fortitude required is a rare thing indeed..."
        assert t110701000_x30(text1=10502200, flag1=1119014, mode5=1)
    elif GetEventFlag(3116):
        """State 1,9"""
        Label('L1')
        assert t110701000_x54()
    elif GetEventFlag(3117):
        """State 5"""
        Goto('L1')
    else:
        """State 7,12"""
        assert t110701000_x46()
    """State 13"""
    return 0

def t110701000_x52():
    """State 0,5"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 3"""
    # action:21052001:"It does"
    AddTalkListDataAlt(1, 21052001, -1, 0, False)
    # action:21052002:"It matters little to me"
    AddTalkListDataAlt(2, 21052002, -1, 0, False)
    """State 4"""
    # talk:10503600:"..."
    # talk:10503601:"Does the idea of leaving the Priestess behind trouble thee?"
    ShowShopMessageWithTalk(0, 10503600)
    """State 1"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 6,11"""
        # talk:10503700:"Hmm, what a tender soul thou art..."
        # talk:10503701:"In that case, I have knowledge I would relay."
        assert t110701000_x30(text1=10503700, flag1=1119012, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 7,12"""
        Label('L0')
        # talk:10503800:"Oh my, what a dreadful thing to say."
        # talk:10503801:"Still, I have knowledge that may yet interest thee..."
        assert t110701000_x30(text1=10503800, flag1=1119013, mode5=1)
    elif GetTalkListEntryResult() == 0:
        """State 8"""
        Goto('L0')
    else:
        """State 9"""
        Goto('L0')
    """State 10,13"""
    return 0

def t110701000_x53():
    """State 0,3"""
    Label('L0')
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t110701000_x0(actionbutton1=6000, flag36=6001, flag40=6000, flag41=6000, flag42=6000, flag43=6000,
            flag35=6000))
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 2"""
    Label('L1')
    Goto('L0')
    """State 4"""
    # talk:10503500:"O warrior."
    # talk:10503501:"A moment, if thou wouldst?"
    call = t110701000_x30(text1=10503500, flag1=1119010, mode5=1)
    def WhilePaused():
        GiveSpEffectToSelf(9625)
    if call.Done():
        Goto('L1')
    elif GetDistanceToPlayer() > 8:
        pass
    """State 5"""
    assert t110701000_x1()
    Goto('L1')
    """State 6"""
    return 0

def t110701000_x54():
    """State 0,1"""
    GiveSpEffectToSelf(9968)
    # talk:10503900:"Seek thee a tear of silver."
    # talk:10503901:"Good fortune upon thy search..."
    assert t110701000_x30(text1=10503900, flag1=1119015, mode5=1)
    """State 2"""
    return 0

def t110701000_x55():
    """State 0,1"""
    if not GetEventFlag(1119016):
        """State 2,4"""
        # talk:10506600:"My heartfelt commendations."
        # talk:10506601:"By thy look, I presume thou hast found one."
        # talk:10506602:"It shan't be long now."
        assert t110701000_x30(text1=10506600, flag1=1119016, mode5=1)
    elif GetEventFlag(1119016):
        """State 3,5"""
        # talk:10506700:"It shan't be long now."
        assert t110701000_x30(text1=10506700, flag1=1119017, mode5=1)
    """State 6"""
    return 0

def t110701000_x56():
    """State 0,5"""
    # talk:10506800:"..."
    assert t110701000_x30(text1=10506800, flag1=1119018, mode5=1)
    """State 3"""
    assert t110701000_x43()
    """State 1"""
    # action:21050012:"About taking the Nightlord's power"
    AddTalkListDataAlt(1, 21050012, -1, 1, False)
    """State 4"""
    assert t110701000_x44()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 8"""
        # talk:10503600:"..."
        # talk:10503601:"Does the idea of leaving the Priestess behind trouble thee?"
        assert t110701000_x30(text1=10503600, flag1=1119011, mode5=1)
        """State 6"""
        assert t110701000_x52()
    else:
        """State 7"""
        assert t110701000_x45()
    """State 9"""
    return 0

