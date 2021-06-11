import itertools

letterMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def recursion(numbers, index, toCheck):
    #end case
    if index >= len(numbers):
        return toCheck
    
    #check this combination against validWords, so far
    words = []
    for x in letterMaps.get(int(numbers[index])):
        for y in validWords:
            for z in toCheck:
                if z + x in y:
                    if z + x not in words:
                        words.append(z + x)
    
    #early out
    if words == []:
        return []
    
    #start recursion
    return recursion(numbers, index + 1, words)
    
def makeWords(numbers):
    return recursion(numbers, 0, [""])
    

print(makeWords("364"))