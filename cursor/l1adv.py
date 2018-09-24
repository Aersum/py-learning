#Advanced Tasks
#1 Fibonacci
print('#1 Fibonacci')
def calculate_fibo(n:int):
	fibo = []
	if n == 1:
		fibo.append(1)
	elif n == 2:
		fibo.extend([1, 1])
	elif n > 2:
		fibo.extend([1, 1])
		for i in range(2, n):
			fibo.append(fibo[i-2]+fibo[i-1])
	return fibo
print(calculate_fibo(12))


#2 Matrix
print("#2 Matrix... \"Wake up Neo... :-)\"\nCreating Matrix...")
def create_matrix(first_number: int,rows: int, cols: int):
	matrix = []
	for i in range(rows):
		row = []
		for j in range(first_number, first_number + cols):
			row.append(j)
		first_number += cols
		matrix.append(row)
	#length of the last element of list without ',' and  +2(space chars)	
	matrix_width = len(str(matrix[-1]).replace(',', '')) + 2 
	#printing matrix
	print(matrix_width * '#')
	for i in range(rows):
		#getting pure row separated with spaces
		mstring = str(matrix[i]).replace(',', '')[1:-1]
		space_count = matrix_width - 4 - len(mstring)
		#adding spaces to the end of the short string
		for j in range(space_count):
			mstring += ' '
		print('# ' + mstring + ' #')
	print(matrix_width * '#')

create_matrix(10,5,5)
create_matrix(2,7,5)

