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
