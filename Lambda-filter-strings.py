words = ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig']

print(words)
words = list(filter(lambda word : len(word) < 5, words))
print(words)

products = [('Apple', 60), ('Banana', 30), ('Orange', 45), ('Avocado', 75), ('Almonds', 55), ('Grapes', 20)]
starts_with_A = list(filter(lambda product : product[0].startswith("A"), products))
print(starts_with_A)