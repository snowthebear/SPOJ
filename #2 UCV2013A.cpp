#include <stdio.h>


long long mod = 1000000007;

long long fast_exponent(long long base, long long e)
	{
		if(e == 0)
			return 1;
		else if(e == 1)
			return base % mod;
		else
		{
			long long hasil = fast_exponent(base, e/2);
			hasil = (hasil % mod * hasil% mod);
		
			if(e & 1)
				hasil = (hasil% mod * base% mod);
		
			return hasil % mod;
		}
	}

int main(){
    int n, l;

    while (true){
        scanf("%d", &n);
        scanf("%d", &l);

        if (n == 0 && l == 0) break;

        long long hasil = 0;

        for (int i = 0; i < l; i++){
            hasil = (hasil + fast_exponent(n, i+1)) % mod;
        }
        
        printf("%lld\n", hasil);
    }
    
}