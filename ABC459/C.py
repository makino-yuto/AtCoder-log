n = 600000

N, Q = map(int, input().split())

a = [0] * (n + 1) #第nマスの高さ
b = [0] * (n + 1) #ある高さnに何回積まれたか(わかりづらい)
b[0] = N

diff = 0

for i in range(Q):
    x, y = map(int, input().split())
    if x == 1:
        a[y] += 1
        b[a[y]] += 1
        if b[a[y]] == N:
            diff = a[y]

    if x == 2:
        print(b[y + diff])
