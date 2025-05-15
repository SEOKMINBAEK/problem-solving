#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct compare {
	bool operator() (pair<int, int>& a, pair<int, int>& b) {
		if (a.second != b.second) {
			return a.second < b.second;
		}
		else {
			return a.first > b.first;
		}
	}
};

int main() {
	int n = 0; // 과제 수
	scanf("%d", &n);

	priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
	pair<int, int> p; // first: 과제 마감일, second: 과제 점수

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &p.first, &p.second);
		pq.push(p);
	}

	bool calendar[1000] = {};
	int score = 0;

	while (!pq.empty()) {
		int d = pq.top().first;
		int w = pq.top().second;

		while (d > 0) {
			if (!calendar[d]) {
				calendar[d] = true;
				score += w;
				break;
			}

			d--;
		}

		pq.pop();
	}

	printf("%d", score);

	return 0;
}