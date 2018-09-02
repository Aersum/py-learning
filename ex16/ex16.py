from sys import argv
#unpucking argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL+C.")
print("If you do want that, hit any key.")
#stopping program until hiiting the key
input("?")
#recieving the object of file with filename in writing mode
print("Opening the file...")
target = open(filename,'w')
#Erasing all informating in file
#(this don't need when file opened with 'w' parameter)
print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")
#Asking user to input lines to recording to the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#writing lines to the file and separating them 
#with \n - symbol of line breaking
target.write(f"{line1}\n{line2}\n{line3}\n")
#closing the file
print("And finally we close it.")
target.close()
