import asyncio

import fastquotes

loop = asyncio.get_event_loop()


def test_stock_len():
    assert len(fastquotes.stock_list()) > 4000


async def get_stock_list():
    return await fastquotes.async_stock_list()


def test_async_stock_len():
    stock_l = loop.run_until_complete(get_stock_list())
    assert len(stock_l) > 4000
