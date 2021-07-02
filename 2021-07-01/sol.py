def meeting_rooms(meetings):
    #order the times
    times = meetings.copy()
    times.sort()
    
    #loop through all times
    que = []
    for x in times:
        #if no rooms are taken rn
        if que == []:
            que.append(x)
            continue
        
        #try to replace a rooms
        for y in que:
            if x[0] >= y[1]:
                y = x
                continue
        
        #add another rooms
        que.append(x)
    
    return len(que)

# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)