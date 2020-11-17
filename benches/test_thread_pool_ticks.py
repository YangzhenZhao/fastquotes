import pytest

import fastquotes

codes = fastquotes.exchange_stock_list()


def get_sina_ticks():
    quotes = fastquotes.SinaQuote()
    ticks = quotes.tick_dict(codes)
    print(len(ticks))


def get_qq_ticks():
    quotes = fastquotes.TencentQuote()
    ticks = quotes.tick_dict(codes)
    print(len(ticks))


@pytest.mark.benchmark
def test_thread_pool_sina_ticks(benchmark):
    benchmark(get_sina_ticks)


@pytest.mark.benchmark
def test_thread_pool_qq_ticks(benchmark):
    benchmark(get_qq_ticks)
