N = int(input())
ans = ""
S = input().split()

for i in range(N):
    if S[i][0] == "a" or S[i][0] == "b" or S[i][0] == "c":
        ans += "2"
    elif S[i][0] == "d" or S[i][0] == "e" or S[i][0] == "f":
        ans += "3"
    elif S[i][0] == "g" or S[i][0] == "h" or S[i][0 ] == "i":
        ans += "4"
    elif S[i][0] == "j" or S[i][0] == "k" or S[i][0] == "l":
        ans += "5"
    elif S[i][0] == "m" or S[i][0] == "n" or S[i][0] == "o":
        ans += "6"
    elif S[i][0] == "p" or S[i][0] == "q" or S[i][0] == "r" or S[i][0] == "s":
        ans += "7"
    elif S[i][0] == "t" or S[i][0] == "u" or S[i][0] == "v":
        ans += "8"
    elif S[i][0] == "w" or S[i][0] == "x" or S[i][0] == "y" or S[i][0] == "z":
        ans += "9"

print(ans)