#include <stdio.h>

int reverse(int n){
    int hasil = 0;
    while (n){
        hasil = (hasil * 10) + (n%10);
         n = n/10;
    }

    return hasil;
}

int main(){
    int tc;
    scanf("%d", &tc);

    for (int i = 0; i < tc; i ++){

        int num1, num2;
        scanf("%d %d", &num1, &num2);

        num1 = reverse(num1);
        num2 = reverse(num2);

        int total = num1 + num2;
        total = reverse(total);

        printf("%d \n", total);
    }
}
