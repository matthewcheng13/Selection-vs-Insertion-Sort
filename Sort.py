import timeit
import random

def insertion_sort(arr):
    for k in range(1,len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur

def selection_sort(arr):
    for k in range(len(arr)-1):
        action = False
        j = k
        min_value = arr[k]
        while j < len(arr):
            if arr[j] < min_value:
                i = j
                min_value = arr[i]
                action = True
            j = j + 1
        if action == True:
            temp = arr[k]
            arr[k] = min_value
            arr[i] = temp

if __name__ == "__main__":

    # generate arrays
    increasing1000 = [i for i in range(1000)]
    increasing2500 = [i for i in range(2500)]
    increasing5000 = [i for i in range(5000)]
    increasing7500 = [i for i in range(7500)]
    increasing10000 = [i for i in range(10000)]

    decreasing1000 = [i for i in range(999,-1,-1)]
    decreasing2500 = [i for i in range(2499,-1,-1)]
    decreasing5000 = [i for i in range(4999,-1,-1)]
    decreasing7500 = [i for i in range(7499,-1,-1)]
    decreasing10000 = [i for i in range(9999,-1,-1)]

    random1000s = [random.randint(0,100000) for i in range(1000)]
    random2500s = [random.randint(0,100000) for i in range(2500)]
    random5000s = [random.randint(0,100000) for i in range(5000)]
    random7500s = [random.randint(0,100000) for i in range(7500)]
    random10000s = [random.randint(0,100000) for i in range(10000)]

    # ensure that selection and insertion are seeing arrays with the same values
    random1000i = random1000s.copy()
    random2500i = random2500s.copy()
    random5000i = random5000s.copy()
    random7500i = random7500s.copy()
    random10000i = random10000s.copy()

    # time all of the increasing arrays for selection sort and then print the time
    runtime_selection_increasing_1000 = timeit.timeit('selection_sort(increasing1000)',
                    setup='from __main__ import selection_sort, increasing1000',
                    number=1)
    runtime_selection_increasing_2500 = timeit.timeit('selection_sort(increasing2500)',
                        setup='from __main__ import selection_sort, increasing2500',
                        number=1)
    runtime_selection_increasing_5000 = timeit.timeit('selection_sort(increasing5000)',
                        setup='from __main__ import selection_sort, increasing5000',
                        number=1)
    runtime_selection_increasing_7500 = timeit.timeit('selection_sort(increasing7500)',
                        setup='from __main__ import selection_sort, increasing7500',
                        number=1)
    runtime_selection_increasing_10000 = timeit.timeit('selection_sort(increasing10000)',
                        setup='from __main__ import selection_sort, increasing10000',
                        number=1)
    print(f"Increasing Selection Timings: {runtime_selection_increasing_1000},{runtime_selection_increasing_2500},{runtime_selection_increasing_5000},\
{runtime_selection_increasing_7500},{runtime_selection_increasing_10000}")

    # do the same for the decreasing arrays
    runtime_selection_decreasing_1000 = timeit.timeit('selection_sort(decreasing1000)',
                    setup='from __main__ import selection_sort, decreasing1000',
                    number=1)
    runtime_selection_decreasing_2500 = timeit.timeit('selection_sort(decreasing2500)',
                        setup='from __main__ import selection_sort, decreasing2500',
                        number=1)
    runtime_selection_decreasing_5000 = timeit.timeit('selection_sort(decreasing5000)',
                        setup='from __main__ import selection_sort, decreasing5000',
                        number=1)
    runtime_selection_decreasing_7500 = timeit.timeit('selection_sort(decreasing7500)',
                        setup='from __main__ import selection_sort, decreasing7500',
                        number=1)
    runtime_selection_decreasing_10000 = timeit.timeit('selection_sort(decreasing10000)',
                        setup='from __main__ import selection_sort, decreasing10000',
                        number=1)
    print(f"Decreasing Selection Timings: {runtime_selection_decreasing_1000},{runtime_selection_decreasing_2500},{runtime_selection_decreasing_5000},\
{runtime_selection_decreasing_7500},{runtime_selection_decreasing_10000}")

    # and then again for the random arrays
    runtime_selection_random_1000 = timeit.timeit('selection_sort(random1000s)',
                    setup='from __main__ import selection_sort, random1000s',
                    number=1)
    runtime_selection_random_2500 = timeit.timeit('selection_sort(random2500s)',
                        setup='from __main__ import selection_sort, random2500s',
                        number=1)
    runtime_selection_random_5000 = timeit.timeit('selection_sort(random5000s)',
                        setup='from __main__ import selection_sort, random5000s',
                        number=1)
    runtime_selection_random_7500 = timeit.timeit('selection_sort(random7500s)',
                        setup='from __main__ import selection_sort, random7500s',
                        number=1)
    runtime_selection_random_10000 = timeit.timeit('selection_sort(random10000s)',
                        setup='from __main__ import selection_sort, random10000s',
                        number=1)
    print(f"Random Selection Timings: {runtime_selection_random_1000},{runtime_selection_random_2500},{runtime_selection_random_5000},\
{runtime_selection_random_7500},{runtime_selection_random_10000}")

    # now repeat for insertion sort but with fresh arrays (random one has already been generated above)

    increasing1000 = [i for i in range(1000)]
    increasing2500 = [i for i in range(2500)]
    increasing5000 = [i for i in range(5000)]
    increasing7500 = [i for i in range(7500)]
    increasing10000 = [i for i in range(10000)]

    decreasing1000 = [i for i in range(999,-1,-1)]
    decreasing2500 = [i for i in range(2499,-1,-1)]
    decreasing5000 = [i for i in range(4999,-1,-1)]
    decreasing7500 = [i for i in range(7499,-1,-1)]
    decreasing10000 = [i for i in range(9999,-1,-1)]

    runtime_insertion_increasing_1000 = timeit.timeit('insertion_sort(increasing1000)',
                    setup='from __main__ import insertion_sort, increasing1000',
                    number=1)
    runtime_insertion_increasing_2500 = timeit.timeit('insertion_sort(increasing2500)',
                        setup='from __main__ import insertion_sort, increasing2500',
                        number=1)
    runtime_insertion_increasing_5000 = timeit.timeit('insertion_sort(increasing5000)',
                        setup='from __main__ import insertion_sort, increasing5000',
                        number=1)
    runtime_insertion_increasing_7500 = timeit.timeit('insertion_sort(increasing7500)',
                        setup='from __main__ import insertion_sort, increasing7500',
                        number=1)
    runtime_insertion_increasing_10000 = timeit.timeit('insertion_sort(increasing10000)',
                        setup='from __main__ import insertion_sort, increasing10000',
                        number=1)
    print(f"Increasing Insertion Timings: {runtime_insertion_increasing_1000},{runtime_insertion_increasing_2500},{runtime_insertion_increasing_5000},\
{runtime_insertion_increasing_7500},{runtime_insertion_increasing_10000}")

    runtime_insertion_decreasing_1000 = timeit.timeit('insertion_sort(decreasing1000)',
                    setup='from __main__ import insertion_sort, decreasing1000',
                    number=1)
    runtime_insertion_decreasing_2500 = timeit.timeit('insertion_sort(decreasing2500)',
                        setup='from __main__ import insertion_sort, decreasing2500',
                        number=1)
    runtime_insertion_decreasing_5000 = timeit.timeit('insertion_sort(decreasing5000)',
                        setup='from __main__ import insertion_sort, decreasing5000',
                        number=1)
    runtime_insertion_decreasing_7500 = timeit.timeit('insertion_sort(decreasing7500)',
                        setup='from __main__ import insertion_sort, decreasing7500',
                        number=1)
    runtime_insertion_decreasing_10000 = timeit.timeit('insertion_sort(decreasing10000)',
                        setup='from __main__ import insertion_sort, decreasing10000',
                        number=1)
    print(f"Decreasing Insertion Timings: {runtime_insertion_decreasing_1000},{runtime_insertion_decreasing_2500},{runtime_insertion_decreasing_5000},\
{runtime_insertion_decreasing_7500},{runtime_insertion_decreasing_10000}")

    runtime_insertion_random_1000 = timeit.timeit('insertion_sort(random1000i)',
                    setup='from __main__ import insertion_sort, random1000i',
                    number=1)
    runtime_insertion_random_2500 = timeit.timeit('insertion_sort(random2500i)',
                        setup='from __main__ import insertion_sort, random2500i',
                        number=1)
    runtime_insertion_random_5000 = timeit.timeit('insertion_sort(random5000i)',
                        setup='from __main__ import insertion_sort, random5000i',
                        number=1)
    runtime_insertion_random_7500 = timeit.timeit('insertion_sort(random7500i)',
                        setup='from __main__ import insertion_sort, random7500i',
                        number=1)
    runtime_insertion_random_10000 = timeit.timeit('insertion_sort(random10000i)',
                        setup='from __main__ import insertion_sort, random10000i',
                        number=1)
    print(f"Random Insertion Timings: {runtime_insertion_random_1000},{runtime_insertion_random_2500},{runtime_insertion_random_5000},\
{runtime_insertion_random_7500},{runtime_insertion_random_10000}")