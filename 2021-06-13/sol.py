#finished in 1h 21m
'''
This problem has an easy solution, which would be to make a
new matrix and place all the values in the correct place,
however this solution is better since I do everything 'in place'
making the space factor much smaller in the case of a huge matrix

Although this wasnt apart of the question, this soultion seemed
more fun to attempt, even at the cost of time it took to
debug and think/math out.
'''
def solveLoop(left, right, mat, length):
    #indexes used to solve each loop, nondesructive to main
    loopLeft = left
    loopRight = right
    matRight = loopLeft
    
    #we are givin a left/right index to some array in the matrix
    #loop through all values in that array that havent been fixed
    for x in range(length - 1):
        carry = None
        matLeft = loopLeft
        
        #move the value to new position and repeat
        #until we return to inital position
        while True:
            #end case
            #once we hit None we are back at the begining 
            #of the loop
            if mat[matLeft][matRight] == None:
                mat[matLeft][matRight] = carry
                break
                
            #switch data
            if carry == None:
                carry = mat[matLeft][matRight]
                mat[matLeft][matRight] = None
            else:
                temp = mat[matLeft][matRight]
                mat[matLeft][matRight] = carry
                carry = temp
            
            #find next position we are going to
            tempLeft = matLeft
            tempRight = matRight
            matLeft = tempRight
            matRight = loopRight - tempLeft
        
        #move up in the inital array 1
        loopLeft += 1
    return

def rotate(mat):
    #assuming atleast 2x2
    length = len(mat)
    left = 0
    right = length - 1
    
    #if 1, then thats the center so we're done
    while length >= 2:
        solveLoop(left, right, mat, length)
        
        #update length and indexes
        length -= 2
        left += 1
    return mat

#print and check below
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Input Matrix:")
for x in mat:
    print(x)

rotate(mat)
print("Output Matrix:")
for x in mat:
    print(x)
#  [7, 4, 1] 
#  [8, 5, 2] 
#  [9, 6, 3]