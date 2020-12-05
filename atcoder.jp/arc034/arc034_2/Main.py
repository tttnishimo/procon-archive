n=input()
ans=[]
for i in range(max(int(n)-len(n)*9,0),int(n)):
  s=list(str(i))
  t=[int(j) for j in s]
  if i+sum(t)==int(n):
    ans.append(i)
print(len(ans))
for i in ans:
  print(i)