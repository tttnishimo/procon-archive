n=int(input())
a=[]
for i in range(n):
  a.append(int(input()))
if n <= 2:
  print(max(a))
elif n == 3:
  print(max(max(a),sum(a)-max(a)))
else:
  a.sort()
  print(min(max(a[3],sum(a[:3])),max(a[3]+a[0],a[1]+a[2]),max(a[3]+a[1],a[0]+a[2])))