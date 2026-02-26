strings = ['a', 'b', 'c']

location_map = { value: index for index, value in enumerate(strings) }
print(location_map)

location_map_2 = { index:value for index, value in enumerate(strings) }
print(location_map_2)
