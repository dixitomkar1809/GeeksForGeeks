# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0

#code

def solution():
    n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n, s = int(n[0]), int(n[1])
    ans = list()
    for x in range(len(a)):
        newA = a[x:x+s]
        if len(newA)==s:
            #print(max(newA), end=" ")
            ans.append(max(newA))
    for x in ans:
        print(x, end=" ")
    print()


if __name__=="__main__":
    tc = int(input())
    for x in range(tc):
        solution()
