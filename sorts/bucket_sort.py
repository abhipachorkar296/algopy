# you can change bucket size according to your input

def bucket_sort(collection , bucket_size = 5):
	length = len(collection)
	if length == 0:
		print("add elements")
	Max , Min = max(collection) , min(collection)
	bucket_count = ((Max - Min ) // bucket_size + 1)
	buckets = [[] for _ in range(int(bucket_count))]
	for i in range(length ):
		buckets[int((collection[i] - Min) // bucket_size)].append(collection[i])
	length1 = len(buckets)
	length2 = len(buckets[0])
	result = sorted(buckets[i][j] for i in range(length1) for j in range(length2))
	return result





if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print(bucket_sort(unsorted) )