import fastquotes

calendar = fastquotes.TradeCalendar()


def test_judge_trade_date():
    is_trade_date = calendar.is_trade_date("20201115")
    assert not is_trade_date
    is_trade_date = calendar.is_trade_date("20201113")
    assert is_trade_date


def test_pre_trade_date():
    pre_date = calendar.pre_trade_date("20201115")
    assert pre_date == "20201113"
    pre_date = calendar.pre_trade_date("20201113")
    assert pre_date == "20201112"
    pre_date = calendar.pre_trade_date("20201004")
    assert pre_date == "20200930"
    pre_date = calendar.pre_trade_date("19901219")
    assert pre_date is None
    pre_date = calendar.pre_trade_date("19901214")
    assert pre_date is None
