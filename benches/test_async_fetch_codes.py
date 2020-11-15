import asyncio

import pytest

import fastquotes

loop = asyncio.get_event_loop()


async def run():
    await fastquotes.async_stock_list()


def fetch_codes():
    loop.run_until_complete(run())


@pytest.mark.benchmark
def test_async_stock_list_bench(benchmark):
    benchmark(fetch_codes)
