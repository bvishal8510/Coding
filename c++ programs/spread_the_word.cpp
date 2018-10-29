#include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
    long long int t, total_people, day_count, people_know, i, num;
    cin >> t;
    while(t--)
    {
        cin >> total_people;
        long long int a[total_people];
        for(i = 0; i<total_people; ++i)
        {
            cin >> a[i];
        }

        day_count = 0;
        people_know = 1;
        while(people_know < total_people)
        {
            num = people_know;
            for(i=0; i < num; ++i)
                people_know = people_know + a[i];
            day_count++;
        }
        cout << day_count << "\n"; 
    }
    return 0;
}