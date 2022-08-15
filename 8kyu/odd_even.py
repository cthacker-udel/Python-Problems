def odd_even():
    num_cases = int(input())
    for eachcase in range(num_cases):
        arr_len = int(input())
        odd_indexes = -1
        """
        0 --> even
        1 --> odd
        """
        even_indexes = -1
        split_input = input.split(' ')
        for i in range(len(split_input)):
            if i % 2 == 0:
                if int(split_input[i]) % 2 == 0:
                    if even_indexes == -1:
                        even_indexes = 0
                    elif even_indexes == 1:
                        print('NO')
                        break
                else:
                    ## is odd
                    if even_indexes == -1:
                        even_indexes = 1
                    elif even_indexes == 0:
                        print('NO')
                        break
            else:
                if int(split_input[i]) % 2 == 0:
                    if odd_indexes == -1:
                        odd_indexes = 0
                    elif odd_indexes == 1:
                        print('NO')
                        break
                else:
                    if odd_indexes == -1:
                        odd_indexes = 1
                    elif odd_indexes == 1:
                        print("NO")
                        break
        print('YES')


        


if __name__ == '__main__':
    odd_even()