def intersection(list1, list2, list3):
    #find sortest list
    shortest = []
    l2 = []
    l3 = []
    one = len(list1)
    two = len(list2)
    three = len(list3)
    if one >= two and one >= three:
        shortest = list1
        l2 = list2
        l3 = list3
    elif two >= one and two >= three:
        shortest = list2
        l2 = list1
        l3 = list3
    else:
        shortest = list3
        l2 = list1
        l3 = list2
    
    #loop through all elements in shortest list
    #check if the element is in the other 2 lists
    for x in shortest:
        if x in l2 and x in l3:
            return x
    print("No overlap found")
    return -1
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]