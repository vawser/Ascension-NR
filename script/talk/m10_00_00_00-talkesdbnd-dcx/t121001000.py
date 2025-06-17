# -*- coding: utf-8 -*-
def t121001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t121001000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=50, val5=55, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode5=1, mode6=1, mode7=1)
    Quit()

def t121001000_1000():
    """State 0,2,4"""
    def WhilePaused():
        RequestAnimation(20026, -1)
    assert t121001000_x58()
    """State 1"""
    Label('L0')
    EndMachine(1000)
    Quit()
    """Unused"""
    """State 3"""
    Label('L1')
    Goto('L0')
    """State 5"""
    def WhilePaused():
        RequestAnimation(20026, -1)
    assert t121001000_x53() == 1
    Goto('L1')

def t121001000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t121001000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000, flag43=6000)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif f302(-1) == 3:
        """State 4"""
        t121001000_x70()
        Quit()

def t121001000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000, flag43=6000):
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

def t121001000_x1():
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

def t121001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t121001000_x3(z7=_):
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

def t121001000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t121001000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t121001000_x1()
    else:
        """State 4,7"""
        call = t121001000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t121001000_x1()
    """State 9"""
    return 0

def t121001000_x5():
    """State 0,1"""
    assert t121001000_x1()
    """State 2"""
    return 0

def t121001000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=50, val5=55, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t121001000_x23(flag40=flag40, flag41=flag41, flag42=flag42, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, flag45=flag45,
                              flag46=flag46, flag47=flag47, z3=z3, z4=z4, z5=z5, z6=z6, mode5=mode5, mode6=mode6,
                              mode7=mode7)
        assert IsClientPlayer()
        """State 1"""
        call = t121001000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t121001000_x7(val1=5, val2=10, val3=12, val4=50, val5=55, actionbutton1=6000, flag43=6000, flag44=6001, flag45=6000,
                  flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    while True:
        """State 2"""
        call = t121001000_x10(actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode7 == 1, 1000000)
            call = t121001000_x14(val1=val1, z3=z3)
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
        elif GetEventFlag(flag47):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag45) and not GetEventFlag(flag46) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t121001000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t121001000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t121001000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t121001000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t121001000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t121001000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t121001000_x9(flag40=6000, val2=10, val3=12):
    """State 0,8"""
    assert t121001000_x35()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag40):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t121001000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t121001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t121001000_x10(actionbutton1=6000, flag43=6000, flag44=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t121001000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t121001000_x0(actionbutton1=actionbutton1, flag44=flag44, flag49=6000, flag50=6000, flag51=6000,
                flag52=6000, flag43=flag43))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121001000_x11(machine1=_, val6=_):
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

def t121001000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t121001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t121001000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t121001000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t121001000_x13():
    """State 0,1"""
    assert t121001000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t121001000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t121001000_x24()
    """State 3"""
    call = t121001000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t121001000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t121001000_x15():
    """State 0,1"""
    assert t121001000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t121001000_x16(val5=55):
    """State 0,2"""
    call = t121001000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t121001000_x27()
    """State 4"""
    return 0

def t121001000_x17():
    """State 0,1"""
    assert t121001000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t121001000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t121001000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t121001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t121001000_x29()
    """Unused"""
    """State 6"""
    return 0

def t121001000_x19():
    """State 0,2"""
    call = t121001000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t121001000_x20():
    """State 0,1"""
    assert t121001000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t121001000_x21():
    """State 0,1"""
    assert t121001000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t121001000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t121001000_x23(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=50, val5=55, actionbutton1=6000,
                   flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode5=1, mode6=1, mode7=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t121001000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag43=flag43, flag44=flag44, flag45=flag45, flag46=flag46, flag47=flag47, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode5=mode5, mode6=mode6, mode7=mode7)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag40):
            """State 3"""
            Label('L0')
            call = t121001000_x9(flag40=flag40, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag40):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag41) or GetEventFlag(flag42):
            """State 2"""
            call = t121001000_x8(val2=val2, val3=val3)
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
        assert t121001000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t121001000_x24():
    """State 0,1"""
    assert t121001000_x25()
    """State 2"""
    return 0

def t121001000_x25():
    """State 0,1"""
    assert t121001000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t121001000_x26():
    """State 0,1"""
    call = t121001000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t121001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121001000_x27():
    """State 0,1"""
    call = t121001000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t121001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121001000_x28():
    """State 0,1"""
    call = t121001000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t121001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121001000_x29():
    """State 0,1"""
    call = t121001000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t121001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t121001000_x30(text1=_, flag1=_, mode9=1):
    """State 0,5"""
    assert t121001000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t121001000_x31(text22=30909100, flag48=1129064, mode8=1):
    """State 0,5"""
    assert t121001000_x32() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    # talk:30909100:"Oh, my champion! Are you quite alright? My champion!?"
    TalkToPlayer(text22, -1, -1, True)
    """State 4"""
    if mode8 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag48, FlagState.On)
    """State 6"""
    return 0

def t121001000_x32():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t121001000_x33():
    """State 0,1"""
    assert t121001000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t121001000_x34():
    """State 0,1"""
    assert t121001000_x1()
    """State 2"""
    return 0

def t121001000_x35():
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

def t121001000_x36(z1=_, z2=_):
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

