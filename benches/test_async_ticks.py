import asyncio

import pytest

import fastquotes

codes = fastquotes.exchange_stock_list()
loop = asyncio.get_event_loop()


async def sina_run():
    quotes = fastquotes.AsyncSinaQuote()
    ticks = await quotes.tick_dict(codes)
    print(len(ticks))


async def qq_run():
    quotes = fastquotes.AsyncTencentQuote()
    ticks = await quotes.tick_dict(codes)
    print(len(ticks))


def get_sina_ticks():
    loop.run_until_complete(sina_run())


def get_qq_ticks():
    loop.run_until_complete(sina_run())


@pytest.mark.benchmark
def test_async_sina_ticks(benchmark):
    benchmark(get_sina_ticks)


@pytest.mark.benchmark
def test_async_qq_ticks(benchmark):
    benchmark(get_qq_ticks)
