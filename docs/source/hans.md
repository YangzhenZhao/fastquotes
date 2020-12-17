# 数字转换为汉字

### 转换为中文

```py
import fastquotes

print(fastquotes.to_hans(23054))
print(fastquotes.to_hans("20500.3"))
```

输出结果:

```
二万三千零五十四
二万零五百点三
```



### 转换为金额 

```py
import fastquotes

print(fastquotes.to_hans_amount(23054))
print(fastquotes.to_hans_amount("20500.3"))
```

输出结果:

```
贰万叁仟零伍拾肆元整
贰万零伍佰元叁角
```
