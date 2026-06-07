# res：当前的累加结果
# sign：当前数字前的符号，1代表+，-1代表-
# stack，若遇到（，则把当前的res和sign先存入栈，并重置，然后去算括号里面的
# 遇到），依次弹出前一个符号pre_sign和进入括号前的结果pre_res
# res = pre_res + pre_sign * res
# 即：(括号外存的结果) + (括号内的结果 × 括号前的符号)
# 遇到空格：跳过

def calculate(s):
    stack = []
    res = 0
    sign = 1
    num = 0      # 当前正在解析的数字
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            res += sign * num
            sign = 1
            num = 0
        elif c == '-':
            res += sign * num
            sign = -1
            num = 0
        elif c == '(':
            stack.append(sign)
            stack.append(res)
            sign = 1
            res = 0
            num = 0
        elif c == ')':
            # 先加上括号内最后一个数字
            res += sign * num
            num = 0
            pre_res = stack.pop()
            pre_sign = stack.pop()
            res = pre_res + pre_sign * res
        
    # 把末尾的数字加上
    res += sign * num
    return res

