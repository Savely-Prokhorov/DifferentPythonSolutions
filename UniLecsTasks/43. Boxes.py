def volume(box):
    vol = 1
    for size in box:
        vol *= size
    return vol


def check_boxes_sizes(box1, box2):
    count = 0
    if sorted(box1) == sorted(box2):
        return "Boxes are equal"

    # если первая коробка больше по объёму
    # проверяем, помещается ли в нее вторая по размерам
    if volume(box1) > volume(box2):
        box1.sort()
        box2.sort()
        for i in range(3):
            if box1[i] >= box2[i]:
                count += 1
        if count == 3:
            return "The first box is larger than the second one"

    # и наоборот
    if volume(box1) < volume(box2):
        box1.sort()
        box2.sort()
        for i in range(3):
            if box1[i] <= box2[i]:
                count += 1
        if count == 3:
            return "The second box is larger than the first one"

    return "Boxes are incomparable"


tests = [[[1, 2, 3], [3, 2, 1]],
         [[2, 2, 3], [3, 2, 1]],
         [[1, 2, 3], [3, 2, 3]],
         [[3, 4, 5], [2, 4, 6]]]

for test in tests:
    print(check_boxes_sizes(test[0], test[1]))
