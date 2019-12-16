def max_num():
	num_list = []
	num = int(input('How many numbers: '))

	for n in range(num):
		numbers = int(input('Enter Number :'))
		num_list.append(numbers)
	return max(num_list)

print(max_num())