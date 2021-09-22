S=[input() for _ in range(3)]
T=input()
ans=''
for i in T:
  ans+=S[int(i)-1]
print(ans)