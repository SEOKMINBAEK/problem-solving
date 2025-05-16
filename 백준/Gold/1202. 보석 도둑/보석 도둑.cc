#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool compareWeight(pair<int, int>& a, pair<int, int>& b) {
	return a.first < b.first;
}

int main() {
	int n = 0, k = 0; // n: 보석의 개수, k: 가방의 개수
	scanf("%d %d", &n, &k);

	vector<pair<int ,int>> jewels;
	pair<int, int> jewel; // first: 무게, second: 가격

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &jewel.first, &jewel.second);
		jewels.push_back(jewel);
	}

	vector<int> bags;
	int c = 0;

	for (int i = 0; i < k; i++) {
		scanf("%d", &c);
		bags.push_back(c);
	}

	// 보석과 가방은 무게가 낮은것부터 높은 순으로 오름차순 정렬
	sort(jewels.begin(), jewels.end(), compareWeight);
	sort(bags.begin(), bags.end());

	priority_queue<int> pq;

	long long total = 0;
	int idx = 0;

	for (int i = 0; i < k; i++) {
		// i번째 가방에 들어갈 수 있는 모든 보석의 가격을 push
		while (idx < n && jewels[idx].first <= bags[i]) {
			pq.push(jewels[idx].second);
			idx++;
		}

		// 가장 가격이 높은 보석을 선택
		if (!pq.empty()) {
			total += pq.top();
			pq.pop();
		}
	}

	printf("%lld", total);

	return 0;
}