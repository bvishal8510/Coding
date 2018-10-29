#include <bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin>>t;
	cin.ignore();
	while(t--){
	    int i,j,k,l,m,n,o;
	    cin>>n>>m;
	    char a[n][m]; 
	    int count[n+m-2]={0};
	    for(i=0;i<n;i++){
	        for(j=0;j<m;j++){
	            cin>>a[i][j];
	        }
	    }
	    for(o=1;o<=n+m-2;o++){
	        for(i=0;i<n;i++){
	            for(j=0;j<m;j++){
	                if(a[i][j] == '1'){ 
	                    for(k=0;k<n;k++){
	                        for(l=0;l<m;l++){
	                            if(a[k][l] == '1'){
	                                if(abs(i-k) + abs(j-l) == o){
	                                    count[o-1]++;
	                                }
	                            }
	                        }
	                    }    
	                }
	            }
	        }
	    }
	    for(o=0;o<n+m-2;o++){
	        cout<<count[o]/2<<" ";
	    }
	    cout<<endl;
	}
	return 0;
}