def reshape_matrix(mat, a, b):
    rows = len(mat)
    cols = len(mat[0])
    numVals = 0
    #with the assumption matrixes dont have to be filled out
    #evenly we must count how many indexes are here (ex: test 3)
    for x in mat:
        numVals += len(x)
    
    #quick end
    if a * b != numVals:
        return None
    
    #start placing values in result mat
    res = []
    index = [0,0]
    for x in mat:
        for y in x:
            #get lengths of res
            ro = len(res)
            #we just started
            if ro == 0:
                res.append([y])
                continue
            co = len(res[ro - 1])
            
            #check if we need to add another row
            if co >= a:
                res.append([y])
                continue
            
            #append val at last row available
            res[ro - 1].append(y)
    return res

print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None

print(reshape_matrix([[1, 2,3,4,5,6], [7,8,9,10,11,12], [13,14]], 7, 2))
# [[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]]

print(reshape_matrix([[1, 2,3,4,5,6], [7,8,9,10,11,12], [13,14]], 2, 7))
# [[1,2][3,4][5,6][7,8][9,10][11,12][13,14]]