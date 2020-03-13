s = input()
n = int(input())
for i in range(n):
  f,l = map(int, input().split())
  tmp = "".join(list(reversed(s[f-1:l])))
  s = s[:f-1] + tmp + s[l:]
print(s)