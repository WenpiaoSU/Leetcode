def backtracking(digits, index, s, result):
    # index 是digits的下标
    if index == len(digits):
        result.append(s)
        return
    digit = int(digits[index])   # 当前index对应的number
    letter = num_to_letter[digit]  # 当前number对应的字母 'abc'
    for i in range(len(letter)):
        s += letter[i]   # 把当前字母a加入s
        backtracking(digits, index + 1, s, result)   # 继续看下一个数字对应的内容
        s = s[:-1]   # 把当前字母a从s中去除
    
def letterComb(digits):
    if len(digits) == 0:
        return []
    s = ''   # 一种组合
    result = []    # 所有组合结果
    backtracking(digits, 0, s, result)
    return result

if __name__ == "__main__":
    num_to_letter = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    # 求不重复的全部组合，‘ab’和‘ba’只算一种组合
    digits = '23'
    result = letterComb(digits)
    print(result)
