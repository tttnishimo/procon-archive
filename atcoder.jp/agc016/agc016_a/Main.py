def long_diff(s, a):
    s = str(a) + s + str(a)
    index_num = [n for n, v in enumerate(s) if v == str(a)]
    res = 0
    for i in range(len(index_num)-1):
        tmp = index_num[i+1] - index_num[i]
        res = max(res,tmp)
    return res-1

s = input()
r = 100
for i in [chr(j) for j in range(97,97+26)]:
    r = min(r, long_diff(s, i))
print(r)