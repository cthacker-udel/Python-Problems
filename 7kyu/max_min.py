def solve(arr):
    sorted_arr = sorted(arr)
    min_ = 0
    max_ = len(sorted_arr) - 1
    result = []
    middle = len(sorted_arr) // 2
    while min_ < middle and max_ > middle:
        result.append(sorted_arr[max_])
        result.append(sorted_arr[min_])
        min_, max_ = min_ + 1, max_ - 1
    if len(arr) % 2 != 0:
        result.append(sorted_arr[max_])
    else:
        result.append(sorted_arr[max_])
        result.append(sorted_arr[min_])
    return result
