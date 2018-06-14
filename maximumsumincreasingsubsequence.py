# https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

#code
def solution(a, n):
    global maximum
    if n == 1:
        return 1
    localMax=1
    for x in range(1, n):
        sol = solution(a, x)
        if a[x-1] < a[n-1] and sol+1 > localMax:
            localMax = sol + 1
    maximum = max(maximum, localMax)
    return localMax

if __name__=="__main__":
    tc = int(input())
    global maximum
    for x in range(tc):
        maximum = 1
        n = int(input())
        a = list(map(int, input().split()))
        solution(a, n)
        print(maximum)
