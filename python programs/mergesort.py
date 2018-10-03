import datetime

def merge(a, l, m, h):

	n1 = m - l +1
	n2 = h-m
	l1 = []
	l2 = []
	for i in range(n1):
		l1.append(a[l+i])
	for j in range(n2):
		l2.append(a[m + j +1])
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if l1[i] < l2[j]:
			a[k] = l1[i]
			i += 1
		else:
			a[k] = l2[j]
			j += 1
		k += 1

	while i < n1:
		a[k] = l1[i]
		i += 1
		k += 1

	while j < n2:
		a[k] = l2[j]
		j += 1
		k += 1


def mergesort(a, l, h):

	if l < h:
		mid = int((l + (h-1))/2)

		mergesort(a, l, mid)
		mergesort(a, mid+1, h)

		merge(a, l, mid, h)


a = list(eval(input("Enter the elements of array ")))
start_time = datetime.datetime.now()
print("unsorted array ",a)
mergesort(a, 0, len(a)-1)
print("Sorted array ",a)
end_time = datetime.datetime.now()
print(end_time - start_time)
