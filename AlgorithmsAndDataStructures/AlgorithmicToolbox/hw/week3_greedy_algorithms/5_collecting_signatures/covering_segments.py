# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort()

    i, count = 0, 0
    while i<len(segments)-1 and count < len(segments):
        j = i+1
        while j<len(segments)-1:
            if segments[i].end in range(segments[j].start, segments[j].end+1):
                j += 1
            else:
                break
        count += j-i+1
        if segments[i].end not in points:
            points.append(segments[i].end)
        i += 1


    """for s in segments:
        points.append(s.start)
        points.append(s.end)"""
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
