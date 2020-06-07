a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=map(int,input().split())
print(a-b)
print(c+d)
print(max(0,f-e+1))
print((g+h+i)//3+1)
if j<=4:
  print('aaai'[:j])
elif j==5:
  print('aaaji')
elif j==6:
  print('aabaji')
elif j==7:
  print('agabaji')
elif j==8:
  print('dagabaji')
ans=[]
for i in range(1,10**7+10**6):
  if i%59==k and i%61==l:
    ans.append(i)
perf=[6,28,496,8128,33550336,8589869056]
for j in perf:
  if abs(j-ans[m-1]) >= n:
    ans.append(j)
    break
print(min(ans[m-1],ans[-1]))
print(max(ans[m-1],ans[-1]))
print((o+p+q)*(r+s+t)*(u+v+w)*(x+y+z)%9973)