def t121001000_x37():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t121001000_x38(text19=30900300, flag37=1209403, text20=30900400, flag38=1209404, text21=30914400, flag39=1209405):
    """State 0"""
    if not GetEventFlag(flag37):
        """State 2"""
        Label('L0')
        assert t121001000_x30(text1=text19, flag1=flag37, mode9=1)
    elif not GetEventFlag(flag38):
        """State 3"""
        assert t121001000_x30(text1=text20, flag1=flag38, mode9=1)
    elif not GetEventFlag(flag39):
        """State 4"""
        assert t121001000_x30(text1=text21, flag1=flag39, mode9=1)
    else:
        """State 1"""
        SetEventFlag(flag37, FlagState.Off)
        SetEventFlag(flag38, FlagState.Off)
        SetEventFlag(flag39, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200, flag31=1209412,
                   text18=_, flag32=_):
    """State 0"""
    if not GetEventFlag(flag29):
        """State 1"""
        assert t121001000_x30(text1=text15, flag1=flag29, mode9=1)
    elif not GetEventFlag(flag30):
        """State 2"""
        assert t121001000_x30(text1=text16, flag1=flag30, mode9=1)
    elif not GetEventFlag(flag31):
        """State 3"""
        assert t121001000_x30(text1=text17, flag1=flag31, mode9=1)
    elif not GetEventFlag(flag32):
        """State 4"""
        assert t121001000_x30(text1=text18, flag1=flag32, mode9=1)
    else:
        """State 5"""
        assert (t121001000_x41(text15=text15, flag33=-1, text16=text16, flag34=-1, text17=text17, flag35=-1, text18=text18,
                flag36=-1))
    """State 6"""
    return 0

def t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200, flag19=1209413,
                   text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=_, flag22=_):
    """State 0"""
    if not GetEventFlag(flag17):
        """State 1"""
        assert t121001000_x30(text1=text9, flag1=flag17, mode9=1)
    elif not GetEventFlag(flag18):
        """State 2"""
        assert t121001000_x30(text1=text10, flag1=flag18, mode9=1)
    elif not GetEventFlag(flag19):
        """State 3"""
        assert t121001000_x30(text1=text11, flag1=flag19, mode9=1)
    elif not GetEventFlag(flag20):
        """State 4"""
        assert t121001000_x30(text1=text12, flag1=flag20, mode9=1)
    elif not GetEventFlag(flag21):
        """State 5"""
        assert t121001000_x30(text1=text13, flag1=flag21, mode9=1)
    elif not GetEventFlag(flag22):
        """State 7"""
        assert t121001000_x30(text1=text14, flag1=flag22, mode9=1)
    else:
        """State 6"""
        assert (t121001000_x42(text9=text9, flag23=-1, text10=text10, flag24=-1, text11=text11, flag25=-1, text12=text12,
                flag26=-1, text13=text13, flag27=-1, text14=text14, flag28=-1))
    """State 8"""
    return 0

