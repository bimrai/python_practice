from random import shuffle

# shuffle ball list

def shuffle_list(ball):
    shuffle(ball)
    return ball

# We now make a player guess so take in input

def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']: # reason list of choice is string in while loop is because input returns string so must match
        guess = input('Pick a number between 0, 1, or 2: ')

    return int(guess) # we then convert that string to a integer afterwards to match the index place of shuffle_list

# now we combine the functions to check the player guess with the balls location

def check_guess(ball, guess):
    if ball[guess] == 'O':
        print("CORRECT GUESS!")
    else:
        print("Unlucky... Maybe next time!")
        print(ball)



# MAIN LOGIC:

# INITIAL LIST

ball = ['', 'O', '']

# SHUFFLE LIST

mix_ball = shuffle_list(ball)

# USER GUESS

guess = player_guess()

# CHECK GUESS AND LIST

check_guess(mix_ball, guess)