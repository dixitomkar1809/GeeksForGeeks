# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

#code
def quickSort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quickSort(a, l, q-1)
        quickSort(a, q+1, r)

def partition(a, l, r):
    pivot = a[r]
    i = l - 1
    for x in range(l, r):
        if a[x]<=pivot:
            i+=1
            a[i],a[x] = a[x], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

# def partition(arr,low,high):
#     i = ( low-1 )         # index of smaller element
#     pivot = arr[high]     # pivot

#     for j in range(low , high):
#         if   arr[j] <= pivot:
#             i = i+1
#             arr[i],arr[j] = arr[j],arr[i]

#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return ( i+1 )

# def quickSort(arr,low,high):
#     if low < high:
#         pi = partition(arr,low,high)
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)

if __name__=="__main__":
    tc = int(input())
    for x in range(tc):
        n = int(input())
        a = list(map(int, input().split()))
        quickSort(a, 0, len(a)-1)
        print(*a)


    
