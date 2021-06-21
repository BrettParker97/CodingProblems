'''
I know this isn't the best solution, however this is the one
I could come up with in a reasonable time and without google
assistance.

The inefficency comes from checking every diagnal, instead of
finding the relationship between the index we're checking and the other
queens. This involves a bit of math and head scratching. Though its an
easy google search I try to do these problems without any help, minus
syntax help, from online.
'''
def recursion(currentQs, index, matSize):
    #end case
    if index[0] > matSize - 1 or index[1] > matSize - 1:
        return [None]
    
    #check vert
    for x in currentQs:
        if x[1] == index[1]:
            return [None]

    #check diags
    for x in range(1, min(index[0], index[1]) + 1):
        if [index[0] - x,index[1] - x] in currentQs:
            return [None]
        if [index[0] - x,index[1] + x] in currentQs:
            return [None]
        if [index[0] + x,index[1] - x] in currentQs:
            return [None]
        if [index[0] + x,index[1] + x] in currentQs:
            return [None]

    #if we pass checks, check if done
    tempQs = currentQs.copy()
    tempQs.append(index)
    if len(tempQs) == matSize:
        return [index]

    #if were not done, try to move on
    for col in range(matSize):
        res = recursion(tempQs, [index[0] + 1, col], matSize)
        if res[0] != None:
            return [index] + res
    
    #if none of the later branches worked return
    return [None]

def n_queens(n):
    for x in range(n):
        res = recursion([], [0, x], n)
        if res[0] != None:
            return res
    return "No layout found"

print(n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .