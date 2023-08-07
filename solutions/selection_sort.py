import random
import time

# O(1) space complexity, O(n^2) time complexity
def selection_sort_in_place(list):

    for i in range(len(list)):

        min_element = list[i]

        for j in range(i, len(list)):

            if list[j] < min_element:
                min_element = list[j]

        temp_element_0 = list[i]

        min_element_ind = list.index(min_element)

        list[i] = min_element

        list[min_element_ind] = temp_element_0

    return list

# O(n) space complexity, O(n) time complexity
def selection_sort_out_of_place(list):

    sorted_list = []

    while len(list) > 0:

        min_element = min(list)

        sorted_list.append(min_element)
        list.remove(min_element)

    return sorted_list

if __name__ == '__main__':

    print("Expecting: [-1, 2, 3, 5]")
    print(selection_sort_in_place([3, -1, 5, 2]))

    print("")

    print("Expecting: []")
    print(selection_sort_in_place([]))

    print("")

    print("Expecting: [-1]")
    print(selection_sort_in_place([-1]))

    print("")

    print("Expecting: [-10, 2, 2, 3, 7]")
    print(selection_sort_in_place([3, 2, 2, 7, -10]))

    print("")

    print("Expecting: [100, 200]")
    print(selection_sort_in_place([100, 200]))

    print("")

    # BENCHMARK HERE

    long_input = []

    for i in range(100):
        long_input.append(random.uniform(0, 1))

    start_time = time.time()

    for i in range(1000):
        selection_sort_in_place([2, 1])
        selection_sort_in_place(long_input)

    avg_time = ( time.time() - start_time ) / 2000

    print(avg_time)