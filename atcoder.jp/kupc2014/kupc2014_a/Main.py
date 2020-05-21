a=list(map(int,input().split()))
ans=[]
ans.append(abs(a[0]-a[3]) + abs(a[1]-a[4]) + abs(a[2]-a[5]))
ans.append(abs(a[0]-a[3]) + abs(a[1]-a[5]) + abs(a[2]-a[4]))
ans.append(abs(a[0]-a[4]) + abs(a[1]-a[3]) + abs(a[2]-a[5]))
ans.append(abs(a[0]-a[4]) + abs(a[1]-a[5]) + abs(a[2]-a[3]))
ans.append(abs(a[0]-a[5]) + abs(a[1]-a[3]) + abs(a[2]-a[4]))
ans.append(abs(a[0]-a[5]) + abs(a[1]-a[4]) + abs(a[2]-a[3]))
print(min(ans))