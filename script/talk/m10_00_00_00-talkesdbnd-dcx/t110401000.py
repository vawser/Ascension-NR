# -*- coding: utf-8 -*-
def t110401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t110401000_x7(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode3=1, mode4=1, mode5=1)
    Quit()

def t110401000_1000():
    """State 0,2,3"""
    assert t110401000_x63()
    """State 1"""
    EndMachine(1000)
    Quit()

def t110401000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t110401000_x0(actionbutton1=6000, flag42=6001, flag47=6000, flag48=6000, flag49=6000, flag50=6000,
            flag41=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t110401000_x0(actionbutton1=6000, flag42=6001, flag47=6000, flag48=6000, flag49=6000, flag50=6000, flag41=6000):
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

def t110401000_x1():
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

def t110401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t110401000_x3(action3=21021000):
    """State 0,1"""
    # action:21021000:""Before returning the earring, there is something I would like\nto try—passing light through the pair when put together...""
    OpenGenericDialog(DialogBoxType.CenterBottom1, action3, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t110401000_x4(z7=_):
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

def t110401000_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t110401000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t110401000_x1()
    else:
        """State 4,7"""
        call = t110401000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t110401000_x1()
    """State 9"""
    return 0

def t110401000_x6():
    """State 0,1"""
    assert t110401000_x1()
    """State 2"""
    return 0

def t110401000_x7(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t110401000_x24(flag38=flag38, flag39=flag39, flag40=flag40, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag41=flag41, flag42=flag42, flag43=flag43,
                              flag44=flag44, flag45=flag45, z3=z3, z4=z4, z5=z5, z6=z6, mode3=mode3, mode4=mode4,
                              mode5=mode5)
        assert IsClientPlayer()
        """State 1"""
        call = t110401000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t110401000_x8(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag41=6000, flag42=6001, flag43=6000,
                  flag44=6000, flag45=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 2"""
        call = t110401000_x11(actionbutton1=actionbutton1, flag41=flag41, flag42=flag42, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode5 == 1, 1000000)
            call = t110401000_x15(val1=val1, z3=z3)
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
            call = t110401000_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t110401000_x28() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t110401000_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t110401000_x9(val2=10, val3=12):
    """State 0,1"""
    call = t110401000_x19(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t110401000_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t110401000_x10(flag38=6000, val2=10, val3=12):
    """State 0,8"""
    assert t110401000_x36()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag38):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t110401000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t110401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t110401000_x11(actionbutton1=6000, flag41=6000, flag42=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t110401000_x12(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t110401000_x0(actionbutton1=actionbutton1, flag42=flag42, flag47=6000, flag48=6000, flag49=6000,
                flag50=6000, flag41=flag41))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110401000_x12(machine1=_, val6=_):
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

def t110401000_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t110401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t110401000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t110401000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t110401000_x14():
    """State 0,1"""
    assert t110401000_x12(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t110401000_x15(val1=5, z3=1):
    """State 0,4"""
    assert t110401000_x25()
    """State 3"""
    call = t110401000_x16()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t110401000_x27()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t110401000_x16():
    """State 0,1"""
    assert t110401000_x12(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t110401000_x17(val5=12):
    """State 0,2"""
    call = t110401000_x18()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t110401000_x28()
    """State 4"""
    return 0

def t110401000_x18():
    """State 0,1"""
    assert t110401000_x12(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t110401000_x19(val2=10, val3=12):
    """State 0,5"""
    assert t110401000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t110401000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t110401000_x30()
    """Unused"""
    """State 6"""
    return 0

def t110401000_x20():
    """State 0,2"""
    call = t110401000_x12(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t110401000_x21():
    """State 0,1"""
    assert t110401000_x12(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t110401000_x22():
    """State 0,1"""
    assert t110401000_x12(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t110401000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t110401000_x24(flag38=6000, flag39=6000, flag40=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag41=6000, flag42=6001, flag43=6000, flag44=6000, flag45=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t110401000_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag41=flag41, flag42=flag42, flag43=flag43, flag44=flag44, flag45=flag45, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode3=mode3, mode4=mode4, mode5=mode5)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag38):
            """State 3"""
            Label('L0')
            call = t110401000_x10(flag38=flag38, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag38):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag39) or GetEventFlag(flag40):
            """State 2"""
            call = t110401000_x9(val2=val2, val3=val3)
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
        assert t110401000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t110401000_x25():
    """State 0,1"""
    assert t110401000_x26()
    """State 2"""
    return 0

def t110401000_x26():
    """State 0,1"""
    assert t110401000_x12(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t110401000_x27():
    """State 0,1"""
    call = t110401000_x12(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t110401000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110401000_x28():
    """State 0,1"""
    call = t110401000_x12(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t110401000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110401000_x29():
    """State 0,1"""
    call = t110401000_x12(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t110401000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110401000_x30():
    """State 0,1"""
    call = t110401000_x12(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t110401000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t110401000_x31(text22=10201600, flag46=1209180, mode8=1):
    """State 0,5"""
    assert t110401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t110401000_x32(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t110401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t110401000_x33(text21=_, mode6=1):
    """State 0,4"""
    assert t110401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
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

def t110401000_x34():
    """State 0,1"""
    assert t110401000_x12(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t110401000_x35():
    """State 0,1"""
    assert t110401000_x1()
    """State 2"""
    return 0

def t110401000_x36():
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

def t110401000_x37(z1=102, z2=3):
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

def t110401000_x38():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t110401000_x39(text18=_, flag35=-1, text19=_, flag36=-1, text20=_, flag37=-1):
    """State 0,5"""
    assert t110401000_x4(z7=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110401000_x32(text1=text18, flag1=flag35, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110401000_x32(text1=text19, flag1=flag36, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t110401000_x32(text1=text20, flag1=flag37, mode7=1)
    """State 6"""
    return 0

def t110401000_x40(action1=21022003, action2=21022004):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21022003:"Give it to her"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:21022004:"Keep it"
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

def t110401000_x41(text16=10209400, flag33=-1, text17=10209500, flag34=-1):
    """State 0,4"""
    assert t110401000_x4(z7=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110401000_x32(text1=text16, flag1=flag33, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110401000_x32(text1=text17, flag1=flag34, mode7=1)
    """State 5"""
    return 0

def t110401000_x42(text18=_, flag30=_, text19=_, flag31=_, text20=_, flag32=_):
    """State 0"""
    if not GetEventFlag(flag30):
        """State 1"""
        assert t110401000_x32(text1=text18, flag1=flag30, mode7=1)
    elif not GetEventFlag(flag31):
        """State 2"""
        assert t110401000_x32(text1=text19, flag1=flag31, mode7=1)
    elif not GetEventFlag(flag32):
        """State 3"""
        assert t110401000_x32(text1=text20, flag1=flag32, mode7=1)
    else:
        """State 4"""
        assert t110401000_x39(text18=text18, flag35=-1, text19=text19, flag36=-1, text20=text20, flag37=-1)
    """State 5"""
    return 0

def t110401000_x43(text16=10209400, flag28=1209162, text17=10209500, flag29=1209163):
    """State 0"""
    if not GetEventFlag(flag28):
        """State 1"""
        assert t110401000_x32(text1=text16, flag1=flag28, mode7=1)
    elif not GetEventFlag(flag29):
        """State 2"""
        assert t110401000_x32(text1=text17, flag1=flag29, mode7=1)
    else:
        """State 3"""
        assert t110401000_x41(text16=text16, flag33=-1, text17=text17, flag34=-1)
    """State 4"""
    return 0

def t110401000_x44(text13=_, flag25=_, text14=_, flag26=_, text15=_, flag27=_):
    """State 0"""
    if not GetEventFlag(flag25):
        """State 2"""
        Label('L0')
        assert t110401000_x32(text1=text13, flag1=flag25, mode7=1)
    elif not GetEventFlag(flag26):
        """State 3"""
        assert t110401000_x32(text1=text14, flag1=flag26, mode7=1)
    elif not GetEventFlag(flag27):
        """State 4"""
        assert t110401000_x32(text1=text15, flag1=flag27, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag25, FlagState.Off)
        SetEventFlag(flag26, FlagState.Off)
        SetEventFlag(flag27, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t110401000_x45(text8=10210700, flag15=1209171, text9=10210800, flag16=1209172, text10=10210900, flag17=1209173,
                   text11=10211000, flag18=1209174, text12=10211100, flag19=1209175):
    """State 0"""
    if not GetEventFlag(flag15):
        """State 1"""
        assert t110401000_x32(text1=text8, flag1=flag15, mode7=1)
    elif not GetEventFlag(flag16):
        """State 2"""
        assert t110401000_x32(text1=text9, flag1=flag16, mode7=1)
    elif not GetEventFlag(flag17):
        """State 3"""
        assert t110401000_x32(text1=text10, flag1=flag17, mode7=1)
    elif not GetEventFlag(flag18):
        """State 4"""
        assert t110401000_x32(text1=text11, flag1=flag18, mode7=1)
    elif not GetEventFlag(flag19):
        """State 5"""
        assert t110401000_x32(text1=text12, flag1=flag19, mode7=1)
    else:
        """State 6"""
        assert (t110401000_x46(text8=text8, flag20=-1, text9=text9, flag21=-1, text10=text10, flag22=-1, text11=text11,
                flag23=-1, text12=text12, flag24=-1))
    """State 7"""
    return 0

def t110401000_x46(text8=10210700, flag20=-1, text9=10210800, flag21=-1, text10=10210900, flag22=-1, text11=10211000,
                   flag23=-1, text12=10211100, flag24=-1):
    """State 0,5"""
    assert t110401000_x4(z7=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110401000_x32(text1=text8, flag1=flag20, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110401000_x32(text1=text9, flag1=flag21, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t110401000_x32(text1=text10, flag1=flag22, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t110401000_x32(text1=text11, flag1=flag23, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t110401000_x32(text1=text12, flag1=flag24, mode7=1)
    """State 8"""
    return 0

def t110401000_x47(text1=10210700, flag8=-1, text2=10210800, flag9=-1, text3=10211000, flag10=-1, text4=10211100,
                   flag11=-1, text5=10211200, flag12=-1, text6=10211300, flag13=-1, text7=10211400, flag14=-1):
    """State 0,5"""
    assert t110401000_x4(z7=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t110401000_x32(text1=text1, flag1=flag8, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t110401000_x32(text1=text2, flag1=flag9, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t110401000_x32(text1=text3, flag1=flag10, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t110401000_x32(text1=text4, flag1=flag11, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t110401000_x32(text1=text5, flag1=flag12, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t110401000_x32(text1=text6, flag1=flag13, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t110401000_x32(text1=text7, flag1=flag14, mode7=1)
    """State 10"""
    return 0

def t110401000_x48(text1=10210700, flag1=1209171, text2=10210800, flag2=1209172, text3=10211000, flag3=1209174,
                   text4=10211100, flag4=1209175, text5=10211200, flag5=1209176, text6=10211300, flag6=1209177,
                   text7=10211400, flag7=1209178):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t110401000_x32(text1=text1, flag1=flag1, mode7=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t110401000_x32(text1=text2, flag1=flag2, mode7=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t110401000_x32(text1=text3, flag1=flag3, mode7=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t110401000_x32(text1=text4, flag1=flag4, mode7=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t110401000_x32(text1=text5, flag1=flag5, mode7=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t110401000_x32(text1=text6, flag1=flag6, mode7=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t110401000_x32(text1=text7, flag1=flag7, mode7=1)
    else:
        """State 8"""
        assert (t110401000_x47(text1=text1, flag8=-1, text2=text2, flag9=-1, text3=text3, flag10=-1, text4=text4,
                flag11=-1, text5=text5, flag12=-1, text6=text6, flag13=-1, text7=text7, flag14=-1))
    """State 9"""
    return 0

def t110401000_x49():
    """State 0,1"""
    if not f308(4) == 20300:
        """State 3"""
        if DoesSelfHaveSpEffect(9675):
            """State 7,15"""
            # talk:10201700:"What is it? You can tell me."
            assert t110401000_x32(text1=10201700, flag1=1209153, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9676):
            """State 8,16"""
            # talk:10210400:"Do you need help with something?"
            assert t110401000_x32(text1=10210400, flag1=1209154, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9677):
            """State 9"""
            pass
        else:
            """State 10"""
            pass
        """State 17"""
        # talk:10210500:"You are always welcome."
        assert t110401000_x32(text1=10210500, flag1=1209155, mode7=1)
    elif f308(4) == 20300:
        """State 2"""
        if GetEventFlag(10002010):
            """State 4,12"""
            # talk:10209200:"Speak, as you wish."
            assert t110401000_x32(text1=10209200, flag1=1209151, mode7=1)
        elif GetEventFlag(10002011):
            """State 5,13"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            assert t110401000_x32(text1=10200200, flag1=1209150, mode7=1)
        elif GetEventFlag(10002012):
            """State 6,14"""
            # talk:10209200:"Speak, as you wish."
            assert t110401000_x32(text1=10209200, flag1=1209151, mode7=1)
        else:
            """State 11"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            # talk:10209200:"Speak, as you wish."
            # talk:10209300:"How can I help?"
            assert (t110401000_x44(text13=10200200, flag25=1209150, text14=10209200, flag26=1209151, text15=10209300,
                    flag27=1209152))
    """State 18"""
    Label('L0')
    return 0

def t110401000_x50(mode1=1):
    """State 0,1"""
    if GetTalkListEntryResult() == 1:
        """State 9,14"""
        assert t110401000_x55()
    elif GetTalkListEntryResult() == 98:
        """State 8,13"""
        assert t110401000_x54()
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
                assert (t110401000_x44(text13=10201800, flag25=1209159, text14=10210200, flag26=1209160, text15=10210300,
                        flag27=1209161))
            elif f308(4) == 20300:
                """State 5,16"""
                assert t110401000_x62()
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

def t110401000_x51(mode2=1):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 3"""
    assert t110401000_x60()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode2 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    return 0

def t110401000_x52():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t110401000_x59()
    else:
        """State 2"""
        assert t110401000_x49()
        """State 4"""
        assert t110401000_x51(mode2=1)
        """State 5"""
        assert t110401000_x53()
        """State 3"""
        assert t110401000_x50(mode1=1)
    """State 7"""
    return 0

def t110401000_x53():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t110401000_x54():
    """State 0"""
    if f308(4) == 20300:
        """State 1"""
        assert t110401000_x57()
    elif not f308(4) == 20300:
        """State 2"""
        assert t110401000_x58()
    """State 3"""
    return 0

def t110401000_x55():
    """State 0"""
    if not GetEventFlag(1209180):
        """State 1,3"""
        # talk:10201400:"Is that...?"
        # talk:10201401:"I'm sorry, but that's the timepiece I misplaced."
        # talk:10201402:"Could I trouble you to have it back?"
        assert t110401000_x32(text1=10201400, flag1=1209179, mode7=1)
        """State 4"""
        assert t110401000_x56()
    elif GetEventFlag(1209180):
        """State 2,5"""
        # talk:10205300:"Won't you please part with the pocketwatch?"
        assert t110401000_x32(text1=10205300, flag1=1209181, mode7=1)
        """State 6"""
        assert t110401000_x56()
    """State 7"""
    return 0

def t110401000_x56():
    """State 0,7"""
    # action:21022003:"Give it to her"
    # action:21022004:"Keep it"
    call = t110401000_x40(action1=21022003, action2=21022004)
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
        assert t110401000_x31(text22=10201600, flag46=1209180, mode8=1)
    """State 8"""
    return 0

def t110401000_x57():
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
        assert (t110401000_x42(text18=10209900, flag30=1209167, text19=10210000, flag31=1209168, text20=10210100,
                flag32=1209169))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10209800:"How are you finding the Roundtable?"
        # talk:10209801:"I pray that you will be met with some comfort here."
        assert t110401000_x32(text1=10209800, flag1=1209166, mode7=1)
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t110401000_x61()
    """State 7"""
    return 0

def t110401000_x58():
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
        assert (t110401000_x48(text1=10210700, flag1=1209171, text2=10210800, flag2=1209172, text3=10211000, flag3=1209174,
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
        assert (t110401000_x45(text8=10210700, flag15=1209171, text9=10210800, flag16=1209172, text10=10210900,
                flag17=1209173, text11=10211000, flag18=1209174, text12=10211100, flag19=1209175))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10210600:"What a dreadful creature..."
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        assert (t110401000_x42(text18=10210600, flag30=1209170, text19=10210700, flag31=1209171, text20=10210800,
                flag32=1209172))
    """State 7"""
    return 0

def t110401000_x59():
    """State 0,1"""
    # talk:10210400:"Do you need help with something?"
    assert t110401000_x33(text21=10210400, mode6=1)
    """State 2"""
    return 0

def t110401000_x60():
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

def t110401000_x61():
    """State 0,1"""
    if True:
        """State 2,4"""
        # talk:10209400:"Did you encounter the beast? That is our quarry."
        # talk:10209401:"...How did we allow so much time to slip by..."
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t110401000_x43(text16=10209400, flag28=1209162, text17=10209500, flag29=1209163)
    else:
        """State 3,5"""
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t110401000_x32(text1=10209500, flag1=1209163, mode7=1)
    """State 6"""
    return 0

def t110401000_x62():
    """State 0"""
    if GetEventFlag(10002010):
        """State 1,5"""
        # talk:10209000:"I await your return."
        assert t110401000_x32(text1=10209000, flag1=1209157, mode7=1)
    elif GetEventFlag(10002011):
        """State 2,6"""
        # talk:10200500:"Fortune favours the well-prepared."
        assert t110401000_x32(text1=10200500, flag1=1209156, mode7=1)
    elif GetEventFlag(10002012):
        """State 3,7"""
        # talk:10209100:"May you triumph in battle."
        assert t110401000_x32(text1=10209100, flag1=1209158, mode7=1)
    else:
        """State 4"""
        # talk:10200500:"Fortune favours the well-prepared."
        # talk:10209000:"I await your return."
        # talk:10209100:"May you triumph in battle."
        assert (t110401000_x44(text13=10200500, flag25=1209156, text14=10209000, flag26=1209157, text15=10209100,
                flag27=1209158))
    """State 8"""
    return 0

def t110401000_x63():
    """State 0,1"""
    assert t110401000_x64()
    """State 2"""
    return 0

def t110401000_x64():
    """State 0"""
    if f302(-1) == 2:
        """State 2"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110401000_x65()
    elif f302(-1) == 3:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110401000_x66()
    elif f302(-1) == 4:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110401000_x67()
    elif f302(-1) == 5:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110401000_x72()
    else:
        """State 1,5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t110401000_x52()
    """State 7"""
    return 0

def t110401000_x65():
    """State 0"""
    if GetEventFlag(3104):
        """State 3,7"""
        Label('L0')
        # action:21021000:""Before returning the earring, there is something I would like\nto try—passing light through the pair when put together...""
        assert t110401000_x3(action3=21021000)
    elif GetEventFlag(3105):
        """State 4"""
        Goto('L0')
    elif GetEventFlag(3106):
        """State 5"""
        assert t110401000_x68()
    elif GetEventFlag(3107):
        """State 1,6"""
        Label('L1')
        assert t110401000_x52()
    else:
        """State 2"""
        Goto('L1')
    """State 8"""
    return 0

def t110401000_x66():
    """State 0"""
    if GetEventFlag(3109):
        """State 4,7"""
        Label('L0')
        call = t110401000_x52()
        assert call.Done() or call.Done() or call.Done()
    elif GetEventFlag(3110):
        """State 2,6"""
        assert t110401000_x69()
    elif GetEventFlag(3111):
        """State 3,8"""
        # talk:10201100:"The Roundtable Hold and I are one and the same."
        # talk:10201101:"I am rooted to this place. My exit forbidden."
        # talk:10201102:"..."
        # talk:10201103:"I'm glad we're in this together. It could be worse."
        # talk:10201104:"We will win this war. I promise."
        assert t110401000_x32(text1=10201100, flag1=1119002, mode7=1)
    elif True:
        """State 5"""
        Goto('L0')
    elif GetEventFlag(3121):
        """State 1"""
        Goto('L0')
    """State 9"""
    return 0

def t110401000_x67():
    """State 0,3,6"""
    assert t110401000_x52()
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 2,4"""
    assert t110401000_x71()
    Goto('L0')
    """State 5"""
    Label('L1')
    assert t110401000_x70()
    Goto('L0')

def t110401000_x68():
    """State 0,7"""
    assert t110401000_x49()
    """State 8"""
    assert t110401000_x51(mode2=1)
    """State 3"""
    # action:21020011:"Give Mended Earring"
    AddTalkListDataAlt(1, 21020011, -1, 1, False)
    """State 9"""
    assert t110401000_x53()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 2,5"""
        # talk:10205200:"What's this? Ah, it must be repaired already."
        # talk:10205201:"That barely took any time at all. Thank you for fetching it."
        # talk:10205202:"This...is a thing of great value to me."
        # talk:10205203:"A compass that will lead me to someone dear."
        # talk:10205204:"I suppose you're thinking that earrings normally come in pairs..."
        # talk:10205205:"...Forgive me, I've likely talked your ear off."
        # talk:10205206:"We must prepare for the next battle."
        assert t110401000_x32(text1=10205200, flag1=1119000, mode7=1)
        """State 4,10"""
        assert t110401000_x38()
    else:
        """State 6"""
        assert t110401000_x50(mode1=1)
    """State 11"""
    return 0

def t110401000_x69():
    """State 0,6"""
    assert t110401000_x49()
    """State 7"""
    assert t110401000_x51(mode2=1)
    """State 4"""
    # action:21020007:"Are you trapped here?"
    AddTalkListDataAlt(1, 21020007, -1, 1, False)
    """State 8"""
    assert t110401000_x53()
    """State 3"""
    if GetTalkListEntryResult() == 1:
        """State 1,5"""
        # talk:10201000:"So our dear caretaker let the cat out the bag..."
        # talk:10201001:"It's true, I'm imprisoned by the Roundtable Hold."
        # talk:10201002:"Far from an architect of this scheme, I am merely another Condemned.\nYou may find it amusing, but it is the truth."
        # talk:10201003:"..."
        # talk:10201004:"Once we're done, it will be goodbye."
        assert t110401000_x32(text1=10201000, flag1=1119001, mode7=1)
    else:
        """State 9"""
        assert t110401000_x50(mode1=1)
        """State 2"""
    """State 10"""
    return 0

def t110401000_x70():
    """State 0,8"""
    assert t110401000_x49()
    """State 9"""
    assert t110401000_x51(mode2=1)
    """State 1"""
    # action:21020009:"Always comes to the rescue"
    AddTalkListDataAlt(1, 21020009, -1, 1, False)
    """State 10"""
    assert t110401000_x53()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 3,7"""
        SetEventFlag(10003057, FlagState.On)
        """State 12"""
        # talk:10201200:"What do you mean to say?"
        # talk:10201201:"You discovered that I was trapped, and..."
        # talk:10201202:"I'm sorry, but this is no fairy tale."
        # talk:10201203:"Then allow me to give you a token of my favour, gallant sir knight."
        assert t110401000_x33(text21=10201200, mode6=1)
        """State 4"""
        SetEventFlag(10003055, FlagState.On)
        assert GetEventFlag(10003056)
        """State 13"""
        # talk:10201300:"There we are."
        # talk:10201301:"...I will try to remain optimistic about my rescue."
        assert t110401000_x32(text1=10201300, flag1=1119003, mode7=1)
        """State 5,14"""
        assert t110401000_x37(z1=102, z2=3)
    else:
        """State 11"""
        assert t110401000_x50(mode1=1)
        """State 6"""
    """State 15"""
    return 0

def t110401000_x71():
    """State 0,1"""
    # talk:10207200:"I will try to remain optimistic about my rescue."
    assert t110401000_x32(text1=10207200, flag1=1119004, mode7=1)
    """State 2"""
    return 0

def t110401000_x72():
    """State 0"""
    if GetEventFlag(3120):
        """State 1"""
        pass
    else:
        """State 2"""
        pass
    """State 3"""
    call = t110401000_x52()
    assert call.Done() or call.Done()
    """State 4"""
    return 0

