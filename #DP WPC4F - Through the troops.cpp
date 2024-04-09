#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
using namespace std;

int n; //number of turtle
int energy[50][5];
int memo[50][5];

int min_energy(int row, int col ){
    if(row>n-1){
        return 0;
    }

    if(memo[row][col] != -1){
        return memo[row][col];
    }

    if (col == 0){
        return memo[row][col] = energy[row][col] + min(min_energy(row+1, col+1), min_energy(row+1, col + 2));
    }
    else if (col == 1){
        return memo[row][col] = energy[row][col] + min(min_energy(row+1, col-1), min_energy(row+1, col + 1));
    }

    else{
		return memo[row][col] = energy[row][col] + min(min_energy(row+1,col-1),min_energy(row+1,col -2));
    }

}   


int main(){
    int tc;
    scanf ("%d", &tc);

    for (int t = 0; t< tc; t++){
        int hasil = 10000005;
        scanf ("%d", &n);

        memset(memo,-1, sizeof(memo)); //isi memo -1 semua

        for(int i = 0; i<n ; i++){
            for (int j = 0; j < 3; j++){
                scanf("%d", &energy[i][j]); //isi memo sesuai scanf
            }
        }

        for (int j = 0; j<3; j++){
            hasil = min(hasil, min_energy(0, j));
        }
        
        printf("%d \n", hasil);
    }

    
}