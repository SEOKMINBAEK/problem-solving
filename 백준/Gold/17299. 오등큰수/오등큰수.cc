#include <stdio.h>
#include <stack>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	stack<int> stk;
	unordered_map<int, int> count;
	vector<int> arr(n);
	vector<int> result(n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		
		if (count.count(arr[i]) == 0) {
			count[arr[i]] = 1;
		}
		else {
			count[arr[i]] += 1;
		}
	}

	for (int i = n - 1; i >= 0; i--) {

		if (stk.empty()) {
			stk.push(arr[i]);
			result[i] = -1;
			continue;
		}

		// 오른쪽 값과 등장횟수
		int top = stk.top();

		// 왼쪽 값의 등장횟수가 오른쪽 값의 등장횟수보다 크거나 같으면 pop
		while (count[arr[i]] >= count[top]) {
			stk.pop();

			if (stk.empty()) {
				break;
			}

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