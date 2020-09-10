# python3


def LeftChild(i):
    return 2*i+1

def RightChild(i):
    return 2*i+2

def SiftDown(data, i, swaps):
    max_ind = i
    left = LeftChild(i)
    if left < len(data) and data[left] < data[max_ind]:
        max_ind = left
    right = RightChild(i)
    if right < len(data) and data[right] < data[max_ind]:
        max_ind = right
    if i != max_ind:
        swaps.append((i, max_ind))
        data[i], data[max_ind] = data[max_ind], data[i]
        SiftDown(data, max_ind, swaps)
    return swaps


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data), -1, -1):
        SiftDown(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    print(data)


if __name__ == "__main__":
    main()
