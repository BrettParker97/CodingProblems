def remove_adjacent_dup(s):
    res = s
    loop = False
    while 1:
        tried = []
        for x in res:
            #if weve tried this char in this string already
            #skip it (saves us from "abababab" strings)
            if x in tried:
                continue
            else:
                tried.append(x)
                
            #try to split string by each value(doubled) in the
            #given string
            temp = res.split(x+x)
            
            #if the split is greater than 1 then "xx"
            #is in our string atleast once
            if len(temp) > 1:
                #string.split() removes the occurances for us
                #so all we do is add them back together
                new = ""
                for y in temp:
                    new += y
                res = new
                
                #retry all chars again since string has changed
                loop = True
                break
        
        #end case
        #loop only breaks when we find no matches in the
        #string        
        if loop == False:
            break
        else:
            loop = False
    return res
            
print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c