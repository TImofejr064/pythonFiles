def iq_test(numbers):
	numbers = numbers.replace(" ", "")
	even_num = []
	odd_num = []
	for i in range(0, len(numbers)):
		if int(numbers[i]) % 2 == 0:
			even_num.append(i+1)
		else:
			odd_num.append(i+1)
	if len(even_num) > len(odd_num):
		return odd_num[0]
	else:
		return even_num[0]

print(iq_test("46 42 30 26 12 6 32 2 48 13 40 44 32 24 28 4 24 48 34 30 16 20 32 40 40 50 20 50 12 18 0 38 48 10 40 14 18 44 40 42 36 28 36 28 50 22 10 3"))