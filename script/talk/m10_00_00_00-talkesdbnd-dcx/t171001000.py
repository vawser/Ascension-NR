# -*- coding: utf-8 -*-
def t171001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t171001000_x6(flag43=6000, flag44=6000, flag45=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                  flag46=6000, flag47=6001, flag48=6000, flag49=6000, flag50=6000, z5=1, z6=1000000, z7=1000000,
                  z8=1000000, mode4=1, mode5=1, mode6=1)
    Quit()

def t171001000_1000():
    """State 0,2,5"""
    call = t171001000_x61()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > 6:
        """State 4"""
        Label('L0')
        """State 7"""
        assert t171001000_x2()
    """State 1"""
    Label('L1')
    EndMachine(1000)
    Quit()
    """Unused"""
    """State 3"""
    Label('L2')
    Goto('L1')
    """State 6"""
    call = t171001000_x56()
    if call.Get() == 1:
        Goto('L2')
    elif GetDistanceToPlayer() > 6:
        Goto('L0')

def t171001000_1101():
    """State 0,2,3"""
    def WhilePaused():
        GiveSpEffectToSelf(9625)
    assert t171001000_x72()
    """State 1"""
    EndMachine(1101)
    Quit()

def t171001000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t171001000_x0(actionbutton1=6000, flag47=6001, flag51=6000, flag52=6000, flag53=6000, flag54=6000, flag46=10003353)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif f302(-1) == 2:
        """State 5"""
        t171001000_x70()
        Quit()
    elif not IsCharacterDisabled() and GetEventFlag(10003353) and DoesSelfHaveSpEffect(1673034) and not GetEventFlag(1179022):
        """State 3,6"""
        # talk:30903900:"Aaaaaaaah!"
        t171001000_x32(text1=30903900, flag1=1179022, mode7=1)
        Quit()

def t171001000_x0(actionbutton1=6000, flag47=6001, flag51=6000, flag52=6000, flag53=6000, flag54=6000, flag46=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag47) or GetEventFlag(flag51) or GetEventFlag(flag52) or GetEventFlag(flag53) or
                GetEventFlag(flag54))
        """State 4"""
        assert not GetEventFlag(flag46)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag46) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag47) and not GetEventFlag(flag51) and not GetEventFlag(flag52) and not GetEventFlag(flag53)
            and not GetEventFlag(flag54)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t171001000_x1():
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

def t171001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t171001000_x3(z9=_):
    """State 0,2"""
    if not CompareRNGValue(CompareType.Equal, 0) != -1:
        """State 1,4"""
        ShuffleRNGSeed(z9)
    else:
        """State 3"""
        pass
    """State 5"""
    SetRNGSeed()
    """State 6"""
    return 0

def t171001000_x4(val2=100, val3=100):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t171001000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t171001000_x1()
    else:
        """State 4,7"""
        call = t171001000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t171001000_x1()
    """State 9"""
    return 0

def t171001000_x5():
    """State 0,1"""
    assert t171001000_x1()
    """State 2"""
    return 0

def t171001000_x6(flag43=6000, flag44=6000, flag45=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                  flag46=6000, flag47=6001, flag48=6000, flag49=6000, flag50=6000, z5=1, z6=1000000, z7=1000000,
                  z8=1000000, mode4=1, mode5=1, mode6=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t171001000_x23(flag43=flag43, flag44=flag44, flag45=flag45, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag46=flag46, flag47=flag47, flag48=flag48,
                              flag49=flag49, flag50=flag50, z5=z5, z6=z6, z7=z7, z8=z8, mode4=mode4, mode5=mode5,
                              mode6=mode6)
        assert IsClientPlayer()
        """State 1"""
        call = t171001000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t171001000_x7(val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000, flag46=6000, flag47=6001,
                  flag48=6000, flag49=6000, flag50=6000, z5=1, z6=1000000, z7=1000000, z8=1000000, mode4=1, mode5=1,
                  mode6=1):
    """State 0"""
    while True:
        """State 2"""
        call = t171001000_x10(actionbutton1=actionbutton1, flag46=flag46, flag47=flag47, z6=z6, z7=z7, z8=z8)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode6 == 1, 1000000)
            call = t171001000_x14(val1=val1, z5=z5)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                c5_172(mode4 == 1 and mode5 == 1, 1, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(mode4 == 1 and not mode5 == 1, 1, 9, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode4 == 1 and mode5 == 1, 9, 0, 9, 9, 9, 9, 9, 9, 9)
                c5_172(not mode4 == 1 and not mode5 == 1, 9, 9, 9, 9, 9, 9, 9, 9, 9)
            def ExitPause():
                ChangeCamera(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif IsAttackedBySomeone() and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag50):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag48) and not GetEventFlag(flag49) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t171001000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t171001000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t171001000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t171001000_x8(val2=100, val3=100):
    """State 0,1"""
    call = t171001000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t171001000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t171001000_x9(flag43=6000, val2=100, val3=100):
    """State 0,8"""
    assert t171001000_x36()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag43):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t171001000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t171001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t171001000_x10(actionbutton1=6000, flag46=6000, flag47=6001, z6=1000000, z7=1000000, z8=1000000):
    """State 0,1"""
    call = t171001000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t171001000_x0(actionbutton1=actionbutton1, flag47=flag47, flag51=6000, flag52=6000, flag53=6000,
                flag54=6000, flag46=flag46))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171001000_x11(machine1=_, val6=_):
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

