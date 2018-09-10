### EX23
### New things in exersise
```python
languages = open("languages.txt",encoding="utf-8")
```
```python
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors = errors)
	cooked_string = raw_bytes.decode(encoding, errors = errors)
```
```python

```

[Return to main repo page](https://github.com/Aersum/py-learning)
