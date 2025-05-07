#include <iostream>
#include <stack>
#include <string>
using namespace std;

void reverseWord(string& result, stack<char>& stk) {
	while (stk.empty() == false) {
		result += stk.top();
		stk.pop();
	}
}

int main() {
	stack<char> stk;
	string result = "";

	string s = "";
	getline(cin, s);
	bool is_continue = false;

	for (int i = 0; i < s.length(); i++) {
		char ch = s[i];

		if (is_continue) {
			result += ch;
			if (ch == '>') {
				is_continue = false;
			}

			continue;
		}

		if (ch == '<') {
			reverseWord(result, stk);
			result += ch;
			is_continue = true;
		}
		else if (ch == ' ') {
			reverseWord(result, stk);
			result += ch;
		}
		else {
			stk.push(ch);
			if (i == s.length() - 1) {
				reverseWord(result, stk);
			}
		}
	}

	cout << result << endl;

	return 0;
}