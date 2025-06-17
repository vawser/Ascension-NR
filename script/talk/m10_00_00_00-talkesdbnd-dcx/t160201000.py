# -*- coding: utf-8 -*-
def t160201000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t160201000_x6(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t160201000_1000():
    """State 0,2,3"""
    assert t160201000_x56()
    """State 1"""
    EndMachine(1000)
    Quit()

def t160201000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t160201000_x0(actionbutton1=6000, flag62=6001, flag66=6000, flag67=6000, flag68=6000, flag69=6000,
            flag61=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t160201000_x0(actionbutton1=6000, flag62=6001, flag66=6000, flag67=6000, flag68=6000, flag69=6000, flag61=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag62) or GetEventFlag(flag66) or GetEventFlag(flag67) or GetEventFlag(flag68) or
                GetEventFlag(flag69))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag61)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag61) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag62) and not GetEventFlag(flag66) and not GetEventFlag(flag67) and not GetEventFlag(flag68)
            and not GetEventFlag(flag69)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t160201000_x1():
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

def t160201000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t160201000_x3(z7=_):
    """State 0,2"""
    if not CompareRNGValue(CompareType.Equal, 0) != -1:
        """State 1,4"""
        ShuffleRNGSeed(z7)
    else:
        """State 3"""
        pass
    """State 5"""
    SetRNGSeed()
    """State 6"""
    return 0

def t160201000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t160201000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t160201000_x1()
    else:
        """State 4,7"""
        call = t160201000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t160201000_x1()
    """State 9"""
    return 0

def t160201000_x5():
    """State 0,1"""
    assert t160201000_x1()
    """State 2"""
    return 0

def t160201000_x6(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t160201000_x23(flag58=flag58, flag59=flag59, flag60=flag60, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag61=flag61, flag62=flag62, flag63=flag63,
                              flag64=flag64, flag65=flag65, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t160201000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t160201000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag61=6000, flag62=6001, flag63=6000,
                  flag64=6000, flag65=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t160201000_x10(actionbutton1=actionbutton1, flag61=flag61, flag62=flag62, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t160201000_x14(val1=val1, z3=z3)
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
        elif GetEventFlag(flag65):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag63) and not GetEventFlag(flag64) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t160201000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t160201000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t160201000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t160201000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t160201000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t160201000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t160201000_x9(flag58=6000, val2=10, val3=12):
    """State 0,8"""
    assert t160201000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag58):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t160201000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t160201000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t160201000_x10(actionbutton1=6000, flag61=6000, flag62=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t160201000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t160201000_x0(actionbutton1=actionbutton1, flag62=flag62, flag66=6000, flag67=6000, flag68=6000,
                flag69=6000, flag61=flag61))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160201000_x11(machine1=_, val6=_):
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

def t160201000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t160201000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t160201000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t160201000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t160201000_x13():
    """State 0,1"""
    assert t160201000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t160201000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t160201000_x24()
    """State 3"""
    call = t160201000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t160201000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t160201000_x15():
    """State 0,1"""
    assert t160201000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t160201000_x16(val5=12):
    """State 0,2"""
    call = t160201000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t160201000_x27()
    """State 4"""
    return 0

def t160201000_x17():
    """State 0,1"""
    assert t160201000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t160201000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t160201000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t160201000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t160201000_x29()
    """Unused"""
    """State 6"""
    return 0

def t160201000_x19():
    """State 0,2"""
    call = t160201000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t160201000_x20():
    """State 0,1"""
    assert t160201000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t160201000_x21():
    """State 0,1"""
    assert t160201000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t160201000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t160201000_x23(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t160201000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag61=flag61, flag62=flag62, flag63=flag63, flag64=flag64, flag65=flag65, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag58):
            """State 3"""
            Label('L0')
            call = t160201000_x9(flag58=flag58, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag58):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag59) or GetEventFlag(flag60):
            """State 2"""
            call = t160201000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag58):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag59) and not GetEventFlag(flag60):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t160201000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t160201000_x24():
    """State 0,1"""
    assert t160201000_x25()
    """State 2"""
    return 0

