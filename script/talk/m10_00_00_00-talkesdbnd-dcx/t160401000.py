# -*- coding: utf-8 -*-
def t160401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t160401000_x6(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode3=1, mode4=1, mode5=1)
    Quit()

def t160401000_1000():
    """State 0,2,3"""
    assert t160401000_x61()
    """State 1"""
    EndMachine(1000)
    Quit()

def t160401000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t160401000_x0(actionbutton1=6000, flag42=6001, flag47=6000, flag48=6000, flag49=6000, flag50=6000,
            flag41=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t160401000_x0(actionbutton1=6000, flag42=6001, flag47=6000, flag48=6000, flag49=6000, flag50=6000, flag41=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag42) or GetEventFlag(flag47) or GetEventFlag(flag48) or GetEventFlag(flag49) or
                GetEventFlag(flag50))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag41)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag41) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag42) and not GetEventFlag(flag47) and not GetEventFlag(flag48) and not GetEventFlag(flag49)
            and not GetEventFlag(flag50)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t160401000_x1():
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

def t160401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t160401000_x3(z5=_):
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

def t160401000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t160401000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t160401000_x1()
    else:
        """State 4,7"""
        call = t160401000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t160401000_x1()
    """State 9"""
    return 0

def t160401000_x5():
    """State 0,1"""
    assert t160401000_x1()
    """State 2"""
    return 0

