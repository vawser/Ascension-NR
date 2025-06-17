# -*- coding: utf-8 -*-
def t180401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t180401000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode3=1, mode4=1, mode5=1)
    Quit()

def t180401000_1000():
    """State 0,2,3"""
    assert t180401000_x63()
    """State 1"""
    EndMachine(1000)
    Quit()

def t180401000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t180401000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000, flag43=6000)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif GetEventFlag(3823):
        """State 4"""
        t180401000_x76()
        Quit()

def t180401000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000, flag43=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag44) or GetEventFlag(flag49) or GetEventFlag(flag50) or GetEventFlag(flag51) or
                GetEventFlag(flag52))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag43)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag43) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag44) and not GetEventFlag(flag49) and not GetEventFlag(flag50) and not GetEventFlag(flag51)
            and not GetEventFlag(flag52)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t180401000_x1():
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

def t180401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t180401000_x3(z7=_):
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

def t180401000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t180401000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t180401000_x1()
    else:
        """State 4,7"""
        call = t180401000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t180401000_x1()
    """State 9"""
    return 0

def t180401000_x5():
    """State 0,1"""
    assert t180401000_x1()
    """State 2"""
    return 0

def t180401000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t180401000_x23(flag40=flag40, flag41=flag41, flag42=flag42, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, flag45=flag45,
                              flag46=flag46, flag47=flag47, z3=z3, z4=z4, z5=z5, z6=z6, mode3=mode3, mode4=mode4,
                              mode5=mode5)
        assert IsClientPlayer()
        """State 1"""
        call = t180401000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t180401000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag43=6000, flag44=6001, flag45=6000,
                  flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 2"""
        call = t180401000_x10(actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode5 == 1, 1000000)
            call = t180401000_x14(val1=val1, z3=z3)
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
        elif GetEventFlag(flag47):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag45) and not GetEventFlag(flag46) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t180401000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t180401000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t180401000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t180401000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t180401000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t180401000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t180401000_x9(flag40=6000, val2=10, val3=12):
    """State 0,8"""
    assert t180401000_x35()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag40):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t180401000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t180401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t180401000_x10(actionbutton1=6000, flag43=6000, flag44=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t180401000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t180401000_x0(actionbutton1=actionbutton1, flag44=flag44, flag49=6000, flag50=6000, flag51=6000,
                flag52=6000, flag43=flag43))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180401000_x11(machine1=_, val6=_):
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

def t180401000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t180401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t180401000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t180401000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t180401000_x13():
    """State 0,1"""
    assert t180401000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t180401000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t180401000_x24()
    """State 3"""
    call = t180401000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t180401000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t180401000_x15():
    """State 0,1"""
    assert t180401000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t180401000_x16(val5=12):
    """State 0,2"""
    call = t180401000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t180401000_x27()
    """State 4"""
    return 0

def t180401000_x17():
    """State 0,1"""
    assert t180401000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t180401000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t180401000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t180401000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t180401000_x29()
    """Unused"""
    """State 6"""
    return 0

def t180401000_x19():
    """State 0,2"""
    call = t180401000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t180401000_x20():
    """State 0,1"""
    assert t180401000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t180401000_x21():
    """State 0,1"""
    assert t180401000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t180401000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t180401000_x23(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t180401000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag43=flag43, flag44=flag44, flag45=flag45, flag46=flag46, flag47=flag47, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode3=mode3, mode4=mode4, mode5=mode5)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag40):
            """State 3"""
            Label('L0')
            call = t180401000_x9(flag40=flag40, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag40):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag41) or GetEventFlag(flag42):
            """State 2"""
            call = t180401000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag40):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag41) and not GetEventFlag(flag42):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t180401000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t180401000_x24():
    """State 0,1"""
    assert t180401000_x25()
    """State 2"""
    return 0

def t180401000_x25():
    """State 0,1"""
    assert t180401000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t180401000_x26():
    """State 0,1"""
    call = t180401000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t180401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180401000_x27():
    """State 0,1"""
    call = t180401000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t180401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180401000_x28():
    """State 0,1"""
    call = t180401000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t180401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180401000_x29():
    """State 0,1"""
    call = t180401000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t180401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t180401000_x30(text24=10201600, flag48=1209180, mode8=1):
    """State 0,5"""
    assert t180401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag48, FlagState.On)
    """State 1"""
    # talk:10201600:"I see. How unfortunate."
    # talk:10201601:"I cannot force you, but I am patient."
    TalkToPlayer(text24, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode8 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t180401000_x31(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t180401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t180401000_x32(text23=10210400, mode6=1):
    """State 0,4"""
    assert t180401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10210400:"Do you need help with something?"
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

def t180401000_x33():
    """State 0,1"""
    assert t180401000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t180401000_x34():
    """State 0,1"""
    assert t180401000_x1()
    """State 2"""
    return 0

def t180401000_x35():
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

def t180401000_x36(z1=_, z2=_):
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

def t180401000_x37():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t180401000_x38(text20=_, flag37=-1, text21=_, flag38=-1, text22=_, flag39=-1):
    """State 0,5"""
    assert t180401000_x3(z7=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180401000_x31(text1=text20, flag1=flag37, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180401000_x31(text1=text21, flag1=flag38, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180401000_x31(text1=text22, flag1=flag39, mode7=1)
    """State 6"""
    return 0

def t180401000_x39(action2=21022003, action3=21022004):
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

def t180401000_x40(text18=10209400, flag35=-1, text19=10209500, flag36=-1):
    """State 0,4"""
    assert t180401000_x3(z7=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180401000_x31(text1=text18, flag1=flag35, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180401000_x31(text1=text19, flag1=flag36, mode7=1)
    """State 5"""
    return 0

def t180401000_x41(text20=_, flag32=_, text21=_, flag33=_, text22=_, flag34=_):
    """State 0"""
    if not GetEventFlag(flag32):
        """State 1"""
        assert t180401000_x31(text1=text20, flag1=flag32, mode7=1)
    elif not GetEventFlag(flag33):
        """State 2"""
        assert t180401000_x31(text1=text21, flag1=flag33, mode7=1)
    elif not GetEventFlag(flag34):
        """State 3"""
        assert t180401000_x31(text1=text22, flag1=flag34, mode7=1)
    else:
        """State 4"""
        assert t180401000_x38(text20=text20, flag37=-1, text21=text21, flag38=-1, text22=text22, flag39=-1)
    """State 5"""
    return 0

def t180401000_x42(text18=10209400, flag30=1209162, text19=10209500, flag31=1209163):
    """State 0"""
    if not GetEventFlag(flag30):
        """State 1"""
        assert t180401000_x31(text1=text18, flag1=flag30, mode7=1)
    elif not GetEventFlag(flag31):
        """State 2"""
        assert t180401000_x31(text1=text19, flag1=flag31, mode7=1)
    else:
        """State 3"""
        assert t180401000_x40(text18=text18, flag35=-1, text19=text19, flag36=-1)
    """State 4"""
    return 0

def t180401000_x43(text15=_, flag27=_, text16=_, flag28=_, text17=_, flag29=_):
    """State 0"""
    if not GetEventFlag(flag27):
        """State 2"""
        Label('L0')
        assert t180401000_x31(text1=text15, flag1=flag27, mode7=1)
    elif not GetEventFlag(flag28):
        """State 3"""
        assert t180401000_x31(text1=text16, flag1=flag28, mode7=1)
    elif not GetEventFlag(flag29):
        """State 4"""
        assert t180401000_x31(text1=text17, flag1=flag29, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag27, FlagState.Off)
        SetEventFlag(flag28, FlagState.Off)
        SetEventFlag(flag29, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t180401000_x44(text10=10210700, flag17=1209171, text11=10210800, flag18=1209172, text12=10210900, flag19=1209173,
                   text13=10211000, flag20=1209174, text14=10211100, flag21=1209175):
    """State 0"""
    if not GetEventFlag(flag17):
        """State 1"""
        assert t180401000_x31(text1=text10, flag1=flag17, mode7=1)
    elif not GetEventFlag(flag18):
        """State 2"""
        assert t180401000_x31(text1=text11, flag1=flag18, mode7=1)
    elif not GetEventFlag(flag19):
        """State 3"""
        assert t180401000_x31(text1=text12, flag1=flag19, mode7=1)
    elif not GetEventFlag(flag20):
        """State 4"""
        assert t180401000_x31(text1=text13, flag1=flag20, mode7=1)
    elif not GetEventFlag(flag21):
        """State 5"""
        assert t180401000_x31(text1=text14, flag1=flag21, mode7=1)
    else:
        """State 6"""
        assert (t180401000_x45(text10=text10, flag22=-1, text11=text11, flag23=-1, text12=text12, flag24=-1, text13=text13,
                flag25=-1, text14=text14, flag26=-1))
    """State 7"""
    return 0

def t180401000_x45(text10=10210700, flag22=-1, text11=10210800, flag23=-1, text12=10210900, flag24=-1, text13=10211000,
                   flag25=-1, text14=10211100, flag26=-1):
    """State 0,5"""
    assert t180401000_x3(z7=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180401000_x31(text1=text10, flag1=flag22, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180401000_x31(text1=text11, flag1=flag23, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180401000_x31(text1=text12, flag1=flag24, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180401000_x31(text1=text13, flag1=flag25, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t180401000_x31(text1=text14, flag1=flag26, mode7=1)
    """State 8"""
    return 0

def t180401000_x46(text3=10210700, flag10=-1, text4=10210800, flag11=-1, text5=10211000, flag12=-1, text6=10211100,
                   flag13=-1, text7=10211200, flag14=-1, text8=10211300, flag15=-1, text9=10211400, flag16=-1):
    """State 0,5"""
    assert t180401000_x3(z7=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t180401000_x31(text1=text3, flag1=flag10, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t180401000_x31(text1=text4, flag1=flag11, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t180401000_x31(text1=text5, flag1=flag12, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t180401000_x31(text1=text6, flag1=flag13, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t180401000_x31(text1=text7, flag1=flag14, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t180401000_x31(text1=text8, flag1=flag15, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t180401000_x31(text1=text9, flag1=flag16, mode7=1)
    """State 10"""
    return 0

def t180401000_x47(text3=10210700, flag3=1209171, text4=10210800, flag4=1209172, text5=10211000, flag5=1209174,
                   text6=10211100, flag6=1209175, text7=10211200, flag7=1209176, text8=10211300, flag8=1209177,
                   text9=10211400, flag9=1209178):
    """State 0"""
    if not GetEventFlag(flag3):
        """State 1"""
        assert t180401000_x31(text1=text3, flag1=flag3, mode7=1)
    elif not GetEventFlag(flag4):
        """State 2"""
        assert t180401000_x31(text1=text4, flag1=flag4, mode7=1)
    elif not GetEventFlag(flag5):
        """State 3"""
        assert t180401000_x31(text1=text5, flag1=flag5, mode7=1)
    elif not GetEventFlag(flag6):
        """State 4"""
        assert t180401000_x31(text1=text6, flag1=flag6, mode7=1)
    elif not GetEventFlag(flag7):
        """State 5"""
        assert t180401000_x31(text1=text7, flag1=flag7, mode7=1)
    elif not GetEventFlag(flag8):
        """State 6"""
        assert t180401000_x31(text1=text8, flag1=flag8, mode7=1)
    elif not GetEventFlag(flag9):
        """State 7"""
        assert t180401000_x31(text1=text9, flag1=flag9, mode7=1)
    else:
        """State 8"""
        assert (t180401000_x46(text3=text3, flag10=-1, text4=text4, flag11=-1, text5=text5, flag12=-1, text6=text6,
                flag13=-1, text7=text7, flag14=-1, text8=text8, flag15=-1, text9=text9, flag16=-1))
    """State 9"""
    return 0

def t180401000_x48(action1=21020027):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21020027:"Assent"
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

def t180401000_x49():
    """State 0,1"""
    if not f308(4) == 20300:
        """State 3"""
        if DoesSelfHaveSpEffect(9675):
            """State 7,15"""
            # talk:10201700:"What is it? You can tell me."
            assert t180401000_x31(text1=10201700, flag1=1209153, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9676):
            """State 8,16"""
            # talk:10210400:"Do you need help with something?"
            assert t180401000_x31(text1=10210400, flag1=1209154, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9677):
            """State 9"""
            pass
        else:
            """State 10"""
            pass
        """State 17"""
        # talk:10210500:"You are always welcome."
        assert t180401000_x31(text1=10210500, flag1=1209155, mode7=1)
    elif f308(4) == 20300:
        """State 2"""
        if GetEventFlag(10002010):
            """State 4,12"""
            # talk:10209200:"Speak, as you wish."
            assert t180401000_x31(text1=10209200, flag1=1209151, mode7=1)
        elif GetEventFlag(10002011):
            """State 5,13"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            assert t180401000_x31(text1=10200200, flag1=1209150, mode7=1)
        elif GetEventFlag(10002012):
            """State 6,14"""
            # talk:10209200:"Speak, as you wish."
            assert t180401000_x31(text1=10209200, flag1=1209151, mode7=1)
        else:
            """State 11"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            # talk:10209200:"Speak, as you wish."
            # talk:10209300:"How can I help?"
            assert (t180401000_x43(text15=10200200, flag27=1209150, text16=10209200, flag28=1209151, text17=10209300,
                    flag29=1209152))
    """State 18"""
    Label('L0')
    return 0

def t180401000_x50(mode1=1):
    """State 0,1"""
    if GetTalkListEntryResult() == 1:
        """State 9,14"""
        assert t180401000_x55()
    elif GetTalkListEntryResult() == 98:
        """State 8,13"""
        assert t180401000_x54()
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
                assert (t180401000_x43(text15=10201800, flag27=1209159, text16=10210200, flag28=1209160, text17=10210300,
                        flag29=1209161))
            elif f308(4) == 20300:
                """State 5,16"""
                assert t180401000_x62()
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

def t180401000_x51(mode2=1):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 3"""
    assert t180401000_x60()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode2 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    return 0

