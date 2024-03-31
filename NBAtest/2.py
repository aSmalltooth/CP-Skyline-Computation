def dominates(point1, point2):
    # 检查 point1 是否支配 point2
    return all(p1 >= p2 for p1, p2 in zip(point1, point2)) and any(p1 >= p2 for p1, p2 in zip(point1, point2))

def find_skyline(points):
    skyline = []
    for point in points:
        dominated = False
        to_remove = []
        for i, skyline_point in enumerate(skyline):
            if dominates(skyline_point, point):
                dominated = True
                break
            if dominates(point, skyline_point):
                to_remove.append(i)
        if not dominated:
            skyline = [p for j, p in enumerate(skyline) if j not in to_remove]
            skyline.append(point)
    return skyline

# 示例数据点集合
data_points = [
    (4, 10),
    (7, 7),
    (6,6),
    (3, 9),
    (8, 3),
    (2, 11),
    (11, 1)
]

result = find_skyline(data_points)
print("Skyline Points:")
for point in result:
    print(point)
