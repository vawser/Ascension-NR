# -*- coding: utf-8 -*-
def t130401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t130401000_x6(flag41=6000, flag42=6000, flag43=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag44=6000, flag45=6001, flag46=6000, flag47=6000, flag48=6000, z4=1, z5=1000000, z6=1000000,
                  z7=1000000, mode5=1, mode6=1, mode7=1)
    Quit()

def t130401000_1000():
    """State 0,2,3"""
    assert t130401000_x63()
    """State 1"""
    EndMachine(1000)
    Quit()

def t130401000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t130401000_x0(actionbutton1=6000, flag45=6001, flag50=6000, flag51=6000, flag52=6000, flag53=6000,
            flag44=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t130401000_x0(actionbutton1=6000, flag45=6001, flag50=6000, flag51=6000, flag52=6000, flag53=6000, flag44=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag45) or GetEventFlag(flag50) or GetEventFlag(flag51) or GetEventFlag(flag52) or
                GetEventFlag(flag53))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag44)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag44) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag45) and not GetEventFlag(flag50) and not GetEventFlag(flag51) and not GetEventFlag(flag52)
            and not GetEventFlag(flag53)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t130401000_x1():
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

def t130401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t130401000_x3(z8=_):
    """State 0,2"""
    if not CompareRNGValue(CompareType.Equal, 0) != -1:
        """State 1,4"""
        ShuffleRNGSeed(z8)
    else:
        """State 3"""
        pass
    """State 5"""
    SetRNGSeed()
    """State 6"""
    return 0

def t130401000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t130401000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t130401000_x1()
    else:
        """State 4,7"""
        call = t130401000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t130401000_x1()
    """State 9"""
    return 0

def t130401000_x5():
    """State 0,1"""
    assert t130401000_x1()
    """State 2"""
    return 0

def t130401000_x6(flag41=6000, flag42=6000, flag43=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag44=6000, flag45=6001, flag46=6000, flag47=6000, flag48=6000, z4=1, z5=1000000, z6=1000000,
                  z7=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t130401000_x23(flag41=flag41, flag42=flag42, flag43=flag43, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag44=flag44, flag45=flag45, flag46=flag46,
                              flag47=flag47, flag48=flag48, z4=z4, z5=z5, z6=z6, z7=z7, mode5=mode5, mode6=mode6,
                              mode7=mode7)
        assert IsClientPlayer()
        """State 1"""
        call = t130401000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t130401000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag44=6000, flag45=6001, flag46=6000,
                  flag47=6000, flag48=6000, z4=1, z5=1000000, z6=1000000, z7=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    while True:
        """State 2"""
        call = t130401000_x10(actionbutton1=actionbutton1, flag44=flag44, flag45=flag45, z5=z5, z6=z6, z7=z7)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode7 == 1, 1000000)
            call = t130401000_x14(val1=val1, z4=z4)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                c5_172(mode5 == 1 and mode6 == 1, 1, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(mode5 == 1 and not mode6 == 1, 1, 9, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode5 == 1 and mode6 == 1, 9, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode5 == 1 and not mode6 == 1, 9, 9, 9, 9, 9, 9, 9, 9, 9)
            def ExitPause():
                ChangeCamera(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif IsAttackedBySomeone() and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag48):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag46) and not GetEventFlag(flag47) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t130401000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t130401000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t130401000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t130401000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t130401000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t130401000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t130401000_x9(flag41=6000, val2=10, val3=12):
    """State 0,8"""
    assert t130401000_x35()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag41):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t130401000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t130401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t130401000_x10(actionbutton1=6000, flag44=6000, flag45=6001, z5=1000000, z6=1000000, z7=1000000):
    """State 0,1"""
    call = t130401000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t130401000_x0(actionbutton1=actionbutton1, flag45=flag45, flag50=6000, flag51=6000, flag52=6000,
                flag53=6000, flag44=flag44))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130401000_x11(machine1=_, val6=_):
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

