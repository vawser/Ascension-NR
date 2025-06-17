# -*- coding: utf-8 -*-
def t650001000_1():
    """State 0,1"""
    t650001000_x1()
    Quit()

def t650001000_x0(actionbutton1=6911, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert GetEventFlag(flag1) or GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5)
        """State 4"""
        # eventflag:6000:Flag to always be OFF
        assert not GetEventFlag(flag6)
        """State 5"""
        assert not DoesPlayerHaveSpEffect(9640)
        """State 2"""
        # eventflag:6000:Flag to always be OFF
        # eventflag:6001:Flag to always be ON
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsPlayerDead() and not IsCharacterDisabled())
            or (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not GetEventFlag(flag4)
            and not GetEventFlag(flag5)) or DoesPlayerHaveSpEffect(9640)):
            pass
        # actionbutton:6911:"Conclude remembrance"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 6"""
    return 0

def t650001000_x1():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6911:"Conclude remembrance"
        # eventflag:6001:Flag to always be ON
        # eventflag:6000:Flag to always be OFF
        assert t650001000_x0(actionbutton1=6911, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000)
        """State 3"""
        call = t650001000_x2()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 7:
            """State 1"""
            ForceCloseGenericDialog()
    """Unused"""
    """State 4"""
    return 0

def t650001000_x2():
    """State 0,2"""
    # action:20002006:"Concluding remembrance and returning. Proceed?"
    OpenGenericDialog(DialogBoxType.CenterMiddleDimScreen2, 20002006, 21032001, 21032002, 2)
    """State 3"""
    if GetGenericDialogButtonResult() == DialogResult.Right:
        """State 4"""
        pass
    elif GetGenericDialogButtonResult() == DialogResult.Cancel:
        """State 5"""
        pass
    elif GetGenericDialogButtonResult() == DialogResult.Left:
        """State 6"""
        c1_164()
        assert not f305()
        """State 1"""
        ConcludeRemembrance()
    """State 7"""
    return 0

