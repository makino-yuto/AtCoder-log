s = input()
ans = 0

length = len(s)

for i in range(length):
    if s[i] == "C":
        ans += 1 + min(i, length - 1 - i)

print(ans)