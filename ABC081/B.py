N = int(input())

A = list(map(int, input().split()))
ans = 0

while True:
  
  flag = True

  #全体を2で割る
  for j in range(N):
    A[j] = A[j] / 2
  
  #全部整数ならans += 1
  for k in range(N):
    if A[k].is_integer():
      pass
    else:
      flag = False

  if flag == False:
    break
  
  ans += 1

print(ans)