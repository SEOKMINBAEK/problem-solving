#include <iostream>
#include <stack>
#include <string>
using namespace std;

struct Data {
	int k;
	int q_len;
};

int main() {
	string s = "";
	cin >> s;

	stack<Data> stk;
	int q_len = 0;
	int k = 0;

	for (char ch : s) {
		if (ch == '(') {
			stk.push({ k, --q_len });
			q_len = 0;
		}
		else if (ch == ')') {
			Data d = stk.top();
			stk.pop();
			q_len = (d.k * q_len) + d.q_len;
		}
		else {
			k = ch - '0';
			q_len++;
		}
	}

	cout << q_len;

	return 0;
}