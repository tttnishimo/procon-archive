n,m,q = map(int, input().split())
res = 0
a = []*n

for i in range(q):
  a.append(list(map(int, input().split())))
for i_1 in range(1,m+1):
  for i_2 in range(i_1,m+1):
    for i_3 in range(i_2,m+1):
      for i_4 in range(i_3,m+1):
        for i_5 in range(i_4,m+1):
          for i_6 in range(i_5,m+1):
            for i_7 in range(i_6,m+1):
              for i_8 in range(i_7,m+1):
                for i_9 in range(i_8,m+1):
                  tmp = 0
                  arr = [1,i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9]
                  for i in range(q):
                    if arr[a[i][1]-1] - arr[a[i][0]-1] == a[i][2]:
                      tmp += a[i][3]
                  res = max(res,tmp)
print(res)