n=int(input())
a=[]
a.append(list(map(int,input().split())))
for i in range(1,n):
  tmp=list(map(int,input().split()))
  a.append([tmp[0]+max(a[i-1][1],a[i-1][2]),tmp[1]+max(a[i-1][0],a[i-1][2]),tmp[2]+max(a[i-1][0],a[i-1][1])])
print(max(a[-1]))