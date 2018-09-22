#Task2
#1
task_two_list = list(range(1,20,2))
print(task_two_list)
#2
task_three_list = []
task_three_list = task_two_list + [1, 5, 13, 20]
print(task_three_list)
#3
task_four_set = set(task_three_list)
print(task_four_set)
#4
def compare_elements(a:list, b:set):
	lena = len(a)
	lenb = len(b)
	if lena > lenb:
		return "List is bigger"
	elif lena == lenb:
		return "They are equal"
	else:
		return "Set is bigger" 
print(compare_elements(task_three_list, task_four_set))
