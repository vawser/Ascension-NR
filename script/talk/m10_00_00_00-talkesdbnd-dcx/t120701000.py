# -*- coding: utf-8 -*-
def t120701000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t120701000_x6(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1, mode3=1)
    Quit()

def t120701000_1000():
    """State 0,2,3"""
    assert t120701000_x54()
    """State 1"""
    EndMachine(1000)
    Quit()

def t120701000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t120701000_x0(actionbutton1=6000, flag36=6001, flag40=6000, flag41=6000, flag42=6000, flag43=6000,
            flag35=10003115))
    """State 1"""
    EndMachine(2000)
    Quit()

def t120701000_x0(actionbutton1=6000, flag36=6001, flag40=6000, flag41=6000, flag42=6000, flag43=6000, flag35=_):
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
        assert not GetEventFlag(flag35)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag35) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag36) and not GetEventFlag(flag40) and not GetEventFlag(flag41) and not GetEventFlag(flag42)
            and not GetEventFlag(flag43)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t120701000_x1():
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

def t120701000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t120701000_x3(z7=_):
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

def t120701000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t120701000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t120701000_x1()
    else:
        """State 4,7"""
        call = t120701000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t120701000_x1()
    """State 9"""
    return 0

def t120701000_x5():
    """State 0,1"""
    assert t120701000_x1()
    """State 2"""
    return 0

