from random import random
from math import ceil
numb = ceil(random()*10)
user_numb = 0
print("Guess number from 0 to 10. input 'show' to show the answer")
while user_numb != numb:
	user_numb = input(">")
	try:
		user_numb = int(user_numb)
	except ValueError:
		if user_numb == 'show':
			print(numb)
	if user_numb == numb:
		print("Guessed!")
	else:
		print("Wrong :-(")
