numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power = list(map(lambda num : num ** 2 , numbers))
print(power)



'''
Question:

You have a list of strings, and you want to create a new list that contains the lengths 
of each string in the original list, but only for strings that have an odd length.
 Write a Python program using map and a lambda function to generate the list of lengths 
 for odd-length strings.
'''

words = ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig']

all_words = list(map(lambda word : None if len(word) % 2 != 0 and len(word) <=5  else {word : len(word) }, words))
odd_words = list(filter(None, all_words))
print(all_words)
print(odd_words)