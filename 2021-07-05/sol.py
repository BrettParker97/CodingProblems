#this is written with the pre req python doesnt have
#BigNum size
def multiply(str1, str2):
    mults = []
    index = 0
    maxSize = 0
    for x in reversed(str1):
        #multiply single value by all values
        #of str2, with position in mind
        position = 0
        for y in reversed(str2):
            valX = int(x)
            valY = int(y)
            mult = valX * valY
            
            #if >/= then we need to reverse diget positions
            stringMult = ""
            if mult < 10:
                stringMult = str(mult)
            else:
                rev = reversed(str(mult))
                for z in rev:
                    stringMult += z
                
            #make a zeros list based on position
            zeros = ""
            for z in range(index + position):
                zeros += "0"
                
            #store with position added   
            if position == 0:
                newString = zeros + stringMult
                mults.append([newString])
            else:
                newString = zeros + stringMult
                mults[index].append(newString)
                
                #keep track of our biggest value
                if len(newString) > maxSize:
                    maxSize = len(newString)
            position += 1
        index += 1
    
    #add all values together
    res = ""
    index = 0
    while 1:
        runningVal = 0
        for x in mults:
            for y in x:
                #check if string is big enough
                if len(y) <= index:
                    continue
                
                #add value to runningVal
                runningVal += int(y[index])
        
        #place index 0 in res then add the carry
        #to any mult list
        
        rev = reversed(str(runningVal))
        string = ""
        for z in rev:
            string += z
        
        res += string[0]
        zeros = ""
        for x in range(index):
            zeros += "0"
        mults[0].append(zeros + string)
        
        
        index += 1
        #end case
        #not sure how big our remainders can get
        #but i assume no bigger than 2maxSize
        if index >= maxSize * 2:
            break
    
    #reversed the reversed num and add commas
    #for my future sanity while testing
    fin = ""
    commaCount = 0
    for x in reversed(res):
        if fin == "" and x == "0":
            continue
            
        if commaCount == 3:
            fin += ","
            commaCount = 1
        else:
            commaCount += 1
            
        fin += x
    return fin
    
print(multiply("11", "13"))
# 143

print(multiply("123456789", "987654321"))
# 121,932,631,112,635,269