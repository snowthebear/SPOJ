#include <stdio.h>

long long base, e, m;

long long f ( long long base, long long e, long long m)
{
    if (e == 0)
        return 1;

    else if(e == 1)
         return base % m;
    else
     {
         long long hasil = f ( base, e / 2, m);
         hasil = ((hasil % m) * (hasil % m)) % m;

         if (e % 2 !=0)
            hasil = ((hasil % m) * (base % m)) % m;
        return hasil;
    }
}

int main(){

    int tc;
    scanf("%d", &tc);

    for (int i = 0; i< tc; i++){
        long long hasil;
        scanf("%lld", &base);
        scanf("%lld", &e);
        scanf("%lld", &m);

        hasil = f ( base, e, m);
        printf ("%d. %lld\n", i+1, hasil);

    }
}