#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> results;
	string code_name = "";

	for (int i = 1; i <= 5; i++) {
		cin >> code_name;

		if (code_name.find("FBI") != string::npos) {
			results.push_back(i);
		}
	}

	if (results.size() == 0) {
		cout << "HE GOT AWAY!";
		exit(0);
	}

	for (int i = 0; i < results.size(); i++) {
		cout << results[i];

		if (i < results.size() - 1) {
			cout << ' ';
		}
	}

	return 0;
}