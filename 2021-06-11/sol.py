#finished in 39m
#input - int
#output - list[string]
def changeToList(num):
    listBits = []
    for x in reversed(range(32)):
        #if pow(2, x) can be subtracted, do so and add 1
        #to this index in the list, else 0
        if num - pow(2, x) < 0:
            listBits.append("0")
        else:
            num -= pow(2, x)
            listBits.append("1")
    return listBits

def swap_bits(num):
    #get list representation of num
    numAsList = changeToList(num)
    
    #swap the values
    for x in range(32):
        if x % 2 == 0:
            temp1 = numAsList[x]
            temp2 = numAsList[x + 1]
            numAsList[x] = temp2
            numAsList[x + 1] = temp1
    
    #create a string from list
    res = ""
    for x in numAsList:
        res += x
    
    #return as int
    return int(res, 2)

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101