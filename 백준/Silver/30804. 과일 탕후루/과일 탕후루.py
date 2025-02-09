N = int(input()) # 막대에 꽂힌 과일의 개수
stick = list(map(int, input().split())) # 막대에 꽂힌 과일 배열

fluits = {} # 연속된 과일의 부분 구간 { 과일번호: 개수 }
max_len = 0 # 조건을 만족하는 부분 구간의 길이
l = 0 # 탐색 구간 시작 포인터

for r in range(N): # 부분 구간 종료 지점을 0부터 N까지 반복하여 탐색
  cur = stick[r] # 부분 구간에 새로 추가할 오른쪽 과일일
  
  if cur in fluits: # 이미 등장한 과일번호인 경우 
    fluits[cur] += 1 # 과일번호 키에 갯수를 올린다
  else: # 처음 등장한 과일 번호인 경우
    fluits[cur] = 1 # 과일번호 키에 갯수를 1로 초기화
  
  while len(fluits) > 2: # 부분 구간 내 과일의 종류가 2가지 이하가 될 때까지 반복
    target = stick[l] # 왼쪽에서 삭제할 과일
    fluits[target] -= 1 # 부분 구간 내 해당 과일번호의 개수를 감소시킨다
    
    if fluits[target] == 0: # 해당번호의 과일이 이제 구간내 없는 경우
      del fluits[target] # 해당 과일 번호 삭제
    
    l += 1 # 삭제할 왼쪽 포인터 이동
  
  max_len = max(max_len, r - l + 1) # 2가지 종류 이하의 부분 구간의 길이와 비교 갱신

print(max_len)