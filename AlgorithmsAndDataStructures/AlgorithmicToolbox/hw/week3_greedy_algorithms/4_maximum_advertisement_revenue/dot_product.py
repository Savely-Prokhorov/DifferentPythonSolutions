#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    iamaxpos, ibmaxpos, iaminneg, ibminneg = 0, 0, -1, -1
    for i in range(len(a)):
        if a[i] > 0 and a[i] > a[iamax]:
            iamax = i
        if b[i] > 0 and b[i] > b[ibmax]:
            ibmax = i
        if a[i] < 0 and iaminneg == -1 or a[i] < a[iaminneg]:
            iaminneg = i
        if b[i] < 0 and ibminneg == -1 or a[i] < b[ibminneg]:
            ibminneg = i
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
