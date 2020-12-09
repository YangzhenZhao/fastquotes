from fastquotes import to_hans, to_hans_amount


def test_to_hans():
    assert to_hans("18446744073.230") == "一百八十四亿四千六百七十四万四千零七十三点二三零"
    assert to_hans("2333") == "二千三百三十三"
    assert to_hans("606015703") == "六亿零六百零一万五千七百零三"
    assert to_hans("606015703.10357") == "六亿零六百零一万五千七百零三点一零三五七"


def test_to_hans_amount():
    assert to_hans_amount("18446744073.230") == "壹佰捌拾肆亿肆仟陆佰柒拾肆万肆仟零柒拾叁元贰角叁分"
    assert to_hans_amount("2333") == "贰仟叁佰叁拾叁元整"
    assert to_hans_amount("606015703") == "陆亿零陆佰零壹万伍仟柒佰零叁元整"
    assert to_hans_amount("606015703.10357") == "陆亿零陆佰零壹万伍仟柒佰零叁元壹角叁厘伍毫"
