# -*- coding: utf-8 -*-
def t140601000_1():
    """State 0"""
    while True:
        """State 6"""
        # eventflag:6000:Flag to always be OFF
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        call = t140601000_x6(flag36=6000, flag37=6000, flag38=6000, val1=5, val2=10, val3=12, val4=10, val5=12,
                             actionbutton1=6000, flag39=6000, flag40=6001, flag41=6001, flag42=6001, flag43=6000,
                             z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1)
        if GetEventFlag(10003204):
            """State 3,4"""
            # eventflag:6000:Flag to always be OFF
            # actionbutton:6000:"Talk"
            # eventflag:6001:Flag to always be ON
            call = t140601000_x6(flag36=6000, flag37=10003204, flag38=6000, val1=30, val2=45, val3=50, val4=45,
                                 val5=50, actionbutton1=6000, flag39=6000, flag40=6001, flag41=6000, flag42=6000,
                                 flag43=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1)
            if IsCharacterDisabled():
                pass
            elif GetEventFlag(10003205):
                """State 1,5"""
                def WhilePaused():
                    RequestAnimation(90300, -1)
                assert t140601000_x59()
                continue
        elif IsCharacterDisabled():
            pass
        """State 2"""
        assert not IsCharacterDisabled()

def t140601000_1000():
    """State 0,2,3"""
    assert t140601000_x53()
    """State 1"""
    EndMachine(1000)
    Quit()

def t140601000_1001():
    """State 0,2,3"""
    # talk:10800600:"What's wrong with you? You hesitate."
    assert t140601000_x32(text22=10800600, flag45=1149049, mode5=1)
    """State 1"""
    EndMachine(1001)
    Quit()

def t140601000_1102():
    """State 0,2"""
    assert GetEventFlag(10003209)
    """State 4"""
    if GetEventFlag(10003211):
        """State 5"""
        pass
    else:
        """State 7"""
        SetEventFlag(1149053, FlagState.On)
        """State 8"""
        # talk:10800300:"I'll kill you. Unless you fell me first."
        assert t140601000_x33(text21=10800300, flag44=1149044, mode4=1)
        """State 6"""
        SetEventFlag(10003211, FlagState.On)
    """State 3"""
    Quit()
    """Unused"""
    """State 1"""
    EndMachine(1102)
    Quit()

def t140601000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t140601000_x0(actionbutton1=6000, flag40=6001, flag46=6000, flag47=6000, flag48=6000, flag49=6000, flag39=6000)
    if call.Done():
        pass
    elif f302(-1) == 2:
        """State 3,5"""
        # actionbutton:6002:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (t140601000_x0(actionbutton1=6002, flag40=6001, flag46=6000, flag47=6000, flag48=6000, flag49=6000,
                flag39=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t140601000_x0(actionbutton1=_, flag40=6001, flag46=6000, flag47=6000, flag48=6000, flag49=6000, flag39=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag40) or GetEventFlag(flag46) or GetEventFlag(flag47) or GetEventFlag(flag48) or
                GetEventFlag(flag49))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag39)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag39) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag40) and not GetEventFlag(flag46) and not GetEventFlag(flag47) and not GetEventFlag(flag48)
            and not GetEventFlag(flag49)) or DoesPlayerHaveSpEffect(9640)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t140601000_x1():
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

def t140601000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t140601000_x3(z5=_):
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

def t140601000_x4(val2=_, val3=_):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t140601000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t140601000_x1()
    else:
        """State 4,7"""
        call = t140601000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t140601000_x1()
    """State 9"""
    return 0

def t140601000_x5():
    """State 0,1"""
    assert t140601000_x1()
    """State 2"""
    return 0

