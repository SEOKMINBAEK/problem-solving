#include <stdio.h>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(stack<int>* a, stack<int>* b) {
	return b->top() < a->top();
}

int main() {
	int n = 0;
	scanf("%d", &n);

	int num = 0;

	stack<int> stk1;
	stack<int> stk2;
	stack<int> stk3;
	stack<int> stk4;

	// top 초기화
	stk1.push(0);
	stk2.push(0);
	stk3.push(0);
	stk4.push(0);

	vector<stack<int>*> stacks{ &stk1, &stk2, &stk3, &stk4 };

	for (int i = 0; i < n; i++) {
		scanf("%d", &num);

		// 스택들을 top()기준으로 내림차 순으로 정렬
		sort(stacks.begin(), stacks.end(), compare);

		bool is_continue = false;

		// 스택들을 순회
		for (stack<int>* stk : stacks) {
			// 스택의 top보다 num이 높으면 push
			if (stk->top() < num) {
				stk->push(num);
				is_continue = true;
				break;
			}
		}

		// 모든 스택들의 top보다 num이 낮으면 실패
		if (!is_continue) {
			printf("NO");
			exit(0);
		}
	}

	printf("YES");

	return 0;
}