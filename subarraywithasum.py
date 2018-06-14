# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

#code

def calc():
    n,s = input().split()
    s = int(s)
    a = list(map(int, input().split()))
    print(a, s)
    for start in range(0, int(n)):
        sum = 0
        if start < int(n):
            for end in range(start, int(n)):
                sum = sum + a[end]
                if sum==s:
                    return start+1, end+1
        else:
            break


if __name__=="__main__":
    ct = int(input())
    for x in range(ct):
        x, y = calc()
        print(x,y)