def t140601000_x6(flag36=6000, flag37=_, flag38=6000, val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000,
                  flag39=6000, flag40=6001, flag41=_, flag42=_, flag43=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t140601000_x23(flag36=flag36, flag37=flag37, flag38=flag38, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag39=flag39, flag40=flag40, flag41=flag41,
                              flag42=flag42, flag43=flag43, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t140601000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t140601000_x7(val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000, flag39=6000, flag40=6001, flag41=_,
                  flag42=_, flag43=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t140601000_x10(actionbutton1=actionbutton1, flag39=flag39, flag40=flag40, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t140601000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag43):
            Goto('L0')
        elif GetEventFlag(flag41) and not GetEventFlag(flag42) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t140601000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t140601000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t140601000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t140601000_x8(val2=_, val3=_):
    """State 0,1"""
    call = t140601000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t140601000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t140601000_x9(flag36=6000, val2=_, val3=_):
    """State 0,8"""
    assert t140601000_x37()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag36):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t140601000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t140601000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t140601000_x10(actionbutton1=6000, flag39=6000, flag40=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t140601000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t140601000_x0(actionbutton1=actionbutton1, flag40=flag40, flag46=6000, flag47=6000, flag48=6000,
                flag49=6000, flag39=flag39))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140601000_x11(machine1=_, val6=_):
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

def t140601000_x12(val2=_, val3=_):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t140601000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t140601000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t140601000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t140601000_x13():
    """State 0,1"""
    assert t140601000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t140601000_x14(val1=_, z1=1):
    """State 0,4"""
    assert t140601000_x24()
    """State 3"""
    call = t140601000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t140601000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t140601000_x15():
    """State 0,1"""
    assert t140601000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t140601000_x16(val5=_):
    """State 0,2"""
    call = t140601000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t140601000_x27()
    """State 4"""
    return 0

def t140601000_x17():
    """State 0,1"""
    assert t140601000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t140601000_x18(val2=_, val3=_):
    """State 0,5"""
    assert t140601000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t140601000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t140601000_x29()
    """Unused"""
    """State 6"""
    return 0

def t140601000_x19():
    """State 0,2"""
    call = t140601000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t140601000_x20():
    """State 0,1"""
    assert t140601000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t140601000_x21():
    """State 0,1"""
    assert t140601000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t140601000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t140601000_x23(flag36=6000, flag37=_, flag38=6000, val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000,
                   flag39=6000, flag40=6001, flag41=_, flag42=_, flag43=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                   mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t140601000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag39=flag39, flag40=flag40, flag41=flag41, flag42=flag42, flag43=flag43, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag36):
            """State 3"""
            Label('L0')
            call = t140601000_x9(flag36=flag36, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag36):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag37) or GetEventFlag(flag38):
            """State 2"""
            call = t140601000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag36):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag37) and not GetEventFlag(flag38):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t140601000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t140601000_x24():
    """State 0,1"""
    assert t140601000_x25()
    """State 2"""
    return 0

def t140601000_x25():
    """State 0,1"""
    assert t140601000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t140601000_x26():
    """State 0,1"""
    call = t140601000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t140601000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140601000_x27():
    """State 0,1"""
    call = t140601000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t140601000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140601000_x28():
    """State 0,1"""
    call = t140601000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t140601000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140601000_x29():
    """State 0,1"""
    call = t140601000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t140601000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140601000_x30(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t140601000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode7 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag1, FlagState.On)
    """State 6"""
    return 0

def t140601000_x31(text23=10800500, mode6=1):
    """State 0,4"""
    assert t140601000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10800500:"I yield."
    TalkToPlayer(text23, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode6 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t140601000_x32(text22=10800600, flag45=1149049, mode5=1):
    """State 0,5"""
    assert t140601000_x34() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag45, FlagState.On)
    """State 1"""
    # talk:10800600:"What's wrong with you? You hesitate."
    TalkToPlayer(text22, -1, -1, True)
    """State 4"""
    if mode5 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t140601000_x33(text21=10800300, flag44=1149044, mode4=1):
    """State 0,5"""
    assert t140601000_x34() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10800300:"I'll kill you. Unless you fell me first."
    TalkToPlayer(text21, -1, -1, True)
    """State 4"""
    if mode4 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag44, FlagState.On)
    """State 6"""
    return 0

def t140601000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t140601000_x35():
    """State 0,1"""
    assert t140601000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t140601000_x36():
    """State 0,1"""
    assert t140601000_x1()
    """State 2"""
    return 0

def t140601000_x37():
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

def t140601000_x38(action1=21082001, action2=21082002):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21082001:"Ready armament"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:21082002:"Leave"
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

