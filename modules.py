import time

def selection_sort(arr):
    n = len(arr)
    comp = 0
    mov = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comp += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        mov += 1
    return comp, mov

def insertion_sort(arr):
    n = len(arr)
    comp = 0
    mov = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            comp += 1
            arr[j+1] = arr[j]
            j -= 1
            mov += 1
        arr[j+1] = key
        mov += 1
    return comp, mov

def bubble_sort(arr):
    n = len(arr)
    comp = 0
    mov = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                mov += 1
    return comp, mov

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comp = 0
    mov = 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                comp += 1
                arr[j] = arr[j-gap]
                j -= gap
                mov += 1
            arr[j] = temp
            mov += 1
        gap //= 2
    return comp, mov

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    comp = 0
    mov = 0
    for j in range(low, high):
        comp += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            mov += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    mov += 1
    return i+1, comp, mov

def quick_sort(arr, low, high):
    comp = 0
    mov = 0
    if low < high:
        pi, c, m = partition(arr, low, high)
        comp += c
        mov += m
        comp1, mov1 = quick_sort(arr, low, pi-1)
        comp2, mov2 = quick_sort(arr, pi+1, high)
        comp += comp1 + comp2
        mov += mov1 + mov2
    return comp, mov