def t180401000_x52():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t180401000_x59()
    else:
        """State 2"""
        assert t180401000_x49()
        """State 4"""
        assert t180401000_x51(mode2=1)
        """State 5"""
        assert t180401000_x53()
        """State 3"""
        assert t180401000_x50(mode1=1)
    """State 7"""
    return 0

def t180401000_x53():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t180401000_x54():
    """State 0"""
    if f308(4) == 20300:
        """State 1"""
        assert t180401000_x57()
    elif not f308(4) == 20300:
        """State 2"""
        assert t180401000_x58()
    """State 3"""
    return 0

def t180401000_x55():
    """State 0"""
    if not GetEventFlag(1209180):
        """State 1,3"""
        # talk:10201400:"Is that...?"
        # talk:10201401:"I'm sorry, but that's the timepiece I misplaced."
        # talk:10201402:"Could I trouble you to have it back?"
        assert t180401000_x31(text1=10201400, flag1=1209179, mode7=1)
        """State 4"""
        assert t180401000_x56()
    elif GetEventFlag(1209180):
        """State 2,5"""
        # talk:10205300:"Won't you please part with the pocketwatch?"
        assert t180401000_x31(text1=10205300, flag1=1209181, mode7=1)
        """State 6"""
        assert t180401000_x56()
    """State 7"""
    return 0

