def aboveNine(val):
    if val == 10:
        return "A"
    elif val == 11:
        return "B"
    elif val == 12:
        return "C"
    elif val == 13:
        return "D"
    elif val == 14:
        return "E"
    elif val == 15:
        return "F"
    else:
        return "-1" #something messed up

def to_hex(n):
    #find biggest pow 16 to take out
    biggest = 0
    for x in range(n):
        test = pow(16, x)
        if test > n:
            biggest = x - 1
            break
        elif test == n:
            biggest = x
            break

    #start from biggest and work down
    #taking out multiples of x as we decend
    res = ""
    val = n
    for x in range(biggest, -1, -1):
        power = pow(16, x)
        if val - power >= 0:
            remainder = val % power
            divTimes = (val - remainder) / power
            val = remainder
            
            if divTimes > 9:
                res += aboveNine(divTimes)
            else:
                res += str(int(divTimes))
        else:
            res += "0"
    return res
  
print(to_hex(123))
# 7B

print(to_hex(23124))
# 5A54

print(to_hex(94907))
# 172BB

print(to_hex(16777215))
# FFFFFF

print(to_hex(0))
# 0