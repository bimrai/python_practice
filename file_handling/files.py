# r = Read
# a = Append
# w = Write
# x = Create

# READ - Read will return error if it does not exist.

# f for file

f = open("names.txt", "r")
# print(f.read()) # reads all file text
# print(f.read(2)) # retrieves only first 2 characters on the file

# print(f.readline()) # reads first line only
# print(f.readline()) # stacking readline reads the next line after previous line
 
 # for loop runs through each line within the text printing it all out. For loop
 # handles repetitive tasks over laborous tasks. Automation woooow   
# for line in f:
#     print(line)
    
# always close your files once opened and done manipulating or reading etc with. 
# f.close()

# a 'try except' (aka try catch in js) method to opening/reading files
# if file exists, it will open and read, if not, it will throw error message 
# it also handles the close if opened.

# try:
#     # f = open("not_exist.txt") # if file doesnt exist
#     f = open("names.txt") # file exists
#     print(f.read())
# except:
#     print("Error: File does not exist.")
# finally:
#     f.close()
#     print("File is closed.")
    
# APPEND - Appending is to add at the end of the files contents
    
f = open("names.txt", 'a') #specify mode to a
f.write("Wanda\n")
f.close()

f = open("names.txt")
print(f.read()) 
f.close()

# open("hero_list.txt", "w").close() <- resets

# Write - Overwrites whatever is in the file
f = open("hero_list.txt", "w")
# this replaces all content that previously existed and replaces it with 
# whatever you write within the write method
f.write("*Thanos clicks* This overwrites all the avengers on the list!")
f.close()

#printing to check 
f = open("hero_list.txt")
print(f.read())
f.close()