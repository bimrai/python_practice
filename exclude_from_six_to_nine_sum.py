# this function adds/sums up any number outside 6 and 9 range. 
# so any number excluding 6 and 9, that are within start of 6 throughout 9, do not get summed up
# any number outside 6 and 9 are summed up and returns that result

def summer_69(arr):

    total = 0
    inside_six_nine = False

    for num in arr:
        if num == 6:
            inside_six_nine = True
        elif num == 9 and inside_six_nine:
            inside_six_nine = False
        elif not inside_six_nine:
            total += num
    return total

summer_69([1, 3, 5]) # 9 because 1 + 3 + 5 = 9
summer_69([4, 5, 6, 7, 8, 9]) # 9 because 4 + 5 = 9, we ignore 6, 7, 8, 9 because the condition within for loop ignores
