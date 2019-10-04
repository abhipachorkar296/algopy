def bubble_sort(collection):
	length = len(collection)
	if length <= 1:
		return collection
	else:
		for i in range(length - 1):
			for j in range(length - i - 1 ):
				if collection[j] > collection [j+1]:
					collection[j] , collection[j+1] = collection[j+1] , collection[j]
					#print(i,j)
		return collection
					
if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( bubble_sort(unsorted) )