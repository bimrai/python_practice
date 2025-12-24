import random

name1 = input('Your name: ')
name2 = input('Their name: ')

gen_num = random.randint(0, 100)

print(f"\nMatch score: {gen_num}%")

if gen_num == 100:
    print(f'You and {name2} are a perfect match!')
elif 80 < gen_num <= 90:
    print('Great match!')
elif 70 < gen_num <= 80:
    print(f'You and {name2} have potential')
elif 50 < gen_num <= 70:
    print('Steps ahead look promising!')
elif 20 < gen_num <= 50:
    print('Not looking great...')
else:
    print('Weak match')
