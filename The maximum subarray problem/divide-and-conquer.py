import math
import tracemalloc
import numpy as np
import time

tracemalloc.start()
start_time = time.time()

def FIND_MAXIMUM_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = -math.inf
    sum = 0

    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -math.inf
    sum = 0

    for j in range (mid+1, high+1):
        sum = sum +A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

def FIND_MAXIMUM_SUBARRAY(A, low, high):
    if high == low:
        return (low, high, A[low])
    mid = (low+high)//2
    left_low, left_high, left_sum = FIND_MAXIMUM_SUBARRAY(A, low, mid)
    right_low, right_high, right_sum = FIND_MAXIMUM_SUBARRAY(A, mid+1, high)
    cross_low, cross_high, cross_sum = FIND_MAXIMUM_CROSSING_SUBARRAY(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return(left_low, left_high, left_sum)
    elif right_sum >= left_sum>=cross_sum:
        return(right_low, right_high, right_sum)
    return(cross_low, cross_high, cross_sum)


A = np.random.randint(-100, 100, 1000000)
print(A)
low = 0
high = len(A)-1

print("low ", low, "high ", high)

start, end, maximum = FIND_MAXIMUM_SUBARRAY(A, low, high)
print("Max subarray: ", maximum)
print("Start index: ", start)
print("End index: ", end)

runtime = time.time()-start_time
size, peak = tracemalloc.get_traced_memory()

print("runtime= ", runtime, "peak=" , peak)