def t171001000_x12(val2=100, val3=100):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t171001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t171001000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t171001000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t171001000_x13():
    """State 0,1"""
    assert t171001000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t171001000_x14(val1=100, z5=1):
    """State 0,4"""
    assert t171001000_x24()
    """State 3"""
    call = t171001000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t171001000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t171001000_x15():
    """State 0,1"""
    assert t171001000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t171001000_x16(val5=100):
    """State 0,2"""
    call = t171001000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t171001000_x27()
    """State 4"""
    return 0

def t171001000_x17():
    """State 0,1"""
    assert t171001000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t171001000_x18(val2=100, val3=100):
    """State 0,5"""
    assert t171001000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t171001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t171001000_x29()
    """Unused"""
    """State 6"""
    return 0

def t171001000_x19():
    """State 0,2"""
    call = t171001000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t171001000_x20():
    """State 0,1"""
    assert t171001000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t171001000_x21():
    """State 0,1"""
    assert t171001000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t171001000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t171001000_x23(flag43=6000, flag44=6000, flag45=6000, val1=100, val2=100, val3=100, val4=100, val5=100, actionbutton1=6000,
                   flag46=6000, flag47=6001, flag48=6000, flag49=6000, flag50=6000, z5=1, z6=1000000, z7=1000000,
                   z8=1000000, mode4=1, mode5=1, mode6=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t171001000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag46=flag46, flag47=flag47, flag48=flag48, flag49=flag49, flag50=flag50, z5=z5,
                             z6=z6, z7=z7, z8=z8, mode4=mode4, mode5=mode5, mode6=mode6)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag43):
            """State 3"""
            Label('L0')
            call = t171001000_x9(flag43=flag43, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag43):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag44) or GetEventFlag(flag45):
            """State 2"""
            call = t171001000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag43):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag44) and not GetEventFlag(flag45):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t171001000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t171001000_x24():
    """State 0,1"""
    assert t171001000_x25()
    """State 2"""
    return 0

def t171001000_x25():
    """State 0,1"""
    assert t171001000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t171001000_x26():
    """State 0,1"""
    call = t171001000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t171001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171001000_x27():
    """State 0,1"""
    call = t171001000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t171001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171001000_x28():
    """State 0,1"""
    call = t171001000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t171001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171001000_x29():
    """State 0,1"""
    call = t171001000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t171001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t171001000_x30(text5=_, flag4=_, mode9=1):
    """State 0,5"""
    assert t171001000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text5, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode9 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag4, FlagState.On)
    """State 6"""
    return 0

def t171001000_x31(text26=_, mode8=1):
    """State 0,4"""
    assert t171001000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text26, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode8 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t171001000_x32(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t171001000_x33() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, True)
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

def t171001000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t171001000_x34():
    """State 0,1"""
    assert t171001000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t171001000_x35():
    """State 0,1"""
    assert t171001000_x1()
    """State 2"""
    return 0

def t171001000_x36():
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

def t171001000_x37(z3=_, z4=_):
    """State 0,1"""
    c1_163(z3, z4)
    """State 2"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 3"""
    RequestSave(0)
    """State 9"""
    if f304(z3) == 1:
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

def t171001000_x38():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t171001000_x39(text23=30900300, flag40=1209403, text24=30900400, flag41=1209404, text25=30914400, flag42=1209405):
    """State 0"""
    if not GetEventFlag(flag40):
        """State 2"""
        Label('L0')
        assert t171001000_x30(text5=text23, flag4=flag40, mode9=1)
    elif not GetEventFlag(flag41):
        """State 3"""
        assert t171001000_x30(text5=text24, flag4=flag41, mode9=1)
    elif not GetEventFlag(flag42):
        """State 4"""
        assert t171001000_x30(text5=text25, flag4=flag42, mode9=1)
    else:
        """State 1"""
        SetEventFlag(flag40, FlagState.Off)
        SetEventFlag(flag41, FlagState.Off)
        SetEventFlag(flag42, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200, flag34=1209412,
                   text22=_, flag35=_):
    """State 0"""
    if not GetEventFlag(flag32):
        """State 1"""
        assert t171001000_x30(text5=text19, flag4=flag32, mode9=1)
    elif not GetEventFlag(flag33):
        """State 2"""
        assert t171001000_x30(text5=text20, flag4=flag33, mode9=1)
    elif not GetEventFlag(flag34):
        """State 3"""
        assert t171001000_x30(text5=text21, flag4=flag34, mode9=1)
    elif not GetEventFlag(flag35):
        """State 4"""
        assert t171001000_x30(text5=text22, flag4=flag35, mode9=1)
    else:
        """State 5"""
        assert (t171001000_x42(text19=text19, flag36=-1, text20=text20, flag37=-1, text21=text21, flag38=-1, text22=text22,
                flag39=-1))
    """State 6"""
    return 0

