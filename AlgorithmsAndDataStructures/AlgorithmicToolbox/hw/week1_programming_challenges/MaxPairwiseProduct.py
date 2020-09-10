# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_ind1, max_ind2 = 0, 0

    for i in range(0, n):
        if numbers[i]>numbers[max_ind1]:
            max_ind2 = max_ind1
            max_ind1 = i
        if max_ind1 == 0:
            if max_ind2 == 0:
                if i != max_ind1:
                    max_ind2 = i
            else:
                if numbers[i] > numbers[max_ind2]:
                    max_ind2 = i
        else:
            if numbers[i] > numbers[max_ind2] and i != max_ind1:
                max_ind2 = i

    max_product = numbers[max_ind1]*numbers[max_ind2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
