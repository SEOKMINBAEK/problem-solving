#include <stdio.h>
#include <stack>
using namespace std;

int main() {
	stack<int*> stk;

	int n = 0;
	scanf("%d", &n);

	int height = 0;
	for (int i = 1; i <= n; i++) {
		if (i > 1) {
			printf(" ");
		}

		scanf("%d", &height);
		
		// 1. [height, index] 동적 배열 생성
		int* arr = new int[2] {height, i};

		// 2-1. 스택이 비어있으면(앞에 더 높은 탑이 없으면) 배열 push 후 index 0 출력, continue
		if (stk.empty()) {
			stk.push(arr);
			printf("%d", 0);
		}
		else {
			// 2-2. top의 높이값이 현재 높이값보다 크거나 같을 때까지 pop, empty여도 종료
			int* top = stk.top();
			while (top[0] < height && !stk.empty()) {
				delete[] stk.top();
				stk.pop();
				if (!stk.empty()) {
					top = stk.top();
				}
			}

			// 3-1. 스택이 비어있으면 push 후 index 0 출력, continue
			if (stk.empty()) {
				stk.push(arr);
				printf("%d", 0);
			}
			// 3-2. 스택이 비어있지않으면(앞에 더 높은 탑이 있으면) front 출력 후 push
			else {
				stk.push(arr);
				printf("%d", top[1]);
			}
		}
	}
	return 0;
}