all_data = [["John", "Emily", "Michael", "Mary", "Steven"], ["Maria", "Juan","Javier", "Natalia", "Pilar"] ]

name_with_two_a = []

for names in all_data:
    more_a = [name for name in names if name.count('a') >= 2]
    name_with_two_a.extend(more_a)
    
print(name_with_two_a)

// nested comprehension list

result = [name for names in all_data for name in names if name.count('a') >= 2]
print(result)
