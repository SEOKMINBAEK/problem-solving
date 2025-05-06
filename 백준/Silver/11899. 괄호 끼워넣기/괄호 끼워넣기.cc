#pragma warning(disable:4996)
#include <iostream>
#include <stdio.h>
#include <stack>
using namespace std;

int main() {
	stack<int> stk;
	string line = "";

	cin >> line;

	for (int i = 0; i < line.length(); i++) {
		bool val = line[i] == ')';

		if (stk.empty()) {
			stk.push(val);
			continue;
		}

		if (val && !stk.top()) {
			stk.pop();
		}
		else {
			stk.push(val);
		}
	}

	cout << stk.size() << endl;

	return 0;
}