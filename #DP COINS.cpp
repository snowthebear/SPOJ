#include <stdio.h>

long long arr[10000005];

long long coin(long long n){

    if (n > 10000000)
        return coin(n/2) + coin(n/3) + coin(n/4);

    if (n >= (n/2)+(n/3)+(n/4))
        return arr[n] = n;
    
    if (arr[n] != 0)
        return arr[n];

    return arr[n] = coin(n/2) + coin(n/3) + coin(n/4);

}
int main(){
    long long n;
    while(scanf("%lld", &n) != EOF) { // Read until end of file
        printf("%lld\n", coin(n));
    }
}