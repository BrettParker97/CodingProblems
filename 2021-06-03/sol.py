def calcIndex(index, moveAmount, listSize):
    if index - moveAmount < 0:
        return listSize + (index - moveAmount)
    else:
        return (index - moveAmount)


def rotate_list(nums, k):
    listLen = len(nums)
    moveBy = None
    if k == listLen:
        moveBy = 0
    elif k > listLen:
        moveBy = k - listLen
    else:
        moveBy = k
    
    index = 0
    hold = None
    while True:
        #end case
        if nums[index] == None:
            if hold == None:
                return nums
            else:
                nums[index] = hold
                return nums
        
        #first case
        if hold == None:
            hold = nums[index]
            nums[index] = None
            index = calcIndex(index, moveBy, listLen)
            continue
        
        #every other time
        temp = nums[index]
        nums[index] = hold
        hold = temp
        index = calcIndex(index, moveBy, listLen)
        
a = [1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]