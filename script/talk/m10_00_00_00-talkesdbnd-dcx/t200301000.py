# -*- coding: utf-8 -*-
def t200301000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t200301000_x6(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t200301000_1000():
    """State 0,2,3"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t200301000_x45()
    """State 1"""
    EndMachine(1000)
    Quit()

def t200301000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t200301000_x0(actionbutton1=6000, flag32=6001, flag36=6000, flag37=6000, flag38=6000, flag39=6000, flag31=6000)
    if call.Done():
        pass
    elif DoesSelfHaveSpEffect(9672):
        """State 3,5"""
        # actionbutton:6002:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (t200301000_x0(actionbutton1=6002, flag32=6001, flag36=6000, flag37=6000, flag38=6000, flag39=6000,
                flag31=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t200301000_x0(actionbutton1=_, flag32=6001, flag36=6000, flag37=6000, flag38=6000, flag39=6000, flag31=6000):
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
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t200301000_x1():
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

def t200301000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t200301000_x3(z5=_):
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

def t200301000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t200301000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t200301000_x1()
    else:
        """State 4,7"""
        call = t200301000_x31()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t200301000_x1()
    """State 9"""
    return 0

def t200301000_x5():
    """State 0,1"""
    assert t200301000_x1()
    """State 2"""
    return 0

def t200301000_x6(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t200301000_x23(flag28=flag28, flag29=flag29, flag30=flag30, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag31=flag31, flag32=flag32, flag33=flag33,
                              flag34=flag34, flag35=flag35, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t200301000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t200301000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag31=6000, flag32=6001, flag33=6000,
                  flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t200301000_x10(actionbutton1=actionbutton1, flag31=flag31, flag32=flag32, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t200301000_x14(val1=val1, z1=z1)
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
            call = t200301000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t200301000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t200301000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t200301000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t200301000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t200301000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t200301000_x9(flag28=6000, val2=10, val3=12):
    """State 0,8"""
    assert t200301000_x33()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag28):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t200301000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200301000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t200301000_x10(actionbutton1=6000, flag31=6000, flag32=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t200301000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t200301000_x0(actionbutton1=actionbutton1, flag32=flag32, flag36=6000, flag37=6000, flag38=6000,
                flag39=6000, flag31=flag31))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200301000_x11(machine1=_, val6=_):
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

def t200301000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t200301000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t200301000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200301000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t200301000_x13():
    """State 0,1"""
    assert t200301000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t200301000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t200301000_x24()
    """State 3"""
    call = t200301000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t200301000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t200301000_x15():
    """State 0,1"""
    assert t200301000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t200301000_x16(val5=12):
    """State 0,2"""
    call = t200301000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t200301000_x27()
    """State 4"""
    return 0

def t200301000_x17():
    """State 0,1"""
    assert t200301000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t200301000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t200301000_x33()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t200301000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t200301000_x29()
    """Unused"""
    """State 6"""
    return 0

def t200301000_x19():
    """State 0,2"""
    call = t200301000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t200301000_x20():
    """State 0,1"""
    assert t200301000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t200301000_x21():
    """State 0,1"""
    assert t200301000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t200301000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t200301000_x23(flag28=6000, flag29=6000, flag30=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag31=6000, flag32=6001, flag33=6000, flag34=6000, flag35=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t200301000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag31=flag31, flag32=flag32, flag33=flag33, flag34=flag34, flag35=flag35, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag28):
            """State 3"""
            Label('L0')
            call = t200301000_x9(flag28=flag28, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag28):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag29) or GetEventFlag(flag30):
            """State 2"""
            call = t200301000_x8(val2=val2, val3=val3)
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
        assert t200301000_x32() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t200301000_x24():
    """State 0,1"""
    assert t200301000_x25()
    """State 2"""
    return 0

def t200301000_x25():
    """State 0,1"""
    assert t200301000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t200301000_x26():
    """State 0,1"""
    call = t200301000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t200301000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200301000_x27():
    """State 0,1"""
    call = t200301000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t200301000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200301000_x28():
    """State 0,1"""
    call = t200301000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t200301000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200301000_x29():
    """State 0,1"""
    call = t200301000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t200301000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200301000_x30(text1=_, flag7=_, mode4=1):
    """State 0,5"""
    assert t200301000_x2() and CheckSpecificPersonTalkHasEnded(0)
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
    SetEventFlag(flag7, FlagState.On)
    """State 6"""
    return 0

def t200301000_x31():
    """State 0,1"""
    assert t200301000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t200301000_x32():
    """State 0,1"""
    assert t200301000_x1()
    """State 2"""
    return 0

def t200301000_x33():
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

def t200301000_x34(text14=10603300, flag26=-1, text15=10603400, flag27=-1):
    """State 0,4"""
    assert t200301000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200301000_x30(text1=text14, flag7=flag26, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200301000_x30(text1=text15, flag7=flag27, mode4=1)
    """State 5"""
    return 0

def t200301000_x35(text14=10603300, flag24=1209106, text15=10603400, flag25=1209107):
    """State 0"""
    if not GetEventFlag(flag24):
        """State 1"""
        assert t200301000_x30(text1=text14, flag7=flag24, mode4=1)
    elif not GetEventFlag(flag25):
        """State 2"""
        assert t200301000_x30(text1=text15, flag7=flag25, mode4=1)
    else:
        """State 3"""
        assert t200301000_x34(text14=text14, flag26=-1, text15=text15, flag27=-1)
    """State 4"""
    return 0

def t200301000_x36(text11=10602700, flag21=1209103, text12=10602800, flag22=1209104, text13=10602900, flag23=1209105):
    """State 0"""
    if not GetEventFlag(flag21):
        """State 2"""
        Label('L0')
        assert t200301000_x30(text1=text11, flag7=flag21, mode4=1)
    elif not GetEventFlag(flag22):
        """State 3"""
        assert t200301000_x30(text1=text12, flag7=flag22, mode4=1)
    elif not GetEventFlag(flag23):
        """State 4"""
        assert t200301000_x30(text1=text13, flag7=flag23, mode4=1)
    else:
        """State 1"""
        SetEventFlag(flag21, FlagState.Off)
        SetEventFlag(flag22, FlagState.Off)
        SetEventFlag(flag23, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t200301000_x37(text7=10603300, flag13=1209106, text8=10603400, flag14=1209107, text9=10603600, flag15=1209109,
                   text10=10603700, flag16=1209110):
    """State 0"""
    if not GetEventFlag(flag13):
        """State 1"""
        assert t200301000_x30(text1=text7, flag7=flag13, mode4=1)
    elif not GetEventFlag(flag14):
        """State 2"""
        assert t200301000_x30(text1=text8, flag7=flag14, mode4=1)
    elif not GetEventFlag(flag15):
        """State 3"""
        assert t200301000_x30(text1=text9, flag7=flag15, mode4=1)
    elif not GetEventFlag(flag16):
        """State 4"""
        assert t200301000_x30(text1=text10, flag7=flag16, mode4=1)
    else:
        """State 5"""
        assert (t200301000_x39(text7=text7, flag17=-1, text8=text8, flag18=-1, text9=text9, flag19=-1, text10=text10,
                flag20=-1))
    """State 6"""
    return 0

def t200301000_x38(text1=10603300, flag1=1209106, text2=10603400, flag2=1209107, text3=10603700, flag3=1209110,
                   text4=10603900, flag4=1209112, text5=10604000, flag5=1209113, text6=10604100, flag6=1209114):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t200301000_x30(text1=text1, flag7=flag1, mode4=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t200301000_x30(text1=text2, flag7=flag2, mode4=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t200301000_x30(text1=text3, flag7=flag3, mode4=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t200301000_x30(text1=text4, flag7=flag4, mode4=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t200301000_x30(text1=text5, flag7=flag5, mode4=1)
    elif not GetEventFlag(flag6):
        """State 7"""
        assert t200301000_x30(text1=text6, flag7=flag6, mode4=1)
    else:
        """State 6"""
        assert (t200301000_x40(text1=text1, flag7=-1, text2=text2, flag8=-1, text3=text3, flag9=-1, text4=text4,
                flag10=-1, text5=text5, flag11=-1, text6=text6, flag12=-1))
    """State 8"""
    return 0

def t200301000_x39(text7=10603300, flag17=-1, text8=10603400, flag18=-1, text9=10603600, flag19=-1, text10=10603700,
                   flag20=-1):
    """State 0,5"""
    assert t200301000_x3(z5=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200301000_x30(text1=text7, flag7=flag17, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200301000_x30(text1=text8, flag7=flag18, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t200301000_x30(text1=text9, flag7=flag19, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t200301000_x30(text1=text10, flag7=flag20, mode4=1)
    """State 7"""
    return 0

def t200301000_x40(text1=10603300, flag7=-1, text2=10603400, flag8=-1, text3=10603700, flag9=-1, text4=10603900,
                   flag10=-1, text5=10604000, flag11=-1, text6=10604100, flag12=-1):
    """State 0,5"""
    assert t200301000_x3(z5=6)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t200301000_x30(text1=text1, flag7=flag7, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t200301000_x30(text1=text2, flag7=flag8, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t200301000_x30(text1=text3, flag7=flag9, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t200301000_x30(text1=text4, flag7=flag10, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t200301000_x30(text1=text5, flag7=flag11, mode4=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t200301000_x30(text1=text6, flag7=flag12, mode4=1)
    """State 9"""
    return 0

def t200301000_x41():
    """State 0"""
    if DoesSelfHaveSpEffect(9671):
        """State 1,5"""
        # talk:10603200:"As ready as I'll ever be."
        assert t200301000_x30(text1=10603200, flag7=1209102, mode4=1)
    elif DoesSelfHaveSpEffect(9670):
        """State 3,6"""
        Label('L0')
        # talk:10603000:"I think I'm good to go."
        assert t200301000_x30(text1=10603000, flag7=1209100, mode4=1)
    elif DoesSelfHaveSpEffect(9672):
        """State 2,7"""
        # talk:10603100:"Make it quick."
        assert t200301000_x30(text1=10603100, flag7=1209101, mode4=1)
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t200301000_x42():
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

def t200301000_x43():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t200301000_x44():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,9"""
        assert t200301000_x46()
    elif GetTalkListEntryResult() == 99:
        """State 2,6"""
        Label('L0')
        if GetEventFlag(10002011) or GetEventFlag(10002012):
            """State 7,10"""
            # talk:10602700:"Of course."
            assert t200301000_x30(text1=10602700, flag7=1209103, mode4=1)
        else:
            """State 8"""
            # talk:10602700:"Of course."
            # talk:10602800:"I stand at the ready."
            # talk:10602900:"Until next time."
            assert (t200301000_x36(text11=10602700, flag21=1209103, text12=10602800, flag22=1209104, text13=10602900,
                    flag23=1209105))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 11"""
    return 0

def t200301000_x45():
    """State 0,1"""
    assert t200301000_x41()
    """State 3"""
    assert t200301000_x42()
    """State 4"""
    assert t200301000_x43()
    """State 2"""
    assert t200301000_x44()
    """State 5"""
    return 0

def t200301000_x46():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10603300:"You only need to land one good blow to punish a fleet-footed adversary."
        # talk:10603301:"Be relentless. That's your best bet."
        # talk:10603400:"A supremely vexing opponent, indeed."
        # talk:10603401:"I've had to face shifting targets before, but never a natural phenomenon..."
        # talk:10603700:"If there's more work to be done, so be it."
        # talk:10603701:"As ever, we forge on."
        # talk:10603900:"Finally, the real thing rears its ugly head."
        # talk:10603901:"This time we cannot miss our mark."
        # talk:10604000:"That wasn't easy. But I learned a great deal."
        # talk:10604001:"This will serve me well in future work..."
        # talk:10604100:"We know what must be done...now, more than ever."
        assert (t200301000_x38(text1=10603300, flag1=1209106, text2=10603400, flag2=1209107, text3=10603700, flag3=1209110,
                text4=10603900, flag4=1209112, text5=10604000, flag5=1209113, text6=10604100, flag6=1209114))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10603300:"You only need to land one good blow to punish a fleet-footed adversary."
        # talk:10603301:"Be relentless. That's your best bet."
        # talk:10603400:"A supremely vexing opponent, indeed."
        # talk:10603401:"I've had to face shifting targets before, but never a natural phenomenon..."
        # talk:10603600:"Are these many Lords vying for the same throne?"
        # talk:10603601:"Perhaps they'll do us a favour and wipe each other out..."
        # talk:10603700:"If there's more work to be done, so be it."
        # talk:10603701:"As ever, we forge on."
        assert (t200301000_x37(text7=10603300, flag13=1209106, text8=10603400, flag14=1209107, text9=10603600,
                flag15=1209109, text10=10603700, flag16=1209110))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10603300:"You only need to land one good blow to punish a fleet-footed adversary."
        # talk:10603301:"Be relentless. That's your best bet."
        # talk:10603400:"A supremely vexing opponent, indeed."
        # talk:10603401:"I've had to face shifting targets before, but never a natural phenomenon..."
        assert t200301000_x35(text14=10603300, flag24=1209106, text15=10603400, flag25=1209107)
    """State 7"""
    return 0

