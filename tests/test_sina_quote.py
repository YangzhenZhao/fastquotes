import easyquotation

import fastquotes

quote = fastquotes.SinaQuote()
eq = easyquotation.use("sina")


def test_current_price():
    p1 = quote.current_price("000001")
    p2 = eq.real("000001")["000001"]["now"]
    assert p1 == p2


def test_pre_close():
    p1 = quote.pre_close("000001")
    p2 = eq.real("000001")["000001"]["close"]
    assert p1 == p2


def test_tick():
    t1 = quote.tick("000001")
    t2 = eq.real("000001")["000001"]
    assert t1["current_price"] == t2["now"]
    assert t1["high"] == t2["high"]


def test_tick_dict():
    t1 = quote.tick_dict(["000001", "600036"])
    t2 = eq.real(["000001", "600036"])
    assert t1["000001"]["current_price"] == t2["000001"]["now"]
    assert t1["000001"]["high"] == t2["000001"]["high"]
    assert t1["600036"]["current_price"] == t2["600036"]["now"]
    assert t1["600036"]["high"] == t2["600036"]["high"]
