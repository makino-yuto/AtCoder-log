import heapq

X = int(input())
Q = int(input())

left = [-X]
right = []

hairetu = [X]

for i in range(Q):
  
  A, B = map(int, input().split())
  
  for j in [A, B]:
    
    if j <= -left[0]:
      heapq.heappush(left, -j)
    else:
      heapq.heappush(right, j)
    if len(left) > len(right) + 1:
      heapq.heappush(right, -heapq.heappop(left)) 
    if len(left) < len(right):
      heapq.heappush(left, -heapq.heappop(right))
  
  print(-left[0])