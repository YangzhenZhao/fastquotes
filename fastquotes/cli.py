import click

from .fund import fund_intro_dict
from .fund.daily import fund_latest_profit_dict


@click.command()
@click.option("-c", "--codes", multiple=True, help="Set fund code to get profit.")
@click.option("-i", "--intro", multiple=True, help="Set fund code to get intro.")
def cli(codes, intro):
    if codes:
        profit_dic = fund_latest_profit_dict(codes)
        for code, profit in profit_dic.items():
            print(f"{code}:", "暂未更新" if profit is None else profit)
    if intro:
        dic = fund_intro_dict()
        for code in intro:
            print(dic[code])
