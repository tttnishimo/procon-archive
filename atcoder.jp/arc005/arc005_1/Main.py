n = int(input())
a = list(map(str, input().split()))
r = 0
a[-1] = a[-1].rstrip(".")

for i in range(n):
  if a[i] == "TAKAHASHIKUN" or a[i] == "Takahashikun" or a[i] == "takahashikun":
    r += 1
print(r)