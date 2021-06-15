import sys

def sqrt(given):
    index = 1
    runningVal = 0
    answer = 0
    
    #search for the correct value in each decimal place
    while index != .0001:
        #loop through all values * index for first value that
        #goes over our given value
        #only do 0 - 9 once we get into decimal values
        for x in range(1, sys.maxsize):
            valToTry = index * x
            temp = answer + valToTry
            temp2 = temp * temp
            
            #if we == given just return now
            if temp2 == given:
                answer = format(answer + valToTry, ".3f")
                return answer
            #if were greater than given get previous value
            elif temp2 > given:
                preValToTry = index * (x - 1)
                answer = answer + preValToTry
                index /= 10
                break
            #if we max out at 9, 
            elif x == 9 and index < 0:
                answer = temp
                index /= 10
                break
                
    return format(answer, ".3f")
  
print(sqrt(5))
# 2.236

print(sqrt(10))
# 3.162

print(sqrt(6))
# 2.449

print(sqrt(12))
# 3.464

print(sqrt(74))
# 8.602

print(sqrt(560000))
# 748.331
