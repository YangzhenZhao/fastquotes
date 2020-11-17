from .const import TRADE_DAYS_FILE_PATH


def read_trade_days():
    with open(TRADE_DAYS_FILE_PATH, "r") as f:
        return f.read().split(",")


def parse_out_tencent_tick_dict(msg: str) -> dict:
    field_list = msg.split("~")
    try:
        res = {
            "time": field_list[30][8:],
            "name": field_list[1],
            "code": field_list[2],
            "current_price": float(field_list[3]),
            "pre_close": float(field_list[4]),
            "open": float(field_list[5]),
            "high": float(field_list[33]),
            "low": float(field_list[34]),
            "total_amount": float(field_list[37]) * 10000,
            "total_vol": float(field_list[6]) * 100,
            "bid1": float(field_list[9]),
            "bid1_vol": int(field_list[10]) * 100,
            "bid2": float(field_list[11]),
            "bid2_vol": int(field_list[12]) * 100,
            "bid3": float(field_list[13]),
            "bid3_vol": int(field_list[14]) * 100,
            "bid4": float(field_list[15]),
            "bid4_vol": int(field_list[16]) * 100,
            "bid5": float(field_list[17]),
            "bid5_vol": int(field_list[18]) * 100,
            "ask1": float(field_list[19]),
            "ask1_vol": int(field_list[20]) * 100,
            "ask2": float(field_list[21]),
            "ask2_vol": int(field_list[22]) * 100,
            "ask3": float(field_list[23]),
            "ask3_vol": int(field_list[24]) * 100,
            "ask4": float(field_list[25]),
            "ask4_vol": int(field_list[26]) * 100,
            "ask5": float(field_list[27]),
            "ask5_vol": int(field_list[28]) * 100,
        }
    except IndexError:
        return None
    return res


def parse_out_sina_tick_dict(msg: str) -> dict:
    field_list = msg.split(",")
    try:
        code_name_part = field_list[0].partition('="')
        res = {
            "time": field_list[31].replace(":", ""),
            "name": code_name_part[2],
            "code": code_name_part[0][-6:],
            "current_price": float(field_list[3]),
            "pre_close": float(field_list[2]),
            "open": float(field_list[1]),
            "high": float(field_list[4]),
            "low": float(field_list[5]),
            "total_amount": float(field_list[9]),
            "total_vol": float(field_list[8]),
            "bid1_vol": int(field_list[10]),
            "bid1": float(field_list[11]),
            "bid2_vol": int(field_list[12]),
            "bid2": float(field_list[13]),
            "bid3_vol": int(field_list[14]),
            "bid3": float(field_list[15]),
            "bid4_vol": int(field_list[16]),
            "bid4": float(field_list[17]),
            "bid5_vol": int(field_list[18]),
            "bid5": float(field_list[19]),
            "ask1_vol": int(field_list[20]),
            "ask1": float(field_list[21]),
            "ask2_vol": int(field_list[22]),
            "ask2": float(field_list[23]),
            "ask3_vol": int(field_list[14]),
            "ask3": float(field_list[25]),
            "ask4_vol": int(field_list[16]),
            "ask4": float(field_list[27]),
            "ask5_vol": int(field_list[28]),
            "ask5": float(field_list[29]),
        }
    except IndexError:
        return None
    return res


def exchange_prefix(code: str) -> str:
    return "sh" if code.startswith("6") else "sz"
