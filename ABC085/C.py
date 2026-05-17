N, Y = map(int, input().split())

for i in range(N + 1):
  for j in range(N + 1):
      k = N - i - j

      if Y == 10000 * i + 5000 * j + 1000 * k and k >= 0:
        print(i, j, k)
        exit()

print(-1, -1, -1)