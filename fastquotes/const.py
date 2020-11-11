import os

SINA_BASE_URL = "http://hq.sinajs.cn/list="
TENCENT_BASE_URL = "http://qt.gtimg.cn/q="
REQ_CODES_NUM_MAX = 300
HEADERS = {
    "Accept-Encoding": "gzip, deflate, sdch",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/54.0.2840.100 "
        "Safari/537.36"
    ),
}
TRADE_DAYS_FILE_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "../static/trade_days.txt")
)
