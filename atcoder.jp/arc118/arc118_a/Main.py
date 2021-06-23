t,N=map(int,input().split())
ans=[i for i in range(1,101+t)]
for i in range(1,101):
  ans.remove(i*(100+t)//100)
print(ans[N%len(ans)-1]+(100+t)*int((N-0.5)//len(ans)))