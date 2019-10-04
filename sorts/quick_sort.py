def quick_sort(collection):
	length = len(collection)
	if length <= 1:
		return collection
	else:
		pivot = collection.pop()
		smaller = []
		greater = []
		for element in collection :
			if element > pivot:
				greater.append(element)
				print(greater)
			else:
				smaller.append(element)
				print(smaller)
		return quick_sort(smaller) + [pivot] + quick_sort(greater)



if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )