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
	int n = 0;
	scanf("%d", &n);

	pair<int, int> p;
	vector<pair<int, int>> vec;

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &p.first, &p.second);
		vec.push_back(p);
	}

	sort(vec.begin(), vec.end(), compare);

	priority_queue<int, vector<int>, greater<int>> pq;

	for (pair<int, int>& p : vec) {
		if (!pq.empty() && pq.top() <= p.first) {
			pq.pop();
		}
		pq.push(p.second);
	}

	printf("%d", pq.size());

	return 0;
}