def t140601000_x39(text19=10802800, flag34=-1, text20=10802900, flag35=-1):
    """State 0,4"""
    assert t140601000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140601000_x30(text1=text19, flag1=flag34, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140601000_x30(text1=text20, flag1=flag35, mode7=1)
    """State 5"""
    return 0

def t140601000_x40(text19=10802800, flag32=1209256, text20=10802900, flag33=1209257):
    """State 0"""
    if not GetEventFlag(flag32):
        """State 1"""
        assert t140601000_x30(text1=text19, flag1=flag32, mode7=1)
    elif not GetEventFlag(flag33):
        """State 2"""
        assert t140601000_x30(text1=text20, flag1=flag33, mode7=1)
    else:
        """State 3"""
        assert t140601000_x39(text19=text19, flag34=-1, text20=text20, flag35=-1)
    """State 4"""
    return 0

def t140601000_x41(text16=10802200, flag29=1209253, text17=10802300, flag30=1209254, text18=10802400, flag31=1209255):
    """State 0"""
    if not GetEventFlag(flag29):
        """State 2"""
        Label('L0')
        assert t140601000_x30(text1=text16, flag1=flag29, mode7=1)
    elif not GetEventFlag(flag30):
        """State 3"""
        assert t140601000_x30(text1=text17, flag1=flag30, mode7=1)
    elif not GetEventFlag(flag31):
        """State 4"""
        assert t140601000_x30(text1=text18, flag1=flag31, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag29, FlagState.Off)
        SetEventFlag(flag30, FlagState.Off)
        SetEventFlag(flag31, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t140601000_x42(text11=10802800, flag19=1209256, text12=10802900, flag20=1209257, text13=10803100, flag21=1209259,
                   text14=10803200, flag22=1209260, text15=10803300, flag23=1209261):
    """State 0"""
    if not GetEventFlag(flag19):
        """State 1"""
        assert t140601000_x30(text1=text11, flag1=flag19, mode7=1)
    elif not GetEventFlag(flag20):
        """State 2"""
        assert t140601000_x30(text1=text12, flag1=flag20, mode7=1)
    elif not GetEventFlag(flag21):
        """State 3"""
        assert t140601000_x30(text1=text13, flag1=flag21, mode7=1)
    elif not GetEventFlag(flag22):
        """State 4"""
        assert t140601000_x30(text1=text14, flag1=flag22, mode7=1)
    elif not GetEventFlag(flag23):
        """State 5"""
        assert t140601000_x30(text1=text15, flag1=flag23, mode7=1)
    else:
        """State 6"""
        assert (t140601000_x43(text11=text11, flag24=-1, text12=text12, flag25=-1, text13=text13, flag26=-1, text14=text14,
                flag27=-1, text15=text15, flag28=-1))
    """State 7"""
    return 0

def t140601000_x43(text11=10802800, flag24=-1, text12=10802900, flag25=-1, text13=10803100, flag26=-1, text14=10803200,
                   flag27=-1, text15=10803300, flag28=-1):
    """State 0,5"""
    assert t140601000_x3(z5=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140601000_x30(text1=text11, flag1=flag24, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140601000_x30(text1=text12, flag1=flag25, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t140601000_x30(text1=text13, flag1=flag26, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t140601000_x30(text1=text14, flag1=flag27, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t140601000_x30(text1=text15, flag1=flag28, mode7=1)
    """State 8"""
    return 0

def t140601000_x44(text3=10802800, flag11=-1, text4=10802900, flag12=-1, text5=10803100, flag13=-1, text6=10803200,
                   flag14=-1, text7=10803300, flag15=-1, text8=10803400, flag16=-1, text9=10803500, flag17=-1,
                   text10=10803600, flag18=-1):
    """State 0,5"""
    assert t140601000_x3(z5=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140601000_x30(text1=text3, flag1=flag11, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140601000_x30(text1=text4, flag1=flag12, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t140601000_x30(text1=text5, flag1=flag13, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t140601000_x30(text1=text6, flag1=flag14, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t140601000_x30(text1=text7, flag1=flag15, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t140601000_x30(text1=text8, flag1=flag16, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t140601000_x30(text1=text9, flag1=flag17, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t140601000_x30(text1=text10, flag1=flag18, mode7=1)
    """State 11"""
    return 0

def t140601000_x45(text3=10802800, flag3=1209256, text4=10802900, flag4=1209257, text5=10803100, flag5=1209259,
                   text6=10803200, flag6=1209260, text7=10803300, flag7=1209261, text8=10803400, flag8=1209262,
                   text9=10803500, flag9=1209263, text10=10803600, flag10=1209264):
    """State 0"""
    if not GetEventFlag(flag3):
        """State 1"""
        assert t140601000_x30(text1=text3, flag1=flag3, mode7=1)
    elif not GetEventFlag(flag4):
        """State 2"""
        assert t140601000_x30(text1=text4, flag1=flag4, mode7=1)
    elif not GetEventFlag(flag5):
        """State 3"""
        assert t140601000_x30(text1=text5, flag1=flag5, mode7=1)
    elif not GetEventFlag(flag6):
        """State 4"""
        assert t140601000_x30(text1=text6, flag1=flag6, mode7=1)
    elif not GetEventFlag(flag7):
        """State 5"""
        assert t140601000_x30(text1=text7, flag1=flag7, mode7=1)
    elif not GetEventFlag(flag8):
        """State 6"""
        assert t140601000_x30(text1=text8, flag1=flag8, mode7=1)
    elif not GetEventFlag(flag9):
        """State 7"""
        assert t140601000_x30(text1=text9, flag1=flag9, mode7=1)
    elif not GetEventFlag(flag10):
        """State 8"""
        assert t140601000_x30(text1=text10, flag1=flag10, mode7=1)
    else:
        """State 9"""
        assert (t140601000_x44(text3=text3, flag11=-1, text4=text4, flag12=-1, text5=text5, flag13=-1, text6=text6,
                flag14=-1, text7=text7, flag15=-1, text8=text8, flag16=-1, text9=text9, flag17=-1, text10=text10,
                flag18=-1))
    """State 10"""
    return 0

def t140601000_x46(text1=10802200, flag1=1209253, text2=10802300, flag2=1209254):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 2"""
        Label('L0')
        assert t140601000_x30(text1=text1, flag1=flag1, mode7=1)
    elif not GetEventFlag(flag2):
        """State 3"""
        assert t140601000_x30(text1=text2, flag1=flag2, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag1, FlagState.Off)
        SetEventFlag(flag2, FlagState.Off)
        Goto('L0')
    """State 4"""
    return 0

def t140601000_x47():
    """State 0"""
    if DoesSelfHaveSpEffect(9685):
        """State 1,5"""
        # talk:10802600:"No idle musings, thank you."
        assert t140601000_x30(text1=10802600, flag1=1209251, mode7=1)
    elif DoesSelfHaveSpEffect(9686):
        """State 2,6"""
        # talk:10802700:"If I let you talk, will you promise to remain on topic?"
        assert t140601000_x30(text1=10802700, flag1=1209252, mode7=1)
    elif DoesSelfHaveSpEffect(9687):
        """State 3,7"""
        Label('L0')
        # talk:10802500:"What is it now?"
        assert t140601000_x30(text1=10802500, flag1=1209250, mode7=1)
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t140601000_x48():
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

def t140601000_x49():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t140601000_x50():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,8"""
        assert t140601000_x52()
    elif GetTalkListEntryResult() == 99:
        """State 2,6"""
        Label('L0')
        if GetEventFlag(10002011) or GetEventFlag(10002012):
            """State 9"""
            # talk:10802200:"Hmph."
            # talk:10802300:"Have you even been listening?"
            assert t140601000_x46(text1=10802200, flag1=1209253, text2=10802300, flag2=1209254)
        else:
            """State 7"""
            # talk:10802200:"Hmph."
            # talk:10802300:"Have you even been listening?"
            # talk:10802400:"Had your fill?"
            assert (t140601000_x41(text16=10802200, flag29=1209253, text17=10802300, flag30=1209254, text18=10802400,
                    flag31=1209255))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 10"""
    return 0

def t140601000_x51():
    """State 0,1"""
    assert t140601000_x47()
    """State 3"""
    assert t140601000_x48()
    """State 4"""
    assert t140601000_x49()
    """State 2"""
    assert t140601000_x50()
    """State 5"""
    return 0

def t140601000_x52():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10802800:"This place reeks of failure."
        # talk:10802900:"I will have...my revenge."
        # talk:10803100:"See how they line up like sheep to the slaughter?"
        # talk:10803101:"Perhaps I'll grant their wish."
        # talk:10803200:"My resentment has festered far too long to be so easily assuaged."
        # talk:10803201:"You as well, if my instincts still serve me?"
        # talk:10803300:"I don't care to fraternize. But I know a useful ally when I see one."
        # talk:10803301:"If the need arises, let's run wild."
        # talk:10803400:"How long I've waited for this moment..."
        # talk:10803500:"What a darling bunch of fools you are. But I wouldn't have it any other way."
        # talk:10803600:"Oh, sweet retribution."
        assert (t140601000_x45(text3=10802800, flag3=1209256, text4=10802900, flag4=1209257, text5=10803100, flag5=1209259,
                text6=10803200, flag6=1209260, text7=10803300, flag7=1209261, text8=10803400, flag8=1209262, text9=10803500,
                flag9=1209263, text10=10803600, flag10=1209264))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10802800:"This place reeks of failure."
        # talk:10802900:"I will have...my revenge."
        # talk:10803100:"See how they line up like sheep to the slaughter?"
        # talk:10803101:"Perhaps I'll grant their wish."
        # talk:10803200:"My resentment has festered far too long to be so easily assuaged."
        # talk:10803201:"You as well, if my instincts still serve me?"
        # talk:10803300:"I don't care to fraternize. But I know a useful ally when I see one."
        # talk:10803301:"If the need arises, let's run wild."
        assert (t140601000_x42(text11=10802800, flag19=1209256, text12=10802900, flag20=1209257, text13=10803100,
                flag21=1209259, text14=10803200, flag22=1209260, text15=10803300, flag23=1209261))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10802800:"This place reeks of failure."
        # talk:10802900:"I will have...my revenge."
        assert t140601000_x40(text19=10802800, flag32=1209256, text20=10802900, flag33=1209257)
    """State 7"""
    return 0

def t140601000_x53():
    """State 0,1"""
    assert t140601000_x54()
    """State 2"""
    return 0

def t140601000_x54():
    """State 0"""
    if f302(-1) == 2:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t140601000_x55()
    elif f302(-1) == 4:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t140601000_x56()
    else:
        """State 1"""
        """State 2"""
        pass
    """State 5"""
    return 0

def t140601000_x55():
    """State 0"""
    if GetEventFlag(3404):
        """State 1,6"""
        Label('L0')
        assert t140601000_x51()
    elif GetEventFlag(3405):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3406):
        """State 3,7"""
        # talk:10801500:"There you are."
        # talk:10801501:"Forgive me, but I didn't want anyone to overhear."
        # talk:10801502:"The Wylder...won't remain among the living much longer..."
        # talk:10801503:"The vitality in him is all too little."
        # talk:10801504:"All that's left is the lees."
        # talk:10801505:"In this form, I am attuned to life's ebb and flow."
        # talk:10801506:"As the Roundtable's custodian, you must decide on the proper course of action."
        assert t140601000_x30(text1=10801500, flag1=1149040, mode7=1)
        """State 5"""
    else:
        """State 4,8"""
        # talk:10802000:"It is your choice. Whether to allow him to continue fighting."
        assert t140601000_x30(text1=10802000, flag1=1149041, mode7=1)
    """State 9"""
    return 0

def t140601000_x56():
    """State 0"""
    if GetEventFlag(3417):
        """State 1,9"""
        assert t140601000_x57()
    elif GetEventFlag(3418):
        """State 2"""
        if not GetEventFlag(1149044):
            """State 3,10"""
            assert t140601000_x58()
        elif GetEventFlag(1149044):
            """State 4,13"""
            assert t140601000_x60()
    elif GetEventFlag(3419):
        """State 5,12"""
        assert t140601000_x59()
    elif GetEventFlag(3420):
        """State 6,11"""
        Label('L0')
        # talk:10802100:"You really don't hold back, do you?"
        # talk:10802101:"I was only trying to give you a nudge, and you practically ground me into the dust..."
        # talk:10802102:"Well. Now I know where I stand, in your eyes."
        assert t140601000_x30(text1=10802100, flag1=1149048, mode7=1)
    elif GetEventFlag(3421):
        """State 8"""
        Goto('L0')
    else:
        """State 7"""
        pass
    """State 14"""
    return 0

def t140601000_x57():
    """State 0,5"""
    assert t140601000_x47()
    """State 6"""
    assert t140601000_x48()
    """State 2"""
    # action:21080003:"Maybe defeating the Nightlord isn't the right thing to do"
    AddTalkListDataAlt(1, 21080003, -1, 0, False)
    """State 7"""
    assert t140601000_x49()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 8"""
        # talk:10800100:"What's the matter with you?"
        # talk:10800101:"Are you mad? I will not hear another word."
        # talk:10800102:"..."
        # talk:10800103:"...We'll need more room."
        assert t140601000_x30(text1=10800100, flag1=1149042, mode7=1)
        """State 3"""
        SetEventFlag(10003203, FlagState.On)
        """State 4"""
        Quit()
    else:
        """State 9"""
        assert t140601000_x50()
        """State 10"""
        return 0

def t140601000_x58():
    """State 0"""
    if not GetEventFlag(1149045):
        """State 1,11"""
        # talk:10800200:"Shall we?"
        assert t140601000_x30(text1=10800200, flag1=1149043, mode7=1)
        """State 12"""
        # action:21082001:"Ready armament"
        # action:21082002:"Leave"
        call = t140601000_x38(action1=21082001, action2=21082002)
        if call.Get() == 0:
            """State 2,10"""
            c1_164()
            assert not f305()
            """State 4"""
            SetEventFlag(10003204, FlagState.On)
        elif call.Get() == 1:
            """State 3,14"""
            # talk:10800400:"Cold feet, I presume?"
            # talk:10800401:"I care not. I won't hear any feeble excuses."
            # talk:10800402:"Prepare yourself."
            assert t140601000_x30(text1=10800400, flag1=1149045, mode7=1)
    elif GetEventFlag(1149045):
        """State 5,15"""
        # talk:10801600:"You are prepared?"
        # talk:10801601:"Shall we?"
        assert t140601000_x30(text1=10801600, flag1=1149046, mode7=1)
        """State 16"""
        # action:21082001:"Ready armament"
        # action:21082002:"Leave"
        call = t140601000_x38(action1=21082001, action2=21082002)
        if call.Get() == 0:
            """State 6,9"""
            c1_164()
            assert not f305()
            """State 8"""
            SetEventFlag(10003204, FlagState.On)
        elif call.Get() == 1:
            """State 7,18"""
            # talk:10800400:"Cold feet, I presume?"
            # talk:10800401:"I care not. I won't hear any feeble excuses."
            # talk:10800402:"Prepare yourself."
            assert t140601000_x30(text1=10800400, flag1=1149045, mode7=1)
    """State 19"""
    return 0
    """Unused"""
    """State 13"""
    # talk:10800300:"I'll kill you. Unless you fell me first."
    t140601000_x30(text1=10800300, flag1=1149044, mode7=1)
    Quit()
    """State 17"""
    # talk:10800300:"I'll kill you. Unless you fell me first."
    t140601000_x30(text1=10800300, flag1=1149044, mode7=1)
    Quit()

def t140601000_x59():
    """State 0,4"""
    # talk:10800500:"I yield."
    assert t140601000_x31(text23=10800500, mode6=1) and DoesSelfHaveSpEffect(9935)
    """State 3"""
    # talk:10800510:"Do you see now? You are strong."
    # talk:10800511:"And only the strong can wield true power. The weak have no such privilege."
    # talk:10800512:"But with strength comes the burden of duty."
    # talk:10800513:"Did it never occur to you that this is precisely why you are here?"
    # talk:10800514:"Take this, if you understand me."
    # talk:10800515:"Now. Not a word of this to anyone."
    assert t140601000_x30(text1=10800510, flag1=1149047, mode7=1) and GetEventFlag(1149047)
    """State 1"""
    SetEventFlag(10003205, FlagState.Off)
    """State 2,5"""
    return 0

def t140601000_x60():
    """State 0,8"""
    # talk:10801700:"One more time. Ready?"
    assert t140601000_x30(text1=10801700, flag1=1149050, mode7=1)
    """State 5"""
    # action:21082001:"Ready armament"
    # action:21082002:"Leave"
    call = t140601000_x38(action1=21082001, action2=21082002)
    if call.Get() == 0:
        """State 1,4"""
        c1_164()
        assert not f305()
        """State 3"""
        SetEventFlag(10003204, FlagState.On)
    elif call.Get() == 1:
        """State 2,7"""
        # talk:10800400:"Cold feet, I presume?"
        # talk:10800401:"I care not. I won't hear any feeble excuses."
        # talk:10800402:"Prepare yourself."
        assert t140601000_x30(text1=10800400, flag1=1149045, mode7=1)
    """State 9"""
    return 0
    """Unused"""
    """State 6"""
    # talk:10800300:"I'll kill you. Unless you fell me first."
    t140601000_x30(text1=10800300, flag1=1149044, mode7=1)
    Quit()

