# Stable count sort (linear time sorting algorithm)

def count_sort(collection):
	length = len(collection)

	if length == 0:
		return collection
	Max = max(collection)
	count = []
	for i in range( Max + 1):
		count.append(0)
	#print(count)
	for i in range(length ):
		count[collection[i]] = count[collection[i]] + 1;
	result = []
	#print(count)
	for j  in  range(Max + 1):
		while count[j] > 0:
			result.append(j)
			count[j] = count[j] - 1
	return result





if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print(count_sort(unsorted) )