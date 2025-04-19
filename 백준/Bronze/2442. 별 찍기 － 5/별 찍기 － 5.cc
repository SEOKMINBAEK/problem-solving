#include <iostream>
#include <string>
using namespace std;

int main() {
    // n번째 줄에 2*n-1개의 별을 찍는다.
    int n = 0;
    cin >> n;
    
    int len = 2 * n - 1; // 9
    
    for (int i = 1; i <= n; i++) {
        int star_len = 2 * i - 1;
        string line = "";
        int space_len = (len - star_len) / 2;
        
        for (int j = 0; j < space_len; j++) {
            line += " ";
        }
        
        for (int j = 0; j < star_len; j++) {
            line += "*";
        }
        
        cout << line;
        
        if (i < n) {
            cout << endl;
        }
    }
}