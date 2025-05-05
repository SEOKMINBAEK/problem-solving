#include <iostream>
using namespace std;

int main() {
	int x = 0, y = 0, w = 0, h = 0;

	cin >> x >> y >> w >> h;

	double half_w = w / 2.0;
	double half_h = h / 2.0;

	int min_x = 0;
	int min_y = 0;

	if (x > half_w) {
		min_x = w - x;
	}
	else {
		min_x = x;
	}

	if (y > half_h) {
		min_y = h - y;
	}
	else {
		min_y = y;
	}

	int result = min(min_x, min_y);

	cout << result << endl;

	return 0;
}