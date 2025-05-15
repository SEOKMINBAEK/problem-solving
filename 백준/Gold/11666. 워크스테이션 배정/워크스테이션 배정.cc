#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int>& a, pair<int, int>& b) {
	if (a.first != b.first) {
		return a.first < b.first;
	}
	else {
		return a.second < b.second;
	}
}

int main() {
	int n = 0; // 연구원의 수
	int m = 0; // 워크스테이션의 잠금 시간

	scanf("%d %d", &n, &m);

	pair<int, int> researcher; // first: 도착시간, second: 종료시간
	vector<pair<int, int>> researchers;

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &researcher.first, &researcher.second);
		researcher.second += researcher.first;
		researchers.push_back(researcher);
	}

	sort(researchers.begin(), researchers.end(), compare);

	priority_queue<int, vector<int>, greater<int>> pq; // 종료시간 우선순위 큐

	int cnt = 0;

	for (pair<int, int>& researcher : researchers) {
		while (!pq.empty() && pq.top() + m < researcher.first) {
			pq.pop();
		}

		if (!pq.empty() && pq.top() <= researcher.first && pq.top() + m >= researcher.first) {
			pq.pop();
			cnt++;
		}

		pq.push(researcher.second);
	}

	printf("%d", cnt);

	return 0; 
}