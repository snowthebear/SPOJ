#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

// Greedy Algorithm

int main(){
    int tc, total, m, n;
    pair<int,int> arr[100001];

    scanf("%d", tc);
    
    for (int t = 0; t< tc; t++){
        scanf("%d", &total);

        for (int i = 0; i< total; i++){
            scanf("%d %d", &m, n);
            arr[i] = make_pair(n,m);
        }
        sort(arr, arr + total);

        int counter =1;
        for (int j = 0, k = 1; k <= total; k++){
            if (arr[k].second > arr[j].first){
                counter++;
                j++;
            }
        }
        printf("%d\n", counter);
    }
}