def t130401000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t130401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t130401000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t130401000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t130401000_x13():
    """State 0,1"""
    assert t130401000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t130401000_x14(val1=5, z4=1):
    """State 0,4"""
    assert t130401000_x24()
    """State 3"""
    call = t130401000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t130401000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t130401000_x15():
    """State 0,1"""
    assert t130401000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t130401000_x16(val5=12):
    """State 0,2"""
    call = t130401000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t130401000_x27()
    """State 4"""
    return 0

def t130401000_x17():
    """State 0,1"""
    assert t130401000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t130401000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t130401000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t130401000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t130401000_x29()
    """Unused"""
    """State 6"""
    return 0

def t130401000_x19():
    """State 0,2"""
    call = t130401000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t130401000_x20():
    """State 0,1"""
    assert t130401000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t130401000_x21():
    """State 0,1"""
    assert t130401000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t130401000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t130401000_x23(flag41=6000, flag42=6000, flag43=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag44=6000, flag45=6001, flag46=6000, flag47=6000, flag48=6000, z4=1, z5=1000000, z6=1000000,
                   z7=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t130401000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag44=flag44, flag45=flag45, flag46=flag46, flag47=flag47, flag48=flag48, z4=z4,
                             z5=z5, z6=z6, z7=z7, mode5=mode5, mode6=mode6, mode7=mode7)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag41):
            """State 3"""
            Label('L0')
            call = t130401000_x9(flag41=flag41, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag41):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag42) or GetEventFlag(flag43):
            """State 2"""
            call = t130401000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag41):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag42) and not GetEventFlag(flag43):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t130401000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t130401000_x24():
    """State 0,1"""
    assert t130401000_x25()
    """State 2"""
    return 0

def t130401000_x25():
    """State 0,1"""
    assert t130401000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t130401000_x26():
    """State 0,1"""
    call = t130401000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t130401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130401000_x27():
    """State 0,1"""
    call = t130401000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t130401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130401000_x28():
    """State 0,1"""
    call = t130401000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t130401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130401000_x29():
    """State 0,1"""
    call = t130401000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t130401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t130401000_x30(text25=10201600, flag49=1209180, mode10=1):
    """State 0,5"""
    assert t130401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag49, FlagState.On)
    """State 1"""
    # talk:10201600:"I see. How unfortunate."
    # talk:10201601:"I cannot force you, but I am patient."
    TalkToPlayer(text25, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode10 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t130401000_x31(text1=_, flag1=_, mode9=1):
    """State 0,5"""
    assert t130401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode9 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag1, FlagState.On)
    """State 6"""
    return 0

