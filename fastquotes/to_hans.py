hans_num_map = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
hans_units_map = ["千", "百", "十", ""]
amount_hans_num_map = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
amount_hans_units_map = ["仟", "佰", "拾", ""]
amount_hans_float_units_map = ["角", "分", "厘", "毫"]


def to_hans(s) -> str:
    s = str(s)
    point_pos = s.find(".")
    if point_pos == -1:
        int_part, float_part = s, ""
    else:
        int_part, float_part = s[:point_pos], s[point_pos + 1 :]

    hans = _int_part_hans(int_part, hans_num_map, hans_units_map)

    if float_part:
        hans += "点"
        for num in float_part:
            hans += hans_num_map[int(num)]

    return hans


def to_hans_amount(s) -> str:
    s = str(s)
    point_pos = s.find(".")
    if point_pos == -1:
        int_part, float_part = s, ""
    else:
        int_part, float_part = s[:point_pos], s[point_pos + 1 :]

    hans = _int_part_hans(int_part, amount_hans_num_map, amount_hans_units_map)

    hans += "元"
    float_len = min(len(float_part), 4)
    if float_len == 0:
        hans += "整"
    for i in range(float_len):
        if float_part[i] != "0":
            hans += (
                amount_hans_num_map[int(float_part[i])] + amount_hans_float_units_map[i]
            )

    return hans


def _convert_4_digit(x: str, num_map: list, units_map: list) -> str:
    res = ""
    for i in range(4):
        if x[i] == "0":
            if not res or res[-1] != "零":
                res += "零"
        else:
            res += num_map[int(x[i])] + units_map[i]
    if len(res) > 1 and res[-1] == '零':
        res = res[:-1]
    return res


def _convert_8_digit(x: str, num_map: list, units_map: list) -> str:
    first = _convert_4_digit(x[:4], num_map, units_map)
    second = _convert_4_digit(x[4:], num_map, units_map)
    if first == "零":
        return second
    if second == "零":
        return first + "万"
    return first + "万" + second


def _int_part_hans(int_part: str, num_map: list, units_map: list) -> str:
    remainder = len(int_part) % 8
    if remainder != 0:
        int_part = "0" * (8 - remainder) + int_part

    hans = ""
    split_cnt = len(int_part) // 8
    for i in range(split_cnt):
        hans += _convert_8_digit(
            int_part[i * 8 : i * 8 + 8], num_map, units_map
        ) + "亿" * (split_cnt - i - 1)
    if hans[0] == "零":
        hans = hans[1:]
    return hans
