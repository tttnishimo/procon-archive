n = int(input())
dict = {}
for i in range(n):
  s = input()
  dict[s] = dict.get(s,0)+1
res = [k for k, v in dict.items() if v == max(dict.values())][0]
print(res)