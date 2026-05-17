N, A, B = map(int, input().split())
ans = 0

for i in range(N + 1):
  sum_digit = sum(map(int, str(i)))
  if A <= sum_digit <= B:
    ans += i

print(ans)