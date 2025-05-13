#include <stdio.h>
#include <queue>
using namespace std;

int main() {
  int n = 0, m = 0;
  scanf("%d", &n);
  scanf("%d", &m);

  priority_queue<int> gifts;
  queue<int> wants;

  int temp = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d", &temp);
    gifts.push(temp);
  }

  for (int i = 0; i < m; i++) {
    scanf("%d", &temp);
    wants.push(temp);
  }

  while (!wants.empty() && wants.front() <= gifts.top()) {
    if (wants.front() < gifts.top()) {
      gifts.push(gifts.top() - wants.front());
    }

    wants.pop();
    gifts.pop();
  }

  if (wants.empty()) {
    printf("%d", 1);
  }
  else {
    printf("%d", 0);
  }

  return 0;
}