a,b,c=map(int,input().split())
t=0
for _ in range(61):
  if t%60<=c<=t%60+a:
    print(t//60*60+c)
    exit()
  else:
    t+=a+b
print(-1)