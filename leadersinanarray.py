#code
#Question https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    max = -10
    answer = list()
    for x in reversed(a):
        if x > max:
            answer.append(x)
            max = x
    for x in reversed(answer):
        print(x, end=" ")
    print()


if __name__=="__main__":
    ct = int(input())
    for x in range(ct):
        solution()
