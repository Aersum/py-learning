from sys import argv
#unpucking argv
scrript, input_file = argv
#Definition function that prints all file
def print_all(f):
	print(f.read())
#Rewind to begin of file
def rewind(f):
	f.seek(0)
#Print one line from current position
def print_a_line(line_count, f):
	print(line_count, f.readline())
#Getting object of file
current_file = open(input_file)

print("First let's print the whole file:\n")
#Passing object of file to function in argument
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
#line_count = 1
current_line = 1
print_a_line(current_line, current_file)
#line_count = 2
current_line += 1
print_a_line(current_line, current_file)
#line_count = 3
current_line += 1
print_a_line(current_line, current_file)
