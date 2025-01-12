# Data-Structures-and-Algorithms

## warmup 
### Exercise 1 : isPalindrome(str)
A "palindrome" is a word, or sometimes a phrase, that reads the same forward and backward. Here is far too much background information: https://en.wikipedia.org/wiki/Palindrome

In this exercise, your task is to write a function that accepts a single string parameter, and figures out whether that string is a palindrome. There are more-complicated and less-complicated ways to interpet this, for example, should "aaabbaa a" count, with those spaces in there? What about "Abba", with the mismatched capitalization?

For the purposes of this exercise, we'll keep it simple: all characters, including spaces, punctuation, digits, symbols, emoji, etc... should be considered as they appear. Therefore, both of the previous examples would not count as palindromes. However, "a, b a a b ,a" would count, because everything aligns, including the spaces and commas.

Don't forget to think carefully about what edge cases you might encounter.

Here, it might work like this:

>>> isPalindrome('abba')
True
>>> isPalindrome('abomination')
False
>>> isPalindrome('racecar')
True
>>> isPalindrome('r aceca r')
True
>>> isPalindrome('race car')
False
>>> isPalindrome('🙃🙂🙃')
True
>>>

### Exercise 2 : counter(iter)
Python has a wonderful counter class built-in, but for this exercise, pretend it doesn't exist, and create your own. Python's is built as a class, with lots of methods, but yours only needs to count the occurrences of items, so you can implement it as a function.

Your task is to write a function that takes in any iterable (such as a list, a string, or a tuple), and returns a dictionary, showing how many of each item there are. So in the output dictionary, the keys are the values from the input, and the values are the counts of each item.

As is typical with a dictionary, any ordering of keys in the output is fine.

It might work like this:

>>> counter('abcabc')
{'a': 2, 'b': 2, 'c': 2}
>>>
>>> counter(['ab', 'ab', 'ba', 'ba', 'aba', 'ab'])
{'ab': 3, 'ba': 2, 'aba': 1}
>>>

### Exercise 3 : ourSharedValues(iter1, iter2)
In this exercise, you'll be given two iterables, like those from the previous exercise, maybe lists or strings or tuples. Your task is to figure out what values the two input iterables have in common, and also how much they have them in common. This is a bit like a set intersection, but there's an added twist with the counting.

If an element is only in one input, but not in the other, then of course they don't have that element in common, so that element won't show up in the output. If both inputs have the element, but in different quantities, then you should report the smaller of the two quantities.

The output will look very similar to the output for counter(), being a dictionary, with the keys being the values from the iterable, and the values being the counts. As with counter(), any ordering of output is fine.

Your function should have the same output (or at least equivalent output) no matter what order the inputs are in (both with respect to each other, and internally).

In the past, many students have taken an approach to this that looked correct until they tried sufficiently tricky inputs, sometimes without noticing. May you succeed where others have failed!

>>> ourSharedValues('abcdef', 'abba')
{'a': 1, 'b': 1}
>>>
>>> ourSharedValues('babar', 'librarian')
{'b': 1, 'a': 2, 'r': 1}
>>>

# Week 1 

### Part I: Linear Search
This one should be pretty easy. Implement linear search.

Please implement it as a function called linear_search. You should have two parameters, the first one for the "needle" (i.e. what you're looking for), and the second one for the "haystack" (i.e. the list to search in). If the needle is in the haystack, return the index where it is found. If the needle is not in the haystack, return None. If there is more than one needle in the haystack, for now you may return any valid index.

Here's a demo of it working in Python REPL:

>>> linear_search(8, [6, 2, 8, 4])
2
>>> linear_search(4, [6, 2, 8, 4])
3
>>> linear_search(5, [6, 2, 8, 4])
>>>
Notice that when you return None to the REPL, it shows nothing. If you want it to show something, you can do this:

>>> linear_search(8, [6, 2, 8, 4]) == 2
True
>>> linear_search(4, [6, 2, 8, 4]) == 3
True
>>> linear_search(5, [6, 2, 8, 4]) == None
True
>>>
Limitations
Of course, Python already has a linear search function for lists, it's called .index, which is a good name, it even tells you right in the name what it will return!

So, to just make sure you're starting correctly, you can try this solution:

```
def linear_search(needle, haystack):
    try:
        return haystack.index(needle)
    except:
        return None
```

BUT WHAT IS THE FUN IN THAT?

So, for your real solution, please stick to the following tools:

if statements (including else)
for loops, all varieties
while loops
return
the following builtin functions: len, range, enumerate, min, max, abs, all, any
all mathmematical operators (+, -, /, and so on, inluding +=, -=, etc)
all logical operators (or, and, etc)
all comparison operators (<, ==, is, etc)
you may create new variables, including lists and dists
you may access the elements of lists and dicts, for reading and for writing, using [ ]
I doubt that you will want try/except, but you can use it if you need to
I doubt you'll need to define helper functions, but you can do so if you really want to
Some particular things that you should NOT use:

recursion
slicing
.index()
the in operator, like if a in b

### Part II: Binary Search
Implement binary search.

Please implement it as a function called binary_search. You should have two parameters, the first one for the "needle" (i.e. what you're looking for), and the second one for the "haystack" (i.e. the list to search in). If the needle is in the haystack, return the index where it is found. If the needle is not in the haystack, return None. If there is more than one needle in the haystack, for now you may return any valid index.

In terms of what it outputs, this has exactly the same outputs as linear_search, it just works faster than linear_search if the list is really big.

>>> binary_search(8, [2, 4, 6, 8]) == 3
True
>>> binary_search(2, [2, 4, 6, 8]) == 0
True
>>> binary_search(1, [2, 4, 6, 8]) == None
True
>>> binary_search(99, [2, 4, 6, 8]) == None
True
>>> binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) == 1
True
>>> binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) == 9
True
Notes
Because binary search only works on sorted input, you should only give it sorted input (possibly by sorting the input just before you call it).

We are not studying recursion this week, and I would like to see a non-recursive solution (we'll look at recursive solutions later). In some ways recursion is easier for this problem, in some ways it's harder, but either way this lab is not about recursion.

Same limitations as Part I. In particular, using slices might be tempting, but please don't.

### Part III: Improving Our Search (optional)
This part is optional. But if you did a great job on parts I and II, I didn't want you to get bored.

What happens if there is more than one match for the needle in the haystack? You know, what if someone looks for a 5 in the list [4, 5, 3, 5]?

So your task, if you choose to accept it, is to create functions linear_search_multi and binary_search_multi, that return every matching index.

That means that they need to return a list. And since they're returning a list anyway, that makes it easier to handle the situation where the needle isn't in the haystack at all, just return an empty list!

For this part, you may add one new tool to your toolkit. (Strictly speaking you can do without it, but I think it's a lot easier with it).

the push method of lists
It should be very easy to write linear_search_multi, and hopefully not too hard to write binary_search_multi.

Once they're working, they should work like this:

>>> linear_search_multi(8, [6, 2, 8, 4, 8, 7])
[2, 4]
>>> linear_search_multi(4, [6, 2, 8, 4, 8, 7])
[3]
>>> linear_search_multi(5, [6, 2, 8, 4, 8, 7])
[]
>>> binary_search_multi(3, [1, 2, 2, 3, 3, 3, 4, 5])
[3, 4, 5]
>>>