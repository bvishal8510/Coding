# # # import math

# # # print(math.factorial(5))
# # # print(math.factorial(3))
# # # print(math.factorial(5-2))


# # # d = {'a':2, 'b':3, 'c':3}
# # # print(d.keys())
# # # print(list(d.keys()))
# # # print(d.items())

# # result = 0
# # l =[]
# # even = [2,4,8,4,4]
# # odd = [1,3]
# # for i in even:
# # 	print((1 | i) & (~1 | ~i))
# # 	if (((1 | i) & (~1 | ~i)) in l) or (((2 | i) & (~2 | ~i)) in l) or (((0 | i) & (~0 | ~i)) in l) :
# # 		result += 1
# # 	l.append(i)
# # l = []
# # for i in odd:
# # 	print((1 | i) & (~1 | ~i))
# # 	if (((1 | i) & (~1 | ~i)) in l) or (((2 | i) & (~2 | ~i)) in l) or (((0 | i) & (~0 | ~i)) in l):
# # 		result += 1
# # 	l.append(i)
# # # print("even")
# # # for j in range(len(even)-1):
# # # 	for k in range(j+1, len(even)):
# # # 		print((even[j] | even[k]) & (~even[j] | ~even[k]))

# # # print("odd")
# # # for j in range(len(odd)-1):
# # # 	for k in range(j+1, len(odd)):
# # # 		print((odd[j] | odd[k]) & (~odd[j] | ~odd[k]))

# # print("l",l)
# # print("result",result)

# while(1):
# 	n1 = int(input("Enter"))
# 	n2 = int(input("enter"))
# 	print((n1 | n2) & (~n1 | ~n2))

l = [2,3,2,5,4,1,7,8,4,8,9,1,2,9,1]
print(list(set(l)))