def t180401000_x56():
    """State 0,7"""
    # action:21022003:"Give it to her"
    # action:21022004:"Keep it"
    call = t180401000_x39(action2=21022003, action3=21022004)
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
        assert t180401000_x30(text24=10201600, flag48=1209180, mode8=1)
    """State 8"""
    return 0

def t180401000_x57():
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
        assert (t180401000_x41(text20=10209900, flag32=1209167, text21=10210000, flag33=1209168, text22=10210100,
                flag34=1209169))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10209800:"How are you finding the Roundtable?"
        # talk:10209801:"I pray that you will be met with some comfort here."
        assert t180401000_x31(text1=10209800, flag1=1209166, mode7=1)
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t180401000_x61()
    """State 7"""
    return 0

def t180401000_x58():
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
        assert (t180401000_x47(text3=10210700, flag3=1209171, text4=10210800, flag4=1209172, text5=10211000, flag5=1209174,
                text6=10211100, flag6=1209175, text7=10211200, flag7=1209176, text8=10211300, flag8=1209177, text9=10211400,
                flag9=1209178))
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
        assert (t180401000_x44(text10=10210700, flag17=1209171, text11=10210800, flag18=1209172, text12=10210900,
                flag19=1209173, text13=10211000, flag20=1209174, text14=10211100, flag21=1209175))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10210600:"What a dreadful creature..."
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        assert (t180401000_x41(text20=10210600, flag32=1209170, text21=10210700, flag33=1209171, text22=10210800,
                flag34=1209172))
    """State 7"""
    return 0

