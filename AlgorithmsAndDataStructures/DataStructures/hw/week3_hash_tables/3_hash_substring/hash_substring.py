# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
        ]

def PolyHash(s, p, x):
    hash = 0
    for i in range(len(s)-1, -1, -1):
        hash = (hash*x + ord(s[i])) % p
    return hash

def PrecomputeHashes(text, p_len, p, x):
    t_len = len(text)
    h = [0 for i in range(t_len-p_len+1)]
    s = text[t_len-p_len:t_len]
    h[t_len-p_len] = PolyHash(s, p, x)
    y = 1
    for i in range(1, p_len+1):
        y = y * x % p
    for i in range(t_len-p_len-1, -1, -1):
        h[i] = (x*h[i+1] + ord(text[i]) - y*ord(text[i+p_len])) % p
    return h

def RabinKarp(pattern, text):
    p = 100000007
    x = randint(1, p)
    result = []
    pHash = PolyHash(pattern, p, x)
    h = PrecomputeHashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if pHash != h[i]:
            continue
        else:
            if text[i:i+len(pattern)] == pattern:
                result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

