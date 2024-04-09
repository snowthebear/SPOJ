#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
using namespace std;

long long l, r, mod;
long long MOD = 1000000007;


long long fast_exponent(long long base, long long e)
{
    if(e == 0)
        return 1;
    else if(e == 1)
        return base % MOD;
    else
    {
        long long hasil = fast_exponent(base, e/2);
        hasil = (hasil % MOD * hasil% MOD);
    
        if(e & 1)
            hasil = (hasil% MOD * base% MOD);
    
        return hasil % MOD;
    }
}

long long pengurangan(long long a, long long b){
    a = a % MOD;
	b = b % MOD;
	long long temp = (a - b) % MOD;
	if(temp<0)
		temp = (temp + MOD) % MOD;
	return temp;

}
long long mod_sum (long long n){

    long long inverse_penyebut = fast_exponent(2, MOD-2) % MOD;
    long long satuputar_pembilang = (mod % MOD * pengurangan(mod,1)) % MOD;

    long long satu_putaran = (satuputar_pembilang * inverse_penyebut) % MOD;


    long long jumlah_putaran = (n % MOD)/ (mod % MOD);
    long long sisa_angka = n % mod;

    long long pembilang = sisa_angka % MOD *( sisa_angka % MOD + 1) % MOD;
    long long deret_sisa_angka = (pembilang * inverse_penyebut) % MOD;


    return (satu_putaran * jumlah_putaran % MOD) + deret_sisa_angka % MOD;

}

int main(){

    scanf("%lld", &l);
    scanf("%lld", &r);
    scanf("%lld", &mod);

    long long mod_kiri =  mod_sum(l-1);
    long long mod_kanan = mod_sum(r);

    long long hasil = pengurangan(mod_kanan, mod_kiri);

    printf("%lld\n", hasil);
}