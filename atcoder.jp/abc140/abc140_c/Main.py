n = int(input())
b = list(map(int, input().split()))
a = [b[0]]
for i in range(len(b)-1):
  a.append(min(b[i], b[i+1]))
a.append(b[-1])
print(sum(a))