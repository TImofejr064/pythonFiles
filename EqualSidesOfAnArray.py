def find_even_index(arr):
	left_sum = 0
	right_sum = 0
	for i in range(0, len(arr)-1):

		if i == 0:
			left_sum = 0

			for j in range(i+1, len(arr)-1):
				right_sum += arr[j]

			if left_sum == right_sum:
				return arr[i]
			else : continue
		else:
			for j in range(i+1, len(arr)-1):
				right_sum += arr[j]

			for g in range(i-1, 0):
				left_sum += arr[g]

		if left_sum == right_sum:
			return arr[i]
		else: continue

print(find_even_index([1,2,1]))