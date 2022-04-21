#include <iostream>
using namespace std;

int calculator(int m, int n){
    int board_size = m * n;
    int result = (board_size -(board_size % 2))/2;
    return result;
}
int main(){
    int m,n, result;
    cin >> m;
    cin >> n;

    result = calculator(m,n);
    cout << result;

    return 0;
}
