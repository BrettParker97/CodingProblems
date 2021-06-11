#completed in 26m 11s
def square_numbers(nums):
    #find index of first non negitive number
    posIndex = 0
    for x in nums:
        if x >= 0:
            break
        posIndex += 1
    negIndex = len(nums) - posIndex - 2
    
    #go through every value of array
    #in accending order, square and add to res    
    res = []
    while posIndex < len(nums) or negIndex > 0:
        #get pos and neg nums
        posVal = None
        if posIndex < len(nums):
            posVal = nums[posIndex]
        negVal = None
        if negIndex >= 0:
            negVal = -(nums[negIndex])

        #if one is None then we only deal with
        #the other
        if negVal == None:
            res.append(posVal * posVal)
            posIndex += 1
        if posVal == None:
            res.append(negVal * negVal)
            negIndex -= 1
        
        #if both exist
        if posVal == negVal:
            res.append(posVal * posVal)
            res.append(negVal * negVal)
            posIndex += 1
            negIndex -= 1
        elif posVal > negVal:
            res.append(negVal * negVal)
            negIndex -= 1
        else:
            res.append(posVal * posVal)
            posIndex += 1
    
    return res

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]