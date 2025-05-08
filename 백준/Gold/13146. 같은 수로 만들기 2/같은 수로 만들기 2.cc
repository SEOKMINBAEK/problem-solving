#include <stdio.h>
#include <stack>
#include <string>
using namespace std;

struct Data {
	int num;
	int cur;
};

int main() {
	int n = 0;
	scanf("%d", &n);
	
	stack<Data> stk;
	int num = 0;
	long long cnt = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", &num);

		if (stk.empty()) {
			stk.push({ num, num });
			continue;
		}

		if (stk.top().num > num) {
			cnt += stk.top().num - num;
			stk.push({ num, stk.top().cur });
		}
		else if (stk.top().num < num) {
			if (stk.top().cur > num) {
				stk.push({ num, stk.top().cur});
			}
			else {
				cnt += num - stk.top().cur;
				stk.push({ num, num });
			}
		}
	}


	printf("%lld", cnt);

	return 0;
}