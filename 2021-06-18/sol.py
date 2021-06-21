def square_sum(n):
    answer = []
    while True:
        #find biggest square factor 
        biggest = 1
        for x in range(n):
            if x * x > biggest and x * x <= n:
                biggest = x
            if x * x > n:
                break
        #take biggest square out of next
        answer.append(biggest)
        n -= biggest * biggest
        
        #we finish when n is 0
        if n <= 0:
            break
    return len(answer)
    
print(square_sum(13))
# Min sum is 3 - 2
# 2

print(square_sum(25))
# Min sum is 5
# 1

print(square_sum(26))
# Min sum is 5 , 1
# 2

print(square_sum(52))
# Min sum is 7 - 1 - 1 - 1
# 4