#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	long long int i,n,count = 0;
	cin>>n;
	long long int a[n],max, temp;
	for(i=0;i<n;i++){
	    cin>>a[i];
	    if(a[i] == -1){
	        count++;
	        a[i] = a[i-1]+1;
	    }
	}
	if(count == n){
	    cout<<"inf";
	    goto h;
	}
	max = *max_element(a, a+n);
	temp = a[0];
	for(i=1;i<n;i++){
	    if(temp+1 != a[i] && a[i]!=1){
	        cout<<"impossible";
	        goto h;
	    }
	    temp = a[i];
	}
	cout<<max;
	h: cout<<endl;
	}
	return 0;
}