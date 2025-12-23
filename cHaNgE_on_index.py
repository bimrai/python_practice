# Function changes letter based on index where odd is lower, even is upper. Enumerate: remember it gets index and letter of word or sentence,
# hence making it easier to specifically manipulate the data.

def myfunc(word):
    
    result = ''
    
    for index, letter in enumerate(word):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        
    return result