def t180401000_x59():
    """State 0,1"""
    # talk:10210400:"Do you need help with something?"
    assert t180401000_x32(text23=10210400, mode6=1)
    """State 2"""
    return 0

def t180401000_x60():
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

def t180401000_x61():
    """State 0,1"""
    if True:
        """State 2,4"""
        # talk:10209400:"Did you encounter the beast? That is our quarry."
        # talk:10209401:"...How did we allow so much time to slip by..."
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t180401000_x42(text18=10209400, flag30=1209162, text19=10209500, flag31=1209163)
    else:
        """State 3,5"""
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t180401000_x31(text1=10209500, flag1=1209163, mode7=1)
    """State 6"""
    return 0

def t180401000_x62():
    """State 0"""
    if GetEventFlag(10002010):
        """State 1,5"""
        # talk:10209000:"I await your return."
        assert t180401000_x31(text1=10209000, flag1=1209157, mode7=1)
    elif GetEventFlag(10002011):
        """State 2,6"""
        # talk:10200500:"Fortune favours the well-prepared."
        assert t180401000_x31(text1=10200500, flag1=1209156, mode7=1)
    elif GetEventFlag(10002012):
        """State 3,7"""
        # talk:10209100:"May you triumph in battle."
        assert t180401000_x31(text1=10209100, flag1=1209158, mode7=1)
    else:
        """State 4"""
        # talk:10200500:"Fortune favours the well-prepared."
        # talk:10209000:"I await your return."
        # talk:10209100:"May you triumph in battle."
        assert (t180401000_x43(text15=10200500, flag27=1209156, text16=10209000, flag28=1209157, text17=10209100,
                flag29=1209158))
    """State 8"""
    return 0

