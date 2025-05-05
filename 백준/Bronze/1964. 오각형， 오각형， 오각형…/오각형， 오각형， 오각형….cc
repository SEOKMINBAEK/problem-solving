#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int n = 0;

	cin >> n;

	// n = 1, 5
	// n = 2, 5 + 10 - 3
	// n = 3, 5 + 10 - 2 + 15 - 5

	int div = 5;

	for (int i = 2; i <= n; i++) {
		div = (div + (i * 5) - (2 * (i - 1) + 1)) % 45678;
	}

	cout << div << endl;


	return 0;
}