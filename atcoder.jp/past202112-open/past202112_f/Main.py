A,B=map(int,input().split())
S=input()+input()+input()
a=['###########','#.........#','#.........#','#.........#','#.........#','#.........#','#.........#','#.........#','#.........#','#.........#','###########']
a[A]=a[A][:B]+'x'+a[A][B+1:]
d=[[A,B]]
dx=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
while d:
  now=d.pop()
  for i in range(9):
    if S[i]=='#':
      c=[now[0]+dx[i][0],now[1]+dx[i][1]]
      if a[c[0]][c[1]]=='.':
        a[c[0]]=a[c[0]][:c[1]]+'x'+a[c[0]][c[1]+1:]
        d.append(c)
print(sum(i.count('x') for i in a))