from sys import argv
from os.path import exists
script, from_file,to_file = argv
print(f"Copying from {from_file} to {to_file}")
#in_file = open(from_file)
#out_file = open(to_file,'w')
#out_file.write(in_file.read())
#out_file.close()
#in_file.close()
#*****************Another realization
print(f"File {to_file} exists? {exists(to_file)}")
with open(from_file) as f:
	in_data = f.read()
with open(to_file,'w') as f:
	f.write(in_data)
