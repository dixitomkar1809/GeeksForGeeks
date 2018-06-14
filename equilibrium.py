# https://practice.geeksforgeeks.org/problems/equilibrium-point/0

#code
def solution(a,n):
    leftSum  = [0] * n
    rightSum = [0] * n
    for x in range(1,n):
        leftSum[x] = sum(a[:x])
    for x in range(1, n):
        rightSum[x-1] = sum(a[x:])
    for x in range(n):
        if leftSum[x]==rightSum[x]:
            return x+1
    return -1


if __name__=="__main__":
    tc = int(input())
    for i in range(tc):
        n = int(input())
        a = list(map(int, input().split()))
        l = []
        print(solution(a,n))
