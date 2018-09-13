### EX23
### New things in exersise
```python
languages = open("languages.txt",encoding="utf-8")
```
```python
def print_line(line, encoding, errors):
	next_lang = line.strip() #delete white spaces from begin and end of string
	raw_bytes = next_lang.encode(encoding, errors = errors) #get byte string b'xxx'
	cooked_string = raw_bytes.decode(encoding, errors = errors)
```
```python
>>> 0b1011010
90
```
```python
ord ( ’Z ’ ) #turns character to number in ASCII table
```
```python
chr(90)  #turns Ascii number into character
```


[Return to main repo page](https://github.com/Aersum/py-learning)
