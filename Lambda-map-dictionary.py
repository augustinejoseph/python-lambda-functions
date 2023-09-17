students = [
    {'name': 'Alice', 'age': 22, 'gender': 'female', 'grades': [90, 88, 92, 87, 89]},
    {'name': 'Bob', 'age': 19, 'gender': 'male', 'grades': [78, 85, 88, 92, 80]},
    {'name': 'Carol', 'age': 24, 'gender': 'female', 'grades': [88, 91, 89, 94, 86]},
    {'name': 'David', 'age': 21, 'gender': 'male', 'grades': [76, 89, 82, 91, 84]},
    {'name': 'Eve', 'age': 23, 'gender': 'female', 'grades': [92, 95, 88, 90, 91]},
]


res = map(lambda x : {**x, 'School' : "New School"} , students)
print(list(res))
print("<!--  END -->")


# Write a Python program that uses map(), a lambda function, and dictionaries to create a new list of dictionaries 
# where each student's age is increased by 5 years while keeping their name and gender unchanged.
age_after_5_years = map(lambda x : {'name' : x['name'] , 'age' :x['age'] +5, 'gender' :x['gender'],'grades': x['grades'] } , students)
age_after_5_years_dict_unpacking = map(lambda student : {**student, "age" : student['age'] +5 } , students )
print(list(age_after_5_years))
print("<!--  END -->")
print(list(age_after_5_years_dict_unpacking))



# Find product using map and lambda function.
products = [
    {'name': 'Widget A', 'price': 10.0, 'quantity': 5},
    {'name': 'Widget B', 'price': 8.0, 'quantity': 8},
    {'name': 'Widget C', 'price': 12.5, 'quantity': 3},
    {'name': 'Widget D', 'price': 15.0, 'quantity': 6},
]

total_price = list(map(lambda product : {'name' : product['name'], "total" : product['price'] * product['quantity'] } , products))
print(total_price)