# -*- coding: utf-8 -*-
def t181001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t181001000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode4=1, mode5=1, mode6=1)
    Quit()

def t181001000_1000():
    """State 0,2,3"""
    assert t181001000_x56()
    """State 1"""
    EndMachine(1000)
    Quit()
    """Unused"""
    """State 4"""
    t181001000_x51()
    def WhilePaused():
        RequestAnimation(20026, -1)
    Quit()

def t181001000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert (t181001000_x0(actionbutton1=6000, flag44=6001, flag48=6000, flag49=6000, flag50=6000, flag51=6000,
            flag43=6000))
    """State 1"""
    EndMachine(2000)
    Quit()

def t181001000_x0(actionbutton1=6000, flag44=6001, flag48=6000, flag49=6000, flag50=6000, flag51=6000, flag43=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag44) or GetEventFlag(flag48) or GetEventFlag(flag49) or GetEventFlag(flag50) or
                GetEventFlag(flag51))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag43)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag43) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag44) and not GetEventFlag(flag48) and not GetEventFlag(flag49) and not GetEventFlag(flag50)
            and not GetEventFlag(flag51)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t181001000_x1():
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

def t181001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t181001000_x3(z7=_):
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

def t181001000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t181001000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t181001000_x1()
    else:
        """State 4,7"""
        call = t181001000_x31()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t181001000_x1()
    """State 9"""
    return 0

def t181001000_x5():
    """State 0,1"""
    assert t181001000_x1()
    """State 2"""
    return 0

def t181001000_x6(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode4=1, mode5=1, mode6=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t181001000_x23(flag40=flag40, flag41=flag41, flag42=flag42, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, flag45=flag45,
                              flag46=flag46, flag47=flag47, z3=z3, z4=z4, z5=z5, z6=z6, mode4=mode4, mode5=mode5,
                              mode6=mode6)
        assert IsClientPlayer()
        """State 1"""
        call = t181001000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t181001000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag43=6000, flag44=6001, flag45=6000,
                  flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode4=1, mode5=1, mode6=1):
    """State 0"""
    while True:
        """State 2"""
        call = t181001000_x10(actionbutton1=actionbutton1, flag43=flag43, flag44=flag44, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode6 == 1, 1000000)
            call = t181001000_x14(val1=val1, z3=z3)
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
        elif GetEventFlag(flag47):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag45) and not GetEventFlag(flag46) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t181001000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t181001000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t181001000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t181001000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t181001000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t181001000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t181001000_x9(flag40=6000, val2=10, val3=12):
    """State 0,8"""
    assert t181001000_x33()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag40):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t181001000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t181001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t181001000_x10(actionbutton1=6000, flag43=6000, flag44=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t181001000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t181001000_x0(actionbutton1=actionbutton1, flag44=flag44, flag48=6000, flag49=6000, flag50=6000,
                flag51=6000, flag43=flag43))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t181001000_x11(machine1=_, val6=_):
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

def t181001000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t181001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t181001000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t181001000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t181001000_x13():
    """State 0,1"""
    assert t181001000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t181001000_x14(val1=5, z3=1):
    """State 0,4"""
    assert t181001000_x24()
    """State 3"""
    call = t181001000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t181001000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t181001000_x15():
    """State 0,1"""
    assert t181001000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t181001000_x16(val5=12):
    """State 0,2"""
    call = t181001000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t181001000_x27()
    """State 4"""
    return 0

def t181001000_x17():
    """State 0,1"""
    assert t181001000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t181001000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t181001000_x33()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t181001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t181001000_x29()
    """Unused"""
    """State 6"""
    return 0

def t181001000_x19():
    """State 0,2"""
    call = t181001000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t181001000_x20():
    """State 0,1"""
    assert t181001000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t181001000_x21():
    """State 0,1"""
    assert t181001000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t181001000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t181001000_x23(flag40=6000, flag41=6000, flag42=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag43=6000, flag44=6001, flag45=6000, flag46=6000, flag47=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode4=1, mode5=1, mode6=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t181001000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag43=flag43, flag44=flag44, flag45=flag45, flag46=flag46, flag47=flag47, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode4=mode4, mode5=mode5, mode6=mode6)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag40):
            """State 3"""
            Label('L0')
            call = t181001000_x9(flag40=flag40, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag40):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag41) or GetEventFlag(flag42):
            """State 2"""
            call = t181001000_x8(val2=val2, val3=val3)
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
        assert t181001000_x32() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t181001000_x24():
    """State 0,1"""
    assert t181001000_x25()
    """State 2"""
    return 0