def t120701000_x6(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t120701000_x23(flag32=flag32, flag33=flag33, flag34=flag34, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag35=flag35, flag36=flag36, flag37=flag37,
                              flag38=flag38, flag39=flag39, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t120701000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t120701000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag35=6000, flag36=6001, flag37=6000,
                  flag38=6000, flag39=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t120701000_x10(actionbutton1=actionbutton1, flag35=flag35, flag36=flag36, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t120701000_x14(val1=val1, z3=z3)
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
            call = t120701000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t120701000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t120701000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t120701000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t120701000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t120701000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t120701000_x9(flag32=6000, val2=10, val3=12):
    """State 0,8"""
    assert t120701000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag32):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t120701000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t120701000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t120701000_x10(actionbutton1=6000, flag35=6000, flag36=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t120701000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t120701000_x0(actionbutton1=actionbutton1, flag36=flag36, flag40=6000, flag41=6000, flag42=6000,
                flag43=6000, flag35=flag35))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t120701000_x11(machine1=_, val6=_):
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

def t120701000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t120701000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t120701000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t120701000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t120701000_x13():
    """State 0,1"""
    assert t120701000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t120701000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t120701000_x24()
    """State 3"""
    call = t120701000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t120701000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t120701000_x15():
    """State 0,1"""
    assert t120701000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t120701000_x16(val5=12):
    """State 0,2"""
    call = t120701000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t120701000_x27()
    """State 4"""
    return 0

def t120701000_x17():
    """State 0,1"""
    assert t120701000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t120701000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t120701000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t120701000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t120701000_x29()
    """Unused"""
    """State 6"""
    return 0

def t120701000_x19():
    """State 0,2"""
    call = t120701000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t120701000_x20():
    """State 0,1"""
    assert t120701000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t120701000_x21():
    """State 0,1"""
    assert t120701000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t120701000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t120701000_x23(flag32=6000, flag33=6000, flag34=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag35=6000, flag36=6001, flag37=6000, flag38=6000, flag39=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t120701000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag35=flag35, flag36=flag36, flag37=flag37, flag38=flag38, flag39=flag39, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag32):
            """State 3"""
            Label('L0')
            call = t120701000_x9(flag32=flag32, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag32):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag33) or GetEventFlag(flag34):
            """State 2"""
            call = t120701000_x8(val2=val2, val3=val3)
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
        assert t120701000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t120701000_x24():
    """State 0,1"""
    assert t120701000_x25()
    """State 2"""
    return 0

def t120701000_x25():
    """State 0,1"""
    assert t120701000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t120701000_x26():
    """State 0,1"""
    call = t120701000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t120701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t120701000_x27():
    """State 0,1"""
    call = t120701000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t120701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t120701000_x28():
    """State 0,1"""
    call = t120701000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t120701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t120701000_x29():
    """State 0,1"""
    call = t120701000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t120701000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t120701000_x30(text2=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t120701000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t120701000_x31(text19=10505400, mode4=1):
    """State 0,4"""
    assert t120701000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:10505400:"What is it?"
    TalkToPlayer(text19, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t120701000_x32():
    """State 0,1"""
    assert t120701000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t120701000_x33():
    """State 0,1"""
    assert t120701000_x1()
    """State 2"""
    return 0

def t120701000_x34():
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

def t120701000_x35(z1=_, z2=_):
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

def t120701000_x36():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t120701000_x37(action4=21052003, action5=21052004):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21052003:"They achieved enlightenment"
    AddTalkListDataAlt(1, action4, -1, 0, False)
    # action:21052004:"They were attacked by brigands"
    AddTalkListDataAlt(2, action5, -1, 0, False)
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

def t120701000_x38(text17=10505800, flag30=-1, text18=10505900, flag31=-1):
    """State 0,4"""
    assert t120701000_x3(z7=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t120701000_x30(text2=text17, flag1=flag30, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t120701000_x30(text2=text18, flag1=flag31, mode5=1)
    """State 5"""
    return 0

def t120701000_x39(text17=10505800, flag28=1209307, text18=10505900, flag29=1209308):
    """State 0"""
    if not GetEventFlag(flag28):
        """State 1"""
        assert t120701000_x30(text2=text17, flag1=flag28, mode5=1)
    elif not GetEventFlag(flag29):
        """State 2"""
        assert t120701000_x30(text2=text18, flag1=flag29, mode5=1)
    else:
        """State 3"""
        assert t120701000_x38(text17=text17, flag30=-1, text18=text18, flag31=-1)
    """State 4"""
    return 0

def t120701000_x40(text14=_, flag25=_, text15=_, flag26=_, text16=_, flag27=_):
    """State 0"""
    if not GetEventFlag(flag25):
        """State 2"""
        Label('L0')
        assert t120701000_x30(text2=text14, flag1=flag25, mode5=1)
    elif not GetEventFlag(flag26):
        """State 3"""
        assert t120701000_x30(text2=text15, flag1=flag26, mode5=1)
    elif not GetEventFlag(flag27):
        """State 4"""
        assert t120701000_x30(text2=text16, flag1=flag27, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag25, FlagState.Off)
        SetEventFlag(flag26, FlagState.Off)
        SetEventFlag(flag27, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t120701000_x41(text9=10505800, flag15=1209307, text10=10505900, flag16=1209308, text11=10506000, flag17=1209309,
                   text12=10506100, flag18=1209310, text13=10506200, flag19=1209311):
    """State 0"""
    if not GetEventFlag(flag15):
        """State 1"""
        assert t120701000_x30(text2=text9, flag1=flag15, mode5=1)
    elif not GetEventFlag(flag16):
        """State 2"""
        assert t120701000_x30(text2=text10, flag1=flag16, mode5=1)
    elif not GetEventFlag(flag17):
        """State 3"""
        assert t120701000_x30(text2=text11, flag1=flag17, mode5=1)
    elif not GetEventFlag(flag18):
        """State 4"""
        assert t120701000_x30(text2=text12, flag1=flag18, mode5=1)
    elif not GetEventFlag(flag19):
        """State 5"""
        assert t120701000_x30(text2=text13, flag1=flag19, mode5=1)
    else:
        """State 6"""
        assert (t120701000_x42(text9=text9, flag20=-1, text10=text10, flag21=-1, text11=text11, flag22=-1, text12=text12,
                flag23=-1, text13=text13, flag24=-1))
    """State 7"""
    return 0

def t120701000_x42(text9=10505800, flag20=-1, text10=10505900, flag21=-1, text11=10506000, flag22=-1, text12=10506100,
                   flag23=-1, text13=10506200, flag24=-1):
    """State 0,5"""
    assert t120701000_x3(z7=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t120701000_x30(text2=text9, flag1=flag20, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t120701000_x30(text2=text10, flag1=flag21, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t120701000_x30(text2=text11, flag1=flag22, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t120701000_x30(text2=text12, flag1=flag23, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t120701000_x30(text2=text13, flag1=flag24, mode5=1)
    """State 8"""
    return 0

def t120701000_x43(text2=10505800, flag8=-1, text3=10505900, flag9=-1, text4=10506100, flag10=-1, text5=10506200,
                   flag11=-1, text6=10506300, flag12=-1, text7=10506400, flag13=-1, text8=10506500, flag14=-1):
    """State 0,5"""
    assert t120701000_x3(z7=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t120701000_x30(text2=text2, flag1=flag8, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t120701000_x30(text2=text3, flag1=flag9, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t120701000_x30(text2=text4, flag1=flag10, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t120701000_x30(text2=text5, flag1=flag11, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t120701000_x30(text2=text6, flag1=flag12, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t120701000_x30(text2=text7, flag1=flag13, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t120701000_x30(text2=text8, flag1=flag14, mode5=1)
    """State 10"""
    return 0

def t120701000_x44(text2=10505800, flag1=1209307, text3=10505900, flag2=1209308, text4=10506100, flag3=1209310,
                   text5=10506200, flag4=1209311, text6=10506300, flag5=1209312, text7=10506400, flag6=1209313,
                   text8=10506500, flag7=1209314):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t120701000_x30(text2=text2, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t120701000_x30(text2=text3, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t120701000_x30(text2=text4, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t120701000_x30(text2=text5, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t120701000_x30(text2=text6, flag1=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t120701000_x30(text2=text7, flag1=flag6, mode5=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t120701000_x30(text2=text8, flag1=flag7, mode5=1)
    else:
        """State 8"""
        assert (t120701000_x43(text2=text2, flag8=-1, text3=text3, flag9=-1, text4=text4, flag10=-1, text5=text5,
                flag11=-1, text6=text6, flag12=-1, text7=text7, flag13=-1, text8=text8, flag14=-1))
    """State 9"""
    return 0

def t120701000_x45(action3=21052005):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21052005:"Show the Ragged Doll"
    AddTalkListDataAlt(1, action3, -1, 0, False)
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

def t120701000_x46(action1=21052006, action2=21052007, text1=10501600):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21052006:"Punish her for her misdeed"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:21052007:"Forgive her misdeed"
    AddTalkListDataAlt(2, action2, -1, 0, False)
    """State 3"""
    # talk:10501600:"..."
    # talk:10501601:"I knew, one day, it would come to this..."
    # talk:10501602:"Now. Do as thou wilt with me."
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

def t120701000_x47():
    """State 0"""
    if DoesSelfHaveSpEffect(9690):
        """State 3,9"""
        Label('L0')
        # talk:10505400:"What is it?"
        assert t120701000_x30(text2=10505400, flag1=1209300, mode5=1)
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
            assert t120701000_x30(text2=10505600, flag1=1209302, mode5=1)
    elif DoesSelfHaveSpEffect(9692):
        """State 1"""
        if GetEventFlag(10002011) or GetEventFlag(10002012):
            """State 6"""
            Goto('L1')
        else:
            """State 10"""
            # talk:10505500:"Wishest thou to converse?"
            assert t120701000_x30(text2=10505500, flag1=1209301, mode5=1)
    else:
        Goto('L1')
    """State 12"""
    return 0
    """Unused"""
    """State 8"""
    # talk:10505400:"What is it?"
    # talk:10505500:"Wishest thou to converse?"
    # talk:10505600:"I fear I may succumb to sleep..."
    t120701000_x40(text14=10505400, flag25=1209301, text15=10505500, flag26=1209302, text16=10505600, flag27=1209303)
    Quit()

def t120701000_x48():
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

def t120701000_x49():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t120701000_x50():
    """State 0,1"""
    if GetTalkListEntryResult() == 98:
        """State 5,6"""
        assert t120701000_x52()
    elif GetTalkListEntryResult() == 99:
        """State 2,7"""
        Label('L0')
        # talk:10505100:"Till next we meet..."
        # talk:10505200:"I see."
        # talk:10505300:"Is our business concluded?"
        assert (t120701000_x40(text14=10505100, flag25=1209307, text15=10505200, flag26=1209308, text16=10505300,
                flag27=1209309))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t120701000_x51():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t120701000_x53()
    else:
        """State 2"""
        assert t120701000_x47()
        """State 4"""
        assert t120701000_x48()
        """State 5"""
        assert t120701000_x49()
        """State 3"""
        assert t120701000_x50()
    """State 7"""
    return 0

def t120701000_x52():
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
        assert (t120701000_x44(text2=10505800, flag1=1209307, text3=10505900, flag2=1209308, text4=10506100, flag3=1209310,
                text5=10506200, flag4=1209311, text6=10506300, flag5=1209312, text7=10506400, flag6=1209313, text8=10506500,
                flag7=1209314))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10505800:"We must put the night sky to rights, to see its beauty once more..."
        # talk:10505900:"I believe myself skilled...in my craft..."
        # talk:10506000:"Can the hound be taught a new trick, I wonder?"
        # talk:10506100:"There is much to be done..."
        # talk:10506200:"How it bustles here, now..."
        assert (t120701000_x41(text9=10505800, flag15=1209307, text10=10505900, flag16=1209308, text11=10506000,
                flag17=1209309, text12=10506100, flag18=1209310, text13=10506200, flag19=1209311))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10505800:"We must put the night sky to rights, to see its beauty once more..."
        # talk:10505900:"I believe myself skilled...in my craft..."
        assert t120701000_x39(text17=10505800, flag28=1209307, text18=10505900, flag29=1209308)
    """State 7"""
    return 0

def t120701000_x53():
    """State 0,1"""
    # talk:10505400:"What is it?"
    assert t120701000_x31(text19=10505400, mode4=1)
    """State 2"""
    return 0

def t120701000_x54():
    """State 0,1"""
    assert t120701000_x55()
    """State 2"""
    return 0

def t120701000_x55():
    """State 0"""
    if f302(-1) == 2:
        """State 4"""
        Label('L0')
        call = t120701000_x58()
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Get() == 1:
            """State 5"""
            call = t120701000_x59()
            def WhilePaused():
                RequestAnimation(90300, -1)
            if call.Get() == 1:
                """State 1"""
                Label('L1')
                """State 7"""
                def WhilePaused():
                    RequestAnimation(90300, -1)
                assert t120701000_x51()
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 3 or f302(-1) == 4 or f302(-1) == 5:
        """State 6"""
        call = t120701000_x60()
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Get() == 1:
            """State 8"""
            call = t120701000_x61()
            if call.Get() == 1:
                Goto('L1')
            elif call.Done():
                pass
        elif call.Done():
            pass
    else:
        Goto('L1')
    """State 9"""
    Label('L2')
    return 0
    """Unused"""
    """State 2"""
    call = t120701000_x56()
    def WhilePaused():
        RequestAnimation(90300, -1)
    if call.Get() == 1:
        Goto('L1')
    elif call.Done():
        Goto('L2')
    """State 3"""
    call = t120701000_x57()
    def WhilePaused():
        RequestAnimation(90300, -1)
    if call.Get() == 1:
        Goto('L0')
    elif call.Done():
        Goto('L2')

def t120701000_x56():
    """State 0,4,8"""
    return 1
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 2"""
    Goto('L0')
    """State 3,5"""
    Label('L0')
    # talk:10504100:"Have our mechanical menial aid thee in finding the answer."
    assert t120701000_x30(text2=10504100, flag1=1129022, mode5=1)
    Goto('L2')
    """State 6"""
    Label('L1')
    assert t120701000_x68()
    """State 7"""
    Label('L2')
    return 0

def t120701000_x57():
    """State 0,6"""
    return 1
    """Unused"""
    """State 1"""
    Goto('L0')
    """State 2"""
    Goto('L1')
    """State 3"""
    Label('L0')
    assert t120701000_x62()
    Goto('L2')
    """State 4"""
    Label('L1')
    # talk:10504200:"Protection alone will not grant salvation."
    # talk:10504201:"Thou wouldst do well to remember that..."
    assert t120701000_x30(text2=10504200, flag1=1129025, mode5=1)
    """State 5"""
    Label('L2')
    return 0

def t120701000_x58():
    """State 0"""
    if GetEventFlag(3206):
        """State 2,9"""
        Label('L0')
        if GetEventFlag(10003116):
            """State 13"""
            # talk:10504200:"Protection alone will not grant salvation."
            # talk:10504201:"Thou wouldst do well to remember that..."
            assert t120701000_x30(text2=10504200, flag1=1129025, mode5=1)
        elif not GetEventFlag(10003116):
            """State 14"""
            assert t120701000_x51()
    elif GetEventFlag(3207):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3208):
        """State 4"""
        Goto('L0')
    elif GetEventFlag(3209):
        """State 5"""
        Goto('L0')
    elif GetEventFlag(3210):
        """State 6,8"""
        Label('L1')
        """State 16"""
        return 1
    elif GetEventFlag(3211):
        """State 7"""
        if not GetEventFlag(1129026):
            """State 10"""
            # talk:10502700:"A tome...thou seekest?"
            # talk:10502701:"Then... Yes, seek thee a great being of stone..."
            assert t120701000_x30(text2=10502700, flag1=1129026, mode5=1)
        elif GetEventFlag(1129026):
            """State 12"""
            # talk:10504300:"Seek thee a great being of stone..."
            assert t120701000_x30(text2=10504300, flag1=1129027, mode5=1)
    else:
        Goto('L1')
    """State 15"""
    return 0
    """Unused"""
    """State 1"""
    Goto('L0')
    """State 11"""
    t120701000_x35(z1=202, z2=1)
    Quit()

def t120701000_x59():
    """State 0"""
    if GetEventFlag(3212):
        """State 1"""
        pass
    elif GetEventFlag(3213):
        """State 2"""
        pass
    elif GetEventFlag(3214):
        """State 3"""
        pass
    else:
        """State 6"""
        return 1
    """State 4"""
    assert t120701000_x63()
    """State 5"""
    return 0

def t120701000_x60():
    """State 0"""
    if GetEventFlag(3215):
        """State 1,12"""
        Label('L0')
        def WhilePaused():
            c1_172(2, 9, 0, 9, 9, 9, 9, 9, 9)
        assert t120701000_x69()
    elif GetEventFlag(3216):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3217):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3219):
        """State 4,9"""
        Label('L1')
        assert t120701000_x64()
    elif GetEventFlag(3220):
        """State 8"""
        Goto('L1')
    elif GetEventFlag(3221):
        """State 5,11"""
        assert t120701000_x51()
    elif GetEventFlag(3222):
        """State 6,10"""
        # talk:10503000:"A demon..."
        # talk:10503001:"Not a partner from whom one might expect fair dealings... I would wager..."
        assert t120701000_x30(text2=10503000, flag1=1129031, mode5=1)
    else:
        """State 7,14"""
        return 1
    """State 13"""
    return 0

def t120701000_x61():
    """State 0"""
    if GetEventFlag(3223):
        """State 1,10"""
        Label('L0')
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x51()
    elif GetEventFlag(3224):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3225):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3226):
        """State 4,11"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x65()
    elif GetEventFlag(3227):
        """State 5,12"""
        # talk:10504600:"I shall wait without. Till next we meet..."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x30(text2=10504600, flag1=1129033, mode5=1)
    elif GetEventFlag(3228):
        """State 6,13"""
        assert t120701000_x66()
    elif GetEventFlag(3229):
        """State 7,14"""
        Label('L1')
        # talk:10504700:"My thanks, good sir knight."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x30(text2=10504700, flag1=1129038, mode5=1)
    elif GetEventFlag(3230):
        """State 8"""
        Goto('L1')
    else:
        """State 9,16"""
        return 1
    """State 15"""
    return 0

def t120701000_x62():
    """State 0,4"""
    # talk:10502500:"Hast thou the answer?"
    assert t120701000_x30(text2=10502500, flag1=1129023, mode5=1)
    """State 5"""
    # action:21052005:"Show the Ragged Doll"
    call = t120701000_x45(action3=21052005)
    if call.Get() == 0:
        """State 6"""
        # talk:10502600:"Yes...the one who had this...was a very special person indeed..."
        # talk:10502601:"It was too late to save them...but abandoned they were not."
        # talk:10502602:"So, in the end, everybody rotted..."
        # talk:10502603:"My avian friend, thou sayest the thing most precious to thee is thy flock..."
        # talk:10502604:"But protection alone will not grant salvation."
        # talk:10502605:"Thou wouldst do well to remember that..."
        assert t120701000_x30(text2=10502600, flag1=1129024, mode5=1)
        """State 3,7"""
        assert t120701000_x35(z1=201, z2=3)
        """State 2"""
        SetEventFlag(10003116, FlagState.On)
    elif call.Get() == 1:
        """State 1"""
        pass
    """State 8"""
    return 0

def t120701000_x63():
    """State 0"""
    if not GetEventFlag(1129028):
        """State 1,3"""
        # talk:10502800:"Didst thou the key procure?"
        # talk:10502801:"I see. Very good."
        # talk:10502802:"Take it to our attendant, please..."
        assert t120701000_x30(text2=10502800, flag1=1129028, mode5=1)
    elif GetEventFlag(1129028):
        """State 2,4"""
        # talk:10504400:"Hand the key to our mechanical menial, please."
        assert t120701000_x30(text2=10504400, flag1=1129029, mode5=1)
    """State 5"""
    return 0

def t120701000_x64():
    """State 0"""
    if not GetEventFlag(10003107):
        """State 2,4"""
        def WhilePaused():
            c1_172(2, 9, 0, 9, 9, 9, 9, 9, 9)
        assert t120701000_x69()
    elif GetEventFlag(10003107):
        """State 1,3"""
        # talk:10504500:"If it had happened in the midst of battle...danger would have abounded."
        assert t120701000_x30(text2=10504500, flag1=1129030, mode5=1)
    """State 5"""
    return 0

def t120701000_x65():
    """State 0,7"""
    assert t120701000_x47()
    """State 3"""
    assert t120701000_x48()
    """State 1"""
    # action:21050010:"Are you the maker of the curse?"
    AddTalkListDataAlt(1, 21050010, -1, 1, False)
    """State 4"""
    assert t120701000_x49()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        assert t120701000_x67()
    else:
        """State 5"""
        assert t120701000_x50()
    """State 8"""
    return 0

def t120701000_x66():
    """State 0,12"""
    SetEventFlag(10003124, FlagState.On)
    """State 13"""
    # talk:10501600:"..."
    # talk:10501601:"I knew, one day, it would come to this..."
    # talk:10501602:"Now. Do as thou wilt with me."
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t120701000_x30(text2=10501600, flag1=1129034, mode5=1)
    """State 8"""
    SetEventFlag(10003112, FlagState.On)
    assert GetCurrentStateElapsedFrames() > 1
    """State 7"""
    assert not GetEventFlag(10003112)
    """State 18"""
    # action:21052006:"Punish her for her misdeed"
    # action:21052007:"Forgive her misdeed"
    # talk:10501600:"..."
    # talk:10501601:"I knew, one day, it would come to this..."
    # talk:10501602:"Now. Do as thou wilt with me."
    call = t120701000_x46(action1=21052006, action2=21052007, text1=10501600)
    if call.Get() == 0:
        """State 1,3"""
        SetEventFlag(10003110, FlagState.On)
        assert GetEventFlag(10003110) and GetCurrentStateElapsedTime() > 1.3
        """State 14"""
        # talk:10501800:"..."
        assert t120701000_x30(text2=10501800, flag1=1129035, mode5=1)
        """State 4"""
        assert not GetEventFlag(10003110)
        """State 15"""
        # talk:10501810:"What is thy purpose?"
        # talk:10501811:"..."
        # talk:10501812:"I see..."
        # talk:10501813:"I will do my utmost to make amends..."
        # talk:10501814:"My thanks, good sir knight."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x30(text2=10501810, flag1=1129036, mode5=1)
        """State 5"""
    elif call.Get() == 1:
        """State 2,9"""
        SetEventFlag(10003114, FlagState.On)
        assert GetEventFlag(10003114)
        """State 10"""
        assert not GetEventFlag(10003114)
        """State 16"""
        # talk:10501700:"But...why?"
        # talk:10501701:"The fault lieth with me, for thy people's..."
        # talk:10501702:"..."
        # talk:10501703:"I believe I understand..."
        # talk:10501704:"I will not forget this kindness."
        # talk:10501705:"My utmost thanks, good sir knight."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t120701000_x30(text2=10501700, flag1=1129037, mode5=1)
        """State 6"""
    """State 11"""
    SetEventFlag(1129040, FlagState.On)
    """State 17"""
    assert t120701000_x36()
    """State 19"""
    return 0

def t120701000_x67():
    """State 0,2"""
    SetEventFlag(10003120, FlagState.On)
    assert GetCurrentStateElapsedFrames() > 1 and GetRelativeAngleBetweenSelfAndPlayer() <= 10
    """State 3"""
    # talk:10501300:"..."
    # talk:10501301:"I see thou hast my role in thy plight deduced..."
    # talk:10501302:"Indeed, I am the one who tore thy kind from the sky..."
    # talk:10501303:"This is a crystallisation of that accursed magic."
    # talk:10501304:"I entrust it to thee."
    assert t120701000_x30(text2=10501300, flag1=1129032, mode5=1)
    """State 1"""
    assert not (CheckSpecificPersonMenuIsOpen(-1, 2) and not CheckSpecificPersonGenericDialogIsOpen(2))
    """State 4"""
    return 0

def t120701000_x68():
    """State 0,6"""
    assert t120701000_x47()
    """State 3"""
    assert t120701000_x48()
    """State 1"""
    # action:21050011:"Today's lesson, master"
    AddTalkListDataAlt(1, 21050011, -1, 1, False)
    """State 4"""
    assert t120701000_x49()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 7"""
        # talk:10502300:"Ah, time for thy lesson, is it?"
        # talk:10502301:"Then for today's subject..."
        # talk:10502302:"There was once a band of pilgrims."
        # talk:10502303:"They would wander from place to place, offering their prayers in search, ultimately, of happiness."
        # talk:10502304:"However, one day, the pilgrims seemingly up and vanished."
        # talk:10502305:"Now, what supposest thou to have occurred?"
        assert t120701000_x30(text2=10502300, flag1=-1, mode5=1)
        """State 8"""
        # action:21052003:"They achieved enlightenment"
        # action:21052004:"They were attacked by brigands"
        assert t120701000_x37(action4=21052003, action5=21052004)
        """State 9"""
        # talk:10502400:"Hah, I wish I could say that were the case."
        # talk:10502401:"But thou wouldst best be served by seeing for thyself."
        # talk:10502402:"Have our mechanical menial aid thee in finding the answer."
        assert t120701000_x30(text2=10502400, flag1=1129021, mode5=1)
    else:
        """State 5"""
        assert t120701000_x50()
    """State 10"""
    return 0

def t120701000_x69():
    """State 0,5"""
    # talk:10505410:"What is it?"
    assert t120701000_x30(text2=10505410, flag1=-1, mode5=1)
    """State 3"""
    assert t120701000_x48()
    """State 4"""
    call = t120701000_x49()
    if call.Done() and GetTalkListEntryResult() == 98:
        """State 1,6"""
        # talk:10505810:"We must put the night sky to rights, to see its beauty once more..."
        assert t120701000_x30(text2=10505810, flag1=-1, mode5=1)
    elif call.Done():
        """State 2,7"""
        # talk:10505110:"Till next we meet..."
        assert t120701000_x30(text2=10505110, flag1=-1, mode5=1)
    """State 8"""
    return 0

