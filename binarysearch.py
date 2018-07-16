def binarysearch(b, e, el):
	mid = int((e+b)/2)
	if (b <= e):
		if l[mid] == el:
			return (mid+1)
		elif el > l[mid]:
			b = mid+1
			return binarysearch(b, e, el)
		else:
			e = mid-1
			return binarysearch(b, e, el)
	else:
		return -1

n = int(input())
a = input()
el = int(input())
l = a.split()
l = list(map(lambda x : int(x), l))
beg = 0
end = len(l)-1
print(binarysearch(beg, end, el))