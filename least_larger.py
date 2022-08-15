def least_larger(arr, ind):
    sorted_arr = sorted(set(arr))
    sorted_ind = sorted_arr.index(arr[ind])
    forward_ind = sorted_ind + \
        1 if sorted_ind != len(sorted_arr) - 1 else sorted_ind
    return arr.index(sorted_arr[forward_ind]) if forward_ind != sorted_ind and sorted_arr[forward_ind] > arr[ind] else -1


if __name__ == '__main__':
    print(least_larger([1, 3, 5, 2, 4], 0))
