import timeit
import random

# from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
# from selection_sort import selection_sort
from merge_sort import merge_sort
# from quick_sort import quicksort
# from shell_sort import shell_sort
# from radix_sort import radix_sort

if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]
    data_large = [random.randint(0, 10_000) for _ in range(100_000)]

    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_small_timsort = timeit.timeit(lambda: data_small[:].sort(), number=10)

    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_medium_timsort = timeit.timeit(lambda: data_medium[:].sort(), number=10)

    time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large[:]), number=10)
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large[:]), number=10)
    time_large_timsort = timeit.timeit(lambda: data_large[:].sort(), number=10)

    print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time large data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f} | {time_large_insertion:<20.5f}")
    print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f} | {time_large_merge:<20.5f}")
    print(f"{'| Tim sort': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f} | {time_large_timsort:<20.5f}")
    
    
