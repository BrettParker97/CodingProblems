import math

#sol 1
def pascal_triangle_row(n):
    res = [1,1]
    temp = []
    for x in range(3, n + 1):
        for y in range(x):
            if y == 0 or y == x - 1:
                temp.append(1)
                continue
            #add from array above
            pre = res[y - 1]
            post = res[y]
            temp.append(pre + post)
        res = temp
        temp = []
    return res

#sol 2
#I knew there was an equation to do this directly
#but wanted my first try to be what I could code
#without assistance
def better(val):
    n = val - 1
    res = []
    for k in range(val):
        res.append((int)((math.factorial(n)) / ((math.factorial(k)) * (math.factorial(n - k)))))
    return res

print(better(6))
# [1, 5, 10, 10, 5, 1]
