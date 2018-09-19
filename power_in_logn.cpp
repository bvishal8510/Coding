#include <bits/stdc++.h>
using namespace std;

int power(int a, unsigned int b)
{
	int res = 1;

	while(b > 0)
	{
		// cout << "the value of b is :" << b;
		if(b & 1)
			res = res * a;

		b = b >> 1;
		a = a*a;
	}
	return res;
}

int main()
{
	int num;
	unsigned int num1;
	cout << "Enter number and power  :";
	cin >> num;
	cin >> num1;
	cout << "power of " << power(num,num1);
	return 0;
}