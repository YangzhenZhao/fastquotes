import click

from .fund import fund_intro_dict
from .fund.daily import fund_real_time_dict


@click.command()
@click.option("-c", "--codes", multiple=True, help="Set fund code to get profit.")
@click.option("-i", "--intro", multiple=True, help="Set fund code to get intro.")
def cli(codes, intro):
    if codes:
        fund_dic = fund_real_time_dict()
        for code in codes:
            item = fund_dic[code]
            profit = float(item["单位净值"]) / float(item["上个交易日单位净值"]) - 1
            print(code, item["update_date"], profit)
    if intro:
        dic = fund_intro_dict()
        for code in intro:
            print(dic[code])
