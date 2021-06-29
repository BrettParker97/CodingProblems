






def larger_number(nums):
    res = []
    for x in range(len(nums)):
        nextIndex = -1
        for y in range(x, len(nums)):
            if nums[y] > nums[x]:
                nextIndex = y
                break
        res.append(nextIndex)
    return res
  
# print [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))