#include <stdio.h>
#include <stack>
#include <vector>
using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	stack<vector<int>> stk;
	vector<int> heights(n);
	int height = 0;
	long long result = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", &height);
		heights[i] = height;
	}

	for (int i = n - 1; i >= 0; i--) {
		// [높이, 보이는 건물의 수]
		vector<int> vec{ heights[i], 0 };

		if (stk.empty()) {
			stk.push(vec);
			continue;
		}

		vector<int> top = stk.top();

		// 현재 높이가 앞 건물보다 높으면 제거, 보이는 건물의 수는 현재 보이는 앞 건물(1) + 앞 건물이 보이는 건물의 수
		while (heights[i] > top[0]) {
			stk.pop();
			vec[1] += 1 + top[1];

			if (stk.empty()) {
				break;
			}

			top = stk.top();
		}

		stk.push(vec);
		result += vec[1];
	}

	printf("%lld\n", result);

	return 0;
}