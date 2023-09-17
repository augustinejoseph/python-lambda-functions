numbers = [10, 25, 15, 30, 8, 40, 50, 3, 20, 5]

div_by_5_and_even = list(filter(lambda num : num %5 ==0 and num % 2 == 0, numbers))
print(div_by_5_and_even)