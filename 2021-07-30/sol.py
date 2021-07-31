from itertools import combinations

def generateAllSubsets(nums):
    res = []
    #loop from 1 - len(nums) sized arrays
    for r in range(len(nums) + 1):
        #get all combinations for this sized array
        com = combinations(nums, r)
        
        #store combinations in res
        for x in com:
            #formating 
            y = list(x)
            res.append(y)
    return res

print(generateAllSubsets([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
# [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]