def t160201000_x25():
    """State 0,1"""
    assert t160201000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t160201000_x26():
    """State 0,1"""
    call = t160201000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t160201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160201000_x27():
    """State 0,1"""
    call = t160201000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t160201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160201000_x28():
    """State 0,1"""
    call = t160201000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t160201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160201000_x29():
    """State 0,1"""
    call = t160201000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t160201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160201000_x30(text1=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t160201000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t160201000_x31(text31=10701900, mode4=1):
    """State 0,4"""
    assert t160201000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10701900:"I am always ready to fight."
    TalkToPlayer(text31, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t160201000_x32():
    """State 0,1"""
    assert t160201000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t160201000_x33():
    """State 0,1"""
    assert t160201000_x1()
    """State 2"""
    return 0

def t160201000_x34():
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

def t160201000_x35(z1=601, z2=_):
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

def t160201000_x36(text28=10702100, flag55=-1, text29=10702200, flag56=-1, text30=10702300, flag57=-1):
    """State 0,5"""
    assert t160201000_x3(z7=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160201000_x30(text1=text28, flag1=flag55, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160201000_x30(text1=text29, flag1=flag56, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160201000_x30(text1=text30, flag1=flag57, mode5=1)
    """State 6"""
    return 0

def t160201000_x37(text28=10702100, flag52=1209056, text29=10702200, flag53=1209057, text30=10702300, flag54=1209058):
    """State 0"""
    if not GetEventFlag(flag52):
        """State 1"""
        assert t160201000_x30(text1=text28, flag1=flag52, mode5=1)
    elif not GetEventFlag(flag53):
        """State 2"""
        assert t160201000_x30(text1=text29, flag1=flag53, mode5=1)
    elif not GetEventFlag(flag54):
        """State 3"""
        assert t160201000_x30(text1=text30, flag1=flag54, mode5=1)
    else:
        """State 4"""
        assert t160201000_x36(text28=text28, flag55=-1, text29=text29, flag56=-1, text30=text30, flag57=-1)
    """State 5"""
    return 0

def t160201000_x38(text25=10701500, flag49=1209053, text26=10701600, flag50=1209054, text27=10701700, flag51=1209055):
    """State 0"""
    if not GetEventFlag(flag49):
        """State 2"""
        Label('L0')
        assert t160201000_x30(text1=text25, flag1=flag49, mode5=1)
    elif not GetEventFlag(flag50):
        """State 3"""
        assert t160201000_x30(text1=text26, flag1=flag50, mode5=1)
    elif not GetEventFlag(flag51):
        """State 4"""
        assert t160201000_x30(text1=text27, flag1=flag51, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag49, FlagState.Off)
        SetEventFlag(flag50, FlagState.Off)
        SetEventFlag(flag51, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t160201000_x39(text21=10702100, flag41=1209056, text22=10702200, flag42=1209057, text23=10702300, flag43=1209058,
                   text24=10702400, flag44=1209059):
    """State 0"""
    if not GetEventFlag(flag41):
        """State 1"""
        assert t160201000_x30(text1=text21, flag1=flag41, mode5=1)
    elif not GetEventFlag(flag42):
        """State 2"""
        assert t160201000_x30(text1=text22, flag1=flag42, mode5=1)
    elif not GetEventFlag(flag43):
        """State 3"""
        assert t160201000_x30(text1=text23, flag1=flag43, mode5=1)
    elif not GetEventFlag(flag44):
        """State 4"""
        assert t160201000_x30(text1=text24, flag1=flag44, mode5=1)
    else:
        """State 5"""
        assert (t160201000_x41(text21=text21, flag45=-1, text22=text22, flag46=-1, text23=text23, flag47=-1, text24=text24,
                flag48=-1))
    """State 6"""
    return 0

def t160201000_x40(text16=10702100, flag31=1209056, text17=10702200, flag32=1209057, text18=10702300, flag33=1209058,
                   text19=10702400, flag34=1209059, text20=10702600, flag35=1209061):
    """State 0"""
    if not GetEventFlag(flag31):
        """State 1"""
        assert t160201000_x30(text1=text16, flag1=flag31, mode5=1)
    elif not GetEventFlag(flag32):
        """State 2"""
        assert t160201000_x30(text1=text17, flag1=flag32, mode5=1)
    elif not GetEventFlag(flag33):
        """State 3"""
        assert t160201000_x30(text1=text18, flag1=flag33, mode5=1)
    elif not GetEventFlag(flag34):
        """State 4"""
        assert t160201000_x30(text1=text19, flag1=flag34, mode5=1)
    elif not GetEventFlag(flag35):
        """State 5"""
        assert t160201000_x30(text1=text20, flag1=flag35, mode5=1)
    else:
        """State 6"""
        assert (t160201000_x42(text16=text16, flag36=-1, text17=text17, flag37=-1, text18=text18, flag38=-1, text19=text19,
                flag39=-1, text20=text20, flag40=-1))
    """State 7"""
    return 0

def t160201000_x41(text21=10702100, flag45=-1, text22=10702200, flag46=-1, text23=10702300, flag47=-1, text24=10702400,
                   flag48=-1):
    """State 0,5"""
    assert t160201000_x3(z7=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160201000_x30(text1=text21, flag1=flag45, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160201000_x30(text1=text22, flag1=flag46, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160201000_x30(text1=text23, flag1=flag47, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160201000_x30(text1=text24, flag1=flag48, mode5=1)
    """State 7"""
    return 0

def t160201000_x42(text16=10702100, flag36=-1, text17=10702200, flag37=-1, text18=10702300, flag38=-1, text19=10702400,
                   flag39=-1, text20=10702600, flag40=-1):
    """State 0,5"""
    assert t160201000_x3(z7=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160201000_x30(text1=text16, flag1=flag36, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160201000_x30(text1=text17, flag1=flag37, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160201000_x30(text1=text18, flag1=flag38, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160201000_x30(text1=text19, flag1=flag39, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t160201000_x30(text1=text20, flag1=flag40, mode5=1)
    """State 8"""
    return 0

def t160201000_x43(text9=10702100, flag24=-1, text10=10702200, flag25=-1, text11=10702300, flag26=-1, text12=10702400,
                   flag27=-1, text13=10702700, flag28=-1, text14=10702800, flag29=-1, text15=10702900, flag30=-1):
    """State 0,5"""
    assert t160201000_x3(z7=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160201000_x30(text1=text9, flag1=flag24, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160201000_x30(text1=text10, flag1=flag25, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160201000_x30(text1=text11, flag1=flag26, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160201000_x30(text1=text12, flag1=flag27, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t160201000_x30(text1=text13, flag1=flag28, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t160201000_x30(text1=text14, flag1=flag29, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t160201000_x30(text1=text15, flag1=flag30, mode5=1)
    """State 10"""
    return 0

def t160201000_x44(text1=10702100, flag16=-1, text2=10702200, flag17=-1, text3=10702300, flag18=-1, text4=10702400,
                   flag19=-1, text5=10702600, flag20=-1, text6=10702700, flag21=-1, text7=10702800, flag22=-1,
                   text8=10702900, flag23=-1):
    """State 0,5"""
    assert t160201000_x3(z7=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160201000_x30(text1=text1, flag1=flag16, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160201000_x30(text1=text2, flag1=flag17, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160201000_x30(text1=text3, flag1=flag18, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160201000_x30(text1=text4, flag1=flag19, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t160201000_x30(text1=text5, flag1=flag20, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t160201000_x30(text1=text6, flag1=flag21, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t160201000_x30(text1=text7, flag1=flag22, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t160201000_x30(text1=text8, flag1=flag23, mode5=1)
    """State 11"""
    return 0

def t160201000_x45(text9=10702100, flag9=1209056, text10=10702200, flag10=1209057, text11=10702300, flag11=1209058,
                   text12=10702400, flag12=1209059, text13=10702700, flag13=1209062, text14=10702800, flag14=1209063,
                   text15=10702900, flag15=1209064):
    """State 0"""
    if not GetEventFlag(flag9):
        """State 1"""
        assert t160201000_x30(text1=text9, flag1=flag9, mode5=1)
    elif not GetEventFlag(flag10):
        """State 2"""
        assert t160201000_x30(text1=text10, flag1=flag10, mode5=1)
    elif not GetEventFlag(flag11):
        """State 3"""
        assert t160201000_x30(text1=text11, flag1=flag11, mode5=1)
    elif not GetEventFlag(flag12):
        """State 4"""
        assert t160201000_x30(text1=text12, flag1=flag12, mode5=1)
    elif not GetEventFlag(flag13):
        """State 5"""
        assert t160201000_x30(text1=text13, flag1=flag13, mode5=1)
    elif not GetEventFlag(flag14):
        """State 6"""
        assert t160201000_x30(text1=text14, flag1=flag14, mode5=1)
    elif not GetEventFlag(flag15):
        """State 7"""
        assert t160201000_x30(text1=text15, flag1=flag15, mode5=1)
    else:
        """State 8"""
        assert (t160201000_x43(text9=text9, flag24=-1, text10=text10, flag25=-1, text11=text11, flag26=-1, text12=text12,
                flag27=-1, text13=text13, flag28=-1, text14=text14, flag29=-1, text15=text15, flag30=-1))
    """State 9"""
    return 0

def t160201000_x46(text1=10702100, flag1=1209056, text2=10702200, flag2=1209057, text3=10702300, flag3=1209058,
                   text4=10702400, flag4=1209059, text5=10702600, flag5=1209061, text6=10702700, flag6=1209062,
                   text7=10702800, flag7=1209063, text8=10702900, flag8=1209064):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t160201000_x30(text1=text1, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t160201000_x30(text1=text2, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t160201000_x30(text1=text3, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t160201000_x30(text1=text4, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t160201000_x30(text1=text5, flag1=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t160201000_x30(text1=text6, flag1=flag6, mode5=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t160201000_x30(text1=text7, flag1=flag7, mode5=1)
    elif not GetEventFlag(flag8):
        """State 8"""
        assert t160201000_x30(text1=text8, flag1=flag8, mode5=1)
    else:
        """State 9"""
        assert (t160201000_x44(text1=text1, flag16=-1, text2=text2, flag17=-1, text3=text3, flag18=-1, text4=text4,
                flag19=-1, text5=text5, flag20=-1, text6=text6, flag21=-1, text7=text7, flag22=-1, text8=text8,
                flag23=-1))
    """State 10"""
    return 0

def t160201000_x47():
    """State 0"""
    if DoesSelfHaveSpEffect(9665):
        """State 1,4"""
        # talk:10701800:"Anything troubling you? I can help."
        assert t160201000_x30(text1=10701800, flag1=1209050, mode5=1)
    elif DoesSelfHaveSpEffect(9666):
        """State 2,5"""
        # talk:10702000:"I will see that our deed is done."
        assert t160201000_x30(text1=10702000, flag1=1209052, mode5=1)
    else:
        """State 3,6"""
        # talk:10701900:"I am always ready to fight."
        assert t160201000_x30(text1=10701900, flag1=1209051, mode5=1)
    """State 7"""
    return 0

def t160201000_x48():
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

def t160201000_x49():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t160201000_x50():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,7"""
        assert t160201000_x52()
    elif GetTalkListEntryResult() == 99:
        """State 2,6"""
        Label('L0')
        # talk:10701500:"I am here to serve."
        # talk:10701600:"Mm. Be safe."
        # talk:10701700:"Rest up while you can."
        assert (t160201000_x38(text25=10701500, flag49=1209053, text26=10701600, flag50=1209054, text27=10701700,
                flag51=1209055))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t160201000_x51():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t160201000_x53()
    else:
        """State 2"""
        assert t160201000_x47()
        """State 4"""
        assert t160201000_x48()
        """State 5"""
        assert t160201000_x49()
        """State 3"""
        assert t160201000_x50()
    """State 7"""
    return 0

def t160201000_x52():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        assert t160201000_x55()
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        assert t160201000_x54()
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        assert (t160201000_x37(text28=10702100, flag52=1209056, text29=10702200, flag53=1209057, text30=10702300,
                flag54=1209058))
    """State 7"""
    return 0

def t160201000_x53():
    """State 0,1"""
    # talk:10701900:"I am always ready to fight."
    assert t160201000_x31(text31=10701900, mode4=1)
    """State 2"""
    return 0

def t160201000_x54():
    """State 0,1"""
    if GetChrHero() == Hero.Recluse:
        """State 2,5"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        # talk:10702400:"Our foes have proven relentless. We must be the same."
        assert (t160201000_x39(text21=10702100, flag41=1209056, text22=10702200, flag42=1209057, text23=10702300,
                flag43=1209058, text24=10702400, flag44=1209059))
    else:
        """State 3,4"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        # talk:10702400:"Our foes have proven relentless. We must be the same."
        # talk:10702600:"The Recluse has taught me much. Only true selflessness can preserve the flock."
        assert (t160201000_x40(text16=10702100, flag31=1209056, text17=10702200, flag32=1209057, text18=10702300,
                flag33=1209058, text19=10702400, flag34=1209059, text20=10702600, flag35=1209061))
    """State 6"""
    return 0

def t160201000_x55():
    """State 0,1"""
    if GetChrHero() == Hero.Recluse:
        """State 2,5"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        # talk:10702400:"Our foes have proven relentless. We must be the same."
        # talk:10702700:"Now we strike at the head of the serpent. Should we prevail, victory will finally be ours."
        # talk:10702701:"Can't be too hard, can it?"
        # talk:10702800:"I can tell how this battle will develop."
        # talk:10702801:"We must charge ahead. Before the winds change."
        # talk:10702900:"Our offspring shall learn of this battle."
        # talk:10702901:"The tale must be told, and I am the one to tell it."
        assert (t160201000_x45(text9=10702100, flag9=1209056, text10=10702200, flag10=1209057, text11=10702300,
                flag11=1209058, text12=10702400, flag12=1209059, text13=10702700, flag13=1209062, text14=10702800,
                flag14=1209063, text15=10702900, flag15=1209064))
    else:
        """State 3,4"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        # talk:10702400:"Our foes have proven relentless. We must be the same."
        # talk:10702600:"The Recluse has taught me much. Only true selflessness can preserve the flock."
        # talk:10702700:"Now we strike at the head of the serpent. Should we prevail, victory will finally be ours."
        # talk:10702701:"Can't be too hard, can it?"
        # talk:10702800:"I can tell how this battle will develop."
        # talk:10702801:"We must charge ahead. Before the winds change."
        # talk:10702900:"Our offspring shall learn of this battle."
        # talk:10702901:"The tale must be told, and I am the one to tell it."
        assert (t160201000_x46(text1=10702100, flag1=1209056, text2=10702200, flag2=1209057, text3=10702300, flag3=1209058,
                text4=10702400, flag4=1209059, text5=10702600, flag5=1209061, text6=10702700, flag6=1209062, text7=10702800,
                flag7=1209063, text8=10702900, flag8=1209064))
    """State 6"""
    return 0

def t160201000_x56():
    """State 0,1"""
    assert t160201000_x57()
    """State 2"""
    return 0

def t160201000_x57():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t160201000_x58()
        if call.Get() == 1:
            """State 4"""
            call = t160201000_x59()
            if call.Get() == 1:
                """State 2,5"""
                Label('L0')
                assert t160201000_x51()
            elif call.Done():
                pass
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L0')
    """State 6"""
    return 0

def t160201000_x58():
    """State 0"""
    if GetEventFlag(3600):
        """State 1,6"""
        Label('L0')
    elif GetEventFlag(3601):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3602):
        """State 3,7"""
        # talk:10700800:"How are you feeling?"
        # talk:10700801:"There are some who are wary of your companionship..."
        # talk:10700802:"But your intent was not much different from our own. I have no mind to doubt you."
        # talk:10700803:"And am honoured to fight on the same side."
        # talk:10700804:"That said, you'd do well to show you are trustworthy."
        # talk:10700805:"I could give you a job to prove yourself."
        # talk:10700806:"I may be old-fashioned, but actions speak louder than words. What do you say?"
        assert t160201000_x30(text1=10700800, flag1=1169010, mode5=1)
        """State 10"""
        Label('L1')
        return 0
    elif GetEventFlag(3603):
        """State 4,8"""
        assert t160201000_x60()
        Goto('L1')
    elif GetEventFlag(3604):
        """State 5,9"""
        # talk:10701300:"Bring me a weapon wielded by a horde leader."
        # talk:10701301:"I leave it in your hands."
        assert t160201000_x30(text1=10701300, flag1=1169013, mode5=1)
        Goto('L1')
    else:
        pass
    """State 11"""
    return 1

def t160201000_x59():
    """State 0"""
    if GetEventFlag(3605):
        """State 1,5"""
        # talk:10701100:"Oh, there you are."
        # talk:10701101:"You found me just what I needed. I am in your debt."
        # talk:10701102:"You've earned a name for yourself, and proven that you belong here with us."
        # talk:10701103:"I will tell the others of your good deed."
        # talk:10701104:"You seem intent on keeping them at arms length,"
        # talk:10701105:"but that matters little. As long as we can work together."
        assert t160201000_x30(text1=10701100, flag1=1169014, mode5=1)
        """State 4,7"""
        assert t160201000_x35(z1=601, z2=3)
    elif GetEventFlag(3606):
        """State 2,6"""
        Label('L0')
        # talk:10701400:"You're one of us now. You've earned your place here."
        assert t160201000_x30(text1=10701400, flag1=1169015, mode5=1)
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0
    """Unused"""
    """State 3"""
    Goto('L0')

def t160201000_x60():
    """State 0,3"""
    # talk:10700900:"Will you hear my request?"
    assert t160201000_x30(text1=10700900, flag1=1169011, mode5=1)
    """State 4"""
    assert t160201000_x48()
    """State 1"""
    # action:21070003:"Speak of your request"
    AddTalkListDataAlt(1, 21070003, -1, 0, False)
    """State 5"""
    call = t160201000_x49()
    if call.Done() and GetTalkListEntryResult() == 1:
        """State 2,7"""
        # talk:10701000:"Without delay."
        # talk:10701001:"I want you to retrieve a weapon wielded by the forces of Night."
        # talk:10701002:"Their fierceness is compounded by the strength of their arms."
        # talk:10701003:"But with a proper understanding of their tools, I can fend them off with my shield."
        # talk:10701004:"It needn't be a perfect specimen. Even a fragment of a blade will do."
        # talk:10701005:"I leave it in your hands."
        assert t160201000_x30(text1=10701000, flag1=1169012, mode5=1)
        """State 8"""
        assert t160201000_x35(z1=601, z2=1)
    elif call.Done():
        """State 6"""
        assert t160201000_x50()
    """State 9"""
    return 0

