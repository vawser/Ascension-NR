# -*- coding: utf-8 -*-
def t140501000_1():
    """State 0,1"""
    if GetCurrentScenarioSection() == Hero.Duchess and f302(-1) == 1:
        """State 2,4"""
        SetUpdateDistance(25)
        """State 5"""
        # eventflag:6000:Flag to always be OFF
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        t140501000_x6(flag36=6000, flag37=6000, flag38=6000, val1=10, val2=20, val3=20, val4=15, val5=20, actionbutton1=6000,
                      flag39=6000, flag40=6001, flag41=6000, flag42=6000, flag43=6000, z3=1, z4=1000000, z5=1000000,
                      z6=1000000, mode1=1, mode2=1, mode3=1)
        Quit()
    else:
        """State 3,6"""
        # eventflag:6000:Flag to always be OFF
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        t140501000_x6(flag36=6000, flag37=6000, flag38=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                      flag39=6000, flag40=6001, flag41=6000, flag42=6000, flag43=6000, z3=1, z4=1000000, z5=1000000,
                      z6=1000000, mode1=1, mode2=1, mode3=1)
        Quit()

def t140501000_1000():
    """State 0,2,3"""
    assert t140501000_x50()
    """State 1"""
    EndMachine(1000)
    Quit()

def t140501000_2000():
    """State 0,2,4"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t140501000_x0(actionbutton1=6000, flag40=6001, flag44=6000, flag45=6000, flag46=6000, flag47=6000, flag39=6000)
    if call.Done():
        pass
    elif f302(-1) == 4:
        """State 6"""
        # actionbutton:6004:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (t140501000_x0(actionbutton1=6004, flag40=6001, flag44=6000, flag45=6000, flag46=6000, flag47=6000,
                flag39=6000))
    """State 1"""
    Label('L0')
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 3"""
    Goto('L0')
    """State 5"""
    t140501000_x57()
    Quit()

def t140501000_x0(actionbutton1=_, flag40=6001, flag44=6000, flag45=6000, flag46=6000, flag47=6000, flag39=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag40) or GetEventFlag(flag44) or GetEventFlag(flag45) or GetEventFlag(flag46) or
                GetEventFlag(flag47))
        """State 4"""
        assert not GetEventFlag(flag39)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag39) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag40) and not GetEventFlag(flag44) and not GetEventFlag(flag45) and not GetEventFlag(flag46)
            and not GetEventFlag(flag47)) or DoesPlayerHaveSpEffect(9640)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t140501000_x1():
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

def t140501000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t140501000_x3(z7=_):
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

def t140501000_x4(val2=_, val3=_):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t140501000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t140501000_x1()
    else:
        """State 4,7"""
        call = t140501000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t140501000_x1()
    """State 9"""
    return 0

def t140501000_x5():
    """State 0,1"""
    assert t140501000_x1()
    """State 2"""
    return 0

def t140501000_x6(flag36=6000, flag37=6000, flag38=6000, val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000,
                  flag39=6000, flag40=6001, flag41=6000, flag42=6000, flag43=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t140501000_x23(flag36=flag36, flag37=flag37, flag38=flag38, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag39=flag39, flag40=flag40, flag41=flag41,
                              flag42=flag42, flag43=flag43, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2,
                              mode3=mode3)
        assert IsClientPlayer()
        """State 1"""
        call = t140501000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t140501000_x7(val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000, flag39=6000, flag40=6001, flag41=6000,
                  flag42=6000, flag43=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t140501000_x10(actionbutton1=actionbutton1, flag39=flag39, flag40=flag40, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode3 == 1, 1000000)
            call = t140501000_x14(val1=val1, z3=z3)
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
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag41) and not GetEventFlag(flag42) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t140501000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t140501000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t140501000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t140501000_x8(val2=_, val3=_):
    """State 0,1"""
    call = t140501000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t140501000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t140501000_x9(flag36=6000, val2=_, val3=_):
    """State 0,8"""
    assert t140501000_x34()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag36):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t140501000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t140501000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t140501000_x10(actionbutton1=6000, flag39=6000, flag40=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t140501000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t140501000_x0(actionbutton1=actionbutton1, flag40=flag40, flag44=6000, flag45=6000, flag46=6000,
                flag47=6000, flag39=flag39))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140501000_x11(machine1=_, val6=_):
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

