def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index - 1] > array[cur_index] and cur_index - 1 >= 0:
            array[cur_index], array[cur_index - 1] = array[cur_index - 1], array[cur_index]
            cur_index -= 1
    return array


if __name__ == '__main__':
    array = [3, 6, 45, 67, 4, 3, 45, 43, 76, 98, 46]
    print(insertion_sort(array))
