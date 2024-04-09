#include <stdio.h>
#include <stdlib.h>
using namespace std;

long long MOD = 1000000007;
long long power3(long long base, long long e){
    if(e == 0)
        return 1;
    else if(e == 1)
        return base % MOD;
    else
    {
        long long hasil = power3(base, e/2);
        hasil = (hasil % MOD * hasil% MOD);
    
        if(e & 1)
            hasil = (hasil% MOD * base% MOD);
    
        return hasil % MOD;
    }
}

long long max_earnings(long long n) {
    if (n <= 2) return n;
    if (n % 3 == 0) {
        return power3(3, n / 3);
    } 
    else if (n % 3 == 1) {
        return (4 * power3(3, (n - 4) / 3)) % MOD;
    } 
    else { // n % 3 == 2, one segment of 2 and the rest in segments of 3
        return (2 * power3(3, (n-2) / 3)) % MOD;
    }
}

int main(){
    long long tc, length;

    scanf("%d", &tc);

    for (int i = 0; i<tc; i++){
        scanf("%lld", &length);
        printf("%lld\n", max_earnings(length));
    }
}