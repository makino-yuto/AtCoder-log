X1, X2, X3 = map(int, input().split())

MOD = 998244353
MAX = X1 + X2 + X3

#階乗の定義
fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
  fact[i] = fact[i - 1] * i % MOD

#階乗の逆数の定義
fact_inv = [1] * (MAX + 1)
fact_inv[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
  fact_inv[i - 1] = fact_inv[i] * i % MOD

#コンビネーションの定義
def nCr(n, r):
  if r < 0 or r > n:
    return 0
  else:
    return fact[n] * fact_inv[r] % MOD * fact_inv[n - r] % MOD

ans = 0

for a in range(1, min(X1, X2 + 1) + 1):
  ans += (
    nCr(X1 - 1, a - 1)
    * nCr(X2 + 1, a)
    % MOD
    * nCr(X2 + X3 - a, X3)
    % MOD
  )
ans %= MOD

print(ans)