def t130401000_x32(text24=10210400, mode8=1):
    """State 0,4"""
    assert t130401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10210400:"Do you need help with something?"
    TalkToPlayer(text24, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode8 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t130401000_x33():
    """State 0,1"""
    assert t130401000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t130401000_x34():
    """State 0,1"""
    assert t130401000_x1()
    """State 2"""
    return 0

def t130401000_x35():
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

def t130401000_x36(z2=302, z3=_):
    """State 0,1"""
    c1_163(z2, z3)
    """State 2"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 3"""
    RequestSave(0)
    """State 9"""
    if f304(z2) == 1:
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

def t130401000_x37():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t130401000_x38(text21=_, flag38=-1, text22=_, flag39=-1, text23=_, flag40=-1):
    """State 0,5"""
    assert t130401000_x3(z8=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t130401000_x31(text1=text21, flag1=flag38, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t130401000_x31(text1=text22, flag1=flag39, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t130401000_x31(text1=text23, flag1=flag40, mode9=1)
    """State 6"""
    return 0

def t130401000_x39(action2=21022003, action3=21022004):
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

def t130401000_x40(text19=10209400, flag36=-1, text20=10209500, flag37=-1):
    """State 0,4"""
    assert t130401000_x3(z8=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t130401000_x31(text1=text19, flag1=flag36, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t130401000_x31(text1=text20, flag1=flag37, mode9=1)
    """State 5"""
    return 0

def t130401000_x41(text21=_, flag33=_, text22=_, flag34=_, text23=_, flag35=_):
    """State 0"""
    if not GetEventFlag(flag33):
        """State 1"""
        assert t130401000_x31(text1=text21, flag1=flag33, mode9=1)
    elif not GetEventFlag(flag34):
        """State 2"""
        assert t130401000_x31(text1=text22, flag1=flag34, mode9=1)
    elif not GetEventFlag(flag35):
        """State 3"""
        assert t130401000_x31(text1=text23, flag1=flag35, mode9=1)
    else:
        """State 4"""
        assert t130401000_x38(text21=text21, flag38=-1, text22=text22, flag39=-1, text23=text23, flag40=-1)
    """State 5"""
    return 0

def t130401000_x42(text19=10209400, flag31=1209162, text20=10209500, flag32=1209163):
    """State 0"""
    if not GetEventFlag(flag31):
        """State 1"""
        assert t130401000_x31(text1=text19, flag1=flag31, mode9=1)
    elif not GetEventFlag(flag32):
        """State 2"""
        assert t130401000_x31(text1=text20, flag1=flag32, mode9=1)
    else:
        """State 3"""
        assert t130401000_x40(text19=text19, flag36=-1, text20=text20, flag37=-1)
    """State 4"""
    return 0

def t130401000_x43(text16=_, flag28=_, text17=_, flag29=_, text18=_, flag30=_):
    """State 0"""
    if not GetEventFlag(flag28):
        """State 2"""
        Label('L0')
        assert t130401000_x31(text1=text16, flag1=flag28, mode9=1)
    elif not GetEventFlag(flag29):
        """State 3"""
        assert t130401000_x31(text1=text17, flag1=flag29, mode9=1)
    elif not GetEventFlag(flag30):
        """State 4"""
        assert t130401000_x31(text1=text18, flag1=flag30, mode9=1)
    else:
        """State 1"""
        SetEventFlag(flag28, FlagState.Off)
        SetEventFlag(flag29, FlagState.Off)
        SetEventFlag(flag30, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t130401000_x44(text11=10210700, flag18=1209171, text12=10210800, flag19=1209172, text13=10210900, flag20=1209173,
                   text14=10211000, flag21=1209174, text15=10211100, flag22=1209175):
    """State 0"""
    if not GetEventFlag(flag18):
        """State 1"""
        assert t130401000_x31(text1=text11, flag1=flag18, mode9=1)
    elif not GetEventFlag(flag19):
        """State 2"""
        assert t130401000_x31(text1=text12, flag1=flag19, mode9=1)
    elif not GetEventFlag(flag20):
        """State 3"""
        assert t130401000_x31(text1=text13, flag1=flag20, mode9=1)
    elif not GetEventFlag(flag21):
        """State 4"""
        assert t130401000_x31(text1=text14, flag1=flag21, mode9=1)
    elif not GetEventFlag(flag22):
        """State 5"""
        assert t130401000_x31(text1=text15, flag1=flag22, mode9=1)
    else:
        """State 6"""
        assert (t130401000_x45(text11=text11, flag23=-1, text12=text12, flag24=-1, text13=text13, flag25=-1, text14=text14,
                flag26=-1, text15=text15, flag27=-1))
    """State 7"""
    return 0

def t130401000_x45(text11=10210700, flag23=-1, text12=10210800, flag24=-1, text13=10210900, flag25=-1, text14=10211000,
                   flag26=-1, text15=10211100, flag27=-1):
    """State 0,5"""
    assert t130401000_x3(z8=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t130401000_x31(text1=text11, flag1=flag23, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t130401000_x31(text1=text12, flag1=flag24, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t130401000_x31(text1=text13, flag1=flag25, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t130401000_x31(text1=text14, flag1=flag26, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t130401000_x31(text1=text15, flag1=flag27, mode9=1)
    """State 8"""
    return 0

def t130401000_x46(text4=10210700, flag11=-1, text5=10210800, flag12=-1, text6=10211000, flag13=-1, text7=10211100,
                   flag14=-1, text8=10211200, flag15=-1, text9=10211300, flag16=-1, text10=10211400, flag17=-1):
    """State 0,5"""
    assert t130401000_x3(z8=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t130401000_x31(text1=text4, flag1=flag11, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t130401000_x31(text1=text5, flag1=flag12, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t130401000_x31(text1=text6, flag1=flag13, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t130401000_x31(text1=text7, flag1=flag14, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t130401000_x31(text1=text8, flag1=flag15, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t130401000_x31(text1=text9, flag1=flag16, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t130401000_x31(text1=text10, flag1=flag17, mode9=1)
    """State 10"""
    return 0

def t130401000_x47(text4=10210700, flag4=1209171, text5=10210800, flag5=1209172, text6=10211000, flag6=1209174,
                   text7=10211100, flag7=1209175, text8=10211200, flag8=1209176, text9=10211300, flag9=1209177,
                   text10=10211400, flag10=1209178):
    """State 0"""
    if not GetEventFlag(flag4):
        """State 1"""
        assert t130401000_x31(text1=text4, flag1=flag4, mode9=1)
    elif not GetEventFlag(flag5):
        """State 2"""
        assert t130401000_x31(text1=text5, flag1=flag5, mode9=1)
    elif not GetEventFlag(flag6):
        """State 3"""
        assert t130401000_x31(text1=text6, flag1=flag6, mode9=1)
    elif not GetEventFlag(flag7):
        """State 4"""
        assert t130401000_x31(text1=text7, flag1=flag7, mode9=1)
    elif not GetEventFlag(flag8):
        """State 5"""
        assert t130401000_x31(text1=text8, flag1=flag8, mode9=1)
    elif not GetEventFlag(flag9):
        """State 6"""
        assert t130401000_x31(text1=text9, flag1=flag9, mode9=1)
    elif not GetEventFlag(flag10):
        """State 7"""
        assert t130401000_x31(text1=text10, flag1=flag10, mode9=1)
    else:
        """State 8"""
        assert (t130401000_x46(text4=text4, flag11=-1, text5=text5, flag12=-1, text6=text6, flag13=-1, text7=text7,
                flag14=-1, text8=text8, flag15=-1, text9=text9, flag16=-1, text10=text10, flag17=-1))
    """State 9"""
    return 0

def t130401000_x48(action1=_):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
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

def t130401000_x49():
    """State 0,1"""
    if not f308(4) == 20300:
        """State 3"""
        if DoesSelfHaveSpEffect(9675):
            """State 7,15"""
            # talk:10201700:"What is it? You can tell me."
            assert t130401000_x31(text1=10201700, flag1=1209153, mode9=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9676):
            """State 8,16"""
            # talk:10210400:"Do you need help with something?"
            assert t130401000_x31(text1=10210400, flag1=1209154, mode9=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9677):
            """State 9"""
            pass
        else:
            """State 10"""
            pass
        """State 17"""
        # talk:10210500:"You are always welcome."
        assert t130401000_x31(text1=10210500, flag1=1209155, mode9=1)
    elif f308(4) == 20300:
        """State 2"""
        if GetEventFlag(10002010):
            """State 4,12"""
            # talk:10209200:"Speak, as you wish."
            assert t130401000_x31(text1=10209200, flag1=1209151, mode9=1)
        elif GetEventFlag(10002011):
            """State 5,13"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            assert t130401000_x31(text1=10200200, flag1=1209150, mode9=1)
        elif GetEventFlag(10002012):
            """State 6,14"""
            # talk:10209200:"Speak, as you wish."
            assert t130401000_x31(text1=10209200, flag1=1209151, mode9=1)
        else:
            """State 11"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            # talk:10209200:"Speak, as you wish."
            # talk:10209300:"How can I help?"
            assert (t130401000_x43(text16=10200200, flag28=1209150, text17=10209200, flag29=1209151, text18=10209300,
                    flag30=1209152))
    """State 18"""
    Label('L0')
    return 0

def t130401000_x50(mode3=1):
    """State 0,1"""
    if GetTalkListEntryResult() == 1:
        """State 9,14"""
        assert t130401000_x55()
    elif GetTalkListEntryResult() == 98:
        """State 8,13"""
        assert t130401000_x54()
    elif GetTalkListEntryResult() == 99:
        """State 2,10"""
        Label('L0')
        if mode3 == 1:
            """State 11,4"""
            if not f308(4) == 20300:
                """State 6,15"""
                # talk:10201800:"Make sure you're ready."
                # talk:10210200:"Yes. Good bye."
                # talk:10210300:"May fortune visit you."
                assert (t130401000_x43(text16=10201800, flag28=1209159, text17=10210200, flag29=1209160, text18=10210300,
                        flag30=1209161))
            elif f308(4) == 20300:
                """State 5,16"""
                assert t130401000_x62()
        elif not mode3 == 1:
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

def t130401000_x51(mode4=1):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 3"""
    assert t130401000_x60()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode4 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    return 0

def t130401000_x52():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t130401000_x59()
    else:
        """State 2"""
        assert t130401000_x49()
        """State 4"""
        assert t130401000_x51(mode4=1)
        """State 5"""
        assert t130401000_x53()
        """State 3"""
        assert t130401000_x50(mode3=1)
    """State 7"""
    return 0

def t130401000_x53():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t130401000_x54():
    """State 0"""
    if f308(4) == 20300:
        """State 1"""
        assert t130401000_x57()
    elif not f308(4) == 20300:
        """State 2"""
        assert t130401000_x58()
    """State 3"""
    return 0

def t130401000_x55():
    """State 0"""
    if not GetEventFlag(1209180):
        """State 1,3"""
        # talk:10201400:"Is that...?"
        # talk:10201401:"I'm sorry, but that's the timepiece I misplaced."
        # talk:10201402:"Could I trouble you to have it back?"
        assert t130401000_x31(text1=10201400, flag1=1209179, mode9=1)
        """State 4"""
        assert t130401000_x56()
    elif GetEventFlag(1209180):
        """State 2,5"""
        # talk:10205300:"Won't you please part with the pocketwatch?"
        assert t130401000_x31(text1=10205300, flag1=1209181, mode9=1)
        """State 6"""
        assert t130401000_x56()
    """State 7"""
    return 0

def t130401000_x56():
    """State 0,7"""
    # action:21022003:"Give it to her"
    # action:21022004:"Keep it"
    call = t130401000_x39(action2=21022003, action3=21022004)
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
        assert t130401000_x30(text25=10201600, flag49=1209180, mode10=1)
    """State 8"""
    return 0

def t130401000_x57():
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
        assert (t130401000_x41(text21=10209900, flag33=1209167, text22=10210000, flag34=1209168, text23=10210100,
                flag35=1209169))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10209800:"How are you finding the Roundtable?"
        # talk:10209801:"I pray that you will be met with some comfort here."
        assert t130401000_x31(text1=10209800, flag1=1209166, mode9=1)
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t130401000_x61()
    """State 7"""
    return 0

def t130401000_x58():
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
        assert (t130401000_x47(text4=10210700, flag4=1209171, text5=10210800, flag5=1209172, text6=10211000, flag6=1209174,
                text7=10211100, flag7=1209175, text8=10211200, flag8=1209176, text9=10211300, flag9=1209177, text10=10211400,
                flag10=1209178))
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
        assert (t130401000_x44(text11=10210700, flag18=1209171, text12=10210800, flag19=1209172, text13=10210900,
                flag20=1209173, text14=10211000, flag21=1209174, text15=10211100, flag22=1209175))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10210600:"What a dreadful creature..."
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        assert (t130401000_x41(text21=10210600, flag33=1209170, text22=10210700, flag34=1209171, text23=10210800,
                flag35=1209172))
    """State 7"""
    return 0

def t130401000_x59():
    """State 0,1"""
    # talk:10210400:"Do you need help with something?"
    assert t130401000_x32(text24=10210400, mode8=1)
    """State 2"""
    return 0

def t130401000_x60():
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

def t130401000_x61():
    """State 0,1"""
    if True:
        """State 2,4"""
        # talk:10209400:"Did you encounter the beast? That is our quarry."
        # talk:10209401:"...How did we allow so much time to slip by..."
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t130401000_x42(text19=10209400, flag31=1209162, text20=10209500, flag32=1209163)
    else:
        """State 3,5"""
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t130401000_x31(text1=10209500, flag1=1209163, mode9=1)
    """State 6"""
    return 0

def t130401000_x62():
    """State 0"""
    if GetEventFlag(10002010):
        """State 1,5"""
        # talk:10209000:"I await your return."
        assert t130401000_x31(text1=10209000, flag1=1209157, mode9=1)
    elif GetEventFlag(10002011):
        """State 2,6"""
        # talk:10200500:"Fortune favours the well-prepared."
        assert t130401000_x31(text1=10200500, flag1=1209156, mode9=1)
    elif GetEventFlag(10002012):
        """State 3,7"""
        # talk:10209100:"May you triumph in battle."
        assert t130401000_x31(text1=10209100, flag1=1209158, mode9=1)
    else:
        """State 4"""
        # talk:10200500:"Fortune favours the well-prepared."
        # talk:10209000:"I await your return."
        # talk:10209100:"May you triumph in battle."
        assert (t130401000_x43(text16=10200500, flag28=1209156, text17=10209000, flag29=1209157, text18=10209100,
                flag30=1209158))
    """State 8"""
    return 0

def t130401000_x63():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t130401000_x64()
    """State 2"""
    return 0

def t130401000_x64():
    """State 0"""
    if f302(-1) == 1:
        """State 7"""
        call = t130401000_x77()
        if call.Get() == 0:
            """State 3"""
            call = t130401000_x65()
            if call.Get() == 1:
                """State 2"""
                Label('L0')
                """State 6"""
                Label('L1')
                assert t130401000_x52()
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 2:
        """State 4"""
        call = t130401000_x66()
        if call.Get() == 1:
            """State 5"""
            call = t130401000_x67()
            if call.Get() == 1:
                Goto('L0')
            elif call.Done():
                pass
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L1')
    """State 8"""
    return 0

def t130401000_x65():
    """State 0"""
    if GetEventFlag(3309):
        """State 1,4"""
        # talk:10204400:"I commend your efforts."
        # talk:10204401:"Please, accept this token of thanks."
        # talk:10204410:"Now then, have you any news to report?"
        assert t130401000_x68(text2=10204400, flag2=1139017, text3=10204410, flag3=1139018, z1=350, mode2=1)
        """State 5"""
        # action:21022001:"Show her the Traitor's Letter"
        assert t130401000_x48(action1=21022001)
        """State 6"""
        # talk:10205700:"I didn't think he would make the first move..."
        # talk:10205701:"We should bide our time for now."
        assert t130401000_x31(text1=10205700, flag1=1139019, mode9=1)
        """State 3,7"""
        assert t130401000_x36(z2=302, z3=3)
    elif GetEventFlag(3310):
        """State 2,8"""
        # talk:10205700:"I didn't think he would make the first move..."
        # talk:10205701:"We should bide our time for now."
        assert t130401000_x31(text1=10205700, flag1=1139019, mode9=1)
    else:
        """State 10"""
        return 1
    """State 9"""
    return 0

def t130401000_x66():
    """State 0"""
    if GetEventFlag(3311):
        """State 1,3"""
        # talk:10205800:"This man has been expecting you."
        # talk:10205801:"It's time you spoke."
        assert t130401000_x31(text1=10205800, flag1=1139020, mode9=1)
    elif GetEventFlag(3312):
        """State 2"""
        if GetEventFlag(1139021):
            """State 4"""
            assert t130401000_x76()
        else:
            """State 5"""
            # talk:10205900:"An Edge of Order..."
            # talk:10205901:"I know how you might find one."
            # talk:10205902:"The beings known as Night Centaurs spill over with sacred power."
            # talk:10205903:"Your search should begin with them."
            assert t130401000_x31(text1=10205900, flag1=1139021, mode9=1)
    else:
        """State 7"""
        return 1
    """State 6"""
    return 0

def t130401000_x67():
    """State 0"""
    if GetEventFlag(3313):
        """State 1,7"""
        # talk:10211700:"..."
        assert t130401000_x31(text1=10211700, flag1=1139024, mode9=1)
    elif GetEventFlag(3314):
        """State 2,4"""
        # talk:10206000:"I am surprised to learn the truth of your natures."
        # talk:10206001:"However, we strive for the same purpose. I need nothing more."
        # talk:10206002:"The sad thing is...I think in other circumstances, he might have joined us here."
        # talk:10206003:"...But in the end, he chose to be a monster."
        assert t130401000_x31(text1=10206000, flag1=1139022, mode9=1)
    elif GetEventFlag(3315):
        """State 3"""
        if not GetEventFlag(1139023):
            """State 5"""
            # talk:10208300:"Allow me to tender my thanks again."
            # talk:10208301:"An invaluable gift. Thank you."
            assert t130401000_x31(text1=10208300, flag1=1139023, mode9=1)
        else:
            """State 6"""
            # talk:10208300:"Allow me to tender my thanks again."
            # talk:10208301:"An invaluable gift. Thank you."
            assert t130401000_x31(text1=10208300, flag1=1139023, mode9=1)
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0

def t130401000_x68(text2=10204400, flag2=1139017, text3=10204410, flag3=1139018, z1=350, mode2=1):
    """State 0"""
    if not GetEventFlag(flag2):
        """State 2"""
        assert t130401000_x31(text1=text2, flag1=flag2, mode9=1)
        """State 1"""
        AddMurk(z1)
        """State 4"""
        assert t130401000_x37() and GetCurrentStateElapsedTime() > mode2
    elif GetEventFlag(flag2):
        pass
    """State 3"""
    assert t130401000_x31(text1=text3, flag1=flag3, mode9=1)
    """State 5"""
    return 0

def t130401000_x69():
    """State 0,1"""
    # action:21020015:"Accept task"
    AddTalkListDataAlt(2, 21020015, -1, 2, False)
    """State 2"""
    return 0

def t130401000_x70():
    """State 0,1"""
    # action:21020016:"About the Fellowship"
    AddTalkListDataAlt(4, 21020016, -1, 4, False)
    """State 2"""
    return 0

def t130401000_x71():
    """State 0,1"""
    # action:21020017:"About the traitor"
    AddTalkListDataAlt(5, 21020017, -1, 5, False)
    """State 2"""
    return 0

def t130401000_x72():
    """State 0,1"""
    # talk:10205400:""The Fellowship." That's the name of the mercenary outfit you belong to, is it not?"
    # talk:10205401:"You travel around the world, settling conflicts through clandestine acts."
    # talk:10205402:"Masters of assassination."
    # talk:10205403:"As unsettling as your talents might seem to an outsider, in service to our cause they are reassuring indeed."
    assert t130401000_x31(text1=10205400, flag1=1139005, mode9=1)
    """State 2"""
    return 0

def t130401000_x73():
    """State 0,1"""
    # talk:10205500:"The traitor you're after."
    # talk:10205501:"It seems I too am involved in all of this."
    # talk:10205502:"One of those summoned to the Roundtable is said to have abandoned their duties."
    # talk:10205503:"Or so the voice has intimated."
    # talk:10205504:"I was thinking of telling the others, but then, you arrived."
    # talk:10205505:"As if you had appeared to help me pursue the matter..."
    # talk:10205506:"The traitors of the Roundtable and the Fellowship appear to be one and the same."
    # talk:10205507:"Let's you and I get to the bottom of this."
    assert t130401000_x31(text1=10205500, flag1=1139006, mode9=1)
    """State 2"""
    return 0

def t130401000_x74(mode1=0):
    """State 0,4"""
    # talk:10205600:"The one who crafted the arrowhead was...the Monster?"
    # talk:10205601:"A student of your order who became obsessed with killing..."
    # talk:10205602:"So that's where it came from."
    # talk:10205603:"An excellent avenue to investigate. My thanks."
    assert t130401000_x31(text1=10205600, flag1=1139010, mode9=1)
    """State 1"""
    if mode1 == 1:
        """State 2"""
        UnlockGarb(106000)
        """State 3"""
        SetEventFlag(10003156, FlagState.On)
        """State 5"""
        assert t130401000_x37()
    else:
        pass
    """State 6"""
    return 0

def t130401000_x75():
    """State 0,3"""
    # talk:10203200:"Then you're good and ready?"
    assert t130401000_x31(text1=10203200, flag1=1139014, mode9=1)
    """State 4"""
    assert t130401000_x51(mode4=1)
    """State 16"""
    assert t130401000_x69()
    """State 12"""
    assert t130401000_x70()
    """State 13"""
    assert t130401000_x71()
    """State 5"""
    assert t130401000_x53()
    """State 1"""
    if GetTalkListEntryResult() == 2:
        """State 2,6"""
        # talk:10204300:"I need you to eliminate a band of Condemned."
        # talk:10204301:"These Condemned valiantly faced down the Night, but ultimately failed and surrendered to the darkness."
        # talk:10204302:"They are, in fact, us."
        # talk:10204303:"Worse still, they multiply through their marriage to the Night, spreading from one world to the next."
        # talk:10204304:"We must stop them before it's too late."
        assert t130401000_x31(text1=10204300, flag1=1139015, mode9=1)
        """State 15"""
        # action:21020028:""Us"?"
        assert t130401000_x48(action1=21020028)
        """State 14"""
        # talk:10204310:"Ahh, yes."
        # talk:10204311:"As you may have surmised, versions of you from other worlds are found among their number."
        # talk:10204312:"And we might just learn something from them."
        # talk:10204313:"Best of luck."
        assert t130401000_x31(text1=10204310, flag1=1139025, mode9=1)
        """State 7"""
        assert t130401000_x36(z2=302, z3=1)
    elif GetTalkListEntryResult() == 4:
        """State 9"""
        assert t130401000_x72()
    elif GetTalkListEntryResult() == 5:
        """State 10"""
        assert t130401000_x73()
    elif GetTalkListEntryResult() == 6:
        """State 11"""
        assert t130401000_x74(mode1=0)
    else:
        """State 8"""
        assert t130401000_x50(mode3=1)
    """State 17"""
    return 0

def t130401000_x76():
    """State 0,4"""
    assert t130401000_x49()
    """State 5"""
    assert t130401000_x51(mode4=1)
    """State 1"""
    # action:21020021:"About an Edge of Order"
    AddTalkListDataAlt(2, 21020021, -1, 2, False)
    """State 6"""
    assert t130401000_x53()
    """State 3"""
    if GetTalkListEntryResult() == 2:
        """State 2,7"""
        # talk:10205900:"An Edge of Order..."
        # talk:10205901:"I know how you might find one."
        # talk:10205902:"The beings known as Night Centaurs spill over with sacred power."
        # talk:10205903:"Your search should begin with them."
        assert t130401000_x31(text1=10205900, flag1=1139021, mode9=1)
    else:
        """State 8"""
        assert t130401000_x50(mode3=1)
    """State 9"""
    return 0

def t130401000_x77():
    """State 0"""
    if GetEventFlag(3305):
        """State 3,5"""
        # talk:10204100:"Oh, there you are."
        # talk:10204101:"Now. About the traitor from your Fellowship."
        # talk:10204102:"Let us talk."
        assert t130401000_x31(text1=10204100, flag1=1139013, mode9=1)
    elif GetEventFlag(3306):
        """State 4,6"""
        # talk:10203200:"Then you're good and ready?"
        assert t130401000_x78(text1=10203200, flag1=1139014)
    elif GetEventFlag(3307):
        """State 1,7"""
        assert t130401000_x75()
    elif GetEventFlag(3308):
        """State 2,8"""
        # talk:10208200:"The Condemned who have fallen to the Night deserve death. There is no doubt."
        assert t130401000_x78(text1=10208200, flag1=1139016)
    else:
        """State 9"""
        return 0
    """State 10"""
    return 1

def t130401000_x78(text1=_, flag1=_):
    """State 0,2"""
    assert t130401000_x31(text1=text1, flag1=flag1, mode9=1)
    """State 3"""
    assert t130401000_x51(mode4=1)
    """State 8"""
    assert t130401000_x70()
    """State 9"""
    assert t130401000_x71()
    """State 4"""
    assert t130401000_x53()
    """State 1"""
    if GetTalkListEntryResult() == 4:
        """State 5"""
        assert t130401000_x72()
    elif GetTalkListEntryResult() == 5:
        """State 6"""
        assert t130401000_x73()
    else:
        """State 7"""
        assert t130401000_x50(mode3=1)
    """State 10"""
    return 0

