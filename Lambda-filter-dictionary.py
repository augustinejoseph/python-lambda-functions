"""
You have a list of dictionaries representing a 
collection of books. Each dictionary has the 
following keys: 'title', 'author', 'year', and 
'genre'. You want to filter this list to find 
books published between 2000 and 2010 (inclusive)
that belong to the 'Science Fiction' genre. 
Write a Python program using filter() and a 
lambda function to accomplish this task.
"""

books = [
    {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965, 'genre': 'Science Fiction'},
    {'title': 'Neuromancer', 'author': 'William Gibson', 'year': 1984, 'genre': 'Science Fiction'},
    {'title': 'Snow Crash', 'author': 'Neal Stephenson', 'year': 1992, 'genre': 'Science Fiction'},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'year': 2008, 'genre': 'Young Adult'},
    {'title': 'Ender\'s Game', 'author': 'Orson Scott Card', 'year': 2003, 'genre': 'Science Fiction'},
    {'title': 'The Martian', 'author': 'Andy Weir', 'year': 2011, 'genre': 'Science Fiction'},
    {'title': 'The Road', 'author': 'Cormac McCarthy', 'year': 2006, 'genre': 'Dystopian Fiction'},
    {'title': '2001: A Space Odyssey', 'author': 'Arthur C. Clarke', 'year': 1968, 'genre': 'Science Fiction'}
]

res = filter(lambda x: 2000 < x['year'] <= 2010 and x['genre'] == 'Science Fiction', books)
# print(list(res))

for book in res :
    print(f"{book['title']} by {book['author']}")


# =================================================QUESTION========================================

"""
You have a list of dictionaries representing students' data.
 Each dictionary contains the following keys: 'name', 'age', 'gender',
and 'grades'. You want to find all the female students 
who are older than 20 years and have an average grade higher 
than 85%.
Write a Python program using filter() and a lambda function 
to accomplish this task.
"""

students = [
    {'name': 'Alice', 'age': 22, 'gender': 'female', 'grades': [90, 88, 92, 87, 89]},
    {'name': 'Bob', 'age': 19, 'gender': 'male', 'grades': [78, 85, 88, 92, 80]},
    {'name': 'Carol', 'age': 24, 'gender': 'female', 'grades': [88, 91, 89, 94, 86]},
    {'name': 'David', 'age': 21, 'gender': 'male', 'grades': [76, 89, 82, 91, 84]},
    {'name': 'Eve', 'age': 23, 'gender': 'female', 'grades': [92, 95, 88, 90, 91]},
]

res = filter(lambda x : x['gender'] == 'female' and x['age'] > 20 and (lambda x : sum(x['grades'] / len['grades'] > 85 ) ),students)
for stu in res:
    grade = sum(stu['grades']) / len(stu['grades'])
    print(f"{stu['name']} scored  {grade}")