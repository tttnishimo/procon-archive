import itertools
n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
arr = list(itertools.permutations(range(1,n + 1),n))
print(abs(arr.index(a) - arr.index(b)))