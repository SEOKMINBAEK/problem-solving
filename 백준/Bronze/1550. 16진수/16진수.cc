#include <iostream>
#include <cmath>
using namespace std;

int main() {
	string hexstr = "";
	cin >> hexstr;

	int total = 0;

	for (int i = 0; i < hexstr.length(); i++) {
		char ch = hexstr[i];
		int ascii_no = ch;
		int num = 0;

		if (ascii_no >= 65 && ascii_no <= 70) {
			num = ascii_no - 55;
		}
		else {
			num = ch - '0';
		}
		int base = pow(16, (hexstr.length() - (i + 1)));
		total += num * base;
	}

	cout << total << endl;

	return 0;
}