def checkStraightLine(coordinates):
    s_coord = sorted(coordinates, key=lambda x: (x[0], x[1]))
    if len(coordinates) > 1:
        d_x = s_coord[1][0] - s_coord[0][0]
        d_y = s_coord[1][1] - s_coord[0][1]

        if d_y == 0:
            for i in range(2, len(s_coord)):
                if (s_coord[i][1] - s_coord[i - 1][1]) != 0:
                    return False
            return True
        else:
            q = d_x / d_y
            for i in range(2, len(s_coord)):
                if (s_coord[i][1] - s_coord[i - 1][1]) == 0:
                    return False
                elif (s_coord[i][0] - s_coord[i - 1][0]) / (s_coord[i][1] - s_coord[i - 1][1]) != q:
                    return False
    return True


# print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
# print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(checkStraightLine([[0, 0], [0, 1], [0, -1]]))
