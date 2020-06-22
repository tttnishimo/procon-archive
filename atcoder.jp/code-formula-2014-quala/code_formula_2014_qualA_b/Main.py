a,b=map(int,input().split())
ans=['x']*10
p=list(map(int,input().split()))
for i in p:
  ans[i]='.'
if b!=0:
  q=list(map(int,input().split()))
  for i in q:
    ans[i]='o'
print(ans[7]+' '+ans[8]+' '+ans[9]+' '+ans[0])
print(' '+ans[4]+' '+ans[5]+' '+ans[6])
print('  '+ans[2]+' '+ans[3])
print('   '+ans[1])