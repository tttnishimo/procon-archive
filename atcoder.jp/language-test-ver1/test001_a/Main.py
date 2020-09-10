n=int(input())
s=list(input())
a=[0,0,0,0]
for i in s:
  a[int(i)-1]+=1
print(max(a),min(a))