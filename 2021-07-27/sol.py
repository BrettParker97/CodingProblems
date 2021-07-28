def one_bits(num):
    #not dealing with negitives in this problem
    num = abs(num)
    
    #find greatest pow 2 in num
    p = 0
    for x in range(num):
        if num - pow(2, x) >= 0:
            p = x
        else:
            break
    
    #start from greatest pow and work down to 0
    res = 0
    for x in reversed(range(0, p + 1)):
        temp = pow(2, x)
        if num - temp >= 0:
            num -= temp
            res += 1
    return res

print(one_bits(23))
# 4
# 23 = 0b10111

print(one_bits(727000))
# 11
# 727000 = 0b10110001011111011000
