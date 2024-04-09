#include <stdio.h>
#include <math.h>

bool isPrime(int n){
    if (n == 1) return false;

    if (n != 2 && n % 2 == 0) return false;

    for (int i = 3; i<= sqrt(n); i += 2){
        if (n % i == 0 ){
            return false;
        }
    }
    return true;

}

void checkPrime(int lowerbound, int upperbound){

    for (int i = lowerbound; i <= upperbound; i++) {
        if (isPrime(i)){
            printf("%d\n", i);
        }
    }
}

int main(){
    int t;
    scanf("%d", &t);

    int lowerbound, upperbound;

    for (int i = 0; i< t; i++){
        scanf("%d %d",&lowerbound, &upperbound);
        checkPrime(lowerbound, upperbound);

    }
}