# -*- coding: utf-8 -*-
def t600001000_1():
    """State 0,1"""
    t600001000_x3(flag1=10002700)
    Quit()

def t600001000_x0(actionbutton1=6900, flag3=6001, flag4=6000, flag5=6000, flag6=6000, flag7=6000, flag8=10003045):
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
        # actionbutton:6900:"Commence expedition"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t600001000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t600001000_x2(text1=_, flag2=_, mode1=1):
    """State 0,5"""
    assert t600001000_x1() and CheckSpecificPersonTalkHasEnded(0)
    """State 1"""
    TalkToPlayer(text1, -1, -1, False)
    assert CheckSpecificPersonTalkHasEnded(0)
    """State 4"""
    if mode1 == 0:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(flag2, FlagState.On)
    """State 6"""
    return 0

def t600001000_x3(flag1=10002700):
    """State 0,6"""
    SetUpdateDistance(100)
    while True:
        """State 7"""
        # actionbutton:6900:"Commence expedition"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        call = t600001000_x0(actionbutton1=6900, flag3=6001, flag4=6000, flag5=6000, flag6=6000, flag7=6000, flag8=10003045)
        if call.Done():
            """State 1"""
            pass
        elif GetEventFlag(flag1):
            """State 4"""
            assert GetDistanceToPlayer() < 13.9
        """State 10"""
        call = t600001000_x5()
        if call.Get() == 1:
            """State 9"""
            call = t600001000_x4()
            if call.Done() and not (CheckSpecificPersonMenuIsOpen(34, 0) and not CheckSpecificPersonGenericDialogIsOpen(0)):
                """State 2"""
                pass
            elif GetDistanceToPlayer() > 14:
                """State 3,8"""
                assert t600001000_x1()
        elif call.Get() == 0:
            pass
        """State 5"""
        SetEventFlag(flag1, FlagState.Off)
    """Unused"""
    """State 11"""
    return 0

def t600001000_x4():
    c1_110()
    
    while True:
        Label('L0')
        ClearTalkListData()
        
        # Expeditions
        AddTalkListData(1, 80000000, -1)
        
        # Shifting Earth
        AddTalkListData(2, 80000001, -1)
        
        # Castigations
        # AddTalkListData(3, 80000002, -1)
        
        c1_140(1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Expeditions
        if GetTalkListEntryResult() == 1:
            assert t600001000_x6()
        # Shifting Earth
        elif GetTalkListEntryResult() == 2:
            assert t600001000_x7()
        # Castigations
        elif GetTalkListEntryResult() == 3:
            assert t600001000_x8()
        else:
            return 0
            
    Goto('L0')

def t600001000_x5():
    """State 0,1"""
    if GetChrHero() == Hero.Executor:
        """State 3"""
        if GetEventFlag(3811):
            """State 4,7"""
            # talk:31300200:"Foolish."
            # talk:31300201:"And pitiful. To cling to an impossible hope."
            assert t600001000_x2(text1=31300200, flag2=1189051, mode1=1)
        elif GetEventFlag(3817):
            """State 5,8"""
            # talk:31300300:"A wretched state of affairs."
            # talk:31300301:"After failing to return to the roots, your cursed frame was beholden to hope,"
            # talk:31300302:"and that only worsened the pain."
            assert t600001000_x2(text1=31300300, flag2=1189052, mode1=1)
        else:
            """State 6"""
            Goto('L0')
        """State 9"""
        return 0
    elif not GetChrHero() == Hero.Executor:
        """State 2"""
        pass
    """State 10"""
    Label('L0')
    return 1

# Expeditions
def t600001000_x6():
    """State 0,1"""
    OpenCommenceExpeditionMenu()
    assert not (CheckSpecificPersonMenuIsOpen(34, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2,3"""
    return 0
    
# Shifting Earth
def t600001000_x7():
    c1_110()
    
    while True:
        Label('L0')
        ClearTalkListData()
        
        # None
        AddTalkListData(1, 80000100, -1)
        
        # The Crater
        AddTalkListData(2, 80000101, -1)
        
        # The Mountaintop
        AddTalkListData(3, 80000102, -1)
        
        # The Rotted Woods
        AddTalkListData(4, 80000103, -1)
        
        # Noklateo, the Shrouded City
        AddTalkListData(5, 80000104, -1)
        
        c1_140(1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # None
        if GetTalkListEntryResult() == 1:
            assert t600001000_x100(6000) # Always OFF flag, we just reset the shifting earth flags here
            assert t600001000_x101(80000110)
        # The Crater
        elif GetTalkListEntryResult() == 2:
            assert t600001000_x100(6070)
            assert t600001000_x101(80000111)
        # The Mountaintop
        elif GetTalkListEntryResult() == 3:
            assert t600001000_x100(6071)
            assert t600001000_x101(80000112)
        # The Rotted Woods
        elif GetTalkListEntryResult() == 4:
            assert t600001000_x100(6072)
            assert t600001000_x101(80000113)
        # Noklateo, the Shrouded City
        elif GetTalkListEntryResult() == 5:
            assert t600001000_x100(6073)
            assert t600001000_x101(80000114)
        else:
            return 0
            
    Goto('L0')
    
# Castigations
def t600001000_x8():
    c1_110()
    
    while True:
        Label('L0')
        ClearTalkListData()
        
        # Expeditions
        AddTalkListData(1, 80000000, -1)
        
        # Shifting Earth
        AddTalkListData(2, 80000001, -1)
        
        # Castigations
        AddTalkListData(3, 80000002, -1)
        
        c1_140(1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Expeditions
        if GetTalkListEntryResult() == 1:
            assert t600001000_x6()
        # Shifting Earth
        elif GetTalkListEntryResult() == 2:
            assert t600001000_x6()
        # Castigations
        elif GetTalkListEntryResult() == 3:
            assert t600001000_x6()
        else:
            return 0
            
    Goto('L0')
    
# Shifting Earth toggler
def t600001000_x100(eventFlag=_):
    # Counts
    SetEventFlag(6080, 0)
    SetEventFlag(6081, 0)
    SetEventFlag(6082, 0)
    SetEventFlag(6083, 0)
    
    # Cooldowns
    SetEventFlag(6085, 0)
    SetEventFlag(6086, 0)
    SetEventFlag(6087, 0)
    SetEventFlag(6088, 0)
    
    SetEventFlag(6070, 0) # The Crater
    SetEventFlag(6071, 0) # The Mountaintop
    SetEventFlag(6072, 0) # The Rotted Woods
    SetEventFlag(6073, 0) # Noklateo, the Shrouded City
    
    SetEventFlag(10002170, 1)
    SetEventFlag(10002171, 1)
    
    # Set target flag
    SetEventFlag(eventFlag, 1)
            
    return 0

# Message display
def t600001000_x101(text=_):
    OpenGenericDialog(8, text, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    return 0
    