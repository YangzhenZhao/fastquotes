import asyncio

import easyquotation

import fastquotes

quote = fastquotes.AsyncSinaQuote()
eq = easyquotation.use("sina")
loop = asyncio.get_event_loop()


async def tick_dict():
    return await quote.tick_dict(["000001", "600036"])


def test_tick_dict():
    t1 = loop.run_until_complete(tick_dict())
    t2 = eq.real(["000001", "600036"])
    assert t1["000001"]["current_price"] == t2["000001"]["now"]
    assert t1["000001"]["high"] == t2["000001"]["high"]
    assert t1["600036"]["current_price"] == t2["600036"]["now"]
    assert t1["600036"]["high"] == t2["600036"]["high"]
