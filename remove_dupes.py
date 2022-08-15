def remove_dupes(integers, cont=[]):
    print('cont = ', cont)
    if len(integers) == 0:
        return cont
    return remove_dupes(integers[1:], cont[:] + [integers[0]] if integers[0] not in cont else cont)


if __name__ == '__main__':
    print(remove_dupes([1, 2, 3, 4, 51, 5, 6, 3, 2]))
