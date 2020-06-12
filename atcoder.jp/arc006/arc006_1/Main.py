e=list(map(int,input().split()))
b=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(0,10):
  if i in e and i in a:
    ans+=1
if ans == 6:
  print(1)
elif ans == 5:
  if b in a:
    print(2)
  else:
    print(3)
elif ans >= 3:
  print(8-ans)
else:
  print(0)