def t181001000_x25():
    """State 0,1"""
    assert t181001000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t181001000_x26():
    """State 0,1"""
    call = t181001000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t181001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t181001000_x27():
    """State 0,1"""
    call = t181001000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t181001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t181001000_x28():
    """State 0,1"""
    call = t181001000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t181001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t181001000_x29():
    """State 0,1"""
    call = t181001000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t181001000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t181001000_x30(text1=_, flag1=_, mode7=1):
    """State 0,5"""
    assert t181001000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t181001000_x31():
    """State 0,1"""
    assert t181001000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t181001000_x32():
    """State 0,1"""
    assert t181001000_x1()
    """State 2"""
    return 0

def t181001000_x33():
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

def t181001000_x34(z1=803, z2=3):
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

def t181001000_x35():
    """State 0,1"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 2"""
    RequestSave(0)
    """State 3"""
    return 0

def t181001000_x36(text19=30900300, flag37=1209403, text20=30900400, flag38=1209404, text21=30914400, flag39=1209405):
    """State 0"""
    if not GetEventFlag(flag37):
        """State 2"""
        Label('L0')
        assert t181001000_x30(text1=text19, flag1=flag37, mode7=1)
    elif not GetEventFlag(flag38):
        """State 3"""
        assert t181001000_x30(text1=text20, flag1=flag38, mode7=1)
    elif not GetEventFlag(flag39):
        """State 4"""
        assert t181001000_x30(text1=text21, flag1=flag39, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag37, FlagState.Off)
        SetEventFlag(flag38, FlagState.Off)
        SetEventFlag(flag39, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200, flag31=1209412,
                   text18=_, flag32=_):
    """State 0"""
    if not GetEventFlag(flag29):
        """State 1"""
        assert t181001000_x30(text1=text15, flag1=flag29, mode7=1)
    elif not GetEventFlag(flag30):
        """State 2"""
        assert t181001000_x30(text1=text16, flag1=flag30, mode7=1)
    elif not GetEventFlag(flag31):
        """State 3"""
        assert t181001000_x30(text1=text17, flag1=flag31, mode7=1)
    elif not GetEventFlag(flag32):
        """State 4"""
        assert t181001000_x30(text1=text18, flag1=flag32, mode7=1)
    else:
        """State 5"""
        assert (t181001000_x39(text15=text15, flag33=-1, text16=text16, flag34=-1, text17=text17, flag35=-1, text18=text18,
                flag36=-1))
    """State 6"""
    return 0

def t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200, flag19=1209413,
                   text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=_, flag22=_):
    """State 0"""
    if not GetEventFlag(flag17):
        """State 1"""
        assert t181001000_x30(text1=text9, flag1=flag17, mode7=1)
    elif not GetEventFlag(flag18):
        """State 2"""
        assert t181001000_x30(text1=text10, flag1=flag18, mode7=1)
    elif not GetEventFlag(flag19):
        """State 3"""
        assert t181001000_x30(text1=text11, flag1=flag19, mode7=1)
    elif not GetEventFlag(flag20):
        """State 4"""
        assert t181001000_x30(text1=text12, flag1=flag20, mode7=1)
    elif not GetEventFlag(flag21):
        """State 5"""
        assert t181001000_x30(text1=text13, flag1=flag21, mode7=1)
    elif not GetEventFlag(flag22):
        """State 7"""
        assert t181001000_x30(text1=text14, flag1=flag22, mode7=1)
    else:
        """State 6"""
        assert (t181001000_x40(text9=text9, flag23=-1, text10=text10, flag24=-1, text11=text11, flag25=-1, text12=text12,
                flag26=-1, text13=text13, flag27=-1, text14=text14, flag28=-1))
    """State 8"""
    return 0

