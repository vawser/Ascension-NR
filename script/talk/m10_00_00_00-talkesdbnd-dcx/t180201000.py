# -*- coding: utf-8 -*-
def t180201000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t180201000_x6(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t180201000_1000():
    """State 0,2,3"""
    assert t180201000_x56()
    """State 1"""
    EndMachine(1000)
    Quit()

def t180201000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t180201000_x0(actionbutton1=6000, flag62=6001, flag66=6000, flag67=6000, flag68=6000, flag69=6000,
            flag61=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t180201000_x0(actionbutton1=6000, flag62=6001, flag66=6000, flag67=6000, flag68=6000, flag69=6000, flag61=6000):
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

def t180201000_x1():
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

def t180201000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t180201000_x3(z5=_):
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

def t180201000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t180201000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t180201000_x1()
    else:
        """State 4,7"""
        call = t180201000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t180201000_x1()
    """State 9"""
    return 0

def t180201000_x5():
    """State 0,1"""
    assert t180201000_x1()
    """State 2"""
    return 0

def t180201000_x6(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t180201000_x23(flag58=flag58, flag59=flag59, flag60=flag60, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag61=flag61, flag62=flag62, flag63=flag63,
                              flag64=flag64, flag65=flag65, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t180201000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t180201000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag61=6000, flag62=6001, flag63=6000,
                  flag64=6000, flag65=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t180201000_x10(actionbutton1=actionbutton1, flag61=flag61, flag62=flag62, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t180201000_x14(val1=val1, z1=z1)
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
            call = t180201000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t180201000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t180201000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t180201000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t180201000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t180201000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t180201000_x9(flag58=6000, val2=10, val3=12):
    """State 0,8"""
    assert t180201000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag58):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t180201000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t180201000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t180201000_x10(actionbutton1=6000, flag61=6000, flag62=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t180201000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t180201000_x0(actionbutton1=actionbutton1, flag62=flag62, flag66=6000, flag67=6000, flag68=6000,
                flag69=6000, flag61=flag61))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180201000_x11(machine1=_, val6=_):
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

def t180201000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t180201000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t180201000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t180201000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t180201000_x13():
    """State 0,1"""
    assert t180201000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t180201000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t180201000_x24()
    """State 3"""
    call = t180201000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t180201000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t180201000_x15():
    """State 0,1"""
    assert t180201000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t180201000_x16(val5=12):
    """State 0,2"""
    call = t180201000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t180201000_x27()
    """State 4"""
    return 0

def t180201000_x17():
    """State 0,1"""
    assert t180201000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t180201000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t180201000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t180201000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t180201000_x29()
    """Unused"""
    """State 6"""
    return 0

def t180201000_x19():
    """State 0,2"""
    call = t180201000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t180201000_x20():
    """State 0,1"""
    assert t180201000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t180201000_x21():
    """State 0,1"""
    assert t180201000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t180201000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t180201000_x23(flag58=6000, flag59=6000, flag60=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag61=6000, flag62=6001, flag63=6000, flag64=6000, flag65=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t180201000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag61=flag61, flag62=flag62, flag63=flag63, flag64=flag64, flag65=flag65, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag58):
            """State 3"""
            Label('L0')
            call = t180201000_x9(flag58=flag58, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag58):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag59) or GetEventFlag(flag60):
            """State 2"""
            call = t180201000_x8(val2=val2, val3=val3)
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
        assert t180201000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t180201000_x24():
    """State 0,1"""
    assert t180201000_x25()
    """State 2"""
    return 0

def t180201000_x25():
    """State 0,1"""
    assert t180201000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t180201000_x26():
    """State 0,1"""
    call = t180201000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t180201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180201000_x27():
    """State 0,1"""
    call = t180201000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t180201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180201000_x28():
    """State 0,1"""
    call = t180201000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t180201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180201000_x29():
    """State 0,1"""
    call = t180201000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t180201000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180201000_x30(text2=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t180201000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text2, -1, -1, False)
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

def t180201000_x31(text32=10701900, mode4=1):
    """State 0,4"""
    assert t180201000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10701900:"I am always ready to fight."
    TalkToPlayer(text32, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t180201000_x32():
    """State 0,1"""
    assert t180201000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t180201000_x33():
    """State 0,1"""
    assert t180201000_x1()
    """State 2"""
    return 0

def t180201000_x34():
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

def t180201000_x35(text29=10702100, flag55=-1, text30=10702200, flag56=-1, text31=10702300, flag57=-1):
    """State 0,5"""
    assert t180201000_x3(z5=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180201000_x30(text2=text29, flag1=flag55, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180201000_x30(text2=text30, flag1=flag56, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180201000_x30(text2=text31, flag1=flag57, mode5=1)
    """State 6"""
    return 0

def t180201000_x36(text29=10702100, flag52=1209056, text30=10702200, flag53=1209057, text31=10702300, flag54=1209058):
    """State 0"""
    if not GetEventFlag(flag52):
        """State 1"""
        assert t180201000_x30(text2=text29, flag1=flag52, mode5=1)
    elif not GetEventFlag(flag53):
        """State 2"""
        assert t180201000_x30(text2=text30, flag1=flag53, mode5=1)
    elif not GetEventFlag(flag54):
        """State 3"""
        assert t180201000_x30(text2=text31, flag1=flag54, mode5=1)
    else:
        """State 4"""
        assert t180201000_x35(text29=text29, flag55=-1, text30=text30, flag56=-1, text31=text31, flag57=-1)
    """State 5"""
    return 0

def t180201000_x37(text26=10701500, flag49=1209053, text27=10701600, flag50=1209054, text28=10701700, flag51=1209055):
    """State 0"""
    if not GetEventFlag(flag49):
        """State 2"""
        Label('L0')
        assert t180201000_x30(text2=text26, flag1=flag49, mode5=1)
    elif not GetEventFlag(flag50):
        """State 3"""
        assert t180201000_x30(text2=text27, flag1=flag50, mode5=1)
    elif not GetEventFlag(flag51):
        """State 4"""
        assert t180201000_x30(text2=text28, flag1=flag51, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag49, FlagState.Off)
        SetEventFlag(flag50, FlagState.Off)
        SetEventFlag(flag51, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t180201000_x38(text22=10702100, flag41=1209056, text23=10702200, flag42=1209057, text24=10702300, flag43=1209058,
                   text25=10702400, flag44=1209059):
    """State 0"""
    if not GetEventFlag(flag41):
        """State 1"""
        assert t180201000_x30(text2=text22, flag1=flag41, mode5=1)
    elif not GetEventFlag(flag42):
        """State 2"""
        assert t180201000_x30(text2=text23, flag1=flag42, mode5=1)
    elif not GetEventFlag(flag43):
        """State 3"""
        assert t180201000_x30(text2=text24, flag1=flag43, mode5=1)
    elif not GetEventFlag(flag44):
        """State 4"""
        assert t180201000_x30(text2=text25, flag1=flag44, mode5=1)
    else:
        """State 5"""
        assert (t180201000_x40(text22=text22, flag45=-1, text23=text23, flag46=-1, text24=text24, flag47=-1, text25=text25,
                flag48=-1))
    """State 6"""
    return 0

def t180201000_x39(text17=10702100, flag31=1209056, text18=10702200, flag32=1209057, text19=10702300, flag33=1209058,
                   text20=10702400, flag34=1209059, text21=10702600, flag35=1209061):
    """State 0"""
    if not GetEventFlag(flag31):
        """State 1"""
        assert t180201000_x30(text2=text17, flag1=flag31, mode5=1)
    elif not GetEventFlag(flag32):
        """State 2"""
        assert t180201000_x30(text2=text18, flag1=flag32, mode5=1)
    elif not GetEventFlag(flag33):
        """State 3"""
        assert t180201000_x30(text2=text19, flag1=flag33, mode5=1)
    elif not GetEventFlag(flag34):
        """State 4"""
        assert t180201000_x30(text2=text20, flag1=flag34, mode5=1)
    elif not GetEventFlag(flag35):
        """State 5"""
        assert t180201000_x30(text2=text21, flag1=flag35, mode5=1)
    else:
        """State 6"""
        assert (t180201000_x41(text17=text17, flag36=-1, text18=text18, flag37=-1, text19=text19, flag38=-1, text20=text20,
                flag39=-1, text21=text21, flag40=-1))
    """State 7"""
    return 0

def t180201000_x40(text22=10702100, flag45=-1, text23=10702200, flag46=-1, text24=10702300, flag47=-1, text25=10702400,
                   flag48=-1):
    """State 0,5"""
    assert t180201000_x3(z5=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180201000_x30(text2=text22, flag1=flag45, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180201000_x30(text2=text23, flag1=flag46, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180201000_x30(text2=text24, flag1=flag47, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180201000_x30(text2=text25, flag1=flag48, mode5=1)
    """State 7"""
    return 0

def t180201000_x41(text17=10702100, flag36=-1, text18=10702200, flag37=-1, text19=10702300, flag38=-1, text20=10702400,
                   flag39=-1, text21=10702600, flag40=-1):
    """State 0,5"""
    assert t180201000_x3(z5=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180201000_x30(text2=text17, flag1=flag36, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180201000_x30(text2=text18, flag1=flag37, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180201000_x30(text2=text19, flag1=flag38, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180201000_x30(text2=text20, flag1=flag39, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t180201000_x30(text2=text21, flag1=flag40, mode5=1)
    """State 8"""
    return 0

def t180201000_x42(text10=10702100, flag24=-1, text11=10702200, flag25=-1, text12=10702300, flag26=-1, text13=10702400,
                   flag27=-1, text14=10702700, flag28=-1, text15=10702800, flag29=-1, text16=10702900, flag30=-1):
    """State 0,5"""
    assert t180201000_x3(z5=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180201000_x30(text2=text10, flag1=flag24, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180201000_x30(text2=text11, flag1=flag25, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180201000_x30(text2=text12, flag1=flag26, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180201000_x30(text2=text13, flag1=flag27, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t180201000_x30(text2=text14, flag1=flag28, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t180201000_x30(text2=text15, flag1=flag29, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t180201000_x30(text2=text16, flag1=flag30, mode5=1)
    """State 10"""
    return 0

def t180201000_x43(text2=10702100, flag16=-1, text3=10702200, flag17=-1, text4=10702300, flag18=-1, text5=10702400,
                   flag19=-1, text6=10702600, flag20=-1, text7=10702700, flag21=-1, text8=10702800, flag22=-1,
                   text9=10702900, flag23=-1):
    """State 0,5"""
    assert t180201000_x3(z5=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180201000_x30(text2=text2, flag1=flag16, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180201000_x30(text2=text3, flag1=flag17, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180201000_x30(text2=text4, flag1=flag18, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180201000_x30(text2=text5, flag1=flag19, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t180201000_x30(text2=text6, flag1=flag20, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t180201000_x30(text2=text7, flag1=flag21, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t180201000_x30(text2=text8, flag1=flag22, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t180201000_x30(text2=text9, flag1=flag23, mode5=1)
    """State 11"""
    return 0

def t180201000_x44(text10=10702100, flag9=1209056, text11=10702200, flag10=1209057, text12=10702300, flag11=1209058,
                   text13=10702400, flag12=1209059, text14=10702700, flag13=1209062, text15=10702800, flag14=1209063,
                   text16=10702900, flag15=1209064):
    """State 0"""
    if not GetEventFlag(flag9):
        """State 1"""
        assert t180201000_x30(text2=text10, flag1=flag9, mode5=1)
    elif not GetEventFlag(flag10):
        """State 2"""
        assert t180201000_x30(text2=text11, flag1=flag10, mode5=1)
    elif not GetEventFlag(flag11):
        """State 3"""
        assert t180201000_x30(text2=text12, flag1=flag11, mode5=1)
    elif not GetEventFlag(flag12):
        """State 4"""
        assert t180201000_x30(text2=text13, flag1=flag12, mode5=1)
    elif not GetEventFlag(flag13):
        """State 5"""
        assert t180201000_x30(text2=text14, flag1=flag13, mode5=1)
    elif not GetEventFlag(flag14):
        """State 6"""
        assert t180201000_x30(text2=text15, flag1=flag14, mode5=1)
    elif not GetEventFlag(flag15):
        """State 7"""
        assert t180201000_x30(text2=text16, flag1=flag15, mode5=1)
    else:
        """State 8"""
        assert (t180201000_x42(text10=text10, flag24=-1, text11=text11, flag25=-1, text12=text12, flag26=-1, text13=text13,
                flag27=-1, text14=text14, flag28=-1, text15=text15, flag29=-1, text16=text16, flag30=-1))
    """State 9"""
    return 0

def t180201000_x45(text2=10702100, flag1=1209056, text3=10702200, flag2=1209057, text4=10702300, flag3=1209058,
                   text5=10702400, flag4=1209059, text6=10702600, flag5=1209061, text7=10702700, flag6=1209062,
                   text8=10702800, flag7=1209063, text9=10702900, flag8=1209064):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t180201000_x30(text2=text2, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t180201000_x30(text2=text3, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t180201000_x30(text2=text4, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t180201000_x30(text2=text5, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t180201000_x30(text2=text6, flag1=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t180201000_x30(text2=text7, flag1=flag6, mode5=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t180201000_x30(text2=text8, flag1=flag7, mode5=1)
    elif not GetEventFlag(flag8):
        """State 8"""
        assert t180201000_x30(text2=text9, flag1=flag8, mode5=1)
    else:
        """State 9"""
        assert (t180201000_x43(text2=text2, flag16=-1, text3=text3, flag17=-1, text4=text4, flag18=-1, text5=text5,
                flag19=-1, text6=text6, flag20=-1, text7=text7, flag21=-1, text8=text8, flag22=-1, text9=text9,
                flag23=-1))
    """State 10"""
    return 0

def t180201000_x46(action1=21072001, action2=21072002, text1=10700400):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21072001:"Affirm"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:21072002:"Deny"
    AddTalkListDataAlt(2, action2, -1, 0, False)
    """State 3"""
    # talk:10700400:"May I ask you something?"
    # talk:10700401:"I heard that in the Lands Between there was once a thing of wonder known as the Erdtree."
    # talk:10700402:"The monolithic tree was said to be a symbol of the land's blessings."
    # talk:10700403:"Did you ever see it for yourself?"
    ShowShopMessageWithTalk(0, text1)
    """State 4"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    else:
        """State 7"""
        return 1

def t180201000_x47():
    """State 0"""
    if DoesSelfHaveSpEffect(9665):
        """State 1,4"""
        # talk:10701800:"Anything troubling you? I can help."
        assert t180201000_x30(text2=10701800, flag1=1209050, mode5=1)
    elif DoesSelfHaveSpEffect(9666):
        """State 2,5"""
        # talk:10702000:"I will see that our deed is done."
        assert t180201000_x30(text2=10702000, flag1=1209052, mode5=1)
    else:
        """State 3,6"""
        # talk:10701900:"I am always ready to fight."
        assert t180201000_x30(text2=10701900, flag1=1209051, mode5=1)
    """State 7"""
    return 0

def t180201000_x48():
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

def t180201000_x49():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t180201000_x50():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,7"""
        assert t180201000_x52()
    elif GetTalkListEntryResult() == 99:
        """State 2,6"""
        Label('L0')
        # talk:10701500:"I am here to serve."
        # talk:10701600:"Mm. Be safe."
        # talk:10701700:"Rest up while you can."
        assert (t180201000_x37(text26=10701500, flag49=1209053, text27=10701600, flag50=1209054, text28=10701700,
                flag51=1209055))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t180201000_x51():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t180201000_x53()
    else:
        """State 2"""
        assert t180201000_x47()
        """State 4"""
        assert t180201000_x48()
        """State 5"""
        assert t180201000_x49()
        """State 3"""
        assert t180201000_x50()
    """State 7"""
    return 0

def t180201000_x52():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        assert t180201000_x55()
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        assert t180201000_x54()
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10702100:"No matter how towering the beasts we face, stand your ground and raise your shield."
        # talk:10702101:"Be patient. Your window of opportunity will come."
        # talk:10702200:"I can't believe it. Facing off against the Night itself?"
        # talk:10702201:"If such is our fate, we must rise to the task."
        # talk:10702300:"I've trained with halberds before."
        # talk:10702301:"No expert by any means, but I can hold my own."
        assert (t180201000_x36(text29=10702100, flag52=1209056, text30=10702200, flag53=1209057, text31=10702300,
                flag54=1209058))
    """State 7"""
    return 0

def t180201000_x53():
    """State 0,1"""
    # talk:10701900:"I am always ready to fight."
    assert t180201000_x31(text32=10701900, mode4=1)
    """State 2"""
    return 0

def t180201000_x54():
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
        assert (t180201000_x38(text22=10702100, flag41=1209056, text23=10702200, flag42=1209057, text24=10702300,
                flag43=1209058, text25=10702400, flag44=1209059))
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
        assert (t180201000_x39(text17=10702100, flag31=1209056, text18=10702200, flag32=1209057, text19=10702300,
                flag33=1209058, text20=10702400, flag34=1209059, text21=10702600, flag35=1209061))
    """State 6"""
    return 0

def t180201000_x55():
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
        assert (t180201000_x44(text10=10702100, flag9=1209056, text11=10702200, flag10=1209057, text12=10702300,
                flag11=1209058, text13=10702400, flag12=1209059, text14=10702700, flag13=1209062, text15=10702800,
                flag14=1209063, text16=10702900, flag15=1209064))
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
        assert (t180201000_x45(text2=10702100, flag1=1209056, text3=10702200, flag2=1209057, text4=10702300, flag3=1209058,
                text5=10702400, flag4=1209059, text6=10702600, flag5=1209061, text7=10702700, flag6=1209062, text8=10702800,
                flag7=1209063, text9=10702900, flag8=1209064))
    """State 6"""
    return 0

def t180201000_x56():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t180201000_x57()
    """State 2"""
    return 0

def t180201000_x57():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t180201000_x58()
        if call.Get() == 1:
            """State 2,4"""
            Label('L0')
            assert t180201000_x51()
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L0')
    """State 5"""
    return 0

def t180201000_x58():
    """State 0"""
    if GetEventFlag(3800):
        """State 1,4"""
        assert t180201000_x59()
    elif GetEventFlag(3801):
        """State 2,5"""
        # talk:10701200:"The Priestess was looking for you. Perhaps she wants a word."
        assert t180201000_x30(text2=10701200, flag1=1189003, mode5=1)
    else:
        """State 3,7"""
        return 1
    """State 6"""
    return 0

def t180201000_x59():
    """State 0,2"""
    # talk:10700400:"May I ask you something?"
    # talk:10700401:"I heard that in the Lands Between there was once a thing of wonder known as the Erdtree."
    # talk:10700402:"The monolithic tree was said to be a symbol of the land's blessings."
    # talk:10700403:"Did you ever see it for yourself?"
    assert t180201000_x30(text2=10700400, flag1=1189000, mode5=1)
    """State 5"""
    # action:21072001:"Affirm"
    # action:21072002:"Deny"
    # talk:10700400:"May I ask you something?"
    # talk:10700401:"I heard that in the Lands Between there was once a thing of wonder known as the Erdtree."
    # talk:10700402:"The monolithic tree was said to be a symbol of the land's blessings."
    # talk:10700403:"Did you ever see it for yourself?"
    call = t180201000_x46(action1=21072001, action2=21072002, text1=10700400)
    if call.Get() == 0:
        """State 3"""
        # talk:10700500:"What a sight it must have been."
        # talk:10700501:"The vastness of nature is apt to stir something within."
        # talk:10700502:"No wonder you were so enamoured by it."
        # talk:10700503:"I must say, where we are headed there shall be no such tree."
        # talk:10700504:"But if we can repulse the Night, it may yet be restored."
        # talk:10700505:"Oh, I should mention..."
        # talk:10700506:"The Priestess was looking for you. Perhaps she wants a word."
        assert t180201000_x30(text2=10700500, flag1=1189001, mode5=1)
    elif call.Get() == 1:
        """State 4"""
        # talk:10700600:"Yes, I see."
        # talk:10700601:"And yet you revere it nonetheless."
        # talk:10700602:"If a marvel of nature can inspire such devotion, I should desire to gaze upon it, if only for a moment."
        # talk:10700603:"I must say, where we are headed there shall be no such tree."
        # talk:10700604:"But if we can repulse the Night, it may yet be restored."
        # talk:10700605:"Oh, I should mention..."
        # talk:10700606:"The Priestess was looking for you. Perhaps she wants a word."
        assert t180201000_x30(text2=10700600, flag1=1189002, mode5=1)
    """State 1"""
    SetEventFlag(1189004, FlagState.On)
    """State 6"""
    return 0