def t160401000_x6(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t160401000_x23(flag38=flag38, flag39=flag39, flag40=flag40, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag41=flag41, flag42=flag42, flag43=flag43,
                              flag44=flag44, flag45=flag45, z1=z1, z2=z2, z3=z3, z4=z4, mode3=mode3, mode4=mode4,
                              mode5=mode5)
        assert IsClientPlayer()
        """State 1"""
        call = t160401000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t160401000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag41=6000, flag42=6001, flag43=6000,
                  flag44=6000, flag45=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 2"""
        call = t160401000_x10(actionbutton1=actionbutton1, flag41=flag41, flag42=flag42, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode5 == 1, 1000000)
            call = t160401000_x14(val1=val1, z1=z1)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                c5_172(mode3 == 1 and mode4 == 1, 1, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(mode3 == 1 and not mode4 == 1, 1, 9, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode3 == 1 and mode4 == 1, 9, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode3 == 1 and not mode4 == 1, 9, 9, 9, 9, 9, 9, 9, 9, 9)
            def ExitPause():
                ChangeCamera(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif IsAttackedBySomeone() and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag45):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag43) and not GetEventFlag(flag44) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t160401000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t160401000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t160401000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t160401000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t160401000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t160401000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t160401000_x9(flag38=6000, val2=10, val3=12):
    """State 0,8"""
    assert t160401000_x35()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag38):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t160401000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t160401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t160401000_x10(actionbutton1=6000, flag41=6000, flag42=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t160401000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t160401000_x0(actionbutton1=actionbutton1, flag42=flag42, flag47=6000, flag48=6000, flag49=6000,
                flag50=6000, flag41=flag41))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160401000_x11(machine1=_, val6=_):
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

def t160401000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t160401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t160401000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t160401000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t160401000_x13():
    """State 0,1"""
    assert t160401000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t160401000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t160401000_x24()
    """State 3"""
    call = t160401000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t160401000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t160401000_x15():
    """State 0,1"""
    assert t160401000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t160401000_x16(val5=12):
    """State 0,2"""
    call = t160401000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t160401000_x27()
    """State 4"""
    return 0

def t160401000_x17():
    """State 0,1"""
    assert t160401000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t160401000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t160401000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t160401000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t160401000_x29()
    """Unused"""
    """State 6"""
    return 0

def t160401000_x19():
    """State 0,2"""
    call = t160401000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t160401000_x20():
    """State 0,1"""
    assert t160401000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t160401000_x21():
    """State 0,1"""
    assert t160401000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t160401000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t160401000_x23(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t160401000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag41=flag41, flag42=flag42, flag43=flag43, flag44=flag44, flag45=flag45, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode3=mode3, mode4=mode4, mode5=mode5)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag38):
            """State 3"""
            Label('L0')
            call = t160401000_x9(flag38=flag38, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag38):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag39) or GetEventFlag(flag40):
            """State 2"""
            call = t160401000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag38):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag39) and not GetEventFlag(flag40):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t160401000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t160401000_x24():
    """State 0,1"""
    assert t160401000_x25()
    """State 2"""
    return 0

def t160401000_x25():
    """State 0,1"""
    assert t160401000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t160401000_x26():
    """State 0,1"""
    call = t160401000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t160401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160401000_x27():
    """State 0,1"""
    call = t160401000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t160401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160401000_x28():
    """State 0,1"""
    call = t160401000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t160401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160401000_x29():
    """State 0,1"""
    call = t160401000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t160401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t160401000_x30(text22=10201600, flag46=1209180, mode8=1):
    """State 0,5"""
    assert t160401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag46, FlagState.On)
    """State 1"""
    # talk:10201600:"I see. How unfortunate."
    # talk:10201601:"I cannot force you, but I am patient."
    TalkToPlayer(text22, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode8 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t160401000_x31(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t160401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t160401000_x32(text21=10210400, mode6=1):
    """State 0,4"""
    assert t160401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10210400:"Do you need help with something?"
    TalkToPlayer(text21, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode6 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t160401000_x33():
    """State 0,1"""
    assert t160401000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t160401000_x34():
    """State 0,1"""
    assert t160401000_x1()
    """State 2"""
    return 0

def t160401000_x35():
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

def t160401000_x36(text18=_, flag35=-1, text19=_, flag36=-1, text20=_, flag37=-1):
    """State 0,5"""
    assert t160401000_x3(z5=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160401000_x31(text1=text18, flag1=flag35, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160401000_x31(text1=text19, flag1=flag36, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160401000_x31(text1=text20, flag1=flag37, mode7=1)
    """State 6"""
    return 0

def t160401000_x37(action2=21022003, action3=21022004):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21022003:"Give it to her"
    AddTalkListDataAlt(1, action2, -1, 0, False)
    # action:21022004:"Keep it"
    AddTalkListDataAlt(2, action3, -1, 0, False)
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

def t160401000_x38(text16=10209400, flag33=-1, text17=10209500, flag34=-1):
    """State 0,4"""
    assert t160401000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160401000_x31(text1=text16, flag1=flag33, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160401000_x31(text1=text17, flag1=flag34, mode7=1)
    """State 5"""
    return 0

def t160401000_x39(text18=_, flag30=_, text19=_, flag31=_, text20=_, flag32=_):
    """State 0"""
    if not GetEventFlag(flag30):
        """State 1"""
        assert t160401000_x31(text1=text18, flag1=flag30, mode7=1)
    elif not GetEventFlag(flag31):
        """State 2"""
        assert t160401000_x31(text1=text19, flag1=flag31, mode7=1)
    elif not GetEventFlag(flag32):
        """State 3"""
        assert t160401000_x31(text1=text20, flag1=flag32, mode7=1)
    else:
        """State 4"""
        assert t160401000_x36(text18=text18, flag35=-1, text19=text19, flag36=-1, text20=text20, flag37=-1)
    """State 5"""
    return 0

def t160401000_x40(text16=10209400, flag28=1209162, text17=10209500, flag29=1209163):
    """State 0"""
    if not GetEventFlag(flag28):
        """State 1"""
        assert t160401000_x31(text1=text16, flag1=flag28, mode7=1)
    elif not GetEventFlag(flag29):
        """State 2"""
        assert t160401000_x31(text1=text17, flag1=flag29, mode7=1)
    else:
        """State 3"""
        assert t160401000_x38(text16=text16, flag33=-1, text17=text17, flag34=-1)
    """State 4"""
    return 0

def t160401000_x41(text13=_, flag25=_, text14=_, flag26=_, text15=_, flag27=_):
    """State 0"""
    if not GetEventFlag(flag25):
        """State 2"""
        Label('L0')
        assert t160401000_x31(text1=text13, flag1=flag25, mode7=1)
    elif not GetEventFlag(flag26):
        """State 3"""
        assert t160401000_x31(text1=text14, flag1=flag26, mode7=1)
    elif not GetEventFlag(flag27):
        """State 4"""
        assert t160401000_x31(text1=text15, flag1=flag27, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag25, FlagState.Off)
        SetEventFlag(flag26, FlagState.Off)
        SetEventFlag(flag27, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t160401000_x42(text8=10210700, flag15=1209171, text9=10210800, flag16=1209172, text10=10210900, flag17=1209173,
                   text11=10211000, flag18=1209174, text12=10211100, flag19=1209175):
    """State 0"""
    if not GetEventFlag(flag15):
        """State 1"""
        assert t160401000_x31(text1=text8, flag1=flag15, mode7=1)
    elif not GetEventFlag(flag16):
        """State 2"""
        assert t160401000_x31(text1=text9, flag1=flag16, mode7=1)
    elif not GetEventFlag(flag17):
        """State 3"""
        assert t160401000_x31(text1=text10, flag1=flag17, mode7=1)
    elif not GetEventFlag(flag18):
        """State 4"""
        assert t160401000_x31(text1=text11, flag1=flag18, mode7=1)
    elif not GetEventFlag(flag19):
        """State 5"""
        assert t160401000_x31(text1=text12, flag1=flag19, mode7=1)
    else:
        """State 6"""
        assert (t160401000_x43(text8=text8, flag20=-1, text9=text9, flag21=-1, text10=text10, flag22=-1, text11=text11,
                flag23=-1, text12=text12, flag24=-1))
    """State 7"""
    return 0

def t160401000_x43(text8=10210700, flag20=-1, text9=10210800, flag21=-1, text10=10210900, flag22=-1, text11=10211000,
                   flag23=-1, text12=10211100, flag24=-1):
    """State 0,5"""
    assert t160401000_x3(z5=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160401000_x31(text1=text8, flag1=flag20, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160401000_x31(text1=text9, flag1=flag21, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160401000_x31(text1=text10, flag1=flag22, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160401000_x31(text1=text11, flag1=flag23, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t160401000_x31(text1=text12, flag1=flag24, mode7=1)
    """State 8"""
    return 0

def t160401000_x44(text1=10210700, flag8=-1, text2=10210800, flag9=-1, text3=10211000, flag10=-1, text4=10211100,
                   flag11=-1, text5=10211200, flag12=-1, text6=10211300, flag13=-1, text7=10211400, flag14=-1):
    """State 0,5"""
    assert t160401000_x3(z5=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t160401000_x31(text1=text1, flag1=flag8, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t160401000_x31(text1=text2, flag1=flag9, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t160401000_x31(text1=text3, flag1=flag10, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t160401000_x31(text1=text4, flag1=flag11, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t160401000_x31(text1=text5, flag1=flag12, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t160401000_x31(text1=text6, flag1=flag13, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t160401000_x31(text1=text7, flag1=flag14, mode7=1)
    """State 10"""
    return 0

def t160401000_x45(text1=10210700, flag1=1209171, text2=10210800, flag2=1209172, text3=10211000, flag3=1209174,
                   text4=10211100, flag4=1209175, text5=10211200, flag5=1209176, text6=10211300, flag6=1209177,
                   text7=10211400, flag7=1209178):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t160401000_x31(text1=text1, flag1=flag1, mode7=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t160401000_x31(text1=text2, flag1=flag2, mode7=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t160401000_x31(text1=text3, flag1=flag3, mode7=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t160401000_x31(text1=text4, flag1=flag4, mode7=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t160401000_x31(text1=text5, flag1=flag5, mode7=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t160401000_x31(text1=text6, flag1=flag6, mode7=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t160401000_x31(text1=text7, flag1=flag7, mode7=1)
    else:
        """State 8"""
        assert (t160401000_x44(text1=text1, flag8=-1, text2=text2, flag9=-1, text3=text3, flag10=-1, text4=text4,
                flag11=-1, text5=text5, flag12=-1, text6=text6, flag13=-1, text7=text7, flag14=-1))
    """State 9"""
    return 0

def t160401000_x46(action1=21022002):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21022002:"I’m not afraid of the Night"
    AddTalkListDataAlt(1, action1, -1, 0, False)
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

def t160401000_x47():
    """State 0,1"""
    if not f308(4) == 20300:
        """State 3"""
        if DoesSelfHaveSpEffect(9675):
            """State 7,15"""
            # talk:10201700:"What is it? You can tell me."
            assert t160401000_x31(text1=10201700, flag1=1209153, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9676):
            """State 8,16"""
            # talk:10210400:"Do you need help with something?"
            assert t160401000_x31(text1=10210400, flag1=1209154, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9677):
            """State 9"""
            pass
        else:
            """State 10"""
            pass
        """State 17"""
        # talk:10210500:"You are always welcome."
        assert t160401000_x31(text1=10210500, flag1=1209155, mode7=1)
    elif f308(4) == 20300:
        """State 2"""
        if GetEventFlag(10002010):
            """State 4,12"""
            # talk:10209200:"Speak, as you wish."
            assert t160401000_x31(text1=10209200, flag1=1209151, mode7=1)
        elif GetEventFlag(10002011):
            """State 5,13"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            assert t160401000_x31(text1=10200200, flag1=1209150, mode7=1)
        elif GetEventFlag(10002012):
            """State 6,14"""
            # talk:10209200:"Speak, as you wish."
            assert t160401000_x31(text1=10209200, flag1=1209151, mode7=1)
        else:
            """State 11"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            # talk:10209200:"Speak, as you wish."
            # talk:10209300:"How can I help?"
            assert (t160401000_x41(text13=10200200, flag25=1209150, text14=10209200, flag26=1209151, text15=10209300,
                    flag27=1209152))
    """State 18"""
    Label('L0')
    return 0

def t160401000_x48(mode1=1):
    """State 0,1"""
    if GetTalkListEntryResult() == 1:
        """State 9,14"""
        assert t160401000_x53()
    elif GetTalkListEntryResult() == 98:
        """State 8,13"""
        assert t160401000_x52()
    elif GetTalkListEntryResult() == 99:
        """State 2,10"""
        Label('L0')
        if mode1 == 1:
            """State 11,4"""
            if not f308(4) == 20300:
                """State 6,15"""
                # talk:10201800:"Make sure you're ready."
                # talk:10210200:"Yes. Good bye."
                # talk:10210300:"May fortune visit you."
                assert (t160401000_x41(text13=10201800, flag25=1209159, text14=10210200, flag26=1209160, text15=10210300,
                        flag27=1209161))
            elif f308(4) == 20300:
                """State 5,16"""
                assert t160401000_x60()
        elif not mode1 == 1:
            """State 12"""
            pass
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 7"""
        pass
    """State 17"""
    return 0

def t160401000_x49(mode2=1):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 3"""
    assert t160401000_x58()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode2 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    return 0

def t160401000_x50():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t160401000_x57()
    else:
        """State 2"""
        assert t160401000_x47()
        """State 4"""
        assert t160401000_x49(mode2=1)
        """State 5"""
        assert t160401000_x51()
        """State 3"""
        assert t160401000_x48(mode1=1)
    """State 7"""
    return 0

def t160401000_x51():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t160401000_x52():
    """State 0"""
    if f308(4) == 20300:
        """State 1"""
        assert t160401000_x55()
    elif not f308(4) == 20300:
        """State 2"""
        assert t160401000_x56()
    """State 3"""
    return 0

def t160401000_x53():
    """State 0"""
    if not GetEventFlag(1209180):
        """State 1,3"""
        # talk:10201400:"Is that...?"
        # talk:10201401:"I'm sorry, but that's the timepiece I misplaced."
        # talk:10201402:"Could I trouble you to have it back?"
        assert t160401000_x31(text1=10201400, flag1=1209179, mode7=1)
        """State 4"""
        assert t160401000_x54()
    elif GetEventFlag(1209180):
        """State 2,5"""
        # talk:10205300:"Won't you please part with the pocketwatch?"
        assert t160401000_x31(text1=10205300, flag1=1209181, mode7=1)
        """State 6"""
        assert t160401000_x54()
    """State 7"""
    return 0

def t160401000_x54():
    """State 0,7"""
    # action:21022003:"Give it to her"
    # action:21022004:"Keep it"
    call = t160401000_x37(action2=21022003, action3=21022004)
    if call.Get() == 0:
        """State 4,1"""
        SetEventFlag(10003040, FlagState.On)
        assert not GetEventFlag(10003040)
        """State 2,5"""
        # eventflag:6031:Hero Unlock Flag_Lady
        SetEventFlag(6031, FlagState.On)
    elif call.Done():
        """State 3,6"""
        # talk:10201600:"I see. How unfortunate."
        # talk:10201601:"I cannot force you, but I am patient."
        assert t160401000_x30(text22=10201600, flag46=1209180, mode8=1)
    """State 8"""
    return 0

def t160401000_x55():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10209900:"It is time."
        # talk:10209901:"To finish this once and for all."
        # talk:10210000:"I am deeply grateful to all of you."
        # talk:10210001:"Even if we should face greater challenges down the road,"
        # talk:10210002:"I'm certain that you will always prevail."
        # talk:10210100:"The Roundtable will soon have served its purpose."
        # talk:10210101:"We need only bid our last farewells."
        assert (t160401000_x39(text18=10209900, flag30=1209167, text19=10210000, flag31=1209168, text20=10210100,
                flag32=1209169))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10209800:"How are you finding the Roundtable?"
        # talk:10209801:"I pray that you will be met with some comfort here."
        assert t160401000_x31(text1=10209800, flag1=1209166, mode7=1)
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t160401000_x59()
    """State 7"""
    return 0

def t160401000_x56():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        # talk:10211000:"Brute force alone will not lead to victory. All things possess an inherent logic."
        # talk:10211001:"If you face an impasse, try looking at things afresh."
        # talk:10211100:"The Roundtable seems so lively these days."
        # talk:10211101:"Perhaps the Menial's exuberance is catching on..."
        # talk:10211200:"A chilling presence. Our true adversary cannot be far."
        # talk:10211201:"The darkness, the cold...a void of purest black."
        # talk:10211300:"I never dreamed I'd be given such a momentous task."
        # talk:10211301:"Stranger still, that I found a way to take it on."
        # talk:10211400:"It's hard to believe we've come this far, don't you think?"
        # talk:10211401:"Let's greet the end with a smile."
        assert (t160401000_x45(text1=10210700, flag1=1209171, text2=10210800, flag2=1209172, text3=10211000, flag3=1209174,
                text4=10211100, flag4=1209175, text5=10211200, flag5=1209176, text6=10211300, flag6=1209177, text7=10211400,
                flag7=1209178))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        # talk:10210900:"One monstrosity was trouble enough. To think there were so many more..."
        # talk:10210901:"But things are finally moving in the right direction. Wouldn't you agree?"
        # talk:10211000:"Brute force alone will not lead to victory. All things possess an inherent logic."
        # talk:10211001:"If you face an impasse, try looking at things afresh."
        # talk:10211100:"The Roundtable seems so lively these days."
        # talk:10211101:"Perhaps the Menial's exuberance is catching on..."
        assert (t160401000_x42(text8=10210700, flag15=1209171, text9=10210800, flag16=1209172, text10=10210900,
                flag17=1209173, text11=10211000, flag18=1209174, text12=10211100, flag19=1209175))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10210600:"What a dreadful creature..."
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        assert (t160401000_x39(text18=10210600, flag30=1209170, text19=10210700, flag31=1209171, text20=10210800,
                flag32=1209172))
    """State 7"""
    return 0

def t160401000_x57():
    """State 0,1"""
    # talk:10210400:"Do you need help with something?"
    assert t160401000_x32(text21=10210400, mode6=1)
    """State 2"""
    return 0

def t160401000_x58():
    """State 0,1"""
    # eventflag:6031:Hero Unlock Flag_Lady
    if not GetEventFlag(6031):
        """State 3"""
        if f301(-1) == 0 or f301(-1) == 10:
            """State 4"""
            if GetEventFlag(10001810):
                """State 2"""
                # action:21020024:"Show her the old pocketwatch"
                AddTalkListDataAlt(1, 21020024, -1, 1, False)
            else:
                """State 7"""
                pass
        else:
            """State 6"""
            pass
    else:
        """State 5"""
        pass
    """State 8"""
    return 0

def t160401000_x59():
    """State 0,1"""
    if True:
        """State 2,4"""
        # talk:10209400:"Did you encounter the beast? That is our quarry."
        # talk:10209401:"...How did we allow so much time to slip by..."
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t160401000_x40(text16=10209400, flag28=1209162, text17=10209500, flag29=1209163)
    else:
        """State 3,5"""
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t160401000_x31(text1=10209500, flag1=1209163, mode7=1)
    """State 6"""
    return 0

def t160401000_x60():
    """State 0"""
    if GetEventFlag(10002010):
        """State 1,5"""
        # talk:10209000:"I await your return."
        assert t160401000_x31(text1=10209000, flag1=1209157, mode7=1)
    elif GetEventFlag(10002011):
        """State 2,6"""
        # talk:10200500:"Fortune favours the well-prepared."
        assert t160401000_x31(text1=10200500, flag1=1209156, mode7=1)
    elif GetEventFlag(10002012):
        """State 3,7"""
        # talk:10209100:"May you triumph in battle."
        assert t160401000_x31(text1=10209100, flag1=1209158, mode7=1)
    else:
        """State 4"""
        # talk:10200500:"Fortune favours the well-prepared."
        # talk:10209000:"I await your return."
        # talk:10209100:"May you triumph in battle."
        assert (t160401000_x41(text13=10200500, flag25=1209156, text14=10209000, flag26=1209157, text15=10209100,
                flag27=1209158))
    """State 8"""
    return 0

def t160401000_x61():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t160401000_x62()
    """State 2"""
    return 0

def t160401000_x62():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t160401000_x63()
        if call.Get() == 1:
            """State 2"""
            Label('L0')
            """State 7"""
            Label('L1')
            assert t160401000_x50()
        elif call.Done():
            pass
    elif f302(-1) == 3:
        """State 4"""
        call = t160401000_x65()
        if call.Get() == 1:
            """State 5"""
            call = t160401000_x67()
            if call.Get() == 0:
                Goto('L0')
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 4:
        """State 6"""
        call = t160401000_x68()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L1')
    """State 8"""
    return 0

def t160401000_x63():
    """State 0"""
    if GetEventFlag(3600):
        """State 1,6"""
        # talk:10206700:"You have awoken?"
        # talk:10206701:"This is your new home. It is as much yours as it is ours."
        # talk:10206702:"I hope you settle in."
        assert t160401000_x31(text1=10206700, flag1=1169020, mode7=1)
    elif GetEventFlag(3601):
        """State 2,7"""
        assert t160401000_x64()
    elif GetEventFlag(3602):
        """State 3,8"""
        Label('L0')
        # talk:10208400:"This might seem all too much right now, but I promise, with time you will grow accustomed to this place."
        assert t160401000_x31(text1=10208400, flag1=1169022, mode7=1)
    elif GetEventFlag(3603):
        """State 4"""
        Goto('L0')
    elif GetEventFlag(3604):
        """State 5"""
        Goto('L0')
    else:
        """State 10"""
        return 1
    """State 9"""
    return 0

def t160401000_x64():
    """State 0,3"""
    assert t160401000_x47()
    """State 4"""
    assert t160401000_x49(mode2=1)
    """State 1"""
    # action:21020025:"Why did you bring me here?"
    AddTalkListDataAlt(2, 21020025, -1, 2, False)
    """State 5"""
    call = t160401000_x51()
    if call.Done() and GetTalkListEntryResult() == 2:
        """State 2"""
        # talk:10206800:"You must have many questions."
        # talk:10206801:"Well, it's simple enough. We have a common cause."
        # talk:10206802:"Perhaps you don't remember... All your talk of getting revenge upon the Nightlord,\nhow you would never forgive it, and so on?"
        # talk:10206803:"Hardly grounds for abandoning you."
        # talk:10206804:"This might seem all too much right now, but I promise, with time you will grow accustomed to this place."
        assert t160401000_x31(text1=10206800, flag1=1169021, mode7=1)
    elif call.Done():
        """State 6"""
        assert t160401000_x48(mode1=1)
    """State 7"""
    return 0

def t160401000_x65():
    """State 0"""
    if GetEventFlag(3612):
        """State 1,5"""
        # talk:10204500:"Your condition has worsened."
        # talk:10204501:"There's only so much that can be hidden... We'll have to do something about that."
        assert t160401000_x31(text1=10204500, flag1=1169023, mode7=1)
    elif GetEventFlag(3613):
        """State 2,6"""
        assert t160401000_x66()
    elif GetEventFlag(3614):
        """State 4,7"""
        Label('L0')
        # talk:10208600:"Go to see the witch. She should be able to help."
        assert t160401000_x31(text1=10208600, flag1=1169027, mode7=1)
    elif GetEventFlag(3615):
        """State 3"""
        Goto('L0')
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0

def t160401000_x66():
    """State 0,3"""
    # talk:10208500:"We need to think of something."
    assert t160401000_x31(text1=10208500, flag1=1169024, mode7=1)
    """State 7"""
    assert t160401000_x49(mode2=1)
    """State 1"""
    # action:21020026:"Ask about the Night's corrosion"
    AddTalkListDataAlt(2, 21020026, -1, 2, False)
    """State 6"""
    call = t160401000_x51()
    if call.Done() and GetTalkListEntryResult() == 2:
        """State 2"""
        # talk:10204600:"Listen carefully."
        # talk:10204601:"Your condition, the contamination, it's spreading."
        # talk:10204602:"If it continues, you'll be swallowed by the Night again."
        # talk:10204603:"You must conquer this. This fear of the Night."
        assert t160401000_x31(text1=10204600, flag1=1169025, mode7=1)
        """State 5"""
        # action:21022002:"I’m not afraid of the Night"
        assert t160401000_x46(action1=21022002)
        """State 4"""
        # talk:10204700:"You might say the words, but deep down, you do not believe them."
        # talk:10204701:"Go to see the witch. She should be able to help."
        assert t160401000_x31(text1=10204700, flag1=1169026, mode7=1)
    elif call.Done():
        """State 8"""
        assert t160401000_x48(mode1=1)
    """State 9"""
    return 0

def t160401000_x67():
    """State 0"""
    if GetEventFlag(3616):
        """State 1"""
        pass
    elif GetEventFlag(3617):
        """State 2"""
        pass
    else:
        """State 4"""
        return 0
    """State 3"""
    assert t160401000_x69()
    """State 5"""
    return 1

def t160401000_x68():
    """State 0"""
    if GetEventFlag(3620):
        """State 1"""
        pass
    elif GetEventFlag(3621):
        """State 2"""
        pass
    else:
        """State 5"""
        return 1
    """State 3"""
    # talk:10206900:"You've overcome your fears. Well done."
    # talk:10206901:"I must look to your example..."
    assert t160401000_x31(text1=10206900, flag1=1169030, mode7=1)
    """State 4"""
    return 0

def t160401000_x69():
    """State 0"""
    if not GetEventFlag(1169028):
        """State 1,3"""
        # talk:10205000:"You've done it."
        # talk:10205001:"I would congratulate you..."
        # talk:10205002:"But judging by the cloud hanging over your head, I suppose you're not out of the woods yet."
        # talk:10205003:"I understand. It's no easy task, facing the truth."
        # talk:10205004:"I understand all too well..."
        assert t160401000_x31(text1=10205000, flag1=1169028, mode7=1)
    elif GetEventFlag(1169028):
        """State 2,4"""
        # talk:10208700:"You are blessed with fortitude..."
        assert t160401000_x31(text1=10208700, flag1=1169029, mode7=1)
    """State 5"""
    return 0

