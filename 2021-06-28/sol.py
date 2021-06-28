def closest_nums(nums, k, x):
    #find closest value in list of nums
    rightIndex = None
    leftIndex = None
    for y in range(len(nums)):
        if nums[y] < x or leftIndex == None:
            leftIndex = y
        elif nums[y] > x:
            rightIndex = y
            break
    
    #increase/decrease val to add to x each loop
    #check if our indexes match the value
    #   yes - add them to res and move index
    #   no - move on to next values
    res = [] 
    val = 0
    safe = max(nums)
    while True:
        temp1 = x - val
        temp2 = x + val
        
        if leftIndex >= 0:            
            if nums[leftIndex] == temp1 and len(res) != k:
                res.append(temp1)
                leftIndex -= 1
            elif nums[leftIndex] > temp1:
                leftIndex -= 1
        if rightIndex < len(nums):
            if nums[rightIndex] == temp2 and len(res) != k:
                res.append(temp2)
                rightIndex += 1
            elif nums[rightIndex] < temp2:
                rightIndex += 1
        
        val += 1
        if len(res) >= k:
            break
        if leftIndex < 0 and rightIndex > len(nums):
            print("not enough values to check in given array")
            break
        #saftey break
        if temp2 > safe:
            break
    return res
    
 
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
