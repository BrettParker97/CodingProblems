def missing_ranges(nums, low, high):
    res = []
    index = low
    for x in nums:
        #skip ahead to next range value
        if index == low and x <= low:
            continue
        
        #check low != x cause no range there
        if index == x:
            continue
        #check for something like 1-2 which has
        #no range as well
        elif index + 1 == x:
            index = x
            continue
        
        #add range to res
        res.append((index + 1, x - 1))
        
        #update index
        index = x
        if index == high:
            break
    return res

print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)] 