#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct compare {
	bool operator() (pair<int, int>& a, pair<int, int>& b) {
		if (a.first != b.first) {
			return a.first < b.first;
		}
		else {
			return a.second > b.second;
		}
	}
};

int main() {
	int n = 0;
	scanf("%d", &n); // 대학의 개수

	priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
	pair<int, int> p;

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &p.first, &p.second);
		pq.push(p);
	}

	int total = 0;
	bool calendar[10000] = {};

	while (!pq.empty()) {
		int money = pq.top().first;
		int day = pq.top().second;

		while (day > 0) {
			if (!calendar[day]) {
				calendar[day] = true;
				total += money;
				break;
			}
			day--;
		}

		pq.pop();
	}

	printf("%d", total);

	return 0;
}