# method 1: returns list

def exist_even(numlist):

    # placeholder variable list for for and if process below
    even_num = []

    for num in numlist:

        if num % 2 == 0:
            even_num.append(num) # adds all even num to list in variable above
        else:
            pass # does not print if odd exists

    return even_num # calls the list variable once for loop finishes loop with updated list of even numbers added within

exist_even([2,1, 5, 29, 19, 26, 84, 46, 21, 74, 62, 55, 44]) # test with mix/calling

# method 2: returns boolean

def exist_even(numlist):

    for num in numlist:

        if num % 2 == 0:
            return True # prints if even exists in list
        else:
            pass # does not print if odd exists

exist_even([1, 2, 5, 7, 8, 10, 11, 15]) # test with mix

# method 3: returns all list with each distinguish value specifically labelled odd or even

numlib = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(numlist):
    
    for num in numlist:
        
        if num % 2 == 0:
            print(f'{num} is EVEN')
        else:
            print(f'{num} is ODD') # allows odd to be distinguished in the output

check_even(numlib)

# method 4: only prints if even number exists via f string

numlib = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(numlist):
    
    for num in numlist:
        
        if num % 2 == 0:
            print(f'{num} is EVEN')
        else:
            None # makes it list only even as odd is ignored 

check_even(numlib)

# method 5: most basic boolean functino pass argument returns true or false

def even_checker(num):
    return num % 2 == 0

even_checker(4)
