# for x in range(k) = O(k)
# add y in arr      = O(k) + O(n)
# searchign a dict is O(1)
# 2 comparisons both O(1)
# overall runtime   = O(kn) which is linear time
def findKthLargest(arr, k):
    res = 0
    exempt = {}
    for x in range(k):
        biggest = None
        for y in arr:
            #check if exempt
            temp = None
            try:
                temp = exempt[y]
            except:
                temp = None
            if temp != None:
                continue
            
            #biggest isnt set
            if biggest == None:
                biggest = y
            
            #check if bigger than biggest
            if y > biggest:
                biggest = y
        exempt[biggest] = True
        if x == k - 1:
            return biggest
  
print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7



