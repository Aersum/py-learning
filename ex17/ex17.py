from sys import argv
from os.path import exists
#unpucking
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file} (Existing: {exists(to_file)})->",end=' ')

#we colud do these two on one line, how?
in_file = open(from_file)
#in_data = in_file.read()

#print(f"The input file is {len(in_data)} bytes long")

#print(f"Does the outout file exist? {exists(to_file)}")
#print("Ready, hit Return to continue. CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(in_file.read())

print("OK")

out_file.close()
in_file.close()
