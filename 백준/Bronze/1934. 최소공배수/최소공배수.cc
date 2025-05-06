#include <iostream>
using namespace std;

int main() {
	int t = 0;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int a = 0, b = 0;
		cin >> a >> b;

		int maxi = 0;
		int mini = 0;

		if (a > b) {
			maxi = a;
			mini = b;
		} else {
			maxi = b;
			mini = a;
		}

		int multi = maxi;

		while (multi % mini != 0) {
			multi += maxi;
		}

		cout << multi << endl;
	}

	return 0;
}