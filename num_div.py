def num_divisors(number, count, divisors):
    total = 0
    for i in range(number // 2, 1, -1):
        key = f'{i}'
        if key in divisors:
            total += divisors[key]
            return [(total + 2) == count, total]
        elif total > count:
            return [False, total]
        else:
            if number % i == 0:
                total += 1
            else:
                continue
    return [(total + 2) == count, total]

def find_min_num(num_div): # memoize me, please!
    divisors = {}
    count = 2
    while True:
        result = num_divisors(count, num_div, divisors)
        divisors[f'{count}'] = result[1]
        if result[0]:
            return count
        count += 2

def main():
    print(find_min_num(10))

if __name__ == "__main__":
    main()