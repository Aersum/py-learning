from sys import argv
#unpucking
script, filename = argv
print(f"Openning file {filename}...")
txt = open(filename)
print("Here's content of file:")
print("------------")
print(txt.read())
print("------------")
print("Closing the file")
txt.close()
