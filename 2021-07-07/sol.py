def common_characters(strs):
    res = []
    #take first string and loop through the chars
    for x in strs[0]:
        add = True
        #loop through the rest of the strings
        for y in range(1, len(strs) - 1):
            #if the char doesnt show up, move on 
            if x not in strs[y]:
                add = False
                break
        #if all strings had the char then add to res
        #if not already in res
        if add:
            if x not in res:                    
                res.append(x)
    return res

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']

print(common_characters(['piee', 'taape', 'pretty']))
# ['p', 'e']