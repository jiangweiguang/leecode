def projectionArea(gird:[[int]]) -> int:
    x_area = y_area = z_area = 0
    for i in gird:
        max_y = i[0]
        for j in i:
            if j > 0:
                x_area += 1
            if j > max_y:
                max_y = j
        y_area += max_y
    for j in range(len(gird[0])):
        max_z = gird[0][j]
        for i in range(len(gird)):
            if gird[i][j] > max_z:
                max_z = gird[i][j]
        z_area += max_z
    return x_area+y_area+z_area

if __name__ =="__main__":
    print(projectionArea([[5,4],[0,3]]))