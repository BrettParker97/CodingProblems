def fourSum(nums, target):
    res = []
    #make 4 indexes that are never == to each other
    for x in range(len(nums)):
        for y in range(len(nums)):
            if y == x:
                continue
            for z in range(len(nums)):
                if z == x or z == y:
                    continue
                for i in range(len(nums)):
                    if i == x or i == y or i == z:
                        continue
                    
                    #check if this combo works
                    temp = [nums[x], nums[y], nums[z], nums[i]]
                    summ = sum(temp)
                    if summ == target:
                        #sort list so we dont have dups in res
                        temp.sort()
                        if temp not in res:
                            res.append(temp)
    return res

print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print("")

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print("")
print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])