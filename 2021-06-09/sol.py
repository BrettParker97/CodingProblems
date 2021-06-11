#completed in 1h 9m
import math

def reverse_words(words):
    wordLen = len(words)
    
    #first reverse the string
    for x in range(wordLen):
        leftIndex = x
        rightIndex = wordLen - x - 1
        if leftIndex >= rightIndex:
            break
        
        left = words[leftIndex]
        right = words[rightIndex]
        words[leftIndex] = right
        words[rightIndex] = left
    
    #reverse each wordLen
    breaks = []
    for x in range(wordLen):
        if words[x] == " ":
            breaks.append(x)
        
    leftIndex = None
    for x in range(len(breaks) + 1):
        if leftIndex == None:
            leftIndex = 0
        if x == len(breaks):
            rightIndex = len(words) - 1
        else:
            rightIndex = breaks[x] - 1
           
           
        print("SSSS")
        for y in range(math.ceil((rightIndex + leftIndex) / 2)):
            if leftIndex + y >= rightIndex - y:
                break
            
            left = words[leftIndex + y]
            right = words[rightIndex - y]
            words[leftIndex + y] = right
            words[rightIndex - y] = left
        
        leftIndex = rightIndex + 2

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can