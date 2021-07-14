def sum_binary(bin1, bin2):
    rb1 = list(reversed(bin1))
    l1 = len(rb1)
    rb2 = list(reversed(bin2))
    l2 = len(rb2)
    
    carry = 0
    i = 0
    res = []
    #loop for max(len(bin1), len(bin2))
    while 1:
        #end case
        if l1 <= i and l2 <= i:
            break
        elif l1 <= i:
            v = int(rb2[i]) + carry
            if v == 2:
                res.append(0)
                res.append(1)
            elif v == 1:
                res.append(1)
            else:
                res.append(0)
            break
        elif l2 <= i:
        
            v = int(rb1[i]) + carry
            if v == 2:
                res.append(0)
                res.append(1)
            elif v == 1:
                res.append(1)
            else:
                res.append(0)
            break
        
        #get bits
        v1 = int(rb1[i])
        v2 = int(rb2[i])
        summ = v1 + v2 + carry
        carry = 0
        
        #place result in res
        if summ == 3:
            carry = 1
            res.append(1)
        elif summ == 2:
            carry = 1
            res.append(0)
        else:
            res.append(1)
            
        #increment
        i += 1
        
    #flip string back to normal and return
    r = ""    
    for x in reversed(res):
        r += str(x)
    return r
  
print(sum_binary("11101", "1011"))
# 101000