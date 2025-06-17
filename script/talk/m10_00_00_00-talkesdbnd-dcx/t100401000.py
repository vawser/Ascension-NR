# -*- coding: utf-8 -*-
def t100401000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t100401000_x6(flag46=6000, flag47=6000, flag48=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag49=6000, flag50=6001, flag51=6000, flag52=6000, flag53=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode3=1, mode4=1, mode5=1)
    Quit()

def t100401000_1000():
    """State 0,2,3"""
    assert t100401000_x60()
    """State 1"""
    EndMachine(1000)
    Quit()

def t100401000_2000():
    """State 0,2,6"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    call = t100401000_x0(actionbutton1=6000, flag50=6001, flag54=6000, flag55=6000, flag56=6000, flag57=6000, flag8=6000)
    if call.Done():
        """State 1"""
        EndMachine(2000)
        Quit()
    elif f301(-1) == 0 and f302(-1) == 1:
        """State 3,7"""
        # talk:10200100:"I am the Priestess. The voice of your formless master."
        # talk:10200101:"You were chosen. For your potential to vanquish the Night."
        # talk:10200102:"The Nightlord is a living cataclysm, bent on laying waste to the very land that anchors us."
        # talk:10200103:"Unless we bring its end, our world will be undone."
        # talk:10200104:"And for this, I need your help."
        t100401000_x65(flag5=10003000, flag6=10003001, text2=10200100, flag7=1109000, flag8=10003008)
        Quit()
    elif f301(-1) == 0 and f302(-1) == 3:
        """State 4,9"""
        # talk:10211500:"There are others. Too many, I am afraid."
        # talk:10211501:"It is not yet clear what this means."
        # talk:10211502:"But that beast left a trace."
        # talk:10211503:"And I believe with traces enough, the parts will begin to resemble a whole."
        # talk:10211504:"As such, our purpose remains unchanged."
        # talk:10211505:"Stay the path. And vanquish our foes. I pray for your success."
        t100401000_x65(flag5=10003002, flag6=10003003, text2=10211500, flag7=1109006, flag8=10003007)
        Quit()
    elif f301(-1) == 0 and f302(-1) == 4:
        """State 5,8"""
        # talk:10207000:"The time has come."
        # talk:10207001:"We now face the primordial Nightlord."
        # talk:10207002:"It will be unlike any other battle. But I have faith."
        # talk:10207003:"The Nightfarers shall prevail."
        t100401000_x79(flag1=10003004, flag2=10003005, text1=10207000, flag3=1109009, flag4=10003007)
        Quit()

def t100401000_x0(actionbutton1=6000, flag50=6001, flag54=6000, flag55=6000, flag56=6000, flag57=6000, flag8=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag50) or GetEventFlag(flag54) or GetEventFlag(flag55) or GetEventFlag(flag56) or
                GetEventFlag(flag57))
        """State 4"""
        assert not GetEventFlag(flag8)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag8) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag50) and not GetEventFlag(flag54) and not GetEventFlag(flag55) and not GetEventFlag(flag56)
            and not GetEventFlag(flag57)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t100401000_x1():
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

def t100401000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t100401000_x3(z5=_):
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

def t100401000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t100401000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t100401000_x1()
    else:
        """State 4,7"""
        call = t100401000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t100401000_x1()
    """State 9"""
    return 0

def t100401000_x5():
    """State 0,1"""
    assert t100401000_x1()
    """State 2"""
    return 0

def t100401000_x6(flag46=6000, flag47=6000, flag48=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag49=6000, flag50=6001, flag51=6000, flag52=6000, flag53=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t100401000_x23(flag46=flag46, flag47=flag47, flag48=flag48, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag49=flag49, flag50=flag50, flag51=flag51,
                              flag52=flag52, flag53=flag53, z1=z1, z2=z2, z3=z3, z4=z4, mode3=mode3, mode4=mode4,
                              mode5=mode5)
        assert IsClientPlayer()
        """State 1"""
        call = t100401000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t100401000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag49=6000, flag50=6001, flag51=6000,
                  flag52=6000, flag53=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 2"""
        call = t100401000_x10(actionbutton1=actionbutton1, flag49=flag49, flag50=flag50, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCameraIf(mode5 == 1, 1000000)
            call = t100401000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag53):
            Goto('L0')
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag51) and not GetEventFlag(flag52) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t100401000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t100401000_x27() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t100401000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t100401000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t100401000_x18(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t100401000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t100401000_x9(flag46=6000, val2=10, val3=12):
    """State 0,8"""
    assert t100401000_x35()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag46):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t100401000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t100401000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t100401000_x10(actionbutton1=6000, flag49=6000, flag50=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t100401000_x11(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t100401000_x0(actionbutton1=actionbutton1, flag50=flag50, flag54=6000, flag55=6000, flag56=6000,
                flag57=6000, flag8=flag49))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100401000_x11(machine1=_, val6=_):
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

def t100401000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t100401000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t100401000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t100401000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t100401000_x13():
    """State 0,1"""
    assert t100401000_x11(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t100401000_x14(val1=5, z1=1):
    """State 0,4"""
    assert t100401000_x24()
    """State 3"""
    call = t100401000_x15()
    def WhilePaused():
        SetTalkTime(1)
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 5"""
        Label('L0')
        SetTalkTime(0)
        assert t100401000_x26()
    elif GetRequestGameMode() == 2:
        """State 2"""
        Goto('L0')
    """State 6"""
    return 0

def t100401000_x15():
    """State 0,1"""
    assert t100401000_x11(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t100401000_x16(val5=12):
    """State 0,2"""
    call = t100401000_x17()
    if call.Done():
        """State 1"""
        SetTalkTime(0.5)
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t100401000_x27()
    """State 4"""
    return 0

def t100401000_x17():
    """State 0,1"""
    assert t100401000_x11(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t100401000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t100401000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t100401000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t100401000_x29()
    """Unused"""
    """State 6"""
    return 0

def t100401000_x19():
    """State 0,2"""
    call = t100401000_x11(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t100401000_x20():
    """State 0,1"""
    assert t100401000_x11(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t100401000_x21():
    """State 0,1"""
    assert t100401000_x11(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t100401000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t100401000_x23(flag46=6000, flag47=6000, flag48=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag49=6000, flag50=6001, flag51=6000, flag52=6000, flag53=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode3=1, mode4=1, mode5=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t100401000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag49=flag49, flag50=flag50, flag51=flag51, flag52=flag52, flag53=flag53, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode3=mode3, mode4=mode4, mode5=mode5)
        def WhilePaused():
            c1_171()
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag46):
            """State 3"""
            Label('L0')
            call = t100401000_x9(flag46=flag46, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag46):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag47) or GetEventFlag(flag48):
            """State 2"""
            call = t100401000_x8(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag46):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag47) and not GetEventFlag(flag48):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t100401000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t100401000_x24():
    """State 0,1"""
    assert t100401000_x25()
    """State 2"""
    return 0

def t100401000_x25():
    """State 0,1"""
    assert t100401000_x11(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t100401000_x26():
    """State 0,1"""
    call = t100401000_x11(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t100401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100401000_x27():
    """State 0,1"""
    call = t100401000_x11(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t100401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100401000_x28():
    """State 0,1"""
    call = t100401000_x11(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t100401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100401000_x29():
    """State 0,1"""
    call = t100401000_x11(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t100401000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t100401000_x30(text1=_, flag3=_, mode8=1):
    """State 0,5"""
    assert t100401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag3, FlagState.On)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode8 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t100401000_x31(text2=_, flag7=_, mode7=1):
    """State 0,5"""
    assert t100401000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text2, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode7 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag7, FlagState.On)
    """State 6"""
    return 0

def t100401000_x32(text23=10210400, mode6=1):
    """State 0,4"""
    assert t100401000_x2() and CheckSpecificPersonTalkHasEnded(0)
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

def t100401000_x33():
    """State 0,1"""
    assert t100401000_x11(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t100401000_x34():
    """State 0,1"""
    assert t100401000_x1()
    """State 2"""
    return 0

def t100401000_x35():
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

def t100401000_x36(text20=_, flag43=-1, text21=_, flag44=-1, text22=_, flag45=-1):
    """State 0,5"""
    assert t100401000_x3(z5=3)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t100401000_x31(text2=text20, flag7=flag43, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t100401000_x31(text2=text21, flag7=flag44, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t100401000_x31(text2=text22, flag7=flag45, mode7=1)
    """State 6"""
    return 0

def t100401000_x37(action1=21022003, action2=21022004):
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

def t100401000_x38(text18=10209400, flag41=-1, text19=10209500, flag42=-1):
    """State 0,4"""
    assert t100401000_x3(z5=2)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t100401000_x31(text2=text18, flag7=flag41, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t100401000_x31(text2=text19, flag7=flag42, mode7=1)
    """State 5"""
    return 0

def t100401000_x39(text20=_, flag38=_, text21=_, flag39=_, text22=_, flag40=_):
    """State 0"""
    if not GetEventFlag(flag38):
        """State 1"""
        assert t100401000_x31(text2=text20, flag7=flag38, mode7=1)
    elif not GetEventFlag(flag39):
        """State 2"""
        assert t100401000_x31(text2=text21, flag7=flag39, mode7=1)
    elif not GetEventFlag(flag40):
        """State 3"""
        assert t100401000_x31(text2=text22, flag7=flag40, mode7=1)
    else:
        """State 4"""
        assert t100401000_x36(text20=text20, flag43=-1, text21=text21, flag44=-1, text22=text22, flag45=-1)
    """State 5"""
    return 0

def t100401000_x40(text18=10209400, flag36=1209162, text19=10209500, flag37=1209163):
    """State 0"""
    if not GetEventFlag(flag36):
        """State 1"""
        assert t100401000_x31(text2=text18, flag7=flag36, mode7=1)
    elif not GetEventFlag(flag37):
        """State 2"""
        assert t100401000_x31(text2=text19, flag7=flag37, mode7=1)
    else:
        """State 3"""
        assert t100401000_x38(text18=text18, flag41=-1, text19=text19, flag42=-1)
    """State 4"""
    return 0

def t100401000_x41(text15=_, flag33=_, text16=_, flag34=_, text17=_, flag35=_):
    """State 0"""
    if not GetEventFlag(flag33):
        """State 2"""
        Label('L0')
        assert t100401000_x31(text2=text15, flag7=flag33, mode7=1)
    elif not GetEventFlag(flag34):
        """State 3"""
        assert t100401000_x31(text2=text16, flag7=flag34, mode7=1)
    elif not GetEventFlag(flag35):
        """State 4"""
        assert t100401000_x31(text2=text17, flag7=flag35, mode7=1)
    else:
        """State 1"""
        SetEventFlag(flag33, FlagState.Off)
        SetEventFlag(flag34, FlagState.Off)
        SetEventFlag(flag35, FlagState.Off)
        Goto('L0')
    """State 5"""
    return 0

def t100401000_x42(text10=10210700, flag23=1209171, text11=10210800, flag24=1209172, text12=10210900, flag25=1209173,
                   text13=10211000, flag26=1209174, text14=10211100, flag27=1209175):
    """State 0"""
    if not GetEventFlag(flag23):
        """State 1"""
        assert t100401000_x31(text2=text10, flag7=flag23, mode7=1)
    elif not GetEventFlag(flag24):
        """State 2"""
        assert t100401000_x31(text2=text11, flag7=flag24, mode7=1)
    elif not GetEventFlag(flag25):
        """State 3"""
        assert t100401000_x31(text2=text12, flag7=flag25, mode7=1)
    elif not GetEventFlag(flag26):
        """State 4"""
        assert t100401000_x31(text2=text13, flag7=flag26, mode7=1)
    elif not GetEventFlag(flag27):
        """State 5"""
        assert t100401000_x31(text2=text14, flag7=flag27, mode7=1)
    else:
        """State 6"""
        assert (t100401000_x43(text10=text10, flag28=-1, text11=text11, flag29=-1, text12=text12, flag30=-1, text13=text13,
                flag31=-1, text14=text14, flag32=-1))
    """State 7"""
    return 0

def t100401000_x43(text10=10210700, flag28=-1, text11=10210800, flag29=-1, text12=10210900, flag30=-1, text13=10211000,
                   flag31=-1, text14=10211100, flag32=-1):
    """State 0,5"""
    assert t100401000_x3(z5=5)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t100401000_x31(text2=text10, flag7=flag28, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t100401000_x31(text2=text11, flag7=flag29, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t100401000_x31(text2=text12, flag7=flag30, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t100401000_x31(text2=text13, flag7=flag31, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t100401000_x31(text2=text14, flag7=flag32, mode7=1)
    """State 8"""
    return 0

def t100401000_x44(text3=10210700, flag16=-1, text4=10210800, flag17=-1, text5=10211000, flag18=-1, text6=10211100,
                   flag19=-1, text7=10211200, flag20=-1, text8=10211300, flag21=-1, text9=10211400, flag22=-1):
    """State 0,5"""
    assert t100401000_x3(z5=7)
    """State 1"""
    if CompareRNGValue(CompareType.Equal, 0) == True:
        """State 2"""
        assert t100401000_x31(text2=text3, flag7=flag16, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 1) == True:
        """State 3"""
        assert t100401000_x31(text2=text4, flag7=flag17, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 2) == True:
        """State 4"""
        assert t100401000_x31(text2=text5, flag7=flag18, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 3) == True:
        """State 6"""
        assert t100401000_x31(text2=text6, flag7=flag19, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 4) == True:
        """State 7"""
        assert t100401000_x31(text2=text7, flag7=flag20, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 5) == True:
        """State 8"""
        assert t100401000_x31(text2=text8, flag7=flag21, mode7=1)
    elif CompareRNGValue(CompareType.Equal, 6) == True:
        """State 9"""
        assert t100401000_x31(text2=text9, flag7=flag22, mode7=1)
    """State 10"""
    return 0

def t100401000_x45(text3=10210700, flag9=1209171, text4=10210800, flag10=1209172, text5=10211000, flag11=1209174,
                   text6=10211100, flag12=1209175, text7=10211200, flag13=1209176, text8=10211300, flag14=1209177,
                   text9=10211400, flag15=1209178):
    """State 0"""
    if not GetEventFlag(flag9):
        """State 1"""
        assert t100401000_x31(text2=text3, flag7=flag9, mode7=1)
    elif not GetEventFlag(flag10):
        """State 2"""
        assert t100401000_x31(text2=text4, flag7=flag10, mode7=1)
    elif not GetEventFlag(flag11):
        """State 3"""
        assert t100401000_x31(text2=text5, flag7=flag11, mode7=1)
    elif not GetEventFlag(flag12):
        """State 4"""
        assert t100401000_x31(text2=text6, flag7=flag12, mode7=1)
    elif not GetEventFlag(flag13):
        """State 5"""
        assert t100401000_x31(text2=text7, flag7=flag13, mode7=1)
    elif not GetEventFlag(flag14):
        """State 6"""
        assert t100401000_x31(text2=text8, flag7=flag14, mode7=1)
    elif not GetEventFlag(flag15):
        """State 7"""
        assert t100401000_x31(text2=text9, flag7=flag15, mode7=1)
    else:
        """State 8"""
        assert (t100401000_x44(text3=text3, flag16=-1, text4=text4, flag17=-1, text5=text5, flag18=-1, text6=text6,
                flag19=-1, text7=text7, flag20=-1, text8=text8, flag21=-1, text9=text9, flag22=-1))
    """State 9"""
    return 0

def t100401000_x46():
    """State 0,1"""
    if not f308(4) == 20300:
        """State 3"""
        if DoesSelfHaveSpEffect(9675):
            """State 7,15"""
            # talk:10201700:"What is it? You can tell me."
            assert t100401000_x31(text2=10201700, flag7=1209153, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9676):
            """State 8,16"""
            # talk:10210400:"Do you need help with something?"
            assert t100401000_x31(text2=10210400, flag7=1209154, mode7=1)
            Goto('L0')
        elif DoesSelfHaveSpEffect(9677):
            """State 9"""
            pass
        else:
            """State 10"""
            pass
        """State 17"""
        # talk:10210500:"You are always welcome."
        assert t100401000_x31(text2=10210500, flag7=1209155, mode7=1)
    elif f308(4) == 20300:
        """State 2"""
        if GetEventFlag(10002010):
            """State 4,12"""
            # talk:10209200:"Speak, as you wish."
            assert t100401000_x31(text2=10209200, flag7=1209151, mode7=1)
        elif GetEventFlag(10002011):
            """State 5,13"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            assert t100401000_x31(text2=10200200, flag7=1209150, mode7=1)
        elif GetEventFlag(10002012):
            """State 6,14"""
            # talk:10209200:"Speak, as you wish."
            assert t100401000_x31(text2=10209200, flag7=1209151, mode7=1)
        else:
            """State 11"""
            # talk:10200200:"What is it? I will do my utmost to aid you."
            # talk:10209200:"Speak, as you wish."
            # talk:10209300:"How can I help?"
            assert (t100401000_x41(text15=10200200, flag33=1209150, text16=10209200, flag34=1209151, text17=10209300,
                    flag35=1209152))
    """State 18"""
    Label('L0')
    return 0

def t100401000_x47(mode1=1):
    """State 0,1"""
    if GetTalkListEntryResult() == 1:
        """State 9,14"""
        assert t100401000_x52()
    elif GetTalkListEntryResult() == 98:
        """State 8,13"""
        assert t100401000_x51()
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
                assert (t100401000_x41(text15=10201800, flag33=1209159, text16=10210200, flag34=1209160, text17=10210300,
                        flag35=1209161))
            elif f308(4) == 20300:
                """State 5,16"""
                assert t100401000_x59()
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

def t100401000_x48(mode2=_):
    """State 0,1"""
    ClearTalkListData()
    ClearPreviousMenuSelection()
    """State 3"""
    assert t100401000_x57()
    """State 2"""
    # action:20000100:"Talk"
    AddTalkListDataAltIf(mode2 == 1, 98, 20000100, -1, 98, False)
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 99, False)
    """State 4"""
    return 0

def t100401000_x49():
    """State 0,1"""
    # eventflag:2001:Title start (test version)
    if GetEventFlag(2001):
        """State 6"""
        assert t100401000_x56()
    else:
        """State 2"""
        assert t100401000_x46()
        """State 4"""
        assert t100401000_x48(mode2=1)
        """State 5"""
        assert t100401000_x50()
        """State 3"""
        assert t100401000_x47(mode1=1)
    """State 7"""
    return 0

def t100401000_x50():
    """State 0,1"""
    ShowShopMessageAlt(TalkOptionsType.Old, True)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t100401000_x51():
    """State 0"""
    if f308(4) == 20300:
        """State 1"""
        assert t100401000_x54()
    elif not f308(4) == 20300:
        """State 2"""
        assert t100401000_x55()
    """State 3"""
    return 0

def t100401000_x52():
    """State 0"""
    if not GetEventFlag(1209180):
        """State 1,3"""
        # talk:10201400:"Is that...?"
        # talk:10201401:"I'm sorry, but that's the timepiece I misplaced."
        # talk:10201402:"Could I trouble you to have it back?"
        assert t100401000_x31(text2=10201400, flag7=1209179, mode7=1)
        """State 4"""
        assert t100401000_x53()
    elif GetEventFlag(1209180):
        """State 2,5"""
        # talk:10205300:"Won't you please part with the pocketwatch?"
        assert t100401000_x31(text2=10205300, flag7=1209181, mode7=1)
        """State 6"""
        assert t100401000_x53()
    """State 7"""
    return 0

def t100401000_x53():
    """State 0,7"""
    # action:21022003:"Give it to her"
    # action:21022004:"Keep it"
    call = t100401000_x37(action1=21022003, action2=21022004)
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
        assert t100401000_x30(text1=10201600, flag3=1209180, mode8=1)
    """State 8"""
    return 0

def t100401000_x54():
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
        assert (t100401000_x39(text20=10209900, flag38=1209167, text21=10210000, flag39=1209168, text22=10210100,
                flag40=1209169))
    # eventflag:110:First cleared
    elif GetEventFlag(110):
        """State 2,5"""
        # talk:10209800:"How are you finding the Roundtable?"
        # talk:10209801:"I pray that you will be met with some comfort here."
        assert t100401000_x31(text2=10209800, flag7=1209166, mode7=1)
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        assert t100401000_x58()
    """State 7"""
    return 0

def t100401000_x55():
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
        assert (t100401000_x45(text3=10210700, flag9=1209171, text4=10210800, flag10=1209172, text5=10211000, flag11=1209174,
                text6=10211100, flag12=1209175, text7=10211200, flag13=1209176, text8=10211300, flag14=1209177,
                text9=10211400, flag15=1209178))
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
        assert (t100401000_x42(text10=10210700, flag23=1209171, text11=10210800, flag24=1209172, text12=10210900,
                flag25=1209173, text13=10211000, flag26=1209174, text14=10211100, flag27=1209175))
    # eventflag:110:First cleared
    elif not GetEventFlag(110):
        """State 1,4"""
        # talk:10210600:"What a dreadful creature..."
        # talk:10210700:"If you ever find yourself at your wit's end, just remember."
        # talk:10210701:"The sun will rise again. The wheel does not cease to turn."
        # talk:10210800:"I'm better with technical weaponry."
        # talk:10210801:"...Heavier armaments are not my forte..."
        assert (t100401000_x39(text20=10210600, flag38=1209170, text21=10210700, flag39=1209171, text22=10210800,
                flag40=1209172))
    """State 7"""
    return 0

def t100401000_x56():
    """State 0,1"""
    # talk:10210400:"Do you need help with something?"
    assert t100401000_x32(text23=10210400, mode6=1)
    """State 2"""
    return 0

def t100401000_x57():
    """State 0,1"""
    # eventflag:6031:Hero Unlock Flag_Lady
    if not GetEventFlag(6031):
        """State 3"""
        if f301(-1) == 0 or f301(-1) == 10:
            """State 8"""
            if GetCurrentScenarioSection() == 0:
                """State 4"""
                if GetEventFlag(10001810):
                    """State 2"""
                    # action:21020024:"Show her the old pocketwatch"
                    AddTalkListDataAlt(1, 21020024, -1, 1, False)
                else:
                    """State 7"""
                    pass
            else:
                """State 9"""
                pass
        else:
            """State 6"""
            pass
    else:
        """State 5"""
        pass
    """State 10"""
    return 0

def t100401000_x58():
    """State 0,1"""
    if True:
        """State 2,4"""
        # talk:10209400:"Did you encounter the beast? That is our quarry."
        # talk:10209401:"...How did we allow so much time to slip by..."
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t100401000_x40(text18=10209400, flag36=1209162, text19=10209500, flag37=1209163)
    else:
        """State 3,5"""
        # talk:10209500:"We have nothing to fear of the Night while I am here at the Roundtable."
        # talk:10209501:"It is one of the few unwavering powers I have been bequeathed."
        assert t100401000_x31(text2=10209500, flag7=1209163, mode7=1)
    """State 6"""
    return 0

def t100401000_x59():
    """State 0"""
    if GetEventFlag(10002010):
        """State 1,5"""
        # talk:10209000:"I await your return."
        assert t100401000_x31(text2=10209000, flag7=1209157, mode7=1)
    elif GetEventFlag(10002011):
        """State 2,6"""
        # talk:10200500:"Fortune favours the well-prepared."
        assert t100401000_x31(text2=10200500, flag7=1209156, mode7=1)
    elif GetEventFlag(10002012):
        """State 3,7"""
        # talk:10209100:"May you triumph in battle."
        assert t100401000_x31(text2=10209100, flag7=1209158, mode7=1)
    else:
        """State 4"""
        # talk:10200500:"Fortune favours the well-prepared."
        # talk:10209000:"I await your return."
        # talk:10209100:"May you triumph in battle."
        assert (t100401000_x41(text15=10200500, flag33=1209156, text16=10209000, flag34=1209157, text17=10209100,
                flag35=1209158))
    """State 8"""
    return 0

def t100401000_x60():
    """State 0,1"""
    if GetEventFlag(10002013) and not f308(4) == 20300 and not GetEventFlag(1209182):
        """State 2,4"""
        # talk:10211800:"We must prepare for the next battle."
        assert t100401000_x31(text2=10211800, flag7=1209182, mode7=1)
    else:
        """State 3"""
        assert t100401000_x61()
    """State 5"""
    return 0

def t100401000_x61():
    """State 0"""
    if f310(0) == 1 and f308(4) == 20300:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t100401000_x62()
    elif f310(0) == 2 and f308(4) == 20300:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t100401000_x71()
    elif f310(0) == 3 and f308(4) == 20300:
        """State 7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t100401000_x63()
    elif f310(0) == 4 and f308(4) == 20300:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t100401000_x64()
    elif f301(-1) == 10:
        """State 2,3"""
        Label('L0')
        def WhilePaused():
            RequestAnimation(90300, -1)
            SetLookAtEntityForTalkIf(GetEventFlag(10003013), 10000712, 10000)
        assert t100401000_x49()
    else:
        """State 1"""
        Goto('L0')
    """State 8"""
    return 0

def t100401000_x62():
    """State 0"""
    if GetEventFlag(3001):
        """State 1"""
        if GetEventFlag(10002010) and not GetEventFlag(1109001):
            """State 3,6"""
            assert t100401000_x67()
        else:
            """State 4"""
            assert t100401000_x66()
    else:
        """State 2,5"""
        assert t100401000_x49()
    """State 7"""
    return 0

def t100401000_x63():
    """State 0"""
    if GetEventFlag(3003):
        """State 1,5"""
        assert t100401000_x74()
    elif GetEventFlag(3004):
        """State 2"""
        # eventflag:111:2nd night boss defeats on the 3rd day
        if GetEventFlag(111) or GetEventFlag(1109043):
            """State 4,8"""
            assert t100401000_x84()
        # eventflag:111:2nd night boss defeats on the 3rd day
        elif not GetEventFlag(111):
            """State 6"""
            assert t100401000_x75()
    else:
        """State 3,7"""
        assert t100401000_x49()
    """State 9"""
    return 0

def t100401000_x64():
    """State 0"""
    if GetEventFlag(3006):
        """State 1,7"""
        if GetCurrentScenarioSection() == 0:
            """State 5,9"""
            # talk:10207100:"I cannot help but think... We were an odd lot, weren't we?"
            # talk:10207101:"Thrown together by forces beyond our control, with no choice but to accept our duty to fight."
            # talk:10207102:"You, for one, were up to the task. And for that, you have my deepest gratitude."
            # talk:10207103:"Eventually, there will be a time to celebrate. When our work is complete."
            # talk:10207104:"For now, let us bury this devourer of worlds."
            assert t100401000_x31(text2=10207100, flag7=1109010, mode7=1)
        else:
            """State 6,8,10"""
            Label('L0')
            assert t100401000_x76()
    elif GetEventFlag(3007):
        """State 2"""
        Goto('L0')
    elif GetEventFlag(3008):
        """State 4"""
        Goto('L0')
    else:
        """State 3,11"""
        assert t100401000_x49()
    """State 12"""
    return 0

def t100401000_x65(flag5=_, flag6=_, text2=_, flag7=_, flag8=_):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t100401000_x0(actionbutton1=6000, flag50=6001, flag54=6000, flag55=6000, flag56=6000, flag57=6000,
                             flag8=flag8)
        if call.Done():
            break
        elif GetEventFlag(flag5):
            pass
        """State 3"""
        SetEventFlag(flag5, FlagState.Off)
        SetEventFlag(flag8, FlagState.Off)
        """State 6"""
        call = t100401000_x31(text2=text2, flag7=flag7, mode7=1)
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 8:
            """State 7"""
            assert t100401000_x1()
        """State 2"""
        SetTalkTime(0.5)
        """State 4"""
        SetEventFlag(flag6, FlagState.On)
        SetEventFlag(10002001, FlagState.Off)
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t100401000_x66():
    """State 0,4"""
    assert t100401000_x46()
    """State 5"""
    assert t100401000_x48(mode2=0)
    """State 8"""
    assert t100401000_x80()
    """State 1"""
    if not GetEventFlag(10002010):
        """State 2,9"""
        assert t100401000_x78()
    else:
        """State 3"""
        pass
    """State 6"""
    assert t100401000_x50()
    """State 7"""
    assert t100401000_x69()
    """State 10"""
    return 0

def t100401000_x67():
    """State 0,1"""
    # eventflag:6031:Hero Unlock Flag_Lady
    if not GetEventFlag(6031):
        """State 2,4"""
        # talk:10200400:"This is a hidden refuge. A place where warriors gather."
        # talk:10200401:"Rest assured, though it is in disrepair, you will be safe here."
        # talk:10200402:"We even have a caretaker. He might strike you as...odd..."
        # talk:10200403:"...But he is worthy of trust. Speak to him, if you please."
        assert t100401000_x31(text2=10200400, flag7=1109001, mode7=1)
    # eventflag:6031:Hero Unlock Flag_Lady
    elif GetEventFlag(6031):
        """State 3,5"""
        # talk:10200300:"This is a hidden refuge. A place where warriors gather."
        # talk:10200301:"Rest assured, though it is in disrepair, you will be safe here."
        # talk:10200302:"We even have a caretaker. He might strike you as...odd..."
        # talk:10200303:"...But he is worthy of trust. Speak to him, if you please."
        assert t100401000_x31(text2=10200300, flag7=1109002, mode7=1)
    """State 6"""
    return 0

def t100401000_x68():
    """State 0,1"""
    assert t100401000_x46()
    """State 2"""
    assert t100401000_x48(mode2=1)
    """State 6"""
    assert t100401000_x80()
    """State 5"""
    assert t100401000_x78()
    """State 7"""
    assert t100401000_x82()
    """State 3"""
    assert t100401000_x50()
    """State 4"""
    assert t100401000_x69()
    """State 8"""
    return 0

def t100401000_x69():
    """State 0,1"""
    if GetTalkListEntryResult() == 30:
        """State 7,15"""
        assert t100401000_x81()
    elif GetTalkListEntryResult() == 29:
        """State 3,14"""
        assert t100401000_x77()
    elif GetTalkListEntryResult() == 28:
        """State 8,16"""
        assert t100401000_x83()
    elif GetTalkListEntryResult() == 27:
        """State 5,12"""
        assert t100401000_x73()
    elif GetTalkListEntryResult() == 26:
        """State 9,17"""
        assert t100401000_x86()
    else:
        """State 6,13"""
        assert t100401000_x47(mode1=1)
    """State 18"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    Goto('L1')
    """State 4"""
    Goto('L2')
    """State 10"""
    Label('L1')
    assert t100401000_x67()
    Goto('L0')
    """State 11"""
    Label('L2')
    assert t100401000_x70()
    Goto('L0')

def t100401000_x70():
    """State 0,3"""
    # talk:10208800:"Indeed, our world faces a grave threat."
    # talk:10208801:"This is what I understand."
    assert t100401000_x31(text2=10208800, flag7=1109004, mode7=1)
    """State 1"""
    SetEventFlag(10002000, FlagState.On)
    SetTalkTime(1)
    """State 2"""
    assert not GetEventFlag(10002000)
    """State 4"""
    # talk:10208900:"But here we stand, warriors, chosen to atone."
    # talk:10208901:"Chosen to vanquish the Night."
    # talk:10208902:"To purge the darkness that would claim this world of mortals."
    # talk:10208903:"And for this...we have only three days."
    assert t100401000_x31(text2=10208900, flag7=1109005, mode7=1)
    """State 5"""
    return 0

def t100401000_x71():
    """State 0"""
    if GetEventFlag(3002):
        """State 1,3"""
        assert t100401000_x68()
    else:
        """State 2,4"""
        assert t100401000_x49()
    """State 5"""
    return 0

def t100401000_x72():
    """State 0,1"""
    # action:21020022:"Why have other Nightlords appeared?"
    AddTalkListDataAlt(27, 21020022, -1, 27, False)
    """State 2"""
    return 0

def t100401000_x73():
    """State 0,2"""
    # talk:10211600:"There are others. Too many, I am afraid."
    # talk:10211601:"It is not yet clear what this means."
    # talk:10211602:"But that beast left a trace."
    # talk:10211603:"And I believe with traces enough, the parts will begin to resemble a whole."
    # talk:10211604:"As such, our purpose remains unchanged."
    # talk:10211605:"Stay the path. And vanquish our foes. I pray for your success."
    assert t100401000_x31(text2=10211600, flag7=1109007, mode7=1)
    """State 1"""
    SetEventFlag(1109006, FlagState.On)
    """State 3"""
    return 0

def t100401000_x74():
    """State 0,1"""
    assert t100401000_x46()
    """State 2"""
    assert t100401000_x48(mode2=1)
    """State 6"""
    assert t100401000_x80()
    """State 5"""
    assert t100401000_x78()
    """State 7"""
    assert t100401000_x72()
    """State 3"""
    assert t100401000_x50()
    """State 4"""
    assert t100401000_x69()
    """State 8"""
    return 0

def t100401000_x75():
    """State 0,1"""
    assert t100401000_x46()
    """State 2"""
    assert t100401000_x48(mode2=1)
    """State 6"""
    assert t100401000_x80()
    """State 5"""
    assert t100401000_x78()
    """State 3"""
    assert t100401000_x50()
    """State 4"""
    assert t100401000_x69()
    """State 7"""
    return 0

def t100401000_x76():
    """State 0,1"""
    assert t100401000_x46()
    """State 2"""
    assert t100401000_x48(mode2=1)
    """State 5"""
    assert t100401000_x80()
    """State 6"""
    assert t100401000_x78()
    """State 3"""
    assert t100401000_x50()
    """State 4"""
    assert t100401000_x69()
    """State 7"""
    return 0

def t100401000_x77():
    """State 0,1"""
    # talk:10205100:"When you first awoke?"
    # talk:10205101:"I did not believe you had any recollection of this Roundtable,"
    # talk:10205102:"but we have fought together countless times."
    # talk:10205103:"Do not be afraid."
    # talk:10205104:"Remember well, that above all else we are allies."
    # talk:10205105:"It is good to have you. Once again."
    assert t100401000_x31(text2=10205100, flag7=1109003, mode7=1)
    """State 2"""
    return 0

def t100401000_x78():
    """State 0,1"""
    # action:21020010:"About what you spoke of..."
    AddTalkListDataAltIf(GetChrHero() == Hero.Wylder, 29, 21020010, -1, 29, False)
    """State 2"""
    return 0

def t100401000_x79(flag1=10003004, flag2=10003005, text1=10207000, flag3=1109009, flag4=10003007):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t100401000_x0(actionbutton1=6000, flag50=6001, flag54=6000, flag55=6000, flag56=6000, flag57=6000,
                             flag8=10003007)
        if call.Done():
            break
        elif GetEventFlag(flag1):
            pass
        """State 3"""
        SetEventFlag(flag1, FlagState.Off)
        SetEventFlag(flag4, FlagState.Off)
        """State 7"""
        call = t100401000_x30(text1=text1, flag3=flag3, mode8=1)
        def WhilePaused():
            RequestAnimation(90300, -1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 8:
            """State 6"""
            assert t100401000_x1()
        """State 2"""
        SetTalkTime(0.5)
        """State 4"""
        SetEventFlag(flag2, FlagState.On)
    """State 1"""
    EndMachine(2000)
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t100401000_x80():
    """State 0,1"""
    # action:21020029:"What does "our formless master" have to say?"
    AddTalkListDataAlt(30, 21020029, -1, 30, False)
    """State 2"""
    return 0

def t100401000_x81():
    """State 0,1"""
    # eventflag:6031:Hero Unlock Flag_Lady
    if not GetEventFlag(6031):
        """State 2,4"""
        # talk:10200600:"This message is for you. You will hear it often."
        # talk:10200601:""Seekers of redemption.""
        # talk:10200602:""On the third night, this land will fall.""
        # talk:10200603:""Band together, and prepare to claim...""
        # talk:10200604:""The life of the Nightlord.""
        # talk:10200605:"That is all."
        # talk:10200606:"..."
        # talk:10200607:"Regrettably, I have no means to fight."
        # talk:10200608:"It might strike you as presumptuous, but I am in need of your help all the same."
        assert t100401000_x31(text2=10200600, flag7=1109012, mode7=1)
    # eventflag:6031:Hero Unlock Flag_Lady
    elif GetEventFlag(6031):
        """State 3,5"""
        # talk:10200620:"This message is for you. You will hear it often."
        # talk:10200621:""Seekers of redemption.""
        # talk:10200622:""On the third night, this land will fall.""
        # talk:10200623:""Band together, and prepare to claim...""
        # talk:10200624:""The life of the Nightlord.""
        # talk:10200625:"That is all."
        assert t100401000_x31(text2=10200620, flag7=1109016, mode7=1)
    """State 6"""
    return 0

def t100401000_x82():
    """State 0,1"""
    # action:21020030:"Ask about the Nightlord"
    AddTalkListDataAlt(28, 21020030, -1, 28, False)
    """State 2"""
    return 0

def t100401000_x83():
    """State 0,1"""
    # talk:10211900:"The Nightlord takes the form of a three-headed beast."
    # talk:10211901:"Brave Nightfarers."
    # talk:10211902:"Travel to the land of Limveld."
    # talk:10211903:"There, in the dead of the third night,\nthis dread Lord will await you."
    assert t100401000_x31(text2=10211900, flag7=1109013, mode7=1)
    """State 2"""
    return 0

def t100401000_x84():
    """State 0,1"""
    # talk:10212000:"Have you found any Traces of Night?"
    assert t100401000_x31(text2=10212000, flag7=1109014, mode7=1)
    """State 2"""
    assert t100401000_x48(mode2=1)
    """State 4"""
    assert t100401000_x80()
    """State 5"""
    assert t100401000_x78()
    """State 3"""
    assert t100401000_x85()
    """State 6"""
    assert t100401000_x50()
    """State 7"""
    assert t100401000_x69()
    """State 8"""
    return 0

def t100401000_x85():
    """State 0,1"""
    # action:21020031:"Ask about Traces of Night"
    AddTalkListDataAlt(26, 21020031, -1, 26, False)
    """State 2"""
    return 0

def t100401000_x86():
    """State 0,1"""
    # talk:10212100:"Each Trace of Night is a beacon."
    # talk:10212101:"That reveals a larger truth."
    # talk:10212102:"Defeat the Nightlords, as you did the beast, to claim four Traces of Night."
    # talk:10212103:"Only then..."
    # talk:10212104:"Will the light reveal what lies beyond."
    assert t100401000_x31(text2=10212100, flag7=1109015, mode7=1)
    """State 2"""
    return 0

