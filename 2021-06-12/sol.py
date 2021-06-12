#finished in 21m 53sec
def convert_to_int(s):
    neg = False
    nums = []
    first = True
    #loop through each char of the string
    for x in s:
        #get ascii value
        asci = ord(x)
        
        #set neg if first value is a neg sign
        if asci == 45 and first:
            neg = True
            first = False
            continue
            
        #check what int the char reps
        value = 0
        for y in range(48, 58):
            if asci == y:
                nums.append(value)
                break
            value += 1
            if value == 10:
                break
            
        #if we reached value 10, the char wasnt an int
        if value == 10:
            return None

    #multiply each indiv value by its place in the
    #base 10 version of the num
    res = 0
    index = 1
    for x in nums:
        res += (x * pow(10, (len(nums) - index)))
        index += 1
        
    #return the int
    if neg:
        return res * -1
    else:
        return res
        
print(convert_to_int('-105') + 1)
# -104