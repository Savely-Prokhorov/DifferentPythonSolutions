coordinates_arr = [(-1, 0), (-1, 4), (2, 4), (2, 0)]

count = 0
for i in range(0, 4):
    vector1 = coordinates_arr[i - 1][0] - coordinates_arr[i][0], coordinates_arr[i - 1][1] - coordinates_arr[i][1]
    if i != 3:
        vector2 = coordinates_arr[i + 1][0] - coordinates_arr[i][0], coordinates_arr[i + 1][1] - coordinates_arr[i][1]
    else:
        vector2 = coordinates_arr[0][0] - coordinates_arr[i][0], coordinates_arr[0][1] - coordinates_arr[i][1]

    scalar_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    if scalar_product == 0:
        count += 1

print(count)
