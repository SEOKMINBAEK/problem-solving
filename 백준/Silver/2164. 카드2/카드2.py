class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class CardList:
  def __init__(self):
    self.head = Node(None)
    self.tail = Node(None)
    self.size = 0
    
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def insert(self, value):
    node = Node(value)
    prev = self.tail.prev
    
    prev.next = node
    node.prev = prev
    self.tail.prev = node
    
    self.size += 1
  
  def suffle(self):
    if self.size < 3:
      self.head.next = self.head.next.next
      self.size -= 1
      return
    
    go_rear = self.head.next.next # 뒤로 가야할 카드
    self.head.next = go_rear.next # front에서 + 2번째가 앞장으로
    self.head.next.prev = self.head.next
    
    prev = self.tail.prev # 원래 뒤에 있던 카드
    prev.next = go_rear
    go_rear.prev = prev
    go_rear.next = self.tail
    self.tail.prev = go_rear
    
    self.size -= 1
  
  def top(self):
    return self.head.next.value

n = int(input())
q = CardList()

for i in range(1, n + 1):
  q.insert(i)

while q.size > 1:
  q.suffle()

print(q.top())