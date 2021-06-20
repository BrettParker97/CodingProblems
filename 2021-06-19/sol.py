'''
assumptions - 
    n tasks/idle must be run before
    we can run the same task again
    
    given answer was wrong (there's not even a 's' in
    the execution)
'''
def schedule_tasks(tasks, n):
    #count occurrences
    countTasks = []
    for x in tasks:
        found = False
        for y in countTasks:
            if y[0] == x:
                y[1] += 1
                found = True
                break
        
        if found is False:
            countTasks.append([x, 1])

    #order lists from largest to smallest
    finList = []
    for x in range(len(countTasks)):
        biggest = [None, 0]
        for y in countTasks:
            if y[1] > biggest[1]:
                biggest = y
        finList.append(biggest)
        countTasks.remove(biggest)
    
    res = []
    cd = []
    while True:
        #pop first into cd list when possiable
        if len(cd) > n :
            cd.pop(0)
        
        #finish when we empty the list
        if len(finList) <= 0:
            break
        
        #find the next task to do
        for x in range(len(finList)):
            if finList[x][0] not in cd:
                res.append(finList[x][0])
                cd.append(finList[x][0])
                finList[x][1] -= 1
                if finList[x][1] <= 0:
                    finList.remove(finList[x])
                break
            
            if x == len(finList) - 1:
                res.append("idle")
                cd.append("idle")
                break
    return len(res)
            
print(schedule_tasks(['q', 'q', 's', 'q', 'w', 'w'], 4))
# q,w,s,idle,idle,q,w,idle,idle,idle,q - 11

