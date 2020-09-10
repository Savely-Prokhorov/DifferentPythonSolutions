def summa(pair_sum, ind, V, T):
    res = []
    for i in range(ind, len(V)+1):
        s = pair_sum + V[i]
        res.append(s)
        summa(s, i+1, V, T)
    print(s)
    return s



def possible_variants(V, T):
    res_v, res_t = [], []
    # только одна модерн-я
    for i in range(len(V)):
        res_v.append(V[i])
        res_t.append(T[i])
    # две модерн-и
    for i in range(0, len(V)):
        pair_sum = V[i] + V[i + 1]
        summa(pair_sum, 2, V, T)

        #res_t.append(T[0] + T[i])

def calc_min_time(dist, speed, V, T):
    min_t = dist / speed
    for i in range(len(V)):
        moder_t = dist / (speed + V[i]) + T[i]
        if moder_t < min_t:
            min_t = moder_t
    return moder_t

print(calc_min_time(100, 5, [1, 2, 3, 4], [1, 2, 3, 4]))

possible_variants([1, 2, 3, 4], [1, 2, 3, 4])