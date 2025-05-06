#pragma warning(disable:4996)
#include <stdio.h>
#include <stack>
using namespace std;

int main() {
	stack<int> stk;

	int n = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int cmd = 0;
		int x = 0;
		scanf("%d", &cmd);

		switch (cmd) {
		case 1:
			scanf("%d", &x);
			stk.push(x);
			break;
		case 2:
			if (!stk.empty()) {
				printf("%d\n", stk.top());
				stk.pop();
			}
			else {
				printf("-1\n");
			}
			break;
		case 3:
			printf("%d\n", (int)stk.size());
			break;
		case 4:
			printf("%d\n", stk.empty());
			break;
		case 5:
			if (stk.empty()) {
				printf("-1\n");
			}
			else {
				printf("%d\n", stk.top());
			}
			break;
		}
	}

	return 0;
}