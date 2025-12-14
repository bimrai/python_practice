# Simple game life counting iteration using while till 0 to end game with a you lose message as well as a else case scenario in any chance player maintains lives and wins!

lives = 5
death = False

print(f'You have {lives} lives!')

while lives > 0:
    lives -= 1
    print(f'You have {lives} lives remaining!')
    

if lives <= 0 or death:
    print(f'You have {lives} remaining! YOU LOSE!')
else:
    print(f'YOU WIN!')
