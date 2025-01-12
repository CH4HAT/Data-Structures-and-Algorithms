# Data Structures and Algorithms Warmup

#ispalindrome
'''
def ispalindrome(str):
    new_str = str[::-1]
    if new_str == str:
        return True
    else:
        return False


if ispalindrome('🙃🙂🙃'):
    print("String is Paindrome")
else:
    print("not palindrome")
'''

#counter(iter)
'''
def counter(iter):
    dict={}
    for i in iter:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] +1
    print(dict)
        

counter('abcabc')
counter(['ab', 'ab', 'ba', 'ba', 'aba', 'ab'])
'''

#our shared values(iter1, iter2)

def ourSharedValues(iter1, iter2):
    shared_dict = {}
    for char in iter1:
        if char in iter2: 
            count = iter2.count(char) 
            if char in shared_dict:
                shared_dict[char] += count  
            else:
                shared_dict[char] = count  
    print(shared_dict)



ourSharedValues('abcdef', 'abba')
ourSharedValues('babar', 'librarian')

