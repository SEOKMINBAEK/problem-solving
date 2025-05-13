#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct subject {
	int score;
	int per_hour;
};

struct compare {
	int calc(subject& sub) {
		return sub.per_hour >= 100 - sub.score ? 100 - sub.score : sub.per_hour;
	}

	bool operator() (subject& a, subject& b) {
		return calc(a) < calc(b);
	}
};

int main() {
	int n = 0; // 주어진 일
	int m = 0; // 시험 과목 수
	scanf("%d %d", &n, &m);

	vector<subject> subs(m);

	for (int i = 0; i < (m); i++) {
		scanf("%d", &subs[i].score);
	}

	for (int i = 0; i < (m); i++) {
		scanf("%d", &subs[i].per_hour);
	}

	priority_queue<subject, vector<subject>, compare> pq;

	for (subject& sub : subs) {
		pq.push(sub);
	}

	int hour = 0;

	while (hour < (24 * n)) {
		subject sub = pq.top();
		sub.score += sub.per_hour;
		sub.score = sub.score > 100 ? 100 : sub.score;
		hour++;
		
		pq.pop();
		pq.push(sub);
	}

	int total = 0;
	while (!pq.empty()) {
		total += pq.top().score;
		pq.pop();
	}

	printf("%d", total);

	return 0;
}