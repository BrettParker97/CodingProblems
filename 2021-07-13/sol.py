import math

def closest_3sum(nums, target):
    best = []
    bestD = None
    #loop nums with 3 iterators
    #if the iterators ever match, skip that iteration
    for x in nums:
        for y in nums:
            if y == x:
                continue
            for z in nums:
                if z == y or z == x:
                    continue
                elif best == []:
                    best = [x, y, z]
                    #if we ever find the target, quick return
                    if sum(best) == target:
                        return best
                    
                    #use abs for distance and store for
                    #later comparison
                    s = sum(best)
                    if target > s:
                        bestD = abs(target - s)
                    else:
                        bestD = abs(s - target)
                    continue
                
                #take abs of this iteration added
                #and compare to best
                #return if we hit target
                #else continue to next iteration
                s = x + y + z
                if target == s:
                    return [x, y, z]
                elif target > s:
                    thisD = target - abs(s)
                    if thisD < bestD:
                        if thisD == 0:
                            return [x,y,z]
                        best = [x,y,z]
                        bestD = thisD
                else:
                    thisD = abs(s) - target
                    if thisD < bestD:
                        if thisD == 0:
                            return [x,y,z]
                        best = [x,y,z]
                        bestD = thisD
    return best

print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]