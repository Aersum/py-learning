from sys import argv
#pass argument from argv to file name
#script, filename = argv
#creating object "txt" of file passed to "filename"
#txt = open(filename)
#printing result of  working method txt.open()
#print(f"Here's your file {filename}:")
#print(txt.read())
#input
filename = input("Enter file name: ")
txt = open(filename)
print("Here's your file:")
print(txt.read())
txt.close()
