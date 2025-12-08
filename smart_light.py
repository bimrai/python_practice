# runs the first if condition - sligtly similar to js 
is_light_on = False
brightness_percentage = 0
light_mood = "Soft Warm Mood"
motion_detected = True
is_night_time = False

if is_night_time == False:
    print(f'The light is off - Light: {is_light_on}, Brightness Percentage: {brightness_percentage}')
elif motion_detected == True and is_night_time != False:
    is_light_on = True
    brightness_percentage = 75
    print(f'The Light is on - Light: {is_light_on}, Brightness Percentage: {brightness_percentage}, Light Mood: {light_mood}')
else:
    print("Lights Off")

# runs the second if condition in elif - attempting pythonic boolean logic
is_light_on = True
brightness_percentage = 0
light_mood = "Soft Warm Mood"
motion_detected = True
is_night_time = True

if not is_night_time:
    print(f'The light is off - Light: {is_light_on}, Brightness Percentage: {brightness_percentage}')
elif motion_detected and is_night_time:
    is_light_on = True
    brightness_percentage = 75
    print(f'The Light is on - Light: {is_light_on}, Brightness Percentage: {brightness_percentage}, Light Mood: {light_mood}')
else:
    print("Lights Off")
