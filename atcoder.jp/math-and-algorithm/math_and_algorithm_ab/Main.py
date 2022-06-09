N=int(input())
ans=[1,1]
for i in range(N-1):
  ans.append(ans[-1]+ans[-2])
print(ans[-1])