import sys
script, input_decoding,  error = sys.argv


def main(language_file, decoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, decoding, errors)
		return main(language_file, decoding, errors)


def print_line(line, decoding, errors):
	next_lang = line.strip()
	print(next_lang)
	jstring = next_lang.decode()
	cooked_string = jstring.encode(decoding, errors = errors)
	
	print(jstring,'<===>',cooked_string)
	
	
languages = open("lang_bytes.txt",encoding="utf-8")

main(languages, input_decoding, error)
