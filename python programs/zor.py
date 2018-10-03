def myXOR(x, y):
	return ((x | y) & (~x | ~y))     #used bitwise and(&) and or(|)

n = int(input())
n1 = int(input())
print("XOR of " ,n," and ",n1," is ", myXOR(n, n1))