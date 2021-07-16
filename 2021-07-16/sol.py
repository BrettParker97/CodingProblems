def reverse_integer(num):
    #check for negitive value
    neg = False
    if num < 0:
        neg = True
        num = abs(num)
        
    #check how big num is
    x = 1
    while num / x >= 1:
        x *= 10
    x /= 10
    
    #divide x out of num, tells us the val at x position
    #then subtract that val out of num
    res = []
    while x >= 1:
        val = int(num / x)
        num -= val * x
        x /= 10
        res.append(val)
    
    #reverse list of vals then return as int
    temp = reversed(res)
    res = []
    for x in temp:
        res.append(str(x))
    res2 = "".join(res)    
    
    if neg:
        return -1 * int(res2) 
    return int(res2)
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123