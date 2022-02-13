def dfs(s,l):
  if len(s)==N:
    if l==0:
      print(s)
    return
  dfs(s+'(',l+1)
  if l>0:
    dfs(s+')',l-1)
N=int(input())
dfs('',0)