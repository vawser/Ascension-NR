# -*- coding: utf-8 -*-
def t991001000_1():
    """State 0,1"""
    # eventflag:6000:Flag to always be OFF
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    t991001000_x5(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1)
    Quit()

def t991001000_1000():
    """State 0,2,5"""
    if f301(-1) == Hero.Wylder:
        """State 3,6"""
        if f302(-1) == 1:
            """State 4,11"""
            assert t991001000_x34()
        elif f302(-1) == 2:
            """State 7,12"""
            assert t991001000_x35()
        else:
            """State 9,10,13"""
            Label('L0')
            # talk:30900200:"How are you faring today, champion?"
            assert t991001000_x30(text1=30900200, flag9=-1, mode3=1)
    else:
        """State 8"""
        Goto('L0')
    """State 1"""
    EndMachine(1000)
    Quit()

def t991001000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    # eventflag:6001:Flag to always be ON
    # eventflag:6000:Flag to always be OFF
    assert t991001000_x0(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag4=6000)
    """State 1"""
    EndMachine(2000)
    Quit()

def t991001000_x0(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert (GetEventFlag(flag5) or GetEventFlag(flag11) or GetEventFlag(flag12) or GetEventFlag(flag13) or
                GetEventFlag(flag14))
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag4)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag4) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag5) and not GetEventFlag(flag11) and not GetEventFlag(flag12) and not GetEventFlag(flag13)
            and not GetEventFlag(flag14))):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t991001000_x1():
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

def t991001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t991001000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if PlayerDiedFromFallInstantly() == False and PlayerDiedFromFallDamage() == False:
        """State 3,6"""
        call = t991001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t991001000_x1()
    else:
        """State 4,7"""
        call = t991001000_x31()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t991001000_x1()
    """State 9"""
    return 0

def t991001000_x4():
    """State 0,1"""
    assert t991001000_x1()
    """State 2"""
    return 0

