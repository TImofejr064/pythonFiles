def descending_order(num):
	num = list(str(num))
	for i in range(len(num)-1):
		for j in range(len(num)-i-1):
			if num[j] < num[j+1]:
				num[j], num[j+1] = num[j+1], num[j]
	ss = ''
	for i in range(0, len(num)):
		ss += str(num[i])

	ss = int(ss)
	return ss

print(descending_order(3213))