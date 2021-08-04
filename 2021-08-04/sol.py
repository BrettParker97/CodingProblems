def findAllConcatenatedWordsInADict(words):
    res = []
    for x in words:
        for y in words:
            if y != x:
                concat = x + y
                if concat in words and concat not in res:
                    res.append(concat)
    return res
    
input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

print(findAllConcatenatedWordsInADict(input))
# ['techlead', 'catsdog']