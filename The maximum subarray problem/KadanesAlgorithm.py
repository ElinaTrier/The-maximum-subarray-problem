import math
import tracemalloc
import numpy as np
import time

tracemalloc.start()
start_time = time.time()

def FIND_MAXIMUM_SUBARRAY(A, array_size):
    max_so_far = A[0]
    max_ending_here = 0
    start = 0
    end= 0
    s= 0

    for i in range(0, array_size):
        max_ending_here = max_ending_here + A[i]
        #print("yolo1")
        if (max_ending_here < 0):
            max_ending_here = 0
            s = i+1
            #print("yolo2")
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            start = s
            end = i
            #print("yolo3")
    print("Max subarray: ", max_so_far)
    print("Start index: ", start)
    print("End index: ", end)

A = np.random.randint(-100, 100, 1000000)
print(A)
print(FIND_MAXIMUM_SUBARRAY(A, len(A)))

runtime = time.time()-start_time
size, peak = tracemalloc.get_traced_memory()

print("runtime= ", runtime, "peak=" , peak)
