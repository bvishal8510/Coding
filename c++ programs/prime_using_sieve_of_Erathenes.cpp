#include<bits/stdc++.h>
using namespace std;

int sieve_of_Erathenes(int n)
{
	int prime[n+1];
	memset(prime, 1, sizeof(prime));

	for(int p=2; p*p<=n; p++)
	{
		if(prime[p])
		{
			for(int i=p*2; i<=n; i=i+p)
				prime[i] = 0;
		}
	}

	for(int i=2; i<=n; ++i)
	{
		if(prime[i])
		{
			cout << i << " "; 
		}
	}
}

int main()
{
	int num;
	cout << "Enter range  :";
	cin >> num;
	sieve_of_Erathenes(num);
	return 0;
}