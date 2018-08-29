import datetime


def partition(a, l, h):

	pivot = a[h]

	i = l-1

	for j in range(l, h):                      #from low to high
		if a[j] <= pivot:                        #less than or equalto
			i += 1
			a[i],a[j] = a[j],a[i]
	i += 1
	a[i],a[h] = a[h], a[i]
	return i


def quicksort(a ,l, h):
	if l < h:
		pi = partition(a, l, h)

		quicksort(a, l, pi-1)
		quicksort(a, pi+1, h)


a = list(eval(input("Enter the elements of array ")))
start_time = datetime.datetime.now()
print("unsorted array ",a)
quicksort(a, 0, len(a)-1)
print("Sorted array ",a)
end_time = datetime.datetime.now()
print(end_time - start_time)
