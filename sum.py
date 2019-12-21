def sum_of_num():
	num_list = []
	num = int(input('How many numbers: '))

	for n in range(num):
		numbers = int(input('Enter Number :'))
		num_list.append(numbers)
	return sum(num_list)

print(sum_of_num())