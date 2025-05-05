#include <iostream>
using namespace std;

int main() {
	int n = 0;

	cin >> n;

	int nums = 2 * n - 1;
	int l = 0;
	int r = nums - 1;
	bool reverse = false;

	for (int i = 0; i < nums; i++) {
		for (int j = 0; j <= r; j++) {
			if (j < l) {
				cout << ' ';
			}
			else {
				cout << '*';
			}
		}
		if (r == l) {
			reverse = true;
		}

		if (reverse) {
			l -= 1, r += 1;
		}
		else {
			l += 1, r -= 1;
		}

		cout << endl;
	}

	return 0;
}