# Uses python3

def edit_distance(s, t):
    #write your code here
    a = [[float("inf")] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s)+1):
        a[i][0] = i
    for j in range(len(t)+1):
        a[0][j] = j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            diff = 0 if s[i-1] == t[j-1] else 1
            a[i][j] = min(a[i-1][j] + 1, a[i][j-1] + 1, a[i-1][j-1] + diff)

    return a[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
