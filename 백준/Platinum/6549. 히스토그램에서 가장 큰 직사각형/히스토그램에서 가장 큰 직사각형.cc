#include <stdio.h>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Rect {
	int h;
	int i;
};

int main() {
	int n = 0;

	while (true) {
		scanf("%d", &n);

		if (n == 0) {
			exit(0);
		}

		stack<Rect> stk;

		long long maxi = 0;
		int h = 0;

		for (int i = 0; i <= n; i++) {
			if (i < n) {
				scanf("%d", &h);
			}
			else {
				h = 0;
			}

			while (!stk.empty() && h < stk.top().h) {
				long long height = stk.top().h;

				stk.pop();

				if (stk.empty()) {
					maxi = max<long long>(maxi, height * i);
				}
				else {
					maxi = max<long long>(maxi, height * (i - stk.top().i - 1));
				}
			}

			stk.push({ h, i });
		}

		printf("%lld\n", maxi);
	}

	return 0;
}