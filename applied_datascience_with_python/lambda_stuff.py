def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [i*j for i in range(10) for j in range(10)]

# user id based q: get each user with two letters and two numbers 
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = []
for firstletter in lowercase:
    for secondletter in lowercase:
        for firstdigit in digits:
            for seconddigit in digits:
                answer.append(firstletter + secondletter + firstdigit + seconddigit)

correct_answer == answer