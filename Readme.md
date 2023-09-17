## Lambda Functions

### Syntax
```
lambda arguments : expressions
``` 

## Filter 
```
<!-- filter Syntax -->
Used to filter the input iterable

filter(function, iterable)

```

## Map
```
<!-- Map Syntax -->
Used to apply the given function to each item in the iterable
map(function, iterable)
```

## How map() Lazily Transforms Data

The map() function in Python doesn't immediately change your data; it's a bit like planning a recipe but not cooking until you're ready. Here's a simplified explanation:

**Delayed Transformation:** When you use map(), it delays the actual transformation of your data. It prepares the steps but doesn't execute them right away.

**Efficient Memory:** Think of it as cutting veggies just before cooking, not all at once. map() processes data piece by piece, which is memory-efficient, especially for big datasets.

**On-Demand Results: **The real work happens when you ask for the results. map() only computes the transformation as you use the data, like a magician who reveals tricks when you're watching.

#### Example:

Suppose you want to double numbers in a list, but you only need them when you decide:

```python
numbers = [1, 2, 3, 4, 5]

# `map()` plans the doubling but doesn't do it yet
doubled = map(lambda x: x * 2, numbers) 

# The magic happens when you request results:
for result in doubled:
    print(result)

```

Here, map() doesn't double the whole list upfront. It does the work only when you need each doubled number. It's like cooking each part of a meal just before eating. This is smart for saving time and resources, especially with lots of data.