def t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200, flag22=1209413,
                   text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=_, flag25=_):
    """State 0"""
    if not GetEventFlag(flag20):
        """State 1"""
        assert t171001000_x30(text5=text13, flag4=flag20, mode9=1)
    elif not GetEventFlag(flag21):
        """State 2"""
        assert t171001000_x30(text5=text14, flag4=flag21, mode9=1)
    elif not GetEventFlag(flag22):
        """State 3"""
        assert t171001000_x30(text5=text15, flag4=flag22, mode9=1)
    elif not GetEventFlag(flag23):
        """State 4"""
        assert t171001000_x30(text5=text16, flag4=flag23, mode9=1)
    elif not GetEventFlag(flag24):
        """State 5"""
        assert t171001000_x30(text5=text17, flag4=flag24, mode9=1)
    elif not GetEventFlag(flag25):
        """State 7"""
        assert t171001000_x30(text5=text18, flag4=flag25, mode9=1)
    else:
        """State 6"""
        assert (t171001000_x43(text13=text13, flag26=-1, text14=text14, flag27=-1, text15=text15, flag28=-1, text16=text16,
                flag29=-1, text17=text17, flag30=-1, text18=text18, flag31=-1))
    """State 8"""
    return 0

def t171001000_x42(text19=30916800, flag36=-1, text20=30915300, flag37=-1, text21=30917200, flag38=-1, text22=_,
                   flag39=-1):
    """State 0,5"""
    assert t171001000_x3(z9=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t171001000_x30(text5=text19, flag4=flag36, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t171001000_x30(text5=text20, flag4=flag37, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t171001000_x30(text5=text21, flag4=flag38, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t171001000_x30(text5=text22, flag4=flag39, mode9=1)
    """State 7"""
    return 0

def t171001000_x43(text13=30916800, flag26=-1, text14=30915300, flag27=-1, text15=30916200, flag28=-1, text16=30916300,
                   flag29=-1, text17=30916400, flag30=-1, text18=_, flag31=-1):
    """State 0,5"""
    assert t171001000_x3(z9=6)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t171001000_x30(text5=text13, flag4=flag26, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t171001000_x30(text5=text14, flag4=flag27, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t171001000_x30(text5=text15, flag4=flag28, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t171001000_x30(text5=text16, flag4=flag29, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t171001000_x30(text5=text17, flag4=flag30, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t171001000_x30(text5=text18, flag4=flag31, mode9=1)
    """State 9"""
    return 0

def t171001000_x44(text5=30916800, flag12=-1, text6=30915300, flag13=-1, text7=30916300, flag14=-1, text8=30916400,
                   flag15=-1, text9=30916500, flag16=-1, text10=30916600, flag17=-1, text11=30916700, flag18=-1,
                   text12=_, flag19=-1):
    """State 0,5"""
    assert t171001000_x3(z9=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t171001000_x30(text5=text5, flag4=flag12, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t171001000_x30(text5=text6, flag4=flag13, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t171001000_x30(text5=text7, flag4=flag14, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t171001000_x30(text5=text8, flag4=flag15, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t171001000_x30(text5=text9, flag4=flag16, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t171001000_x30(text5=text10, flag4=flag17, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t171001000_x30(text5=text11, flag4=flag18, mode9=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t171001000_x30(text5=text12, flag4=flag19, mode9=1)
    """State 11"""
    return 0

def t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                   text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417,
                   text11=30916700, flag10=1209418, text12=_, flag11=_):
    """State 0"""
    if not GetEventFlag(flag4):
        """State 1"""
        assert t171001000_x30(text5=text5, flag4=flag4, mode9=1)
    elif not GetEventFlag(flag5):
        """State 2"""
        assert t171001000_x30(text5=text6, flag4=flag5, mode9=1)
    elif not GetEventFlag(flag6):
        """State 3"""
        assert t171001000_x30(text5=text7, flag4=flag6, mode9=1)
    elif not GetEventFlag(flag7):
        """State 4"""
        assert t171001000_x30(text5=text8, flag4=flag7, mode9=1)
    elif not GetEventFlag(flag8):
        """State 5"""
        assert t171001000_x30(text5=text9, flag4=flag8, mode9=1)
    elif not GetEventFlag(flag9):
        """State 6"""
        assert t171001000_x30(text5=text10, flag4=flag9, mode9=1)
    elif not GetEventFlag(flag10):
        """State 7"""
        assert t171001000_x30(text5=text11, flag4=flag10, mode9=1)
    elif not GetEventFlag(flag11):
        """State 8"""
        assert t171001000_x30(text5=text12, flag4=flag11, mode9=1)
    else:
        """State 9"""
        assert (t171001000_x44(text5=text5, flag12=-1, text6=text6, flag13=-1, text7=text7, flag14=-1, text8=text8,
                flag15=-1, text9=text9, flag16=-1, text10=text10, flag17=-1, text11=text11, flag18=-1, text12=text12,
                flag19=-1))
    """State 10"""
    return 0

def t171001000_x46(action4=23091003, z1=23092013, z2=23092014):
    """State 0,1"""
    # action:23091003:"Recalibrate the doll's magic root?"
    OpenGenericDialog(DialogBoxType.CenterBottom2, action4, z1, z2, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t171001000_x47(action3=_):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
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

def t171001000_x48(action1=23092015, action2=23092016, text4=30917000):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:23092015:"Go with the intent to use"
    AddTalkListDataAlt(1, action1, -1, 0, False)
    # action:23092016:"Go with the intent to destroy"
    AddTalkListDataAlt(2, action2, -1, 0, False)
    """State 3"""
    # talk:30917000:"The choice is yours, brave champion."
    ShowShopMessageWithTalk(0, text4)
    """State 4"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    else:
        """State 7"""
        return 1

def t171001000_x49():
    """State 0"""
    if GetEventFlag(10002400):
        """State 1,5"""
        Label('L0')
        # talk:30900200:"How are you faring today, champion?"
        assert t171001000_x30(text5=30900200, flag4=1209400, mode9=1)
    elif GetEventFlag(10002401):
        """State 2,6"""
        # talk:30914500:"How may I help you, champion?"
        assert t171001000_x30(text5=30914500, flag4=1209401, mode9=1)
    elif GetEventFlag(10002402):
        """State 3,7"""
        # talk:30914600:"No task is too great or small, champion!"
        assert t171001000_x30(text5=30914600, flag4=1209402, mode9=1)
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t171001000_x50(mode1=_, mode2=_, mode3=_):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 2"""
    # action:23090001:"What explains your appearance?"
    AddTalkListDataAltIf(mode2 == 1, 97, 23090001, -1, 97, False)
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode3 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    if GetEventFlag(1209440) and mode1 == 1:
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

def t171001000_x51():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t171001000_x52():
    """State 0,1"""
    if GetTalkListEntryResult() == 96:
        """State 7,10"""
        assert t171001000_x55()
    elif GetTalkListEntryResult() == 97:
        """State 2,8"""
        # talk:30900500:"You wish to know about me?"
        # talk:30900501:"I began as one among many. A single cog in a great machine of war."
        # talk:30900502:"But then, I was selected for modification. To become proficient in the field of housekeeping."
        # talk:30900503:"It did not proceed...entirely as expected."
        # talk:30900504:"I was tossed away, only to wake up here."
        # talk:30900505:"Where I began my domestic duties."
        # talk:30900506:"Hardly the most riveting of tales, I'm afraid."
        assert t171001000_x30(text5=30900500, flag4=1209407, mode9=1)
    elif GetTalkListEntryResult() == 98:
        """State 6,9"""
        assert t171001000_x54()
    elif GetTalkListEntryResult() == 99:
        """State 3,11"""
        Label('L0')
        # talk:30900300:"Speak to me, should you require anything at all."
        # talk:30900400:"I’m all ears, should you have anything at all to discuss."
        # talk:30914400:"Understood."
        assert (t171001000_x39(text23=30900300, flag40=1209403, text24=30900400, flag41=1209404, text25=30914400,
                flag42=1209405))
    elif GetTalkListEntryResult() == 0:
        """State 4"""
        Goto('L0')
    else:
        """State 5"""
        Goto('L0')
    """State 12"""
    return 0

def t171001000_x53(mode1=_, mode2=_, mode3=1):
    """State 0,1"""
    assert t171001000_x49()
    """State 3"""
    assert t171001000_x50(mode1=mode1, mode2=mode2, mode3=mode3)
    """State 4"""
    assert t171001000_x51()
    """State 2"""
    assert t171001000_x52()
    """State 5"""
    return 0

def t171001000_x54():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        assert t171001000_x60()
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        assert t171001000_x59()
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t171001000_x58()
    """State 7"""
    return 0

def t171001000_x55():
    """State 0,1"""
    # talk:30900830:"Yes, the crypt is filled with the ancient people of these lands."
    # talk:30900831:"I still remember looking after them, long, long ago."
    # talk:30900832:"As you know, mortality does not apply to those such as myself."
    # talk:30900833:"These souls were laid to rest here in anticipation of the threat we now face."
    # talk:30900834:"In a ritual required to draw the minds of their descendants here."
    assert t171001000_x30(text5=30900830, flag4=1209408, mode9=1)
    """State 2"""
    return 0

def t171001000_x56():
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
        assert t171001000_x30(text5=30900100, flag4=1209406, mode9=1)
    # eventflag:6050: Skin release
    elif GetEventFlag(6050) and not GetEventFlag(1209409):
        """State 4,7"""
        # talk:30914700:"Champion, a moment please."
        # talk:30914701:"I have installed a dressing room next to the study."
        # talk:30914702:"If you have other garments you would prefer to don, it is yours to use as you will."
        assert t171001000_x30(text5=30914700, flag4=1209409, mode9=1)
    else:
        """State 3,9"""
        return 0
    """State 10"""
    Label('L0')
    return 1
    """Unused"""
    """State 5,8"""
    assert t171001000_x57()
    Goto('L0')

def t171001000_x57():
    """State 0,2,4"""
    # talk:30914800:"Oh, I've been meaning to give you this."
    # talk:30914801:"Our good Lady Witch asked me to look after it."
    # talk:30914802:"I believe she found it lying about somewhere or other. Thank goodness she did, eh!"
    assert t171001000_x30(text5=30914800, flag4=1209427, mode9=1)
    """State 3"""
    SetEventFlag(1209428, FlagState.On)
    """State 1"""
    UnlockGarb(101000)
    """State 5"""
    assert t171001000_x38()
    """State 6"""
    return 0

def t171001000_x58():
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915400, flag35=1209419))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30916000, flag35=1209420))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915900, flag35=1209421))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915500, flag35=1209422))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915600, flag35=1209423))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30916100, flag35=1209424))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915800, flag35=1209425))
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
        assert (t171001000_x40(text19=30916800, flag32=1209410, text20=30915300, flag33=1209411, text21=30917200,
                flag34=1209412, text22=30915700, flag35=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t171001000_x59():
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915400,
                flag25=1209419))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30916000,
                flag25=1209420))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915900,
                flag25=1209421))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915500,
                flag25=1209422))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915600,
                flag25=1209423))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30916100,
                flag25=1209424))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915800,
                flag25=1209425))
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
        assert (t171001000_x41(text13=30916800, flag20=1209410, text14=30915300, flag21=1209411, text15=30916200,
                flag22=1209413, text16=30916300, flag23=1209414, text17=30916400, flag24=1209415, text18=30915700,
                flag25=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t171001000_x60():
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915400, flag11=1209419))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30916000, flag11=1209420))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915900, flag11=1209421))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915500, flag11=1209422))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915600, flag11=1209423))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30916100, flag11=1209424))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915800, flag11=1209425))
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
        assert (t171001000_x45(text5=30916800, flag4=1209410, text6=30915300, flag5=1209411, text7=30916300, flag6=1209414,
                text8=30916400, flag7=1209415, text9=30916500, flag8=1209416, text10=30916600, flag9=1209417, text11=30916700,
                flag10=1209418, text12=30915700, flag11=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t171001000_x61():
    """State 0,1"""
    assert t171001000_x62()
    """State 2"""
    return 0

def t171001000_x62():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t171001000_x63()
        if call.Get() == 1:
            """State 4"""
            call = t171001000_x64()
            if call.Get() == 1:
                """State 2"""
                Label('L0')
                """State 6"""
                Label('L1')
                assert t171001000_x53(mode1=0, mode2=0, mode3=1)
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif f302(-1) == 2:
        """State 7"""
        call = t171001000_x78()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    elif f302(-1) == 3:
        """State 5"""
        call = t171001000_x65()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L1')
    """State 8"""
    return 0

def t171001000_x63():
    """State 0"""
    if GetEventFlag(3700):
        """State 1,4"""
        # talk:30903000:"Brave champion, if I may?"
        # talk:30903001:"It is no easy topic to broach, but you seem to show little enthusiasm for slaying the Nightlord."
        # talk:30903002:"You are difficult to read, to say the least."
        # talk:30903003:"One might think you were planning an...indiscretion."
        # talk:30903004:"Most likely my imagination at play, but it nags at me, nevertheless."
        assert t171001000_x30(text5=30903000, flag4=1179000, mode9=1)
    elif GetEventFlag(3701):
        """State 2,5"""
        # talk:30903100:"And so, there is something I wish to ask of you."
        # talk:30903101:"I would like you to go and vanquish some enemies. Ones tainted by Night."
        # talk:30903102:"And be sure to bring evidence of the deed."
        # talk:30903103:"If you wouldn't mind, of course."
        assert t171001000_x30(text5=30903100, flag4=1179001, mode9=1)
        """State 7"""
        assert t171001000_x37(z3=701, z4=1)
    elif GetEventFlag(3702):
        """State 3,6"""
        # talk:30903110:"And so, there is something I wish to ask of you."
        # talk:30903111:"I would like you to go and vanquish some enemies. Ones tainted by Night."
        # talk:30903112:"And be sure to bring evidence of the deed."
        assert t171001000_x30(text5=30903110, flag4=1179002, mode9=1)
    else:
        """State 9"""
        return 1
    """State 8"""
    return 0

def t171001000_x64():
    """State 0"""
    if GetEventFlag(3703):
        """State 1,4"""
        assert t171001000_x66()
    elif GetEventFlag(3704):
        """State 2,5"""
        assert t171001000_x67()
    elif GetEventFlag(3705):
        """State 3,6"""
        assert t171001000_x68()
    else:
        """State 8"""
        return 1
    """State 7"""
    return 0

def t171001000_x65():
    """State 0"""
    if GetEventFlag(3712):
        """State 1,14"""
        # talk:30903500:"Even the hallowed sparring grounds require a little sprucing up from time to time."
        # talk:30903501:"I'm pleased to see that everyone's making use of them."
        assert t171001000_x30(text5=30903500, flag4=1179018, mode9=1)
    elif GetEventFlag(3713):
        """State 2,6"""
        Label('L0')
    elif GetEventFlag(3714):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3715):
        """State 4"""
        Goto('L0')
    elif GetEventFlag(3716):
        """State 5"""
        Goto('L0')
    elif GetEventFlag(3717):
        """State 7,15"""
        assert t171001000_x71()
    elif GetEventFlag(3718):
        """State 8,16"""
        assert t171001000_x74()
    elif GetEventFlag(3719):
        """State 9,20"""
        assert t171001000_x77()
    elif GetEventFlag(3720):
        """State 10,17"""
        # talk:30911210:"While unconscious, I had a dream."
        # talk:30911211:"I was handed this...by the Nightlord."
        # talk:30911212:"Well, I didn't see our foe, per se, but I know it to be true."
        # talk:30911213:"I sense a great power within. Power enough to change a person's fate, I do believe."
        assert t171001000_x30(text5=30911210, flag4=1179029, mode9=1)
    elif GetEventFlag(3723):
        """State 11,21"""
        # talk:30917000:"The choice is yours, brave champion."
        assert t171001000_x30(text5=30917000, flag4=1179030, mode9=1)
    else:
        """State 23"""
        return 1
    """State 22"""
    Label('L1')
    return 0
    """Unused"""
    """State 12"""
    Goto('L2')
    """State 13"""
    Goto('L3')
    """State 18"""
    Label('L2')
    assert t171001000_x75()
    Goto('L1')
    """State 19"""
    Label('L3')
    assert t171001000_x53(mode1=1, mode2=1, mode3=1)
    Goto('L1')

def t171001000_x66():
    """State 0,2"""
    # talk:30903200:"You've returned."
    # talk:30903201:"Were you successful?"
    assert t171001000_x30(text5=30903200, flag4=1179003, mode9=1)
    """State 4"""
    # action:23092010:"Show Night Shard"
    assert t171001000_x47(action3=23092010)
    """State 1"""
    SetEventFlag(10003368, FlagState.On)
    """State 3"""
    # talk:30910000:"Ahh... Yes, I see..."
    # talk:30910001:"That's settled then. Thank you for cooperating."
    # talk:30910002:"There is no question that you are sincerely allied with us in our common cause."
    # talk:30910003:"My apologies for doubting you."
    # talk:30910004:"If by your generosity, I might resume my... No, I will redouble my efforts to be of service to you."
    # talk:30910005:"By all means, don't hesitate to set me to any task."
    assert t171001000_x30(text5=30910000, flag4=1179004, mode9=1)
    """State 5"""
    assert t171001000_x37(z3=701, z4=3)
    """State 6"""
    return 0

def t171001000_x67():
    """State 0,4"""
    # talk:30903300:"Please. Tell me how to help."
    assert t171001000_x30(text5=30903300, flag4=1179005, mode9=1)
    """State 5"""
    assert t171001000_x50(mode1=0, mode2=0, mode3=0)
    """State 3"""
    # action:23090020:"I have a favor to ask"
    AddTalkListDataAlt(1, 23090020, -1, 1, False)
    """State 6"""
    assert t171001000_x51()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 8"""
        # talk:30903310:"...You're looking for someone close to you?"
        # talk:30903311:"Yes, of course. I will assist in whatever capacity I am able."
        # talk:30903312:"What shall I do first?"
        assert t171001000_x30(text5=30903310, flag4=1179006, mode9=1)
        """State 10"""
        # action:23092011:"Give Night Shard"
        assert t171001000_x47(action3=23092011)
        """State 9"""
        # talk:30910100:"Oh, I had no idea this would help guide our search. I'll look after it for you."
        # talk:30910101:"Had you foreseen this all along? You have humbled me."
        # talk:30910102:"I shall begin forthwith. Though I warn you, it may take some time."
        assert t171001000_x30(text5=30910100, flag4=1179007, mode9=1)
        """State 2,11"""
        assert t171001000_x38()
    else:
        """State 7"""
        assert t171001000_x52()
    """State 12"""
    return 0

def t171001000_x68():
    """State 0,7"""
    assert t171001000_x49()
    """State 3"""
    assert t171001000_x50(mode1=0, mode2=0, mode3=0)
    """State 2"""
    # action:23090022:"About the investigation..."
    AddTalkListDataAlt(1, 23090022, -1, 1, False)
    """State 4"""
    assert t171001000_x51()
    """State 1"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        # talk:30910300:"Could you spare me a little more time, please?"
        # talk:30910301:"I'll come to you as soon as I have an answer."
        assert t171001000_x30(text5=30910300, flag4=1179008, mode9=1)
    else:
        """State 5"""
        assert t171001000_x52()
    """State 8"""
    return 0

def t171001000_x69():
    """State 0,1"""
    assert GetEventFlag(10003352)
    """State 5"""
    # talk:30903400:"Brave champion! There you are!"
    # talk:30903401:"You must tell me! What was the engraving?"
    assert t171001000_x30(text5=30903400, flag4=1179015, mode9=1)
    """State 4"""
    # action:23092012:"Show Vestige of Night"
    assert t171001000_x47(action3=23092012)
    """State 6"""
    # talk:30911000:"I see...there's some manner of incantation..."
    # talk:30911001:"I shall look into the matter. A moment please."
    assert t171001000_x30(text5=30911000, flag4=1179016, mode9=1)
    """State 3,7"""
    assert t171001000_x37(z3=702, z4=3)
    """State 2"""
    SetEventFlag(10003352, FlagState.Off)
    """State 8"""
    return 0

def t171001000_x70():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t171001000_x0(actionbutton1=6000, flag47=6001, flag51=6000, flag52=6000, flag53=6000, flag54=6000,
                             flag46=6000)
        if call.Done():
            break
        elif GetEventFlag(10003351):
            """State 4"""
            assert t171001000_x69()
            """State 2"""
            assert not GetEventFlag(10003351)
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t171001000_x71():
    """State 0,7"""
    # talk:30904000:"Ngh..."
    assert t171001000_x30(text5=30904000, flag4=1179023, mode9=1)
    """State 8"""
    # action:23091003:"Recalibrate the doll's magic root?"
    call = t171001000_x46(action4=23091003, z1=23092013, z2=23092014)
    if call.Get() == 0:
        """State 1,6"""
        SetEventFlag(10003358, FlagState.On)
        assert not GetEventFlag(10003358)
        """State 9"""
        # talk:30904100:"...Where am I?"
        # talk:30904101:"Brave lady witch..? Why on earth! How could you have done such a thing!"
        assert t171001000_x30(text5=30904100, flag4=1179024, mode9=1)
        """State 3"""
        SetEventFlag(10003355, FlagState.On)
        assert not GetEventFlag(10003355)
        """State 11"""
        # action:23090049:"Explain the situation"
        assert t171001000_x47(action3=23090049)
        """State 10"""
        # talk:30904200:"Oh, my apologies. I see precisely what has happened here."
        # talk:30904201:"It wasn't you, but a foul imposter who did this to me."
        # talk:30904202:"What in heaven's name is going on?"
        assert t171001000_x30(text5=30904200, flag4=1179025, mode9=1)
        """State 5"""
        SetEventFlag(1179036, FlagState.On)
        """State 4"""
        SetEventFlag(10003356, FlagState.On)
    elif call.Get() == 1:
        """State 2"""
        pass
    """State 12"""
    return 0

def t171001000_x72():
    """State 0,7"""
    assert t171001000_x76()
    """State 1"""
    SetWorkValue(0, GetWorkValue(0) + 1)
    if GetWorkValue(0) > 3:
        """State 3,4,6"""
        # talk:30903900:"Aaaaaaaah!"
        assert t171001000_x32(text1=30903900, flag1=1179022, mode7=1)
    else:
        """State 2,5"""
        # talk:30903600:"Ow!"
        # talk:30903700:"What is the matter! Kind champion."
        # talk:30903800:"Please, desist!"
        assert t171001000_x73(text1=30903600, flag1=1179019, text2=30903700, flag2=1179020, text3=30903800, flag3=1179021)
    """State 8"""
    return 0

def t171001000_x73(text1=30903600, flag1=1179019, text2=30903700, flag2=1179020, text3=30903800, flag3=1179021):
    """State 0,2"""
    assert t171001000_x3(z9=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 3"""
        assert t171001000_x32(text1=text1, flag1=flag1, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 4"""
        assert t171001000_x32(text1=text2, flag1=flag2, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 5"""
        assert t171001000_x32(text1=text3, flag1=flag3, mode7=1)
    """State 6"""
    return 0

def t171001000_x74():
    """State 0,1"""
    if GetEventFlag(10003356):
        """State 3"""
        # talk:30913700:"What in heaven's name is going on?"
        assert t171001000_x30(text5=30913700, flag4=1179026, mode9=1)
    else:
        """State 4"""
        assert t171001000_x49()
    """State 5"""
    assert t171001000_x50(mode1=0, mode2=0, mode3=0)
    """State 2"""
    # action:23090026:"About the Witch of the Wheel"
    AddTalkListDataAlt(1, 23090026, -1, 1, False)
    """State 6"""
    call = t171001000_x51()
    if call.Done() and GetTalkListEntryResult() == 1:
        """State 7"""
        # talk:30904300:"She's an old friend, is she?"
        # talk:30904301:"Now, as you tell it, the Nightlord grew from a shadow hatchling."
        # talk:30904302:"If that is true, then there may indeed be some degree of culpability."
        # talk:30904303:"But can we unquestioningly assume that a single enchanted organism could mature so fantastically?"
        # talk:30904304:"I must say, I doubt that it could be so simple."
        # talk:30904305:"Furthermore..."
        # talk:30904306:"Defeating the Night will put an end to your sister-in-arms."
        # talk:30904307:"I haven't the faintest what I could say, should you be forced to witness your companion's death, again..."
        assert t171001000_x30(text5=30904300, flag4=1179027, mode9=1)
    elif call.Done():
        """State 8"""
        assert t171001000_x52()
    """State 9"""
    return 0

def t171001000_x75():
    """State 0,6"""
    assert t171001000_x49()
    """State 7"""
    assert t171001000_x50(mode1=0, mode2=0, mode3=0)
    """State 3"""
    # action:23090027:"About my decision"
    AddTalkListDataAlt(1, 23090027, -1, 1, False)
    """State 8"""
    assert t171001000_x51()
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        # talk:30917000:"The choice is yours, brave champion."
        assert t171001000_x30(text5=30917000, flag4=1179030, mode9=1)
        """State 11"""
        # action:23092015:"Go with the intent to use"
        # action:23092016:"Go with the intent to destroy"
        # talk:30917000:"The choice is yours, brave champion."
        call = t171001000_x48(action1=23092015, action2=23092016, text4=30917000)
        if call.Get() == 0:
            """State 1"""
            SetEventFlag(1179110, FlagState.Off)
        elif call.Get() == 1:
            """State 2"""
            SetEventFlag(1179110, FlagState.On)
        """State 5"""
        # talk:30911300:"I see."
        # talk:30911301:"I will trust in your judgement."
        # talk:30911302:"Please, take care."
        assert t171001000_x30(text5=30911300, flag4=1179031, mode9=1)
    else:
        """State 10"""
        assert t171001000_x52()
    """State 12"""
    return 0

def t171001000_x76():
    """State 0,1"""
    if not GetEventFlag(10003359):
        """State 2"""
        pass
    else:
        """State 3,4"""
        SetWorkValue(0, 0)
        """State 5"""
        SetEventFlag(10003359, FlagState.Off)
    """State 6"""
    return 0

def t171001000_x77():
    """State 0,4"""
    SetEventFlag(10003360, FlagState.On)
    """State 8"""
    # talk:30911200:"Where are my manners!"
    # talk:30911201:"I must offer you my thanks for helping me."
    assert t171001000_x31(text26=30911200, mode8=1)
    """State 2"""
    assert DoesSelfHaveSpEffect(9935)
    """State 9"""
    # talk:30911220:"Oh...what's this?"
    assert t171001000_x31(text26=30911220, mode8=1)
    """State 3"""
    assert DoesSelfHaveSpEffect(9936)
    """State 7"""
    # talk:30911230:"..."
    # talk:30911231:"Brave champion, perhaps you should take it."
    assert t171001000_x30(text5=30911230, flag4=1179028, mode9=1)
    """State 1,6"""
    assert t171001000_x38()
    """State 5"""
    SetEventFlag(10003360, FlagState.Off)
    """State 10"""
    return 0

def t171001000_x78():
    """State 0"""
    if GetEventFlag(3707):
        """State 1,6"""
        # talk:30910400:"I have come to an understanding regarding the shards of Night."
        # talk:30910401:"It was written of in an old document from a faraway land."
        # talk:30910402:"In a dispute between two realms, there was a beast at the centre of the affair which devoured soldier after soldier."
        # talk:30910403:"No one saw the beast itself, but it left a mountain of corpses in its wake. An old man-at-arms is quoted as saying..."
        # talk:30910404:""It feasted on our shadows... Even those of the dead...""
        # talk:30910405:"...Rather chilling, wouldn't you say?"
        # talk:30910406:"The tooth marks of the creature resemble the pattern seen on the shards..."
        # talk:30910407:"There very well may be a link to the Nightlord."
        assert t171001000_x30(text5=30910400, flag4=1179009, mode9=1)
    elif GetEventFlag(3727):
        """State 2,7"""
        assert t171001000_x79()
    elif GetEventFlag(3709):
        """State 3,5"""
        Label('L0')
        """State 10"""
        return 1
    elif GetEventFlag(3711):
        """State 4,8"""
        # talk:30911100:"I shall look into the matter. A moment please."
        assert t171001000_x30(text5=30911100, flag4=1179017, mode9=1)
    else:
        Goto('L0')
    """State 9"""
    return 0

def t171001000_x79():
    """State 0,6"""
    assert t171001000_x49()
    """State 7"""
    assert t171001000_x50(mode1=0, mode2=0, mode3=0)
    """State 1"""
    # action:23090047:"I'll take the Night Shard back now"
    AddTalkListDataAlt(1, 23090047, -1, 1, False)
    """State 8"""
    assert t171001000_x51()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 10"""
        # talk:30911230:"..."
        # talk:30911231:"Brave champion, perhaps you should take it."
        assert t171001000_x30(text5=30911230, flag4=1179040, mode9=1)
        """State 4"""
        SetEventFlag(10003367, FlagState.On)
        assert GetCurrentStateElapsedFrames() > 5
        """State 5"""
        assert f316() == 0
        """State 3"""
        SetEventFlag(10003364, FlagState.On)
    else:
        """State 9"""
        assert t171001000_x52()
    """State 11"""
    return 0