def t181001000_x39(text15=30916800, flag33=-1, text16=30915300, flag34=-1, text17=30917200, flag35=-1, text18=_,
                   flag36=-1):
    """State 0,5"""
    assert t181001000_x3(z7=4)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t181001000_x30(text1=text15, flag1=flag33, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t181001000_x30(text1=text16, flag1=flag34, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t181001000_x30(text1=text17, flag1=flag35, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t181001000_x30(text1=text18, flag1=flag36, mode7=1)
    """State 7"""
    return 0

def t181001000_x40(text9=30916800, flag23=-1, text10=30915300, flag24=-1, text11=30916200, flag25=-1, text12=30916300,
                   flag26=-1, text13=30916400, flag27=-1, text14=_, flag28=-1):
    """State 0,5"""
    assert t181001000_x3(z7=6)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t181001000_x30(text1=text9, flag1=flag23, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t181001000_x30(text1=text10, flag1=flag24, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t181001000_x30(text1=text11, flag1=flag25, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t181001000_x30(text1=text12, flag1=flag26, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t181001000_x30(text1=text13, flag1=flag27, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t181001000_x30(text1=text14, flag1=flag28, mode7=1)
    """State 9"""
    return 0

def t181001000_x41(text1=30916800, flag9=-1, text2=30915300, flag10=-1, text3=30916300, flag11=-1, text4=30916400,
                   flag12=-1, text5=30916500, flag13=-1, text6=30916600, flag14=-1, text7=30916700, flag15=-1,
                   text8=_, flag16=-1):
    """State 0,5"""
    assert t181001000_x3(z7=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t181001000_x30(text1=text1, flag1=flag9, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t181001000_x30(text1=text2, flag1=flag10, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t181001000_x30(text1=text3, flag1=flag11, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t181001000_x30(text1=text4, flag1=flag12, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t181001000_x30(text1=text5, flag1=flag13, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t181001000_x30(text1=text6, flag1=flag14, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t181001000_x30(text1=text7, flag1=flag15, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t181001000_x30(text1=text8, flag1=flag16, mode7=1)
    """State 11"""
    return 0

def t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                   text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417,
                   text7=30916700, flag7=1209418, text8=_, flag8=_):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t181001000_x30(text1=text1, flag1=flag1, mode7=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t181001000_x30(text1=text2, flag1=flag2, mode7=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t181001000_x30(text1=text3, flag1=flag3, mode7=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t181001000_x30(text1=text4, flag1=flag4, mode7=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t181001000_x30(text1=text5, flag1=flag5, mode7=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t181001000_x30(text1=text6, flag1=flag6, mode7=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t181001000_x30(text1=text7, flag1=flag7, mode7=1)
    elif not GetEventFlag(flag8):
        """State 8"""
        assert t181001000_x30(text1=text8, flag1=flag8, mode7=1)
    else:
        """State 9"""
        assert (t181001000_x41(text1=text1, flag9=-1, text2=text2, flag10=-1, text3=text3, flag11=-1, text4=text4,
                flag12=-1, text5=text5, flag13=-1, text6=text6, flag14=-1, text7=text7, flag15=-1, text8=text8,
                flag16=-1))
    """State 10"""
    return 0

def t181001000_x43(action1=23092009):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:23092009:"Give Blessed Flowers"
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

def t181001000_x44():
    """State 0"""
    if GetEventFlag(10002400):
        """State 1,5"""
        Label('L0')
        # talk:30900200:"How are you faring today, champion?"
        assert t181001000_x30(text1=30900200, flag1=1209400, mode7=1)
    elif GetEventFlag(10002401):
        """State 2,6"""
        # talk:30914500:"How may I help you, champion?"
        assert t181001000_x30(text1=30914500, flag1=1209401, mode7=1)
    elif GetEventFlag(10002402):
        """State 3,7"""
        # talk:30914600:"No task is too great or small, champion!"
        assert t181001000_x30(text1=30914600, flag1=1209402, mode7=1)
    else:
        """State 4"""
        Goto('L0')
    """State 8"""
    return 0

def t181001000_x45(mode1=_, mode2=_, mode3=1):
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

def t181001000_x46():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t181001000_x47():
    """State 0,1"""
    if GetTalkListEntryResult() == 96:
        """State 7,10"""
        assert t181001000_x50()
    elif GetTalkListEntryResult() == 97:
        """State 2,8"""
        # talk:30900500:"You wish to know about me?"
        # talk:30900501:"I began as one among many. A single cog in a great machine of war."
        # talk:30900502:"But then, I was selected for modification. To become proficient in the field of housekeeping."
        # talk:30900503:"It did not proceed...entirely as expected."
        # talk:30900504:"I was tossed away, only to wake up here."
        # talk:30900505:"Where I began my domestic duties."
        # talk:30900506:"Hardly the most riveting of tales, I'm afraid."
        assert t181001000_x30(text1=30900500, flag1=1209407, mode7=1)
    elif GetTalkListEntryResult() == 98:
        """State 6,9"""
        assert t181001000_x49()
    elif GetTalkListEntryResult() == 99:
        """State 3,11"""
        Label('L0')
        # talk:30900300:"Speak to me, should you require anything at all."
        # talk:30900400:"I’m all ears, should you have anything at all to discuss."
        # talk:30914400:"Understood."
        assert (t181001000_x36(text19=30900300, flag37=1209403, text20=30900400, flag38=1209404, text21=30914400,
                flag39=1209405))
    elif GetTalkListEntryResult() == 0:
        """State 4"""
        Goto('L0')
    else:
        """State 5"""
        Goto('L0')
    """State 12"""
    return 0

def t181001000_x48(mode1=_, mode2=_, mode3=1):
    """State 0,1"""
    assert t181001000_x44()
    """State 3"""
    assert t181001000_x45(mode1=mode1, mode2=mode2, mode3=mode3)
    """State 4"""
    assert t181001000_x46()
    """State 2"""
    assert t181001000_x47()
    """State 5"""
    return 0

def t181001000_x49():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        assert t181001000_x55()
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        assert t181001000_x54()
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t181001000_x53()
    """State 7"""
    return 0

def t181001000_x50():
    """State 0,1"""
    # talk:30900830:"Yes, the crypt is filled with the ancient people of these lands."
    # talk:30900831:"I still remember looking after them, long, long ago."
    # talk:30900832:"As you know, mortality does not apply to those such as myself."
    # talk:30900833:"These souls were laid to rest here in anticipation of the threat we now face."
    # talk:30900834:"In a ritual required to draw the minds of their descendants here."
    assert t181001000_x30(text1=30900830, flag1=1209408, mode7=1)
    """State 2"""
    return 0

def t181001000_x51():
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
        assert t181001000_x30(text1=30900100, flag1=1209406, mode7=1)
    # eventflag:6050: Skin release
    elif GetEventFlag(6050) and not GetEventFlag(1209409):
        """State 4,7"""
        # talk:30914700:"Champion, a moment please."
        # talk:30914701:"I have installed a dressing room next to the study."
        # talk:30914702:"If you have other garments you would prefer to don, it is yours to use as you will."
        assert t181001000_x30(text1=30914700, flag1=1209409, mode7=1)
    else:
        """State 3,9"""
        return 0
    """State 10"""
    Label('L0')
    return 1
    """Unused"""
    """State 5,8"""
    assert t181001000_x52()
    Goto('L0')

def t181001000_x52():
    """State 0,2,4"""
    # talk:30914800:"Oh, I've been meaning to give you this."
    # talk:30914801:"Our good Lady Witch asked me to look after it."
    # talk:30914802:"I believe she found it lying about somewhere or other. Thank goodness she did, eh!"
    assert t181001000_x30(text1=30914800, flag1=1209427, mode7=1)
    """State 3"""
    SetEventFlag(1209428, FlagState.On)
    """State 1"""
    UnlockGarb(101000)
    """State 5"""
    assert t181001000_x35()
    """State 6"""
    return 0

def t181001000_x53():
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
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
        assert (t181001000_x37(text15=30916800, flag29=1209410, text16=30915300, flag30=1209411, text17=30917200,
                flag31=1209412, text18=30915700, flag32=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t181001000_x54():
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
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
        assert (t181001000_x38(text9=30916800, flag17=1209410, text10=30915300, flag18=1209411, text11=30916200,
                flag19=1209413, text12=30916300, flag20=1209414, text13=30916400, flag21=1209415, text14=30915700,
                flag22=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t181001000_x55():
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
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
        assert (t181001000_x42(text1=30916800, flag1=1209410, text2=30915300, flag2=1209411, text3=30916300, flag3=1209414,
                text4=30916400, flag4=1209415, text5=30916500, flag5=1209416, text6=30916600, flag6=1209417, text7=30916700,
                flag7=1209418, text8=30915700, flag8=1209426))
    else:
        """State 10"""
        pass
    """State 19"""
    return 0

def t181001000_x56():
    """State 0,1"""
    assert t181001000_x57()
    """State 2"""
    return 0

def t181001000_x57():
    """State 0"""
    if f302(-1) == 1:
        """State 3"""
        call = t181001000_x58()
        def WhilePaused():
            RequestAnimation(20026, -1)
        if call.Get() == 1:
            """State 2"""
            Label('L0')
            """State 5"""
            Label('L1')
            def WhilePaused():
                RequestAnimation(20026, -1)
            assert t181001000_x48(mode1=1, mode2=1, mode3=1)
        elif call.Done():
            pass
    elif f302(-1) == 4:
        """State 4"""
        call = t181001000_x60()
        def WhilePaused():
            RequestAnimation(20026, -1)
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    else:
        """State 1"""
        Goto('L1')
    """State 6"""
    return 0

def t181001000_x58():
    """State 0"""
    if GetEventFlag(3803):
        """State 1,6"""
        assert t181001000_x48(mode1=0, mode2=0, mode3=1)
    elif GetEventFlag(3804):
        """State 2,7"""
        assert t181001000_x59()
    elif GetEventFlag(3805):
        """State 3,8"""
        Label('L0')
        # talk:30913400:"Brave champion, how would you like to preserve this scene upon a canvas?"
        # talk:30913401:"The bloom is just upon us, after all!"
        assert t181001000_x30(text1=30913400, flag1=1189042, mode7=1)
    elif GetEventFlag(3806):
        """State 4"""
        Goto('L0')
    elif GetEventFlag(3807):
        """State 5"""
        Goto('L0')
    else:
        """State 10"""
        return 1
    """State 9"""
    return 0

def t181001000_x59():
    """State 0,1"""
    # talk:30904400:"Oh, if it isn't our brave champion."
    # talk:30904401:"Look here. My pride and joy. Now in full bloom."
    # talk:30904402:"Life finds purchase, even here."
    # talk:30904403:"Just gazing at them gives me a measure of peace."
    # talk:30904404:"Oh, what's that you have there?"
    assert t181001000_x30(text1=30904400, flag1=1189040, mode7=1)
    """State 3"""
    # action:23092009:"Give Blessed Flowers"
    assert t181001000_x43(action1=23092009)
    """State 2"""
    # talk:30911600:"This flower simply radiates warmth. Thank you very much!"
    # talk:30911601:"I was just thinking we could do with a bit more colour around here. This is just perfect."
    # talk:30911602:"Brave champion, how would you like to preserve this scene upon a canvas?"
    # talk:30911603:"The bloom is just upon us, after all!"
    assert t181001000_x30(text1=30911600, flag1=1189041, mode7=1)
    """State 4"""
    assert t181001000_x34(z1=803, z2=3)
    """State 5"""
    return 0

def t181001000_x60():
    """State 0"""
    if GetEventFlag(3823):
        """State 1"""
        """State 2"""
        pass
    elif GetEventFlag(3824):
        """State 3,5"""
        # talk:30913500:"My champion, have you noticed..."
        # talk:30913501:"The blade you wear upon your hip is not the same as it once was."
        # talk:30913502:"Not in outward appearance, but in its very being."
        # talk:30913503:"..."
        # talk:30913504:"I wonder why I feel so strongly this must be true..."
        # talk:30913505:"Perhaps it is because I too reside in a frame inanimate."
        assert t181001000_x30(text1=30913500, flag1=1189043, mode7=1)
    elif GetEventFlag(3825):
        """State 4,6"""
        assert t181001000_x48(mode1=0, mode2=0, mode3=1)
    else:
        """State 8"""
        return 1
    """State 7"""
    return 0

