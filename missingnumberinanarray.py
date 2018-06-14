# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

#code
tc = int(input())
for x in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    print(int((n*(n+1))/2 - sum(a)))
