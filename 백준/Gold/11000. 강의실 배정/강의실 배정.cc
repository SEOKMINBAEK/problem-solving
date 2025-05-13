#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
  if (a.first != b.first) {
    return a.first < b.first;
  }
  else {
    return a.second < b.second;
  }
}

int main() {
  int n = 0; // 강의의 개수
  scanf("%d", &n);

  vector<pair<int, int>> lectures;
  pair<int, int> p;

  for (int i = 0; i < n; i++) {
    scanf("%d %d", &p.first, &p.second);
    lectures.push_back(p);
  }

  sort(lectures.begin(), lectures.end(), compare);
  priority_queue<int, vector<int>, greater<int>> end_times;

  for (pair<int, int>& lect : lectures) {
    if (!end_times.empty() && end_times.top() <= lect.first) {
      end_times.pop();
    }
    end_times.push(lect.second);
  }

  printf("%d", end_times.size());

  return 0;
}