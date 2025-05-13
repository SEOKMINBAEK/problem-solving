#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct lecture {
  int id;
  int start;
  int end;
};

bool compare(lecture& a, lecture& b) {
  return a.start < b.start;
}

int main() {
  int n = 0; // 강의의 개수
  scanf("%d", &n);

  vector<lecture> lects;
  lecture lect;

  for (int i = 0; i < n; i++) {
    scanf("%d %d %d", &lect.id, &lect.start, &lect.end);
    lects.push_back(lect);
  }

  sort(lects.begin(), lects.end(), compare);

  priority_queue<int, vector<int>, greater<int>> min_pq;

  for (lecture& lect : lects) {
    if (!min_pq.empty() && min_pq.top() <= lect.start) {
      min_pq.pop();
    }
    min_pq.push(lect.end);
  }

  printf("%d", min_pq.size());

  return 0;
}