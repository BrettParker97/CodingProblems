#finished in 18m
def pow(x, n):
    extra = []
    
    currentVal = x
    while n > 1:
        #make n even
        if n % 2 != 0:
            extra.append(currentVal)
            n -= 1
        
        #increase val
        currentVal *= currentVal
        
        #update n
        n /= 2
    
    #multiply all the values we skipped
    #because they didnt have partners
    for x in extra:
        currentVal *= x
    return currentVal
        
print(pow(5, 3))
# 125

print(pow(5, 8))
# 390625

print(pow(5, 9))
# 1953125