def t121001000_x41(text15=30916800, flag33=-1, text16=30915300, flag34=-1, text17=30917200, flag35=-1, text18=_,
                   flag36=-1):
    """State 0,5"""
    assert t121001000_x3(z7=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t121001000_x30(text1=text15, flag1=flag33, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t121001000_x30(text1=text16, flag1=flag34, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t121001000_x30(text1=text17, flag1=flag35, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t121001000_x30(text1=text18, flag1=flag36, mode9=1)
    """State 7"""
    return 0

def t121001000_x42(text9=30916800, flag23=-1, text10=30915300, flag24=-1, text11=30916200, flag25=-1, text12=30916300,
                   flag26=-1, text13=30916400, flag27=-1, text14=_, flag28=-1):
    """State 0,5"""
    assert t121001000_x3(z7=6)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t121001000_x30(text1=text9, flag1=flag23, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t121001000_x30(text1=text10, flag1=flag24, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t121001000_x30(text1=text11, flag1=flag25, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t121001000_x30(text1=text12, flag1=flag26, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t121001000_x30(text1=text13, flag1=flag27, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t121001000_x30(text1=text14, flag1=flag28, mode9=1)
    """State 9"""
    return 0

def t121001000_x43(text1=30916800, flag9=-1, text2=30915300, flag10=-1, text3=30916300, flag11=-1, text4=30916400,
                   flag12=-1, text5=30916500, flag13=-1, text6=30916600, flag14=-1, text7=30916700, flag15=-1,
                   text8=_, flag16=-1):
    """State 0,5"""
    assert t121001000_x3(z7=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t121001000_x30(text1=text1, flag1=flag9, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t121001000_x30(text1=text2, flag1=flag10, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t121001000_x30(text1=text3, flag1=flag11, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t121001000_x30(text1=text4, flag1=flag12, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t121001000_x30(text1=text5, flag1=flag13, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t121001000_x30(text1=text6, flag1=flag14, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t121001000_x30(text1=text7, flag1=flag15, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t121001000_x30(text1=text8, flag1=flag16, mode9=1)
    """State 11"""
    return 0

def t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                   text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417,
                   text7=30916700, flag7=1209418, text8=_, flag8=_):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t121001000_x30(text1=text1, flag1=flag1, mode9=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t121001000_x30(text1=text2, flag1=flag2, mode9=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t121001000_x30(text1=text3, flag1=flag3, mode9=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t121001000_x30(text1=text4, flag1=flag4, mode9=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t121001000_x30(text1=text5, flag1=flag5, mode9=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t121001000_x30(text1=text6, flag1=flag6, mode9=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t121001000_x30(text1=text7, flag1=flag7, mode9=1)
    elif not GetEventFlag(flag8):
        """State 8"""
        assert t121001000_x30(text1=text8, flag1=flag8, mode9=1)
    else:
        """State 9"""
        assert (t121001000_x43(text1=text1, flag9=-1, text2=text2, flag10=-1, text3=text3, flag11=-1, text4=text4,
                flag12=-1, text5=text5, flag13=-1, text6=text6, flag14=-1, text7=text7, flag15=-1, text8=text8,
                flag16=-1))
    """State 10"""
    return 0

def t121001000_x45(action1=_):
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

def t121001000_x46():
    """State 0"""
    if GetEventFlag(10002400):
        """State 1,5"""
        Label('L0')
        # talk:30900200:"How are you faring today, champion?"
        assert t121001000_x30(text1=30900200, flag1=1209400, mode9=1)
    elif GetEventFlag(10002401):
        """State 2,6"""
        # talk:30914500:"How may I help you, champion?"
        assert t121001000_x30(text1=30914500, flag1=1209401, mode9=1)
    elif GetEventFlag(10002402):
        """State 3,7"""
        # talk:30914600:"No task is too great or small, champion!"
        assert t121001000_x30(text1=30914600, flag1=1209402, mode9=1)
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t121001000_x47(mode2=_, mode3=_, mode4=_):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 2"""
    # action:23090001:"What explains your appearance?"
    AddTalkListDataAltIf(mode3 == 1, 97, 23090001, -1, 97, False)
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode4 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    if GetEventFlag(1209440) and mode2 == 1:
        """State 5"""
        if not GetChrHero() == Hero.Duchess:
            """State 3"""
            # action:23090045:"About the crypt..."
            AddTalkListDataAltIf(GetEventFlag(1109020) and not GetChrHero() == Hero.Duchess, 96, 23090045, -1,
                                 96, False)
        else:
            pass
    else:
        pass
    """State 6"""
    return 0

def t121001000_x48():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t121001000_x49():
    """State 0,1"""
    if GetTalkListEntryResult() == 96:
        """State 7,10"""
        assert t121001000_x52()
    elif GetTalkListEntryResult() == 97:
        """State 2,8"""
        # talk:30900500:"You wish to know about me?"
        # talk:30900501:"I began as one among many. A single cog in a great machine of war."
        # talk:30900502:"But then, I was selected for modification. To become proficient in the field of housekeeping."
        # talk:30900503:"It did not proceed...entirely as expected."
        # talk:30900504:"I was tossed away, only to wake up here."
        # talk:30900505:"Where I began my domestic duties."
        # talk:30900506:"Hardly the most riveting of tales, I'm afraid."
        assert t121001000_x30(text1=30900500, flag1=1209407, mode9=1)
    elif GetTalkListEntryResult() == 98:
        """State 6,9"""
        assert t121001000_x51()
    elif GetTalkListEntryResult() == 99:
        """State 3,11"""
        Label('L0')
        # talk:30900300:"Speak to me, should you require anything at all."
        # talk:30900400:"I’m all ears, should you have anything at all to discuss."
        # talk:30914400:"Understood."
        assert (t121001000_x38(text19=30900300, flag37=1209403, text20=30900400, flag38=1209404, text21=30914400,
                flag39=1209405))
    elif GetTalkListEntryResult() == 0:
        """State 4"""
        Goto('L0')
    else:
        """State 5"""
        Goto('L0')
    """State 12"""
    return 0

def t121001000_x50(mode2=_, mode3=_, mode4=1):
    """State 0,1"""
    assert t121001000_x46()
    """State 3"""
    assert t121001000_x47(mode2=mode2, mode3=mode3, mode4=mode4)
    """State 4"""
    assert t121001000_x48()
    """State 2"""
    assert t121001000_x49()
    """State 5"""
    return 0

def t121001000_x51():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        assert t121001000_x57()
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        assert t121001000_x56()
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t121001000_x55()
    """State 7"""
    return 0

def t121001000_x52():
    """State 0,1"""
    # talk:30900830:"Yes, the crypt is filled with the ancient people of these lands."
    # talk:30900831:"I still remember looking after them, long, long ago."
    # talk:30900832:"As you know, mortality does not apply to those such as myself."
    # talk:30900833:"These souls were laid to rest here in anticipation of the threat we now face."
    # talk:30900834:"In a ritual required to draw the minds of their descendants here."
    assert t121001000_x30(text1=30900830, flag1=1209408, mode9=1)
    """State 2"""
    return 0

def t121001000_x53():
    """State 0,1"""
    if not GetEventFlag(1209406) and not GetChrHero() == Hero.Duchess:
        """State 2,6"""
        # talk:30900100:"Welcome to the Roundtable Hold, brave champion."
        # talk:30900101:"I am but a humble attendant, here to serve your needs."
        # talk:30900102:"I am told that each of you has committed a grave misdeed, but I beg to differ."
        # talk:30900103:"You aim to preserve this very land, and that is no small matter."
        # talk:30900104:"Indeed, it is an ambition most worthy of praise."
        # talk:30900105:"I've spruced up the facilities to make your stay as pleasant as possible."
        # talk:30900106:"By all means, do make yourself at home."
        assert t121001000_x30(text1=30900100, flag1=1209406, mode9=1)
    # eventflag:6050: Skin release
    elif GetEventFlag(6050) and not GetEventFlag(1209409):
        """State 4,7"""
        # talk:30914700:"Champion, a moment please."
        # talk:30914701:"I have installed a dressing room next to the study."
        # talk:30914702:"If you have other garments you would prefer to don, it is yours to use as you will."
        assert t121001000_x30(text1=30914700, flag1=1209409, mode9=1)
    else:
        """State 3,9"""
        return 0
    """State 10"""
    Label('L0')
    return 1
    """Unused"""
    """State 5,8"""
    assert t121001000_x54()
    Goto('L0')

def t121001000_x54():
    """State 0,2,4"""
    # talk:30914800:"Oh, I've been meaning to give you this."
    # talk:30914801:"Our good Lady Witch asked me to look after it."
    # talk:30914802:"I believe she found it lying about somewhere or other. Thank goodness she did, eh!"
    assert t121001000_x30(text1=30914800, flag1=1209427, mode9=1)
    """State 3"""
    SetEventFlag(1209428, FlagState.On)
    """State 1"""
    UnlockGarb(101000)
    """State 5"""
    assert t121001000_x37()
    """State 6"""
    return 0

def t121001000_x55():
    """State 0,1"""
    if GetChrHero() == Hero.Wylder:
        """State 2,11"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915400:"My thanks for your continued help maintaining the armaments."
        # talk:30915401:"Once we have more, I implore you to continue."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915400, flag32=1209419))
    elif GetChrHero() == Hero.Guardian:
        """State 3,12"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30916000:"I must thank you for keeping such a vigilant watch."
        # talk:30916001:"It's kept the number of structural failures to a minimum."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30916000, flag32=1209420))
    elif GetChrHero() == Hero.Ironeye:
        """State 4,13"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915900:"So, the arrows haven't been carved in a manner that ensures sound flight?"
        # talk:30915901:"Then, would you mind teaching me again?"
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915900, flag32=1209421))
    elif GetChrHero() == Hero.Duchess:
        """State 5,14"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915500:"Oh dear, I seem to have dirtied the garb you gave me..."
        # talk:30915501:"Such a fine gift—I mustn't neglect its care."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915500, flag32=1209422))
    elif GetChrHero() == Hero.Raider:
        """State 6,15"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915600:"There's nothing wrong with a drink, but I'd be delighted to see you sculpting again."
        # talk:30915601:"That sort of talent is too good to waste!"
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915600, flag32=1209423))
    elif GetChrHero() == Hero.Revenant:
        """State 7,16"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30916100:"Don't be afraid to come to me if you require any...maintenance."
        # talk:30916101:"As a kindred being, I take such matters very seriously."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30916100, flag32=1209424))
    elif GetChrHero() == Hero.Recluse:
        """State 8,17"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915800:"Apparently, procuring the new volumes will take a bit more time."
        # talk:30915801:"Perhaps we should take the opportunity to expand the study."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915800, flag32=1209425))
    elif GetChrHero() == Hero.Executor:
        """State 9,18"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30917200:"The enemy our battle will reveal...is some manner of beast..."
        # talk:30917201:""When all roads lie sundered, and all hope is lost, only sacred power shall reveal the bridge to be crossed.""
        # talk:30917202:"Or so the saying goes..."
        # talk:30917203:"If you were to find this "sacred power", the winds of war may very well shift in our favour..."
        # talk:30915700:"How would you like to display the painting you gave me?"
        # talk:30915701:"I'm certain that any frame will complement it."
        assert (t121001000_x39(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915700, flag32=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t121001000_x56():
    """State 0,1"""
    if GetChrHero() == Hero.Wylder:
        """State 2,11"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915400:"My thanks for your continued help maintaining the armaments."
        # talk:30915401:"Once we have more, I implore you to continue."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915400,
                flag22=1209419))
    elif GetChrHero() == Hero.Guardian:
        """State 3,12"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916000:"I must thank you for keeping such a vigilant watch."
        # talk:30916001:"It's kept the number of structural failures to a minimum."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30916000,
                flag22=1209420))
    elif GetChrHero() == Hero.Ironeye:
        """State 4,13"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915900:"So, the arrows haven't been carved in a manner that ensures sound flight?"
        # talk:30915901:"Then, would you mind teaching me again?"
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915900,
                flag22=1209421))
    elif GetChrHero() == Hero.Duchess:
        """State 5,14"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915500:"Oh dear, I seem to have dirtied the garb you gave me..."
        # talk:30915501:"Such a fine gift—I mustn't neglect its care."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915500,
                flag22=1209422))
    elif GetChrHero() == Hero.Raider:
        """State 6,15"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915600:"There's nothing wrong with a drink, but I'd be delighted to see you sculpting again."
        # talk:30915601:"That sort of talent is too good to waste!"
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915600,
                flag22=1209423))
    elif GetChrHero() == Hero.Revenant:
        """State 7,16"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916100:"Don't be afraid to come to me if you require any...maintenance."
        # talk:30916101:"As a kindred being, I take such matters very seriously."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30916100,
                flag22=1209424))
    elif GetChrHero() == Hero.Recluse:
        """State 8,17"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915800:"Apparently, procuring the new volumes will take a bit more time."
        # talk:30915801:"Perhaps we should take the opportunity to expand the study."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915800,
                flag22=1209425))
    elif GetChrHero() == Hero.Executor:
        """State 9,18"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916200:"The Nightlords... At first glance, they appear unruly, ramshackle, even..."
        # talk:30916201:"The Traces of Night must be the sole reason they can work as one..."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30915700:"How would you like to display the painting you gave me?"
        # talk:30915701:"I'm certain that any frame will complement it."
        assert (t121001000_x40(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915700,
                flag22=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t121001000_x57():
    """State 0,1"""
    if GetChrHero() == Hero.Wylder:
        """State 2,11"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915400:"My thanks for your continued help maintaining the armaments."
        # talk:30915401:"Once we have more, I implore you to continue."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915400, flag8=1209419))
    elif GetChrHero() == Hero.Guardian:
        """State 3,12"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30916000:"I must thank you for keeping such a vigilant watch."
        # talk:30916001:"It's kept the number of structural failures to a minimum."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30916000, flag8=1209420))
    elif GetChrHero() == Hero.Ironeye:
        """State 4,13"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915900:"So, the arrows haven't been carved in a manner that ensures sound flight?"
        # talk:30915901:"Then, would you mind teaching me again?"
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915900, flag8=1209421))
    elif GetChrHero() == Hero.Duchess:
        """State 5,14"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915500:"Oh dear, I seem to have dirtied the garb you gave me..."
        # talk:30915501:"Such a fine gift—I mustn't neglect its care."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915500, flag8=1209422))
    elif GetChrHero() == Hero.Raider:
        """State 6,15"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915600:"There's nothing wrong with a drink, but I'd be delighted to see you sculpting again."
        # talk:30915601:"That sort of talent is too good to waste!"
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915600, flag8=1209423))
    elif GetChrHero() == Hero.Revenant:
        """State 7,16"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30916100:"Don't be afraid to come to me if you require any...maintenance."
        # talk:30916101:"As a kindred being, I take such matters very seriously."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30916100, flag8=1209424))
    elif GetChrHero() == Hero.Recluse:
        """State 8,17"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915800:"Apparently, procuring the new volumes will take a bit more time."
        # talk:30915801:"Perhaps we should take the opportunity to expand the study."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915800, flag8=1209425))
    elif GetChrHero() == Hero.Executor:
        """State 9,18"""
        # talk:30916800:"The arena of champions...the great Lands Between...tremble in the grasp of the Night."
        # talk:30916801:"As the day wanes, this grip will only tighten."
        # talk:30916802:"Beware, the terror that is rain."
        # talk:30915300:"Is there anything at all that you require?"
        # talk:30915301:"I'm as dexterous as a seamstress, and strong as an ox."
        # talk:30915302:"...My work does, however, take some time."
        # talk:30916300:"Have you noticed, dear champion?"
        # talk:30916301:"Periodic changes of scenery, shifts in the footing, of the Lands Between?"
        # talk:30916302:"You might not think it, but there is a logic to the Night's devouring creep."
        # talk:30916303:"Pay careful attention, and you are sure to reap dividends."
        # talk:30916400:"I'm pleased to see everyone making use of the Roundtable."
        # talk:30916401:"I can only offer scant aid, but offer it I shall."
        # talk:30916500:"A lord of lords...surely this will be the final battle."
        # talk:30916501:"Brave champion. In my heart, your victory is certain."
        # talk:30916600:"Though I am but an assemblage of scrap and bolts, I was honoured with the duty of your care."
        # talk:30916601:"And now it seems that we stand at a historical crossroads."
        # talk:30916602:"How far we have come, I say..."
        # talk:30916700:"My only hope was that I might play some role in fulfilling the Roundtable's destiny."
        # talk:30916701:"And it is you who made it possible. Thank you."
        # talk:30915700:"How would you like to display the painting you gave me?"
        # talk:30915701:"I'm certain that any frame will complement it."
        assert (t121001000_x44(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915700, flag8=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t121001000_x58():
    """State 0,1"""
    assert t121001000_x59()
    """State 2"""
    return 0

def t121001000_x59():
    """State 0"""
    if f302(-1) == 2:
        """State 4"""
        Label('L0')
        call = t121001000_x62()
        if call.Get() == 1:
            """State 5"""
            call = t121001000_x63()
            if call.Get() == 1:
                """State 1"""
                Label('L1')
                """State 7"""
                assert t121001000_x50(mode2=1, mode3=1, mode4=1)
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 3 or f302(-1) == 4 or f302(-1) == 5:
        """State 6"""
        call = t121001000_x64()
        if call.Get() == 1:
            """State 8"""
            call = t121001000_x69()
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
    call = t121001000_x60()
    if call.Get() == 1:
        Goto('L1')
    elif call.Done():
        Goto('L2')
    """State 3"""
    call = t121001000_x61()
    if call.Get() == 1:
        Goto('L0')
    elif call.Done():
        Goto('L2')

def t121001000_x60():
    """State 0,4,9"""
    return 1
    """Unused"""
    """State 1"""
    Goto('L0')
    """State 2"""
    Goto('L1')
    """State 3"""
    Goto('L2')
    """State 5"""
    Label('L0')
    assert t121001000_x50(mode2=1, mode3=1, mode4=1)
    Goto('L3')
    """State 6"""
    Label('L1')
    assert t121001000_x65(mode1=1)
    Goto('L3')
    """State 7"""
    Label('L2')
    assert t121001000_x65(mode1=0)
    """State 8"""
    Label('L3')
    return 0

def t121001000_x61():
    """State 0,2,7"""
    return 1
    """Unused"""
    """State 1"""
    Goto('L0')
    """State 3"""
    Goto('L1')
    """State 4"""
    Label('L0')
    assert t121001000_x50(mode2=1, mode3=1, mode4=1)
    Goto('L2')
    """State 5"""
    Label('L1')
    # talk:30908700:"There's nothing extraordinary in the story of the pilgrims."
    # talk:30908701:"They simply refused to abandon one of their number. Who would censure them for such an act?"
    # talk:30908702:"...The Lands Between continue to crumble away, even now."
    # talk:30908703:"Everything will be lost, unless you champions are triumphant, of course."
    assert t121001000_x30(text1=30908700, flag1=1129051, mode9=1)
    """State 6"""
    Label('L2')
    return 0

def t121001000_x62():
    """State 0"""
    if GetEventFlag(3206):
        """State 2,11"""
        assert t121001000_x66()
    elif GetEventFlag(3207):
        """State 3,12"""
        # talk:30902100:"I once read a story in a very old tome."
        # talk:30902101:"About a realm, far west of the Lands Between, where fighting erupted."
        # talk:30902102:"One side was comprised of winged men."
        # talk:30902103:"They were robbed of these wings by an accursed weapon known as an Ictarus."
        # talk:30902104:"Countless Pinionfolk were killed, while their kingdom's fate hung in the balance. Or so the story goes."
        # talk:30902105:"I never imagined I would meet a living victim..."
        assert t121001000_x30(text1=30902100, flag1=1129055, mode9=1)
        """State 10"""
        SetEventFlag(10003117, FlagState.On)
    elif GetEventFlag(3208):
        """State 4,13"""
        assert t121001000_x67()
    elif GetEventFlag(3209):
        """State 5,14"""
        GiveSpEffectToSelf(9956)
        # talk:30902210:"..."
        # talk:30902211:"Good champion, we must pursue this further."
        # talk:30902212:"We must determine the origin of the curse, to keep history from repeating itself."
        # talk:30902213:"The books might yet be found in the Lands Between."
        # talk:30902214:"And I too would be most gladdened if you were to find them."
        assert t121001000_x30(text1=30902210, flag1=1129059, mode9=1)
        """State 19"""
        assert t121001000_x36(z1=202, z2=1)
    elif GetEventFlag(3210):
        """State 6,15"""
        Label('L0')
        # talk:30909900:"If you find them, bring them to me."
        # talk:30909901:"I will make sure they are preserved in the study."
        assert t121001000_x30(text1=30909900, flag1=1129060, mode9=1)
        """State 16"""
        assert t121001000_x68()
    elif GetEventFlag(3211):
        """State 7"""
        Goto('L0')
    else:
        """State 21"""
        return 1
    """State 20"""
    Label('L1')
    return 0
    """Unused"""
    """State 1"""
    if GetEventFlag(10003116):
        pass
    elif not GetEventFlag(10003116):
        Goto('L2')
    """State 8"""
    Goto('L3')
    """State 9"""
    Label('L2')
    Goto('L4')
    """State 17"""
    Label('L3')
    # talk:30908700:"There's nothing extraordinary in the story of the pilgrims."
    # talk:30908701:"They simply refused to abandon one of their number. Who would censure them for such an act?"
    # talk:30908702:"...The Lands Between continue to crumble away, even now."
    # talk:30908703:"Everything will be lost, unless you champions are triumphant, of course."
    assert t121001000_x30(text1=30908700, flag1=1129051, mode9=1)
    Goto('L1')
    """State 18"""
    Label('L4')
    assert t121001000_x50(mode2=1, mode3=1, mode4=1)
    Goto('L1')

def t121001000_x63():
    """State 0"""
    if GetEventFlag(3212):
        """State 1,6"""
        # talk:30902300:"Is that... Did you find it?"
        # talk:30902301:"Thank you. Indeed, that's the key we're after."
        # talk:30902302:"The witch brought the tome to me, bound though it was..."
        # talk:30902303:"But now the seal can be undone..."
        assert t121001000_x30(text1=30902300, flag1=1129061, mode9=1)
        """State 8"""
        assert t121001000_x36(z1=202, z2=3)
    elif GetEventFlag(3213):
        """State 2,7"""
        # talk:30902400:"The terrible thing is a product of war."
        # talk:30902401:"However, the origin of the curse is still frustratingly opaque."
        # talk:30902402:"Perhaps we shall discover it in the remaining volume..."
        assert t121001000_x30(text1=30902400, flag1=1129062, mode9=1)
        """State 5,10"""
        assert t121001000_x37()
    elif GetEventFlag(3214):
        """State 3,9"""
        # talk:30902500:"One volume remains."
        # talk:30902501:"Brave champion. Should you retrieve the book, do be so kind as to inform me."
        assert t121001000_x30(text1=30902500, flag1=1129063, mode9=1)
    else:
        """State 4,12"""
        return 1
    """State 11"""
    return 0

def t121001000_x64():
    """State 0"""
    if GetEventFlag(3215):
        """State 1,11"""
        Label('L0')
        assert t121001000_x50(mode2=0, mode3=0, mode4=1)
    elif GetEventFlag(3216):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3217):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3219):
        """State 4,10"""
        Label('L1')
        if GetEventFlag(10003107):
            """State 5,12"""
            # talk:30909410:"I have informed everyone who received a charm to dispose of it."
            # talk:30909411:"There is nothing more to worry about."
            assert t121001000_x30(text1=30909410, flag1=1129030, mode9=1)
        elif not GetEventFlag(10003107):
            """State 6,13"""
            assert t121001000_x50(mode2=0, mode3=0, mode4=1)
    elif GetEventFlag(3220):
        """State 9"""
        Goto('L1')
    elif GetEventFlag(3221):
        """State 7,14"""
        assert t121001000_x72()
        """State 15"""
        assert t121001000_x36(z1=203, z2=1)
    elif GetEventFlag(3222):
        """State 8,16"""
        # talk:30914000:""Conveyed to a demon"... Whatever could it mean...?"
        assert t121001000_x30(text1=30914000, flag1=1129072, mode9=1)
    else:
        """State 18"""
        return 1
    """State 17"""
    return 0

def t121001000_x65(mode1=_):
    """State 0,5"""
    assert t121001000_x46()
    """State 6"""
    assert t121001000_x47(mode2=1, mode3=1, mode4=1)
    """State 1"""
    # action:23090041:"About the question posed by the Recluse"
    AddTalkListDataAlt(1, 23090041, -1, 1, False)
    """State 7"""
    assert t121001000_x48()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        # talk:30908600:"You wish to know more of the pilgrims?"
        # talk:30908601:"Their story is no fabrication."
        # talk:30908602:"Take a look inside the church. You will find your answers there."
        assert t121001000_x30(text1=30908600, flag1=1129050, mode9=1)
        """State 3"""
        if 1 == mode1:
            """State 10"""
            assert t121001000_x36(z1=201, z2=1)
        else:
            """State 4"""
            pass
    else:
        """State 8"""
        assert t121001000_x49()
    """State 11"""
    return 0

def t121001000_x66():
    """State 0,3"""
    # talk:30908800:"I hesitate to ask, good champion..."
    # talk:30908801:"But would you mind explaining what happened between you and the Raider?"
    assert t121001000_x30(text1=30908800, flag1=1129052, mode9=1)
    """State 2"""
    # action:23092017:"I lost my flock"
    call = t121001000_x45(action1=23092017)
    if call.Get() == 0:
        """State 4"""
        # talk:30908900:"You speak of the chivalric band to which you belonged?"
        # talk:30908901:"How did you come to lose them, as you say?"
        assert t121001000_x30(text1=30908900, flag1=1129053, mode9=1)
        """State 5"""
        # action:23092018:"Our wings were clipped, we couldn't fly"
        call = t121001000_x45(action1=23092018)
        if call.Get() == 0:
            """State 6"""
            # talk:30909000:"I see... A tragic tale indeed. And your form, heartbreaking."
            # talk:30909001:"Though it boggles the mind to think there was an attack which your defensive prowess could not overcome."
            # talk:30909002:"Indeed, what could have caused such a thing...?"
            # talk:30909003:"..."
            assert t121001000_x30(text1=30909000, flag1=1129054, mode9=1)
            """State 7"""
            # action:23092024:"It's because of the curse"
            call = t121001000_x45(action1=23092024)
            if call.Get() == 0:
                """State 8"""
                # talk:30909010:"Oh, the scarring..."
                # talk:30909011:"This is the work of an accursed blade."
                assert t121001000_x30(text1=30909010, flag1=1129082, mode9=1)
            elif call.Get() == 1:
                """State 1"""
                Label('L0')
        elif call.Get() == 1:
            Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    """State 9"""
    return 0

def t121001000_x67():
    """State 0,1"""
    if not GetEventFlag(10003117):
        """State 3,4"""
        assert t121001000_x46()
    elif GetEventFlag(10003117):
        """State 2,5"""
        # talk:30913800:"To think the legends were true..."
        assert t121001000_x30(text1=30913800, flag1=1129056, mode9=1)
    """State 6"""
    assert t121001000_x68()
    """State 7"""
    return 0

def t121001000_x68():
    """State 0,5"""
    assert t121001000_x47(mode2=0, mode3=0, mode4=0)
    """State 1"""
    # action:23090043:"About the cursed weapon"
    AddTalkListDataAlt(2, 23090043, -1, 2, False)
    """State 6"""
    assert t121001000_x48()
    """State 2"""
    if GetTalkListEntryResult() == 2:
        """State 4,9"""
        GiveSpEffectToSelfIf(not GetEventFlag(1129058), 9955)
        # talk:30902200:"The accursed weapon, the Ictarus, is chronicled in a certain tome."
        # talk:30902201:"But I'm afraid...there are no other clues."
        # talk:30902202:"The tome was part of a three-volume collection."
        # talk:30902203:"And two of the set are missing."
        # talk:30902204:"If I could have read their contents, I may have been able to help you."
        assert t121001000_x30(text1=30902200, flag1=1129058, mode9=1)
    else:
        """State 7"""
        assert t121001000_x49()
    """State 10"""
    Label('L0')
    return 0
    """Unused"""
    """State 3,8"""
    assert t121001000_x30(text1=30913900, flag1=1129057, mode9=1)
    Goto('L0')

def t121001000_x69():
    """State 0"""
    if GetEventFlag(3223):
        """State 1,13"""
        # talk:30902600:"Well, well. Have you retrieved the final volume?"
        # talk:30902601:"Ah, I see, I needn't have asked!"
        # talk:30902602:"Very well, let us see what it says."
        assert t121001000_x30(text1=30902600, flag1=1129073, mode9=1)
        """State 14"""
        assert t121001000_x36(z1=203, z2=3)
    elif GetEventFlag(3224):
        """State 2,15"""
        # talk:30902700:"It appears the curse itself was brought from afar."
        # talk:30902701:"Well, even if we weren't able to unravel the mystery to its fullest extent..."
        # talk:30902702:"You have my deepest gratitude for your efforts, brave champion."
        assert t121001000_x30(text1=30902700, flag1=1129074, mode9=1)
    elif GetEventFlag(3225):
        """State 3,16"""
        # talk:30914100:"I have a troubling feeling..."
        # talk:30914101:"The curse we spoke of... It may be closer than we think..."
        # talk:30914102:"Perhaps I'm overthinking things. I dearly hope I am..."
        assert t121001000_x30(text1=30914100, flag1=1129075, mode9=1)
    elif GetEventFlag(3226):
        """State 4,17"""
        # talk:30914100:"I have a troubling feeling..."
        # talk:30914101:"The curse we spoke of... It may be closer than we think..."
        # talk:30914102:"Perhaps I'm overthinking things. I dearly hope I am..."
        assert t121001000_x30(text1=30914100, flag1=1129075, mode9=1)
    elif GetEventFlag(3227):
        """State 5,8"""
        Label('L0')
        """State 23"""
        return 1
    elif GetEventFlag(3228):
        """State 6,12"""
        if not GetEventFlag(1129076):
            """State 10,19"""
            assert t121001000_x73()
        elif GetEventFlag(1129076):
            """State 11,18"""
            # talk:30914200:"Take the path that does not lead to regret."
            assert t121001000_x30(text1=30914200, flag1=1129077, mode9=1)
    elif GetEventFlag(3229):
        """State 7,20"""
        assert t121001000_x74()
    elif GetEventFlag(3230):
        """State 9,21"""
        # talk:30914300:"I pray for your success in battle."
        assert t121001000_x30(text1=30914300, flag1=1129081, mode9=1)
    else:
        Goto('L0')
    """State 22"""
    return 0

def t121001000_x70():
    """State 0"""
    while True:
        """State 6"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t121001000_x0(actionbutton1=6000, flag44=6001, flag49=6000, flag50=6000, flag51=6000, flag52=6000,
                             flag43=6000)
        if call.Done():
            break
        elif GetEventFlag(10003104):
            """State 2,7"""
            # talk:30909100:"Oh, my champion! Are you quite alright? My champion!?"
            def WhilePaused():
                GiveSpEffectToSelf(9625)
            assert t121001000_x31(text22=30909100, flag48=1129064, mode8=1) and CheckSpecificPersonTalkHasEnded(0)
            """State 5"""
            SetEventFlag(10003104, FlagState.Off)
        elif GetEventFlag(10003105):
            """State 3,8"""
            assert t121001000_x71()
            """State 4"""
            SetEventFlag(10003105, FlagState.Off)
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t121001000_x71():
    """State 0,5"""
    # talk:30909200:"Oh good, you're awake!"
    # talk:30909201:"You gave us such a fright, collapsing like that!"
    # talk:30909202:"Your body is in reasonable condition, as far as I can tell. How do you feel?"
    assert t121001000_x30(text1=30909200, flag1=1129065, mode9=1)
    """State 1"""
    SetEventFlag(10003106, FlagState.On)
    assert GetCurrentStateElapsedFrames() > 1
    """State 4"""
    assert not GetEventFlag(10003106)
    """State 6"""
    # talk:30909300:"All seems well. Thank goodness..."
    # talk:30909301:"Remembrest thou the charm thou wert given?"
    # talk:30909302:"Indeed. The cause..."
    # talk:30909303:"was immaturity. A wish became a curse..."
    # talk:30909304:"I doubt there was any malice involved, but..."
    # talk:30909305:"If it had happened in the midst of battle...danger would have abounded."
    # talk:30909306:"I have informed everyone who received a charm to dispose of it."
    # talk:30909307:"There is nothing more to worry about."
    assert t121001000_x30(text1=30909300, flag1=1129066, mode9=1)
    """State 2,3"""
    SetEventFlag(10003107, FlagState.On)
    """State 7"""
    return 0

def t121001000_x72():
    """State 0,2"""
    # talk:30909500:"I haven't seen the merchant of late. Do you happen to know anything?"
    assert t121001000_x30(text1=30909500, flag1=1129068, mode9=1)
    """State 3"""
    # action:23092020:"I eliminated him"
    call = t121001000_x45(action1=23092020)
    if call.Get() == 0:
        """State 4"""
        # talk:30909600:"Oh, you didn't have to go and..."
        assert t121001000_x30(text1=30909600, flag1=1129069, mode9=1)
        """State 5"""
        # action:23092021:"It was to protect the flock"
        call = t121001000_x45(action1=23092021)
        if call.Get() == 0:
            """State 6"""
            # talk:30909700:"..."
            # talk:30909701:"I see. Well, we'll let bygones be bygones, shall we. I won't speak any more on the matter."
            # talk:30909702:"In any case, it appears as if you have more to say..."
            assert t121001000_x30(text1=30909700, flag1=1129070, mode9=1)
            """State 7"""
            # action:23092022:"Show Merchant's Ledger"
            call = t121001000_x45(action1=23092022)
            if call.Get() == 0:
                """State 8"""
                # talk:30909800:"What's this? A list of transactions?"
                # talk:30909801:"Ah! Here! The tome we're looking for!"
                # talk:30909802:""Conveyed to a demon""
                # talk:30909803:"What on earth could it mean!?"
                assert t121001000_x30(text1=30909800, flag1=1129071, mode9=1)
            elif call.Get() == 1:
                """State 1"""
                Label('L0')
        elif call.Get() == 1:
            Goto('L0')
    elif call.Get() == 1:
        Goto('L0')
    """State 9"""
    return 0

def t121001000_x73():
    """State 0,6"""
    assert t121001000_x46()
    """State 7"""
    assert t121001000_x47(mode2=0, mode3=0, mode4=0)
    """State 1"""
    # action:23090039:"About the Recluse"
    AddTalkListDataAlt(1, 23090039, -1, 1, False)
    """State 9"""
    assert t121001000_x48()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 3,5"""
        # talk:30902800:"Brave champion..."
        # talk:30902801:"It appears the witch is responsible for producing that accursed weapon."
        # talk:30902802:"..."
        # talk:30902803:"...Brave champion, it is no surprise to find you unsure of the proper course of action."
        # talk:30902804:"For her crime has claimed the lives of many."
        # talk:30902805:"And yet, you have fought side-by-side through thick and thin."
        # talk:30902806:"I am sure you're as keenly aware of this as anyone."
        # talk:30902807:"But please consider..."
        # talk:30902808:"Whatever your choice, the burden is sure to be weighty indeed."
        # talk:30902809:"Take the path that does not lead to regret."
        assert t121001000_x30(text1=30902800, flag1=1129076, mode9=1)
    else:
        """State 8"""
        assert t121001000_x49()
    """State 10"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    SetEventFlag(1129039, FlagState.On)
    Goto('L0')

def t121001000_x74():
    """State 0,8,9"""
    # talk:30902900:"I see you've made your choice."
    # talk:30902901:"I am certain you will not regret it."
    assert t121001000_x30(text1=30902900, flag1=1129078, mode9=1)
    """State 13"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Label('L1')
    Goto('L5')
    """State 2"""
    SetEventFlag(10003108, FlagState.On)
    assert GetCurrentStateElapsedFrames() > 1
    Goto('L3')
    """State 3"""
    Label('L2')
    SetEventFlag(10003109, FlagState.On)
    assert not GetEventFlag(10003109)
    Goto('L7')
    """State 4"""
    Label('L3')
    if not GetEventFlag(10003108):
        Goto('L6')
    elif GetEventFlag(10003112):
        pass
    """State 5"""
    Goto('L0')
    """State 6"""
    Label('L4')
    """State 7"""
    Label('L5')
    Goto('L8')
    """State 10"""
    Label('L6')
    # talk:30902910:"I found it discarded, but I've given it a nice polish."
    # talk:30902911:"The new path you have chosen is of your own making."
    # talk:30902912:"Your values do not emanate from a common good. They are your own innate beliefs."
    # talk:30902913:"Stay true to them, and I have no doubt you will dispatch the dire Lord you face."
    assert t121001000_x30(text1=30902910, flag1=1129079, mode9=1)
    Goto('L2')
    """State 11"""
    Label('L7')
    # talk:30902920:"I pray for your success in battle."
    call = t121001000_x30(text1=30902920, flag1=1129080, mode9=1)
    if call.Done() and GetEventFlag(1129036):
        Goto('L4')
    elif call.Done():
        Goto('L1')
    """State 12"""
    Label('L8')
    assert t121001000_x37()
    Goto('L0')

