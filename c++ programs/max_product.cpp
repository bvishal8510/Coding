#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define o 1000000007

int main() {
    ll t;
    cin>>t;
    while(t--){
	ll i,n,k,pro=1,max=-1;
	cin>>n>>k;
	ll a[k];
	ll diff = n - ((k*(k+1))/2);
	ll j=k-1;
	if(k == 1){
		cout << ((n*n) - n) << endl;
	    continue;
	}
	if((k*(k+1))/2 <= n){
	    for(i=k-1;i>=0;i--){
	        a[i] = i+1 + (diff/k);
	    }
	    for(i=0;i<(diff%k);i++){
	        a[j]++;
	        j--;
	    }
	    for(i=0;i<k;i++){
	        pro = ((pro%o)*(((a[i]*a[i]) - a[i])%o))%o;
	    }
	    cout << (pro%o);
	}
	else {
	    cout << -1;
	}
	cout << endl;
    }
	return 0;
}