#include <stdio.h>

int total = 0;
int arr[100];

int sum(int x){
    total += x;
    return total;
}


int main(){
    int tc;
    scanf("%d", &tc);

    for (int i = 0; i<tc; i++){
        int num;
        scanf("%d", &num);

        for (int j = 0; j< num; j++){
            scanf("%d", &arr[j]);
            // int n;
            sum(arr[j]);
        }
        printf("%d", total);
    }
}