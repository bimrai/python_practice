# practice with map() function

# this script prints out names with either odd or even characters string beside it to indicate odd/even characters within the string/name

name_list = ['Bim', 'Olya', 'Drishya', 'Samon', 'John', 'Steve', 'Fox']

def splicer(mystring):
    if len(mystring)%2 == 0:
        return f'{mystring}: Even Characters'
    else:
        return f'{mystring}: Odd Characters'

for names in map(splicer, name_list):
    print(names)
