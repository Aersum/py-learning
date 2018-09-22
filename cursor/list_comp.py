#list comprehension trying
#matrix transpose
matrix = [
[1,  2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
transposed = []
for i in range(4):
    trans_row = []
    for row in matrix:
	    trans_row.append(row[i])
    transposed.append(trans_row)
print(transposed)
