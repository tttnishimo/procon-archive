x,y=map(int,input().split())
N=int(input())
li=[]
for _ in range(N):
  s,t=map(int,input().split())
  li.append([s-x,t-y])
ans=1000
for i in range(N):
  a=li[i][1]-li[i-1][1]
  b=-li[i][0]+li[i-1][0]
  c=-(li[i][1]-li[i-1][1])*li[i-1][0]+(li[i][0]-li[i-1][0])*li[i-1][1]
  p=-a*c/(a*a+b*b)
  q=-b*c/(a*a+b*b)
  d1=(li[i][0]**2+li[i][1]**2)**0.5
  d2=(li[i-1][0]**2+li[i-1][1]**2)**0.5
  d3=abs(c)/(a*a+b*b)**0.5
  if min(li[i][0],li[i-1][0])<=p<=max(li[i][0],li[i-1][0]) and min(li[i][1],li[i-1][1])<=q<=max(li[i][1],li[i-1][1]):
    ans=min(ans,d1,d2,d3)
  else:
    ans=min(ans,d1,d2)
print(ans)