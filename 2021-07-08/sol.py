def transpose(mat):
    #get OG measurements
    height = len(mat)
    width = len(mat[0])
    
    res = []
    #x and y are our position in OG mat
    for x in range(height):
        for y in range(width):
            #the OG mat width should be = to res height
            #if its not then make a new list there with
            #our value
            if y >= len(res):
                res.append([mat[x][y]])
                continue
            
            #if we didnt make a new list, just add this value
            #to the list that is there
            res[y].append(mat[x][y])
    return res

mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5], 
#  [3, 6]]