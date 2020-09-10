def partition3(a, l, r):
    #write your code here
    x = a[l]
    print(x)
    j = l
    count = 0
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            if a[i] == x:
                count+=1
                a[i], a[j] = a[j], a[i]
                a[count], a[j] = a[j], a[count]
            else:
                a[i], a[j] = a[j], a[i]
    for i in range(count+1):
        a[i], a[j-i] = a[j-i], a[i]
    print(j, j-count, sep=";")
    return j, j-count

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

a = [2, 3, -1, 5, 10, 7, 5, 8, 1, 2, 5, 5]
for el in a:
    print(el, end=" ")
a_copy = [5, 3, 2, -1, 10, 7, 5, 8, 1, 2, 5, 5]
partition3(a, 0, len(a)-1)
print(a)