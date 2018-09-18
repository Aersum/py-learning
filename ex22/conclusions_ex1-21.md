### EX22
### Laearned Pywords list

 * print
 * input
 * ==, >=, <=, !=
 * True, False
```python
print("We have",passengers,"to carpool today")
```
```python
round(x) #rounds a number
```
```python
print(f"Let's talk about {name}.") #f-string
```
```python
print("328/30={0:0.2f}".format(x))   #formtting for float numbers
```
 ```python
"Isn't that joke so funny?! {}".format(some_var)
```
```python
print("."*10) 
```
```python 
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') 
```
```python
print ("""
 Some
          Formatted
    Text
""")
```
```python
taby_cat = "\tI'm tabbed in."
```
```python
from sys import argv
script, name, surname, age = argv
```
```python
txt = open(filename)
print(txt.read())
txt.close()
```
```python
target = open(filename,'w')
```
```python
from os.path import exists
exists(to_file)
```
```python
with open(from_file) as f:
	in_data = f.read()
```
```python
#so many args
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
```
```python
#Rewind to begin of file
def rewind(f):
	f.seek(0)
```
```python
f.readline() #read only one line from current position
```
```python
# standart def form
def func(arg)
    b=arg
    return b
```

[Return to main repo page](https://github.com/Aersum/py-learning)
