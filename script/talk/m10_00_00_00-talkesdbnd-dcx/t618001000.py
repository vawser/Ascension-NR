# -*- coding: utf-8 -*-
def t618001000_1():
    """State 0,1"""
    SetUpdateDistance(200)
    """State 2"""
    t618001000_x4(flag1=10002707)
    def WhilePaused():
        RunMachine(14)
    Quit()

def t618001000_14():
    """State 0"""
    while True:
        """State 2"""
        assert GetDistanceToPlayer() < 5
        """State 1"""
        GiveSpEffectToPlayer(9653)
        if GetDistanceToPlayer() > 5.1:
            """State 3"""
            GiveSpEffectToPlayer(9654)
        # eventflag:202:Multiplayer
        elif GetEventFlag(202):
            """State 4"""
            assert GetCurrentStateElapsedTime() > 6
            """State 5"""
            GiveSpEffectToPlayer(9654)
            # eventflag:202:Multiplayer
            assert not GetEventFlag(202)

def t618001000_x0(action1=_):
    """State 0,1"""
    OpenGenericDialog(DialogBoxType.CenterBottom2, action1, DialogResult.Leave, DialogBoxStyle.Unk, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == DialogResult.Left:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t618001000_x1(actionbutton1=6913, flag3=6001, flag4=6000, flag5=6000, flag6=6000, flag7=6000, flag8=10003045):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5) or GetEventFlag(flag6) or GetEventFlag(flag7)
        """State 4"""
        assert not GetEventFlag(flag8)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        if (GetEventFlag(flag8) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag3) and not GetEventFlag(flag4) and not GetEventFlag(flag5) and not GetEventFlag(flag6)
            and not GetEventFlag(flag7)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6913:"Examine sign"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t618001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t618001000_x3(action2=26101090):
    """State 0,1"""
    # action:26101090:"Insufficient Sovereign Sigils"
    OpenGenericDialog(DialogBoxType.CenterBottom1, action2, DialogResult.Left, DialogBoxStyle.OrnateNoOptions, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t618001000_x4(flag1=10002707):
    """State 0"""
    while True:
        """State 9"""
        # actionbutton:6913:"Examine sign"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t618001000_x1(actionbutton1=6913, flag3=6001, flag4=6000, flag5=6000, flag6=6000, flag7=6000, flag8=10003045)
        if call.Done():
            """State 1"""
            pass
        elif GetEventFlag(flag1):
            """State 3"""
            assert GetDistanceToPlayer() < 5
        """State 7"""
        SetEventFlag(10001860, FlagState.On)
        """State 8"""
        call = t618001000_x5()
        if call.Done():
            """State 2"""
            pass
        elif GetDistanceToPlayer() > 5.1:
            """State 5,10"""
            assert t618001000_x2()
        """State 4"""
        SetEventFlag(flag1, FlagState.Off)
        """State 6"""
    """Unused"""
    """State 11"""
    return 0

def t618001000_x5():
    """State 0,3"""
    ClearPreviousMenuSelection()
    while True:
        """State 1,6"""
        ClearTalkListData()
        """State 7"""
        assert t618001000_x6()
        """State 2"""
        ShowShopMessageAlt(TalkOptionsType.Old, False)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 8"""
            assert t618001000_x7()
            continue
        elif GetTalkListEntryResult() == 2:
            """State 9"""
            call = t618001000_x8()
            if call.Get() == 1:
                continue
            elif call.Get() == 0:
                pass
        elif GetTalkListEntryResult() == 3:
            """State 10"""
            call = t618001000_x9()
            if call.Get() == 1:
                continue
            elif call.Get() == 0:
                pass
        elif GetTalkListEntryResult() == 4:
            """State 11"""
            call = t618001000_x10()
            if call.Get() == 1:
                continue
            elif call.Get() == 0:
                pass
        else:
            """State 4"""
            pass
        """State 12"""
        return 0

def t618001000_x6():
    """State 0,1"""
    # action:26100000:"View catalog"
    AddTalkListDataAlt(1, 26100000, -1, 0, False)
    """State 7"""
    if ComparePlayerInventoryNumber(4, 12002, CompareType.Equal, 1, False):
        """State 2"""
        # action:26100010:"Give Witch's Brooch"
        AddTalkListDataAlt(2, 26100010, -1, 0, False)
    elif ComparePlayerInventoryNumber(4, 12003, CompareType.Equal, 1, False):
        """State 6"""
        # action:26100011:"Give Cracked Witch's Brooch"
        AddTalkListDataAlt(2, 26100011, -1, 0, False)
    else:
        """State 8"""
        pass
    """State 3"""
    # eventflag:140:Rare Terrain Unlocked: Volcano
    # eventflag:141:Rare Terrain Unlocked: Snowy Mountain
    # eventflag:142:Rare Terrain Unlocked: Corruption
    # eventflag:143:Rare Terrain Unlocked: Noclone
    # action:26100020:"Conjure a shift in the earth"
    AddTalkListDataAltIf(GetEventFlag(140) or GetEventFlag(141) or GetEventFlag(142) or GetEventFlag(143), 3, 26100020,
                         -1, 0, False)
    """State 4"""
    # eventflag:113:4th night boss defeats on the 3rd day
    # eventflag:160:3-Day Table Mode: Defeat Nameless
    # eventflag:960:Saw normal ending flag
    # action:26100030:"Alter Great Site of Grace"
    AddTalkListDataAltIf(GetEventFlag(113) and (GetEventFlag(160) or GetEventFlag(960)), 4, 26100030, -1, 0, False)
    """State 5"""
    # action:20000009:"Leave"
    AddTalkListDataAlt(99, 20000009, -1, 0, False)
    """State 9"""
    return 0

def t618001000_x7():
    """State 0,1"""
    OpenCatalogShop(13000, 13999)
    assert not (CheckSpecificPersonMenuIsOpen(47, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2,3"""
    return 0

def t618001000_x8():
    """State 0,1,2"""
    if ComparePlayerInventoryNumber(4, 12002, CompareType.Equal, 1, False):
        """State 3,21"""
        # action:26101010:"Give Witch's Brooch\nand receive Cracked Witch's Brooch?\nRequired Sovereign Sigils: 3"
        call = t618001000_x0(action1=26101010)
        if call.Get() == 0:
            """State 6,14"""
            if CompareSovereignSigils(CompareType.GreaterOrEqual, 3):
                """State 15,13"""
                AddSovereignSigils(-3)
                """State 7"""
                # antique:12002:Witch's Brooch
                # antique:12003:Cracked Witch's Brooch
                ExchangeAntiques(12002, 12003)
                assert not IsMenuOpen(MenuType.Bonfire)
                """State 8"""
            else:
                """State 16,23"""
                # action:26101090:"Insufficient Sovereign Sigils"
                assert t618001000_x3(action2=26101090)
                """State 26"""
                Label('L0')
                return 1
        elif call.Get() == 1:
            """State 5"""
            Goto('L0')
    elif ComparePlayerInventoryNumber(4, 12003, CompareType.Equal, 1, False):
        """State 4,22"""
        # action:26101011:"Give Cracked Witch's Brooch\nand receive Witch's Brooch?\nRequired Sovereign Sigils: 3"
        call = t618001000_x0(action1=26101011)
        if call.Get() == 0:
            """State 9,17"""
            if CompareSovereignSigils(CompareType.GreaterOrEqual, 3):
                """State 19,20"""
                AddSovereignSigils(-3)
                """State 10"""
                # antique:12003:Cracked Witch's Brooch
                # antique:12002:Witch's Brooch
                ExchangeAntiques(12003, 12002)
                assert not IsMenuOpen(MenuType.Bonfire)
                """State 11"""
            else:
                """State 18,24"""
                # action:26101090:"Insufficient Sovereign Sigils"
                assert t618001000_x3(action2=26101090)
                Goto('L0')
        elif call.Get() == 1:
            """State 12"""
            Goto('L0')
    """State 25"""
    return 0

def t618001000_x9():
    """State 0,1"""
    while True:
        """State 3,2"""
        ClearTalkListData()
        """State 11"""
        assert t618001000_x11()
        """State 4"""
        ShowShopMessageAlt(TalkOptionsType.Old, False)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,12"""
            # action:26101021:"Conjure Crater?\nRequired Sovereign Sigils: 1"
            # eventflag:6070: During Fever: Volcano
            call = t618001000_x13(action1=26101021, flag2=6070)
            if call.Get() == 0:
                break
            elif call.Get() == 1:
                pass
        elif GetTalkListEntryResult() == 2:
            """State 7,13"""
            # action:26101022:"Conjure Mountaintop?\nRequired Sovereign Sigils: 1"
            # eventflag:6071: During Fever: Snowy mountain
            call = t618001000_x13(action1=26101022, flag2=6071)
            if call.Get() == 0:
                break
            elif call.Get() == 1:
                pass
        elif GetTalkListEntryResult() == 3:
            """State 8,14"""
            # action:26101023:"Conjure Rotted Woods?\nRequired Sovereign Sigils: 1"
            # eventflag:6072: During Fever: Corruption
            call = t618001000_x13(action1=26101023, flag2=6072)
            if call.Get() == 0:
                break
            elif call.Get() == 1:
                pass
        elif GetTalkListEntryResult() == 4:
            """State 9,15"""
            # action:26101024:"Conjure Noklateo, the Shrouded City?\nRequired Sovereign Sigils: 1"
            # eventflag:6073: During Fever: Noclone
            call = t618001000_x13(action1=26101024, flag2=6073)
            if call.Get() == 0:
                break
            elif call.Get() == 1:
                pass
        else:
            """State 10,17"""
            return 1
    """State 16"""
    return 0

def t618001000_x10():
    """State 0,1"""
    if not GetEventFlag(10001951):
        """State 3,15"""
        # action:26101030:"Restore Great Site of Grace to former illuminated state?\nRequired Sovereign Sigils: 1 (1st time only)"
        call = t618001000_x0(action1=26101030)
        if call.Get() == 0:
            """State 9"""
            if CompareSovereignSigils(CompareType.GreaterOrEqual, 1):
                """State 10,4"""
                AddSovereignSigils(-1)
                """State 5"""
                SetEventFlag(10002173, FlagState.On)
                assert not GetEventFlag(10002173)
                """State 12"""
                SetEventFlag(10001951, FlagState.On)
            else:
                """State 11,18"""
                # action:26101090:"Insufficient Sovereign Sigils"
                assert t618001000_x3(action2=26101090)
                """State 20"""
                Label('L0')
                return 1
        elif call.Get() == 1:
            Goto('L0')
    else:
        """State 2,6"""
        if not GetEventFlag(10001950):
            """State 7,16"""
            # action:26101031:"Restore Great Site of Grace to darkened state?"
            call = t618001000_x0(action1=26101031)
            if call.Get() == 0:
                """State 13"""
                SetEventFlag(10002173, FlagState.On)
                assert not GetEventFlag(10002173)
            elif call.Get() == 1:
                Goto('L0')
        elif GetEventFlag(10001950):
            """State 8,17"""
            # action:26101032:"Restore Great Site of Grace to illuminated state?"
            call = t618001000_x0(action1=26101032)
            if call.Get() == 0:
                """State 14"""
                SetEventFlag(10002173, FlagState.On)
                assert not GetEventFlag(10002173)
            elif call.Get() == 1:
                Goto('L0')
    """State 19"""
    return 0

def t618001000_x11():
    """State 0,1"""
    # eventflag:140:Rare Terrain Unlocked: Volcano
    # action:26100021:"Crater"
    AddTalkListDataAltIf(GetEventFlag(140), 1, 26100021, -1, 0, False)
    """State 2"""
    # eventflag:141:Rare Terrain Unlocked: Snowy Mountain
    # action:26100022:"Mountaintop"
    AddTalkListDataAltIf(GetEventFlag(141), 2, 26100022, -1, 0, False)
    """State 3"""
    # eventflag:142:Rare Terrain Unlocked: Corruption
    # action:26100023:"Rotted Woods"
    AddTalkListDataAltIf(GetEventFlag(142), 3, 26100023, -1, 0, False)
    """State 4"""
    # eventflag:143:Rare Terrain Unlocked: Noclone
    # action:26100024:"Noklateo, the Shrouded City"
    AddTalkListDataAltIf(GetEventFlag(143), 4, 26100024, -1, 0, False)
    """State 5"""
    # action:26100029:"Cancel"
    AddTalkListDataAlt(99, 26100029, -1, 0, False)
    """State 6"""
    return 0

def t618001000_x12(flag2=_):
    """State 0,2"""
    # eventflag:6070: During Fever: Volcano
    SetEventFlag(6070, FlagState.Off)
    # eventflag:6071: During Fever: Snowy mountain
    SetEventFlag(6071, FlagState.Off)
    # eventflag:6072: During Fever: Corruption
    SetEventFlag(6072, FlagState.Off)
    # eventflag:6073: During Fever: Noclone
    SetEventFlag(6073, FlagState.Off)
    """State 3"""
    # eventflag:6080:Number of fever counts
    SetEventFlag(6080, FlagState.Off)
    SetEventFlag(6081, FlagState.Off)
    SetEventFlag(6082, FlagState.Off)
    SetEventFlag(6083, FlagState.Off)
    """State 4"""
    # eventflag:6085:Number of cooldowns used
    SetEventFlag(6085, FlagState.Off)
    SetEventFlag(6086, FlagState.Off)
    SetEventFlag(6087, FlagState.Off)
    SetEventFlag(6088, FlagState.Off)
    """State 1"""
    SetEventFlag(flag2, FlagState.On)
    """State 5"""
    SetEventFlag(10002170, FlagState.On)
    """State 6"""
    SetEventFlag(10002171, FlagState.On)
    """State 7"""
    assert t618001000_x14()
    """State 8"""
    return 0

def t618001000_x13(action1=_, flag2=_):
    """State 0,5"""
    call = t618001000_x0(action1=action1)
    if call.Get() == 0:
        """State 2"""
        if CompareSovereignSigils(CompareType.GreaterOrEqual, 1):
            """State 3,1"""
            AddSovereignSigils(-1)
            """State 6"""
            assert t618001000_x12(flag2=flag2)
            """State 8"""
            return 0
        else:
            """State 4,7"""
            # action:26101090:"Insufficient Sovereign Sigils"
            assert t618001000_x3(action2=26101090)
    elif call.Done():
        pass
    """State 9"""
    return 1

def t618001000_x14():
    """State 0,1"""
    if f305():
        """State 2,4"""
        SetEventFlag(10002166, FlagState.On)
    elif not f305():
        """State 3"""
        pass
    """State 5"""
    return 0

