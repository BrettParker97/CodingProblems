from itertools import permutations

def sum_combinations(nums, target):
    #get all permutations of the num list
    perms = permutations(nums)
    perms = list(perms)
    
    #now theres a list of "unique" lists of values so check
    #each perm from 0,0-1,0-2,0-3,0-n and see if they add up to
    #target
    res = []
    #0-n
    for x in range(len(nums)):
        #all perm strings
        for y in perms:
            val = []
            #add everything from 0-x together
            for z in range(x + 1):
                val.append(int(y[z]))
            
            #if the sum hits then add to res only if
            #the list of values isnt already there
            if sum(val) == target:
                val.sort()
                lis = list(val)
                tup = tuple(lis)
                if tup not in res:
                    res.append(tup)
    return res

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]