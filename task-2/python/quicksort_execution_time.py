from quicksort import quicksort

import random as r
import time as t
import matplotlib.pyplot as plt

if __name__ == "__main__":

    execution_time_list = []
    lengths_list = []
    max_list_length_digits = 6 
    for i in range(1, max_list_length_digits):
        l = [r.randint(1, 10**i) for _ in range(10**i)]
        t0 = t.time()
        _ = quicksort(l)
        t1 = t.time()
        print("Done with list of length: ", len(l))
        execution_time = t1 - t0
        execution_time_list.append(execution_time)
        lengths_list.append(len(l))

    plt.figure(figsize=(10, 6))
    plt.plot(lengths_list, execution_time_list)
    #plt.xticks(lengths_list)
    plt.xlabel("Length of list")
    plt.ylabel("Execution time")
    plt.title("Execution time of insertion sort")
    plt.show()