def t180401000_x63():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t180401000_x64()
    """State 2"""
    return 0

def t180401000_x64():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t180401000_x65()
        if call.Get() == 1:
            """State 4"""
            call = t180401000_x66()
            if call.Get() == 1:
                """State 2"""
                Label('L0')
                """State 9"""
                Label('L1')
                assert t180401000_x52()
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 2:
        """State 5"""
        call = t180401000_x67()
        if call.Get() == 1:
            """State 6"""
            call = t180401000_x69()
            if call.Get() == 0:
                Goto('L0')
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 3:
        """State 10"""
        call = t180401000_x72()
        if call.Get() == 1:
            """State 7"""
            call = t180401000_x73()
            if call.Get() == 1:
                Goto('L0')
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 4:
        """State 8"""
        call = t180401000_x74()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L1')
    """State 11"""
    return 0

def t180401000_x65():
    """State 0"""
    if GetEventFlag(3800):
        """State 3,6"""
        assert t180401000_x52()
    elif GetEventFlag(3801):
        """State 1,4"""
        # talk:10202300:"There you are."
        # talk:10202301:"There is a task I would like you to perform. Would you be so kind as to find me some flowers?"
        # talk:10202302:"Since you're familiar with the old, golden realm and have an eye for beauty,"
        # talk:10202303:"I'm sure you can locate some which positively brim with Grace."
        # talk:10202304:"If you wouldn't mind, of course."
        assert t180401000_x31(text1=10202300, flag1=1189010, mode7=1)
        """State 7"""
        assert t180401000_x36(z1=803, z2=1)
    elif GetEventFlag(3802):
        """State 2,5"""
        # talk:10207300:"Please bring me flowers abundant with Grace from the land beyond."
        assert t180401000_x31(text1=10207300, flag1=1189011, mode7=1)
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0

