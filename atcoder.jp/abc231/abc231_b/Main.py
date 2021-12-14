import collections
N=int(input())
S=[input() for _ in range(N)]
print(collections.Counter(S).most_common()[0][0])