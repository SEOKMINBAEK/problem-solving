#include <stdio.h>
#include <stack>
#include <vector>
using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	vector<int> arr(n, 0);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	vector<int> result(n, 0);
	stack<int> stk;

	for (int i = n - 1; i >= 0; i--) {
		if (stk.empty()) {
			stk.push(arr[i]);
			result[i] = -1;
			continue;
		}

		// 오른쪽 값
		int top = stk.top();

		// 왼쪽값이 오른쪽 값보다 크거나 같으면 pop
		while (arr[i] >= top) {
			stk.pop();

			if (stk.empty()) {
				break;
			}

			// 오른쪽 값 갱신
			top = stk.top();
		}

		if (stk.empty()) {
			result[i] = -1;
		}
		else {
			result[i] = top;
		}

		stk.push(arr[i]);
	}

	for (int i = 0; i < n; i++) {
		printf("%d", result[i]);
		if (i < n - 1) {
			printf(" ");
		}
	}

	return 0;
}