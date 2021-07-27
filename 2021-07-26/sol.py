def majority_element(nums):
    #count up all the elements
    count = {}
    for x in nums:
        if x not in count:
            count[x] = 1
            continue
        count[x] += 1
    
    #pick the majority_element
    #assumes there is one, from question
    res = None
    ignore = []
    bestCount = 0
    for x in count:
        if res == None:
            res = x
            bestCount = count[x]
            continue
        if count[x] > bestCount:
            res = x
            bestCount = count[x]
    return res

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3

print(majority_element([3, 5, 5, 5, 5, 4, 3]))
# 5