def t140501000_x12(val2=_, val3=_):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t140501000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t140501000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t140501000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t140501000_x13():
    """State 0,1"""
    assert t140501000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t140501000_x14(val1=_, z3=1):
    """State 0,4"""
    assert t140501000_x24()
    """State 3"""
    call = t140501000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t140501000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t140501000_x15():
    """State 0,1"""
    assert t140501000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t140501000_x16(val5=_):
    """State 0,2"""
    call = t140501000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t140501000_x27()
    """State 4"""
    return 0

def t140501000_x17():
    """State 0,1"""
    assert t140501000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t140501000_x18(val2=_, val3=_):
    """State 0,5"""
    assert t140501000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t140501000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t140501000_x29()
    """Unused"""
    """State 6"""
    return 0

def t140501000_x19():
    """State 0,2"""
    call = t140501000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t140501000_x20():
    """State 0,1"""
    assert t140501000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t140501000_x21():
    """State 0,1"""
    assert t140501000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t140501000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t140501000_x23(flag36=6000, flag37=6000, flag38=6000, val1=_, val2=_, val3=_, val4=_, val5=_, actionbutton1=6000,
                   flag39=6000, flag40=6001, flag41=6000, flag42=6000, flag43=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode1=1, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t140501000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag39=flag39, flag40=flag40, flag41=flag41, flag42=flag42, flag43=flag43, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2, mode3=mode3)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag36):
            """State 3"""
            Label('L0')
            call = t140501000_x9(flag36=flag36, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag36):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag37) or GetEventFlag(flag38):
            """State 2"""
            call = t140501000_x8(val2=val2, val3=val3)
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
        assert t140501000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t140501000_x24():
    """State 0,1"""
    assert t140501000_x25()
    """State 2"""
    return 0

