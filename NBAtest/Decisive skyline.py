import csv
import time
from itertools import combinations
data = []

# 打开 CSV 文件
with open('all_seasons.csv', newline='') as csvfile:
    # 创建 CSV 字典读取器，指定列名
    reader = csv.DictReader(csvfile, fieldnames=[
        "index", "player_name", "team_abbreviation", "age", "player_height",
        "player_weight", "college", "country", "draft_year", "draft_round",
        "draft_number", "gp", "pts", "reb", "ast", "net_rating", "oreb_pct",
        "dreb_pct", "usg_pct", "ts_pct", "ast_pct", "season"
    ])

    # 跳过标题行（如果存在）
    next(reader)

    # 遍历读取 CSV 文件的每一行
    for row in reader:
        # 将每行数据转换为字典并添加到列表中
        data.append(dict(row))

def dominates(point1, point2, attributes):
    # 检查 point1 是否支配 point2（假设更大的值更优）
    return all(float(point1[attr]) >= float(point2[attr]) for attr in attributes) and any(float(point1[attr]) > float(point2[attr]) for attr in attributes)

def find_skyline(data, attributes):
    skyline = []
    for point in data:
        dominated = False
        to_remove = []
        for i, skyline_point in enumerate(skyline):
            if dominates(skyline_point, point, attributes):
                dominated = True
                break
            if dominates(point, skyline_point, attributes):
                to_remove.append(i)
        if not dominated:
            skyline = [p for j, p in enumerate(skyline) if j not in to_remove]
            skyline.append(point)
    return skyline

# 指定进行 Skyline 查询的属性
attributes_to_compare = ['pts','reb','ast','net_rating','usg_pct']


start = time.perf_counter()
result = find_skyline(data, attributes_to_compare)

all_subsets = [list(subset) for subset_size in range(1, len(attributes_to_compare) + 1)
               for subset in combinations(attributes_to_compare, subset_size)]

# 输出所有子集
for i, subset in enumerate(all_subsets):
    print(f'skyline in a[{i}] = {subset}')
    skyline = find_skyline(result,all_subsets[i])
    for j in skyline:
        print(j)
end = time.perf_counter()
print((end - start)*1000)
