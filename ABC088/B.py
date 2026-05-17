N = int(input())
A = list(map(int, input().split()))

alice, bob = 0, 0

for i in range(len(A) // 2):
  ma = max(A)
  alice += ma
  A.remove(ma)
  ma = max(A)
  bob += ma
  A.remove(ma)

if len(A) != 0:
  ma = max(A)
  alice += ma

print(alice - bob)