def t140501000_x25():
    """State 0,1"""
    assert t140501000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t140501000_x26():
    """State 0,1"""
    call = t140501000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t140501000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140501000_x27():
    """State 0,1"""
    call = t140501000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t140501000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140501000_x28():
    """State 0,1"""
    call = t140501000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t140501000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140501000_x29():
    """State 0,1"""
    call = t140501000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t140501000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t140501000_x30(text1=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t140501000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
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

def t140501000_x31(text20=_, mode4=1):
    """State 0,4"""
    assert t140501000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text20, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 3"""
    if mode4 == 0:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t140501000_x32():
    """State 0,1"""
    assert t140501000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t140501000_x33():
    """State 0,1"""
    assert t140501000_x1()
    """State 2"""
    return 0

def t140501000_x34():
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

def t140501000_x35(z1=_, z2=_):
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

def t140501000_x36(text17=10302800, flag33=-1, text18=10302900, flag34=-1, text19=10303000, flag35=-1):
    """State 0,5"""
    assert t140501000_x3(z7=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140501000_x30(text1=text17, flag1=flag33, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140501000_x30(text1=text18, flag1=flag34, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t140501000_x30(text1=text19, flag1=flag35, mode5=1)
    """State 6"""
    return 0

def t140501000_x37(text17=10302800, flag30=1209206, text18=10302900, flag31=1209207, text19=10303000, flag32=1209208):
    """State 0"""
    if not GetEventFlag(flag30):
        """State 1"""
        assert t140501000_x30(text1=text17, flag1=flag30, mode5=1)
    elif not GetEventFlag(flag31):
        """State 2"""
        assert t140501000_x30(text1=text18, flag1=flag31, mode5=1)
    elif not GetEventFlag(flag32):
        """State 3"""
        assert t140501000_x30(text1=text19, flag1=flag32, mode5=1)
    else:
        """State 4"""
        assert t140501000_x36(text17=text17, flag33=-1, text18=text18, flag34=-1, text19=text19, flag35=-1)
    """State 5"""
    return 0

def t140501000_x38(text14=10302200, flag27=1209203, text15=10302300, flag28=1209204, text16=10302400, flag29=1209205):
    """State 0"""
    if not GetEventFlag(flag27):
        """State 2"""
        Label('L0')
        assert t140501000_x30(text1=text14, flag1=flag27, mode5=1)
    elif not GetEventFlag(flag28):
        """State 3"""
        assert t140501000_x30(text1=text15, flag1=flag28, mode5=1)
    elif not GetEventFlag(flag29):
        """State 4"""
        assert t140501000_x30(text1=text16, flag1=flag29, mode5=1)
    else:
        """State 1"""
        SetEventFlag(flag27, FlagState.Off)
        SetEventFlag(flag28, FlagState.Off)
        SetEventFlag(flag29, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t140501000_x39(text9=10302900, flag17=1209207, text10=10303000, flag18=1209208, text11=10303100, flag19=1209209,
                   text12=10303200, flag20=1209210, text13=10303300, flag21=1209211):
    """State 0"""
    if not GetEventFlag(flag17):
        """State 1"""
        assert t140501000_x30(text1=text9, flag1=flag17, mode5=1)
    elif not GetEventFlag(flag18):
        """State 2"""
        assert t140501000_x30(text1=text10, flag1=flag18, mode5=1)
    elif not GetEventFlag(flag19):
        """State 3"""
        assert t140501000_x30(text1=text11, flag1=flag19, mode5=1)
    elif not GetEventFlag(flag20):
        """State 4"""
        assert t140501000_x30(text1=text12, flag1=flag20, mode5=1)
    elif not GetEventFlag(flag21):
        """State 5"""
        assert t140501000_x30(text1=text13, flag1=flag21, mode5=1)
    else:
        """State 6"""
        assert (t140501000_x40(text9=text9, flag22=-1, text10=text10, flag23=-1, text11=text11, flag24=-1, text12=text12,
                flag25=-1, text13=text13, flag26=-1))
    """State 7"""
    return 0

def t140501000_x40(text9=10302900, flag22=-1, text10=10303000, flag23=-1, text11=10303100, flag24=-1, text12=10303200,
                   flag25=-1, text13=10303300, flag26=-1):
    """State 0,5"""
    assert t140501000_x3(z7=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140501000_x30(text1=text9, flag1=flag22, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140501000_x30(text1=text10, flag1=flag23, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t140501000_x30(text1=text11, flag1=flag24, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t140501000_x30(text1=text12, flag1=flag25, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t140501000_x30(text1=text13, flag1=flag26, mode5=1)
    """State 8"""
    return 0

def t140501000_x41(text1=10302900, flag9=-1, text2=10303000, flag10=-1, text3=10303100, flag11=-1, text4=10303200,
                   flag12=-1, text5=10303300, flag13=-1, text6=10303400, flag14=-1, text7=10303500, flag15=-1,
                   text8=10303600, flag16=-1):
    """State 0,5"""
    assert t140501000_x3(z7=8)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t140501000_x30(text1=text1, flag1=flag9, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t140501000_x30(text1=text2, flag1=flag10, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t140501000_x30(text1=text3, flag1=flag11, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t140501000_x30(text1=text4, flag1=flag12, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t140501000_x30(text1=text5, flag1=flag13, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t140501000_x30(text1=text6, flag1=flag14, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t140501000_x30(text1=text7, flag1=flag15, mode5=1)
    elif CompareRNGValue(CompareType.Equal, 7) == True:
        """State 10"""
        assert t140501000_x30(text1=text8, flag1=flag16, mode5=1)
    """State 11"""
    return 0

def t140501000_x42(text1=10302900, flag1=1209207, text2=10303000, flag2=1209208, text3=10303100, flag3=1209209,
                   text4=10303200, flag4=1209210, text5=10303300, flag5=1209211, text6=10303400, flag6=1209212,
                   text7=10303500, flag7=1209213, text8=10303600, flag8=1209214):
    """State 0"""
    if not GetEventFlag(flag1):
        """State 1"""
        assert t140501000_x30(text1=text1, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 2"""
        assert t140501000_x30(text1=text2, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 3"""
        assert t140501000_x30(text1=text3, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4):
        """State 4"""
        assert t140501000_x30(text1=text4, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5):
        """State 5"""
        assert t140501000_x30(text1=text5, flag1=flag5, mode5=1)
    elif not GetEventFlag(flag6):
        """State 6"""
        assert t140501000_x30(text1=text6, flag1=flag6, mode5=1)
    elif not GetEventFlag(flag7):
        """State 7"""
        assert t140501000_x30(text1=text7, flag1=flag7, mode5=1)
    elif not GetEventFlag(flag8):
        """State 8"""
        assert t140501000_x30(text1=text8, flag1=flag8, mode5=1)
    else:
        """State 9"""
        assert (t140501000_x41(text1=text1, flag9=-1, text2=text2, flag10=-1, text3=text3, flag11=-1, text4=text4,
                flag12=-1, text5=text5, flag13=-1, text6=text6, flag14=-1, text7=text7, flag15=-1, text8=text8,
                flag16=-1))
    """State 10"""
    return 0

def t140501000_x43(action1=21022005):
    """State 0,1"""
    ClearPreviousMenuSelection()
    ClearTalkListData()
    """State 2"""
    # action:21022005:"Explain"
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

def t140501000_x44():
    """State 0"""
    if DoesSelfHaveSpEffect(9681):
        """State 4,1"""
        if GetChrHero() == Hero.Duchess:
            """State 2,8"""
            # talk:10303700:"How about we take to the seas together?"
            # talk:10303701:"You remind me of Weathervane. I could see you reading the winds just as well. What say you?"
            assert t140501000_x30(text1=10303700, flag1=1209215, mode5=1)
        else:
            """State 9"""
            Label('L0')
            # talk:10302500:"Care for a drink?"
            assert t140501000_x30(text1=10302500, flag1=1209201, mode5=1)
    elif DoesSelfHaveSpEffect(9682):
        """State 5,6"""
        Label('L1')
        if GetEventFlag(10002012) or GetEventFlag(10002011):
            """State 7"""
            Label('L2')
            Goto('L0')
        else:
            """State 10"""
            # talk:10302600:"I can wait, but I only have so much patience..."
            # talk:10302601:"What if my sword arm rusts! Ha ha!"
            assert t140501000_x30(text1=10302600, flag1=1209200, mode5=1)
    elif True:
        """State 3"""
        Goto('L1')
    else:
        Goto('L2')
    """State 11"""
    return 0

def t140501000_x45():
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 4"""
    if GetChrHero() == Hero.Duchess:
        """State 3"""
        # action:21030003:"About Weathervane"
        AddTalkListDataAlt(97, 21030003, -1, 97, False)
    else:
        pass
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAlt(98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 5"""
    return 0

def t140501000_x46():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Regular, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t140501000_x47():
    """State 0,1"""
    if GetTalkListEntryResult() == 97:
        """State 6,9"""
        # talk:10303800:"Oh, Weathervane was the navigator on my old sea vessel. Best apprentice a man could ask for."
        # talk:10303801:"The kid read the winds like no other."
        # talk:10303802:"You've proved yourself a good navigator, helming the Roundtable..."
        # talk:10303803:"Even if this "ship" of yours doesn't move!"
        # talk:10303804:"Hah hah hah."
        assert t140501000_x30(text1=10303800, flag1=1209216, mode5=1)
    elif GetTalkListEntryResult() == 98:
        """State 5,8"""
        assert t140501000_x49()
    elif GetTalkListEntryResult() == 99:
        """State 2,7"""
        Label('L0')
        # talk:10302200:"Come back anytime."
        # talk:10302300:"Bye, then."
        # talk:10302400:"All right."
        assert (t140501000_x38(text14=10302200, flag27=1209203, text15=10302300, flag28=1209204, text16=10302400,
                flag29=1209205))
    elif GetTalkListEntryResult() == 0:
        """State 3"""
        Goto('L0')
    else:
        """State 4"""
        Goto('L0')
    """State 10"""
    return 0

def t140501000_x48():
    """State 0,1"""
    assert t140501000_x44()
    """State 3"""
    assert t140501000_x45()
    """State 4"""
    assert t140501000_x46()
    """State 2"""
    assert t140501000_x47()
    """State 5"""
    return 0

def t140501000_x49():
    """State 0"""
    # eventflag:113:4th night boss defeats on the 3rd day
    if GetEventFlag(113):
        """State 3,6"""
        # talk:10302900:"The night is nothing to be afraid of. "
        # talk:10302901:"It is only the setting of the sun."
        # talk:10303000:"The best weapons are the ones that require unvarnished might to swing."
        # talk:10303001:"Let me at 'em. The bigger the better!"
        # talk:10303100:"I was right to come here—what a deadly bunch you are!"
        # talk:10303101:"I can't wait to jump into the fray!"
        # talk:10303200:"Don't be intimidated by the monsters' numbers."
        # talk:10303201:"There isn't one of them who won't go down with a clean blow to the head."
        # talk:10303300:"What a glorious way to pass the time!"
        # talk:10303301:"That's what I love about this place. Nowhere else comes close."
        # talk:10303400:"We might have seen a few close scrapes, but who's keeping score?"
        # talk:10303401:"It's time to go out with bang."
        # talk:10303402:"Are you with me?"
        # talk:10303500:"Let's show this thing a good time!"
        # talk:10303600:"The big finale? Ahh, I hardly want it to end..."
        # talk:10303601:"Isn't that always the way!"
        assert (t140501000_x42(text1=10302900, flag1=1209207, text2=10303000, flag2=1209208, text3=10303100, flag3=1209209,
                text4=10303200, flag4=1209210, text5=10303300, flag5=1209211, text6=10303400, flag6=1209212, text7=10303500,
                flag7=1209213, text8=10303600, flag8=1209214))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10302900:"The night is nothing to be afraid of. "
        # talk:10302901:"It is only the setting of the sun."
        # talk:10303000:"The best weapons are the ones that require unvarnished might to swing."
        # talk:10303001:"Let me at 'em. The bigger the better!"
        # talk:10303100:"I was right to come here—what a deadly bunch you are!"
        # talk:10303101:"I can't wait to jump into the fray!"
        # talk:10303200:"Don't be intimidated by the monsters' numbers."
        # talk:10303201:"There isn't one of them who won't go down with a clean blow to the head."
        # talk:10303300:"What a glorious way to pass the time!"
        # talk:10303301:"That's what I love about this place. Nowhere else comes close."
        assert (t140501000_x39(text9=10302900, flag17=1209207, text10=10303000, flag18=1209208, text11=10303100,
                flag19=1209209, text12=10303200, flag20=1209210, text13=10303300, flag21=1209211))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10302800:"A fine beast we're facing this time."
        # talk:10302801:"Well, take it as a challenge. Don't overthink it."
        # talk:10302900:"The night is nothing to be afraid of. "
        # talk:10302901:"It is only the setting of the sun."
        # talk:10303000:"The best weapons are the ones that require unvarnished might to swing."
        # talk:10303001:"Let me at 'em. The bigger the better!"
        assert (t140501000_x37(text17=10302800, flag30=1209206, text18=10302900, flag31=1209207, text19=10303000,
                flag32=1209208))
    """State 7"""
    return 0

def t140501000_x50():
    """State 0,1"""
    assert t140501000_x51()
    """State 2"""
    return 0

def t140501000_x51():
    """State 0"""
    if f302(-1) == 1:
        """State 4"""
        call = t140501000_x52()
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 8:
            """State 2,8"""
            assert t140501000_x2()
    elif f302(-1) == 2:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t140501000_x53()
    elif f302(-1) == 4:
        """State 6"""
        call = t140501000_x54()
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 3:
            """State 3,9"""
            assert t140501000_x2()
    else:
        """State 1,7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t140501000_x48()
    """State 10"""
    return 0

def t140501000_x52():
    """State 0"""
    if GetEventFlag(3400):
        """State 1,6"""
        # talk:10301100:"Do you have a moment?"
        # talk:10301101:"Something's been troubling me. Maybe you could help?"
        # talk:10301102:"It's the lad with the greatsword. He seems...off..."
        # talk:10301103:"Just stares into the distance when I talk to him..."
        # talk:10301104:"I have an inkling the constant combat might be taking its toll..."
        # talk:10301105:"Maybe you'd have better luck than me if you tried to get him to talk?"
        assert t140501000_x30(text1=10301100, flag1=1149020, mode5=1)
    elif GetEventFlag(3401):
        """State 2,7"""
        # talk:10301700:"Can you check on the lad with the greatsword?"
        assert t140501000_x30(text1=10301700, flag1=1149021, mode5=1)
    elif GetEventFlag(3402):
        """State 3,8"""
        # talk:10301200:"So, how was he?"
        # talk:10301201:"Not looking good, I take it..."
        # talk:10301202:"Times like these, finding something simple to focus on can help clear the mind."
        # talk:10301203:"Maybe you could get him something to tune up his weaponry?"
        # talk:10301204:"Keeping a trusted tool in top condition always makes me feel better, for one."
        assert t140501000_x30(text1=10301200, flag1=1149022, mode5=1)
        """State 9"""
        assert t140501000_x35(z1=401, z2=1)
    elif GetEventFlag(3403):
        """State 4,10"""
        # talk:10301800:"If only he had something to sharpen up his weapons..."
        assert t140501000_x30(text1=10301800, flag1=1149023, mode5=1)
    else:
        """State 5"""
        pass
    """State 11"""
    return 0

def t140501000_x53():
    """State 0"""
    if GetEventFlag(3404):
        """State 1,6"""
        assert t140501000_x48()
    elif GetEventFlag(3405):
        """State 2,7"""
        # talk:10301300:"Managed to help our friend, did you?"
        # talk:10301301:"Thanks. I like a woman who wants to pitch in."
        # talk:10301302:"Let's see how things are going to play out before we meddle any further."
        # talk:10301303:"And pray the passage of time does our work for us..."
        # talk:10301304:"One more thing..."
        # talk:10301305:"The doll's looking for you."
        # talk:10301306:"Go and see her."
        assert t140501000_x30(text1=10301300, flag1=1149024, mode5=1)
    elif GetEventFlag(3406):
        """State 3,8"""
        Label('L0')
        # talk:10301900:"The doll's looking for you."
        assert t140501000_x30(text1=10301900, flag1=1149025, mode5=1)
    elif GetEventFlag(3407):
        """State 4"""
        Goto('L0')
    else:
        """State 5"""
        pass
    """State 9"""
    return 0

def t140501000_x54():
    """State 0"""
    if GetEventFlag(3412):
        """State 1,8"""
        assert t140501000_x55()
    elif GetEventFlag(3414):
        """State 3,11"""
        # talk:10302000:"That kid always loved the sound of the wind."
        # talk:10302001:"Must be somewhere up above by now, savouring the breeze."
        assert t140501000_x30(text1=10302000, flag1=1149028, mode5=1)
    elif GetEventFlag(3415):
        """State 4,13"""
        assert t140501000_x56()
    elif GetEventFlag(3416):
        """State 5,12"""
        Label('L0')
        # talk:10302100:"Take it from me. You'll be good as gold!"
        # talk:10302101:"(hearty laugh)"
        assert t140501000_x30(text1=10302100, flag1=1149030, mode5=1)
    elif GetEventFlag(3421):
        """State 7"""
        Goto('L0')
    else:
        """State 6,14"""
        assert t140501000_x48()
    """State 15"""
    Label('L1')
    return 0
    """Unused"""
    """State 2,9"""
    # talk:10300300:"Reminds me of an old tale, if you'll indulge me."
    # talk:10300301:"I wasn't much of a pirate, but out at sea every man who toiled by my side was my brother."
    # talk:10300302:"There was this younger kid who looked up to me. Must have figured me for an older brother."
    # talk:10300303:"Till one day, we had a falling out."
    # talk:10300304:"Things got so bad, the sailor snuck off on land without saying a word."
    # talk:10300305:"I-I didn't think much of it. Thought it was a bid for a little attention."
    # talk:10300306:"But I never once saw the kid again."
    # talk:10300307:"When you let your passions get the best of you, things have an awful way of going south."
    # talk:10300308:"Keep your cool, lest you do anything you come to regret."
    # talk:10300309:"Alright, a meagre lesson it might have been, but perhaps you'll glean something from it."
    # talk:10300310:"Worry not, that's all I've a mind to teach right now. Thanks for letting me bend your ear."
    # talk:10300311:"Hah hah..."
    assert t140501000_x30(text1=10300300, flag1=1149027, mode5=1)
    """State 10"""
    assert t140501000_x35(z1=403, z2=1)
    Goto('L1')

def t140501000_x55():
    """State 0,5"""
    SetEventFlagIf(DoesPlayerHaveSpEffect(102000) or DoesPlayerHaveSpEffect(102001) or DoesPlayerHaveSpEffect(102010),
                   10003225, FlagState.On)
    """State 6"""
    assert t140501000_x44()
    """State 7"""
    assert t140501000_x45()
    """State 1"""
    # action:21030001:"Maybe we shouldn't defeat the Nightlord"
    AddTalkListDataAlt(1, 21030001, -1, 1, False)
    """State 8"""
    assert t140501000_x46()
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 3,4"""
        SetEventFlag(10003202, FlagState.On)
        assert not GetEventFlag(10003202) and GetCurrentStateElapsedFrames() > 1
        """State 10"""
        # talk:10300200:"What is it now? Got something funny to say?"
        # talk:10300201:"...Apparently not. Go on, then, spit it out."
        assert t140501000_x30(text1=10300200, flag1=1149026, mode5=1)
        """State 14"""
        # action:21022005:"Explain"
        assert t140501000_x43(action1=21022005)
        """State 15"""
        # talk:10300220:"..."
        # talk:10300221:"The two of you were brother and sister all along...?"
        # talk:10300222:"..."
        assert t140501000_x31(text20=10300220, mode4=1)
        """State 11"""
        Label('L0')
        # talk:10300300:"Reminds me of an old tale, if you'll indulge me."
        # talk:10300301:"I wasn't much of a pirate, but out at sea every man who toiled by my side was my brother."
        # talk:10300302:"There was this younger kid who looked up to me. Must have figured me for an older brother."
        # talk:10300303:"Till one day, we had a falling out."
        # talk:10300304:"Things got so bad, the sailor snuck off on land without saying a word."
        # talk:10300305:"I-I didn't think much of it. Thought it was a bid for a little attention."
        # talk:10300306:"But I never once saw the kid again."
        # talk:10300307:"When you let your passions get the best of you, things have an awful way of going south."
        # talk:10300308:"Keep your cool, lest you do anything you come to regret."
        # talk:10300309:"Alright, a meagre lesson it might have been, but perhaps you'll glean something from it."
        # talk:10300310:"Worry not, that's all I've a mind to teach right now. Thanks for letting me bend your ear."
        # talk:10300311:"Hah hah..."
        assert t140501000_x30(text1=10300300, flag1=1149027, mode5=1)
        """State 12"""
        assert t140501000_x35(z1=403, z2=1)
    else:
        """State 9"""
        assert t140501000_x47()
    """State 16"""
    return 0
    """Unused"""
    """State 13"""
    # talk:10300210:"..."
    assert t140501000_x31(text20=10300210, mode4=1)
    Goto('L0')

def t140501000_x56():
    """State 0,8"""
    SetEventFlagIf(DoesPlayerHaveSpEffect(102000) or DoesPlayerHaveSpEffect(102001) or DoesPlayerHaveSpEffect(102010),
                   10003225, FlagState.On)
    """State 9"""
    if GetEventFlag(1149029):
        """State 7,16"""
        Label('L0')
        # talk:10300410:"You said you were on the fence. Well, my advice has changed."
        # talk:10300411:"I say refuse the choice."
        # talk:10300412:"Who says that when you choose one path, you forego the other?"
        # talk:10300413:"It's your journey. Take all the paths you like."
        # talk:10300414:"I know you won't let it come to nothing."
        # talk:10300415:"Take it from me. You'll be good as gold!"
        # talk:10300416:"Hah..."
        assert t140501000_x30(text1=10300410, flag1=1149032, mode5=1)
        """State 11"""
        assert t140501000_x35(z1=403, z2=3)
    else:
        """State 12"""
        assert t140501000_x44()
        """State 13"""
        assert t140501000_x45()
        """State 2"""
        # action:21030002:"Share Weathervane's message"
        AddTalkListDataAlt(1, 21030002, -1, 1, False)
        """State 14"""
        assert t140501000_x46()
        """State 3"""
        if GetTalkListEntryResult() == 1:
            """State 4,5"""
            SetEventFlag(10003220, FlagState.On)
            """State 10"""
            # talk:10300400:"Are you sure of this?"
            # talk:10300401:"..."
            # talk:10300402:"Damned fool... Why not just tell me?"
            # talk:10300403:"The kid went out like a warrior. Not a bad way, all things considered."
            # talk:10300404:"Thank you. I might never have known, and didn't expect to."
            # talk:10300405:"That settles it—now I'm sure. Take this, would you?"
            assert t140501000_x30(text1=10300400, flag1=1149029, mode5=1) and GetCurrentStateElapsedFrames() > 1
            """State 6"""
            assert f316() == 0
            Goto('L0')
        else:
            """State 15"""
            assert t140501000_x47()
    """State 17"""
    return 0
    """Unused"""
    """State 1"""
    UnlockGarb(102010)
    Quit()

def t140501000_x57():
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t140501000_x0(actionbutton1=6000, flag40=6001, flag44=6000, flag45=6000, flag46=6000, flag47=6000,
                             flag39=10003210)
        if call.Done():
            break
        elif GetEventFlag(10003202):
            """State 2"""
            assert not GetEventFlag(10003202)
            """State 3,6"""
            # talk:10300300:"Reminds me of an old tale, if you'll indulge me."
            # talk:10300301:"I wasn't much of a pirate, but out at sea every man who toiled by my side was my brother."
            # talk:10300302:"There was this younger kid who looked up to me. Must have figured me for an older brother."
            # talk:10300303:"Till one day, we had a falling out."
            # talk:10300304:"Things got so bad, the sailor snuck off on land without saying a word."
            # talk:10300305:"I-I didn't think much of it. Thought it was a bid for a little attention."
            # talk:10300306:"But I never once saw the kid again."
            # talk:10300307:"When you let your passions get the best of you, things have an awful way of going south."
            # talk:10300308:"Keep your cool, lest you do anything you come to regret."
            # talk:10300309:"Alright, a meagre lesson it might have been, but perhaps you'll glean something from it."
            # talk:10300310:"Worry not, that's all I've a mind to teach right now. Thanks for letting me bend your ear."
            # talk:10300311:"Hah hah..."
            def WhilePaused():
                RequestAnimation(90300, -1)
            assert t140501000_x30(text1=10300300, flag1=1149027, mode5=1)
            """State 7"""
            assert t140501000_x35(z1=403, z2=1)
            """State 4"""
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 8"""
    return 0

