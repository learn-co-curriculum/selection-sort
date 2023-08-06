import random
import time

def selection_sort(list):

    # THE LONGER WAY OF DOING THE SAME THING AS LINES 26 - 35

    '''
    sorted = []

    while len(list) > 0:

        min_element = list[0]

        for i in range(len(list)):

            if list[i] < min_element:
                min_element = list[i]

        sorted.append(min_element)
        list.remove(min_element)

    return sorted
    '''

    sorted = []

    while len(list) > 0:

        min_element = min(list)

        sorted.append(min_element)
        list.remove(min_element)

    return sorted

if __name__ == '__main__':

    print("Expecting: [-1, 2, 3, 5]")
    print(selection_sort([3, -1, 5, 2]))

    print("")

    print("Expecting: []")
    print(selection_sort([]))

    print("")

    print("Expecting: [-1]")
    print(selection_sort([-1]))

    print("")

    print("Expecting: [-10, 2, 2, 3, 7]")
    print(selection_sort([3, 2, 2, 7, -10]))

    print("")

    print("Expecting: [100, 200]")
    print(selection_sort([100, 200]))

    print("")

    # BENCHMARK HERE

    long_input = []

    for i in range(100):
        long_input.append(random.uniform(0, 1))

    start_time = time.time()

    for i in range(1000):
        selection_sort([2, 1])
        selection_sort(long_input)

    avg_time = ( time.time() - start_time ) / 2000

    print(avg_time)