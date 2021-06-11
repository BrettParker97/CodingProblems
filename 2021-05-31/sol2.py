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

def makeWords(numbers):
    #get each numbers rep letters
    letters = []
    for x in numbers:
        letters.append(letterMaps.get(int(x)))
    
    #get all combinations of the different letters
    temp2 = []
    temp = itertools.product(*letters)
    for x in temp:
        str1 = ""
        temp2.append(str1.join(x))
    
    #check if any combinations are valid
    res = []
    for x in temp2:
        if x in validWords:
            res.append(x)
            
    #return any valid words
    return res

print(makeWords("364"))