def t180401000_x66():
    """State 0"""
    if GetEventFlag(3803):
        """State 1,12"""
        Label('L0')
        assert t180401000_x77()
    elif GetEventFlag(3804):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3805):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3806):
        """State 4,9"""
        # talk:10206200:"He seemed to like the flowers."
        # talk:10206201:"And now I know your memories are trustworthy."
        # talk:10206202:"I'm sorry I had to test you."
        # talk:10206203:"There is a voice...I can hear. I fear something will happen before long..."
        assert t180401000_x31(text1=10206200, flag1=1189014, mode7=1)
    elif GetEventFlag(3807):
        """State 5,10"""
        # talk:10206300:"This place mirrors the traditions of yore."
        # talk:10206301:"Only the light of Grace preserves our connection to the outside world."
        # talk:10206302:"But it is a pale carryover. Embers of the warmth that once was. No-one knows how much longer it can last."
        # talk:10206303:"But you, you knew Grace, first hand... Your knowledge is vital."
        # talk:10206304:"Please keep that in mind."
        assert t180401000_x31(text1=10206300, flag1=1189015, mode7=1)
        """State 7"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 8"""
    elif GetEventFlag(3808):
        """State 6,11"""
        # talk:10207800:"One day, your knowledge of Grace will be vital."
        # talk:10207801:"Remember that, always..."
        assert t180401000_x31(text1=10207800, flag1=1189016, mode7=1)
    else:
        """State 14"""
        return 1
    """State 13"""
    return 0

