h, w = map(int, input().split())

A = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
      if h == 1 and w == 1:
        A[i][j] = 0
          
      elif h == 1:
        if j in [0, w - 1]:
          A[i][j] = 1
        else:
          A[i][j] = 2
            
      elif w == 1:
        if i in [0, h - 1]:
          A[i][j] = 1
        else:
          A[i][j] = 2
            
      elif i in [0, h - 1] and j in [0, w - 1]:
        A[i][j] = 2
      elif (i in [0, h - 1]) ^ (j in [0, w - 1]):
        A[i][j] = 3
      else:
        A[i][j] = 4 
    
for row in A:
    print(*row)
