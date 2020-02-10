# find the missing number from the sorted list of integers where one integer is missing between 1 to n

n = 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]


def find_missing_number(n, numbers):
	sum_of_numbers = (n * (n + 1)) / 2

	for num in numbers:
		sum_of_numbers -= num

	return int(sum_of_numbers)


print(find_missing_number(n, numbers))
