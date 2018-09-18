import sys
#script, input_decoding,  error = sys.argv

def bfile_create():
	file_wbytestr = open('lang_bytes.txt')
	binary_file = open("raw_bytes_lang.txt", "wb")
	line = file_wbytestr.readline()
	if line:
		binary_file.write(line)
		return bfile_create()
	bynary_file.close()
	file_wbytestr.close()
	print('OK')
bfile_create()
