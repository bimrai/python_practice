import time
from datetime import datetime

# set what year by year, month, day and time
target = datetime(2026, 1, 1, 0, 0, 0)

while True:
    # gets the date and time of current live
    now = datetime.now() 
    # calculate what we have remaining doing differencec from target to live 
    remaining = target - now
    
    # set condition when met, celebration message comes out
    if remaining.total_seconds() <= 0:
        print("🎉 Happy New Year! Welcome to 2026! 🎉")
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(
        f"\rTime until New Year: "
        f"{days}d {hours}h {minutes}m {seconds}s",
        end=""
    )
    
    time.sleep(1)