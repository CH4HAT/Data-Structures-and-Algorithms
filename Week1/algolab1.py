# Part 1 Linear Search

def linear_search(needle, haystack):
    count=0
    for i in haystack:
        count+=1
        if needle == i:
            return count

print(linear_search(8, [6,2,8,4]))


# Part 2 

def binary_search(needle,haystack):
    high = len(haystack)-1
    mid = 0
    low = 0
    while low <=high:
        mid = (high + low) //2
        if haystack[mid] < needle:
            low = mid + 1
        elif haystack[mid] > needle:
            high = mid - 1
        else:
            return mid
    return 0

prob1 = binary_search(8, [2, 4, 6, 8])    
prob2 = binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) 

if prob1 == 0:
    print("not present")
else:
    print(prob1)
    
if prob2 == 0:
    print("not present")
else:
    print(prob2)

# Part 3 

def linear_search_multi(needle, haystack):
    count = 0
    answer=[]

    for i in haystack:
        if i == needle:
            answer.append(count)
        count +=1
    return answer

print(linear_search_multi(8, [6, 2, 8, 4, 8, 7]))