def t991001000_x5(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t991001000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3, val4=val4,
                              val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7,
                              flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        assert IsClientPlayer()
        """State 1"""
        call = t991001000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t991001000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001, flag6=6001,
                  flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t991001000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            ChangeCamera(1000000)
            call = t991001000_x13(val1=val1, z1=z1)
            def WhilePaused():
                ChangeCameraIf(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() and (DoesSelfHaveSpEffect(9626) and DoesSelfHaveSpEffect(9627)))
                GiveSpEffectToPlayer(9640)
                SetLookAtEntityForTalkIf(mode1 == 1, -1, 0)
                SetLookAtEntityForTalkIf(mode2 == 1, 0, -1)
            def ExitPause():
                ChangeCamera(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif IsAttackedBySomeone() and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag8):
            Goto('L0')
        # eventflag:6001:Flag to always be ON
        elif GetEventFlag(flag6) and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t991001000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone():
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t991001000_x26() and CheckSpecificPersonTalkHasEnded(0)
            continue
        elif GetEventFlag(9000):
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t991001000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t991001000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t991001000_x17(val2=val2, val3=val3)
    assert IsPlayerDead()
    """State 2"""
    t991001000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t991001000_x8(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t991001000_x33()
    """State 1"""
    # eventflag:6000:Flag to always be OFF
    if GetEventFlag(flag1):
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t991001000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t991001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t991001000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t991001000_x10(machine1=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        assert (t991001000_x0(actionbutton1=actionbutton1, flag5=flag5, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t991001000_x10(machine1=_, val6=_):
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

def t991001000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t991001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking():
            """State 6"""
            call = t991001000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t991001000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t991001000_x12():
    """State 0,1"""
    assert t991001000_x10(machine1=1101, val6=1101)
    """State 2"""
    return 0

def t991001000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t991001000_x23()
    """State 1"""
    call = t991001000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t991001000_x25()
    """State 4"""
    return 0

def t991001000_x14():
    """State 0,1"""
    assert t991001000_x10(machine1=1000, val6=1000)
    """State 2"""
    return 0

def t991001000_x15(val5=12):
    """State 0,1"""
    call = t991001000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t991001000_x26()
    """State 3"""
    return 0

def t991001000_x16():
    """State 0,1"""
    assert t991001000_x10(machine1=1100, val6=1100)
    """State 2"""
    return 0

def t991001000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t991001000_x33()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t991001000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t991001000_x28()
    """Unused"""
    """State 6"""
    return 0

def t991001000_x18():
    """State 0,2"""
    call = t991001000_x10(machine1=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t991001000_x19():
    """State 0,1"""
    assert t991001000_x10(machine1=1001, val6=1001)
    """State 2"""
    return 0

def t991001000_x20():
    """State 0,1"""
    assert t991001000_x10(machine1=1103, val6=1103)
    """State 2"""
    return 0

def t991001000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t991001000_x22(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                   mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t991001000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3,
                             z4=z4, mode1=mode1, mode2=mode2)
        # eventflag:6000:Flag to always be OFF
        if CheckSelfDeath() or GetEventFlag(flag1):
            """State 3"""
            Label('L0')
            call = t991001000_x8(flag1=flag1, val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000):
                pass
        # eventflag:6000:Flag to always be OFF
        elif GetEventFlag(flag2) or GetEventFlag(flag3):
            """State 2"""
            call = t991001000_x7(val2=val2, val3=val3)
            # eventflag:6000:Flag to always be OFF
            if CheckSelfDeath() or GetEventFlag(flag1):
                Goto('L0')
            # eventflag:6000:Flag to always be OFF
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000):
                pass
        elif GetEventFlag(9000) or (IsPlayerDead() and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t991001000_x32() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t991001000_x23():
    """State 0,1"""
    assert t991001000_x24()
    """State 2"""
    return 0

def t991001000_x24():
    """State 0,1"""
    assert t991001000_x10(machine1=1104, val6=1104)
    """State 2"""
    return 0

def t991001000_x25():
    """State 0,1"""
    call = t991001000_x10(machine1=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t991001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t991001000_x26():
    """State 0,1"""
    call = t991001000_x10(machine1=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t991001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t991001000_x27():
    """State 0,1"""
    call = t991001000_x10(machine1=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t991001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t991001000_x28():
    """State 0,1"""
    call = t991001000_x10(machine1=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t991001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t991001000_x29(text2=_, flag10=_, mode4=1):
    """State 0,5"""
    assert t991001000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 2"""
    SetEventFlag(flag10, FlagState.On)
    """State 1"""
    TalkToPlayer(text2, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode4 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t991001000_x30(text1=_, flag9=_, mode3=1):
    """State 0,5"""
    assert t991001000_x2() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode3 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag9, FlagState.On)
    """State 6"""
    return 0

def t991001000_x31():
    """State 0,1"""
    assert t991001000_x10(machine1=1002, val6=1002)
    """State 2"""
    return 0

def t991001000_x32():
    """State 0,1"""
    assert t991001000_x1()
    """State 2"""
    return 0

def t991001000_x33():
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

def t991001000_x34():
    """State 0,10"""
    if f304(1010) == 0:
        """State 11,14,17"""
        # talk:30905700:"Wylder, I have a boon to ask of you."
        # talk:30905701:"Would it be possible for you to procure me a whetstone?"
        # talk:30905702:"I consider it my inviolable duty to keep everyone's armaments in tip-top shape."
        # talk:30905703:"But I'm afraid there's very little life left in the stone I have here."
        # talk:30905704:"You have a discerning eye, do you not?"
        # talk:30905705:"Would you be willing to hunt one down for me?"
        assert t991001000_x30(text1=30905700, flag9=10009405, mode3=1)
        """State 3"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 4"""
        # action:23090011:""
        AddTalkListData(1, 23090011, -1)
        # action:23090012:""
        AddTalkListData(2, 23090012, -1)
        """State 5"""
        ShowShopMessage(TalkOptionsType.Regular)
        """State 6"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        if GetTalkListEntryResult() == 1:
            """State 7,1"""
            c1_163(1010, 1)
            """State 21"""
            # talk:30905800:"Simply marvellous!"
            # talk:30905801:"I advise you make your way to the mining tunnel."
            # talk:30905802:"The underground passageways are sure to contain ore suitable for metalwork."
            # talk:30905803:"There are whetstones to be found there, I'm certain."
            assert t991001000_x29(text2=30905800, flag10=10009406, mode4=1)
        elif GetTalkListEntryResult() == 2:
            """State 8,18"""
            # talk:30905900:"Well. I see."
            # talk:30905901:"No matter. I'll make do with what's left."
            assert t991001000_x30(text1=30905900, flag9=-1, mode3=1)
        else:
            """State 9"""
            pass
    elif f304(1010) == 1:
        """State 12,15,19"""
        # talk:30905800:"Simply marvellous!"
        # talk:30905801:"I advise you make your way to the mining tunnel."
        # talk:30905802:"The underground passageways are sure to contain ore suitable for metalwork."
        # talk:30905803:"There are whetstones to be found there, I'm certain."
        assert t991001000_x30(text1=30905800, flag9=-1, mode3=1)
    else:
        """State 13,16,20"""
        # talk:30900200:"How are you faring today, champion?"
        assert t991001000_x30(text1=30900200, flag9=-1, mode3=1)
    """State 22"""
    return 0

def t991001000_x35():
    """State 0,1"""
    if f304(1010) == 2:
        """State 2,6,8"""
        c1_163(1010, 3)
        """State 9"""
        # talk:30906200:"Oh! You've managed to procure one. Very kind of you."
        # talk:30906201:"This will make repairing armaments much easier."
        # talk:30906202:"I've little to offer, but if anything strikes your fancy, consider it yours."
        assert t991001000_x29(text2=30906200, flag10=-1, mode4=1)
    elif f304(1010) == 3:
        """State 3,7,10"""
        # talk:30906400:"Once you're finished, be certain to return it to her."
        assert t991001000_x29(text2=30906400, flag10=-1, mode4=1)
    else:
        """State 4,5,11"""
        # talk:30900200:"How are you faring today, champion?"
        assert t991001000_x29(text2=30900200, flag10=-1, mode4=1)
    """State 12"""
    return 0

