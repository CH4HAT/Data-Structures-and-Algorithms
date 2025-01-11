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