#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct lecture {
	int id;
	int start;
	int end;
	int classroom;
};

bool compareStart(lecture& a, lecture& b) {
	if (a.start != b.start) {
		return a.start < b.start;
	}
	else {
		return a.end < b.end;
	}
}
bool compareId(lecture& a, lecture& b) {
	return a.id < b.id;
}

struct compareEnd {
	bool operator() (lecture& a, lecture& b) {
		return a.end > b.end;
	}
};

int main() {
	int n = 0; // 강의의 개수
	scanf("%d", &n);

	vector<lecture> lects;
	lecture lect = { 0, 0, 0, 0 };

	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &lect.id, &lect.start, &lect.end);
		lects.push_back(lect);
	}

	sort(lects.begin(), lects.end(), compareStart);

	priority_queue<lecture, vector<lecture>, compareEnd> pq;
	vector<lecture> results;

	int classroom = 0;
	
	for (lecture& lect : lects) {
		if (!pq.empty() && (pq.top().end <= lect.start)) {
			results.push_back(pq.top());
			lect.classroom = pq.top().classroom;
			pq.pop();
		}
		else {
			lect.classroom = ++classroom;
		}

		pq.push(lect);
	}

	printf("%d\n", pq.size());

	while (!pq.empty()) {
		results.push_back(pq.top());
		pq.pop();
	}

	sort(results.begin(), results.end(), compareId);

	for (lecture lect : results) {
		printf("%d\n", lect.classroom);
	}

	return 0;
}