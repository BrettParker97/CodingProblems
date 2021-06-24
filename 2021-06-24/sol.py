def base_2(n):
    #first find biggest pow 2 that can be taken
    #out of n
    biggest = 0
    for x in range(n):
        if 2 ** x <= n:
            biggest = x
        else:
            break
    
    #start from biggest and take out values
    #if you can
    base_2 = ""
    for x in reversed(range(biggest + 1)):
        val = 2 ** x
        if val <= n:
            base_2 += str(1)
            n -= val
        else:
            base_2 += str(0)
    return base_2

counter = 1
res = base_2(123)
if res == "1111011": #place answer here
    print(f"case {counter}: Pass")
else:
    print(f"case {counter}: Fail")
counter += 1

res = base_2(1563)
if res == "11000011011": #place answer here
    print(f"case {counter}: Pass")
else:
    print(f"case {counter}: Fail")
counter += 1

res = base_2(5)
if res == "101": #place answer here
    print(f"case {counter}: Pass")
else:
    print(f"case {counter}: Fail")
counter += 1

res = base_2(123456789) 
if res == "111010110111100110100010101": #place answer here
    print(f"case {counter}: Pass")
else:
    print(f"case {counter}: Fail")
counter += 1
    
