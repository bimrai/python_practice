name1 = input('Your name: ')
name2 = input('Their name: ')

gen_num = range(0, 101)

if gen_num == 100:
    print(f'You and {name2} are a perfect match!')
elif gen_num > 80 and gen_num < 91:
    print('Great match!')
elif gen_num > 70 and gen_num < 81:
    print(f'You and {name2} have potential')
elif gen_num > 50 and gen_num < 71:
    print('Steps ahead look promising!')
elif gen_num > 20 and gen_num < 51:
    print('Not looking great...')
elif gen_num > 0 and gen_num < 21:
    print('Weak match')
