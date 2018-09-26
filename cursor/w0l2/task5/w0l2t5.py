def print_numbers():
	res_list = []
	for i in range(1, 31):
		if (i % 3 == 0) and (i % 5 == 0):
			res_list.append('FizzBuzz')
		elif i % 3 == 0:
			res_list.append('Fizz')
		elif i % 5 == 0:
			res_list.append('Buzz')
		else:
			res_list.append(str(i))
	return res_list


if __name__ == '__main__':
	print(print_numbers())