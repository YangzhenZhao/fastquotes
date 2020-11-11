from .const import TRADE_DAYS_FILE_PATH


def read_trade_days():
    with open(TRADE_DAYS_FILE_PATH, "r") as f:
        return f.read().split(",")