def t180401000_x67():
    """State 0,9"""
    return 1
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 2"""
    Goto('L2')
    """State 3"""
    Goto('L2')
    """State 4"""
    Goto('L2')
    """State 5"""
    Label('L0')
    SetEventFlag(10003400, FlagState.On)
    Goto('L3')
    """State 6"""
    Label('L1')
    # talk:10202400:"Surely you can see it."
    # talk:10202401:"The light is fading fast. It won't be long now."
    # talk:10202402:"We have no choice but to augment what little Grace we enjoy."
    # talk:10202403:"And your memories will be the key."
    assert t180401000_x31(text1=10202400, flag1=1189017, mode7=1)
    Goto('L0')
    """State 7"""
    Label('L2')
    assert t180401000_x68()
    """State 8"""
    Label('L3')
    return 0

def t180401000_x68():
    """State 0,4"""
    if f304(801) == 0 or GetEventFlag(10003400):
        """State 5"""
        # talk:10207500:"I only pray that our Grace will last..."
        assert t180401000_x31(text1=10207500, flag1=1189018, mode7=1)
    else:
        """State 11"""
        assert t180401000_x49()
    """State 6"""
    assert t180401000_x51(mode2=1)
    """State 1"""
    # action:21020012:"About my memories"
    AddTalkListDataAlt(2, 21020012, -1, 2, False)
    """State 7"""
    assert t180401000_x53()
    """State 2"""
    if GetTalkListEntryResult() == 2:
        """State 3,9"""
        # talk:10206400:"The Erdtree would once scatter its seeds across the lands."
        # talk:10206401:"Every man, woman, and child desperate for the Grace of gold."
        # talk:10206402:"And you, you have touched it for yourself."
        # talk:10206403:"Your memories should show where the seeds have fallen."
        # talk:10206404:"Please, search them out for us."
        assert t180401000_x31(text1=10206400, flag1=1189019, mode7=1)
        """State 10"""
        assert t180401000_x36(z1=801, z2=1)
    else:
        """State 8"""
        assert t180401000_x50(mode1=1)
    """State 12"""
    return 0

def t180401000_x69():
    """State 0,20"""
    return 0
    """Unused"""
    """State 1"""
    if GetEventFlag(10003400):
        Goto('L0')
    elif not GetEventFlag(10003400):
        pass
    """State 2"""
    Goto('L5')
    """State 3"""
    Label('L0')
    Goto('L4')
    """State 4"""
    Label('L1')
    SetEventFlag(10003400, FlagState.Off)
    Goto('L11')
    """State 5"""
    if GetEventFlag(10003400):
        Goto('L3')
    elif not GetEventFlag(10003400):
        pass
    """State 6"""
    Goto('L7')
    """State 7"""
    Label('L2')
    SetEventFlag(10003400, FlagState.Off)
    Goto('L11')
    """State 8"""
    Goto('L8')
    """State 9"""
    Goto('L9')
    """State 10"""
    Goto('L10')
    """State 11"""
    Goto('L10')
    """State 12"""
    Label('L3')
    Goto('L6')
    """State 13"""
    Label('L4')
    # talk:10202500:"Is that...?"
    # talk:10202501:"Though faint, I feel its radiance..."
    # talk:10202502:"Let's give it a try."
    assert t180401000_x70(text2=10202500, flag2=1189020)
    Goto('L1')
    """State 14"""
    Label('L5')
    # talk:10207600:"Just a few more...and there will be hope."
    # talk:10207601:"Please, seek them. Yet undiscovered seeds."
    assert t180401000_x31(text1=10207600, flag1=1189023, mode7=1)
    Goto('L11')
    """State 15"""
    Label('L6')
    # talk:10202800:"Oh, you found more."
    # talk:10202801:"Let's try again."
    assert t180401000_x70(text2=10202800, flag2=1189021)
    Goto('L2')
    """State 16"""
    Label('L7')
    # talk:10207600:"Just a few more...and there will be hope."
    # talk:10207601:"Please, seek them. Yet undiscovered seeds."
    assert t180401000_x31(text1=10207600, flag1=1189023, mode7=1)
    Goto('L11')
    """State 17"""
    Label('L8')
    # talk:10202800:"Oh, you found more."
    # talk:10202801:"Let's try again."
    assert t180401000_x71(text1=10202800, flag1=1189021)
    Goto('L11')
    """State 18"""
    Label('L9')
    # talk:10202500:"Is that...?"
    # talk:10202501:"Though faint, I feel its radiance..."
    # talk:10202502:"Let's give it a try."
    assert t180401000_x71(text1=10202500, flag1=1189020)
    Goto('L11')
    """State 19"""
    Label('L10')
    # talk:10206500:"We've exhausted this avenue. Let's focus on the original plan."
    assert t180401000_x31(text1=10206500, flag1=1189025, mode7=1)
    """State 21"""
    Label('L11')
    return 1

def t180401000_x70(text2=_, flag2=_):
    """State 0,3"""
    assert t180401000_x31(text1=text2, flag1=flag2, mode7=1)
    """State 1"""
    SetEventFlag(10003401, FlagState.On)
    def WhilePaused():
        c1_172(3, 3, 9, 9, 9, 9, 9, 9, 9)
    assert not GetEventFlag(10003401)
    """State 4"""
    # talk:10202600:"No luck."
    # talk:10202601:"We haven't enough..."
    assert t180401000_x31(text1=10202600, flag1=1189022, mode7=1)
    """State 2"""
    SetEventFlag(10003410, FlagState.On)
    """State 5"""
    return 0

def t180401000_x71(text1=_, flag1=_):
    """State 0,4"""
    assert t180401000_x31(text1=text1, flag1=flag1, mode7=1)
    """State 1"""
    SetEventFlag(10003402, FlagState.On)
    def WhilePaused():
        c1_172(3, 3, 9, 9, 9, 9, 9, 9, 9)
    assert not GetEventFlag(10003402)
    """State 5"""
    # talk:10202700:"..."
    # talk:10202701:"That's that."
    # talk:10202702:"It's like a cracked chalice, leaking as it's replenished."
    # talk:10202703:"If the seeds would only sprout, it could be restored. But that will take time."
    # talk:10202704:"We've tried all we can. Our original plan will have to do."
    # talk:10202705:"I'm grateful for your assistance, nonetheless."
    assert t180401000_x31(text1=10202700, flag1=1189024, mode7=1)
    """State 2,6"""
    assert t180401000_x36(z1=801, z2=3)
    """State 3"""
    SetEventFlag(10003410, FlagState.On)
    """State 7"""
    return 0

def t180401000_x72():
    """State 0"""
    if GetEventFlag(3819):
        """State 1,3"""
        # talk:10202400:"Surely you can see it."
        # talk:10202401:"The light is fading fast. It won't be long now."
        # talk:10202402:"We have no choice but to augment what little Grace we enjoy."
        # talk:10202403:"And your memories will be the key."
        assert t180401000_x31(text1=10202400, flag1=1189017, mode7=1)
        """State 7"""
        # action:21020027:"Assent"
        assert t180401000_x48(action1=21020027)
        """State 6"""
        # talk:10206600:"I heard the voice..."
        # talk:10206601:"A golden seed has begun to sprout..."
        # talk:10206602:"In a harsh land of frigid cold, where no-one sets foot."
        # talk:10206603:"It's calling to you."
        # talk:10206604:"This might be selfish, but please..."
        # talk:10206605:"Imagine if we're successful this time..."
        # talk:10206606:"Would you lend me your strength, once more?"
        assert t180401000_x31(text1=10206600, flag1=1189026, mode7=1)
        """State 4"""
        assert t180401000_x36(z1=802, z2=1)
    elif GetEventFlag(3820):
        """State 2,5"""
        # talk:10207700:"A wintry land beckons you."
        # talk:10207701:"Would you lend me your strength, once more?"
        assert t180401000_x31(text1=10207700, flag1=1189027, mode7=1)
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0

def t180401000_x73():
    """State 0"""
    if GetEventFlag(3821):
        """State 1"""
        pass
    elif GetEventFlag(3822):
        """State 4"""
        pass
    else:
        """State 10"""
        return 1
    """State 6"""
    SetEventFlag(10003411, FlagState.On)
    """State 7"""
    # talk:10202900:"I knew you'd soon return..."
    # talk:10202901:"I can feel the warmth of its radiance."
    # talk:10202902:"Please...this time it has to work..."
    assert t180401000_x31(text1=10202900, flag1=1189028, mode7=1)
    """State 8"""
    assert t180401000_x36(z1=802, z2=3)
    """State 2"""
    c1_164()
    assert not f305()
    """State 3"""
    SetEventFlag(10003403, FlagState.On)
    """State 5"""
    def WhilePaused():
        c1_172(2, 2, 9, 9, 9, 9, 9, 9, 9)
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t180401000_x74():
    """State 0"""
    if GetEventFlag(3823):
        """State 1"""
        """State 2"""
        pass
    elif GetEventFlag(3824):
        """State 3,5"""
        Label('L0')
        # talk:10207900:"The Erdtree will live again. It shall be as you remember."
        assert t180401000_x31(text1=10207900, flag1=1189030, mode7=1)
    elif GetEventFlag(3825):
        """State 4"""
        Goto('L0')
    else:
        """State 7"""
        return 1
    """State 6"""
    return 0

def t180401000_x75():
    """State 0,4"""
    # talk:10203000:"We've reclaimed the light of Grace. We owe this to you."
    # talk:10203001:"Thank you. Truly."
    # talk:10203002:"But what's this wound...? Ah, from your memories..."
    # talk:10203003:"I vow, as Priestess,"
    # talk:10203004:"that the Erdtree will live again. It shall be as you remember."
    # talk:10203005:"So please. Do not lose sight of yourself."
    assert t180401000_x31(text1=10203000, flag1=1189029, mode7=1)
    """State 2"""
    SetEventFlag(10003404, FlagState.Off)
    """State 1"""
    UnlockGarb(104000)
    """State 3,5"""
    assert t180401000_x37()
    """State 6"""
    return 0

def t180401000_x76():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t180401000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000,
                             flag43=6000)
        if call.Done():
            break
        elif GetEventFlag(10003404):
            """State 2,4"""
            assert t180401000_x75()
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t180401000_x77():
    """State 0"""
    if not GetEventFlag(1189012):
        """State 1,3"""
        # talk:10206100:"You've returned."
        # talk:10206101:"Thank you for the flowers."
        # talk:10206102:"Would you mind taking them to the Iron Menial?"
        assert t180401000_x31(text1=10206100, flag1=1189012, mode7=1)
    elif GetEventFlag(1189012):
        """State 2,4"""
        # talk:10207400:"Would you mind taking them to the Iron Menial?"
        assert t180401000_x31(text1=10207400, flag1=1189013, mode7=1)
    """State 5"""
    return 0

