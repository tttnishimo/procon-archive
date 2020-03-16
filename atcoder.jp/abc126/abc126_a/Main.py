a,b = map(int, input().split())
s = input()
if b == 1:
  s = s[b - 1].lower() + s[b:]
else:
  s = s[:b - 1] + s[b - 1].lower() + s[b:]
print(s)