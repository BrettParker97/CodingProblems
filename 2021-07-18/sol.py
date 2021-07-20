from itertools import permutations

def generate_brackets(n):
    binary = []
    #put n closed and opened brackets
    for x in range(n):
        binary.append("(")
        binary.append(")")
    
    #get all permutations of the list
    perm = permutations(binary)
    perm = list(perm)
    
    #for each perm check its a valid bracket set
    #if it is, add it to res 
    res = []
    for x in perm:    
        running = ""        
        opens = 0
        close = 0
        for y in x:
            if y == "(":
                opens += 1
            else:
                close += 1
            
            #if close > open then not valid
            if close > opens:
                running = ""
                break
            running += y
        
        #if running is "", it wasnt valid
        #if running is in res, dont add it again
        if running == "":
            continue
        if running in res:
            continue
        res.append(running)
    return res
   
print(generate_brackets(1))
# ['()']

print(generate_brackets(3))
# ['((()))', '(()())', '()(())', '()()()', '(())()']