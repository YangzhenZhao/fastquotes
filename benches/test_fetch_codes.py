import pytest

import fastquotes


def fetch_stock_list():
    fastquotes.stock_list()


@pytest.mark.benchmark
def test_stock_list_bench(benchmark):
    benchmark(fetch_stock_list)
