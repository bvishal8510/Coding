#include <bits/stdc++.h> 
using namespace std; 
  
int power(int a, unsigned int n, int p) 
{ 
    int res = 1;
    a = a % p; 
    

    while (n > 0) 
    { 
        if (n & 1) 
            res = (res*a) % p; 
  
        n = n>>1; 
        a = (a*a) % p; 
    } 
    cout << "res after change" << res << "\n";
    return res; 
} 
  
bool isPrime(unsigned int n, int k) 
{ 
   if (n <= 1 || n == 4)  return false; 
   if (n <= 3) return true; 
  
   while (k>0) 
   { 
       int a = 2 + rand()%(n-4);   
      cout << "value of a is " << a << "\n";
       if (power(a, n-1, n) != 1) 
          return false; 
  
       k--; 
    } 
    cout << "End";
    return true; 
} 
  
int main() 
{ 
    int k = 3;
    int a,b; 
    cout << "Enter numbers ";
    cin >> a >> b;
    isPrime(a, k)?  cout << " true\n": cout << " false\n"; 
    isPrime(b, k)?  cout << " true\n": cout << " false\n"; 
    return 0; 
} 