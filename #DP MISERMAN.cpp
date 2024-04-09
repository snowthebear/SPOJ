#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
using namespace std;

int n, m;
int fare[101][101];
int arr[101][101];

int total_fare(int row, int col){
    if(row>n-1){return 0;}
    
    if (arr[row][col] != -1){
        return arr[row][col];
    }

    if (col == 0){
        return arr[row][col] = fare[row][col] + min(total_fare(row+1, col+1), total_fare(row+1, col));
    }
    else if(col==m-1){
		return arr[row][col] = fare[row][col] + min(total_fare(row+1,col-1),total_fare(row+1,col));
    }
	else{
		return arr[row][col] = fare[row][col] + min(total_fare(row+1,col+1),min(total_fare(row+1,col),total_fare(row+1,col-1)));
	}

}

int main(){
    scanf ("%d", &n);
    scanf ("%d", &m);

    int hasil = 1000005;

    memset(arr,-1, sizeof(arr));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m ; j++){
            scanf ("%d", &fare[i][j]);
        }
    }

    for (int j = 0; j < m; j++) {
        hasil = min(hasil, total_fare(0, j));
    }

    printf("%d", hasil);
    
}