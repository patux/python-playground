#!/usr/bin/python

def partition(arr, high):
    pivot = high
    n = len(arr)
    i = -1 
    for j in range(n):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[n - 1] = arr[n -1], arr[i + 1]

if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40]
    high = len(arr) 
    
    partition(arr,high)
    for e in arr:
        print (e, end = ' ')


