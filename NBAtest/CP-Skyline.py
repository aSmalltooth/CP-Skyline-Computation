import csv
import time
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

filtered_data = [point for point in data if float(point['pts']) > 15 and float(point['reb']) > 8  ]


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
count1 = 0
result = find_skyline(filtered_data, attributes_to_compare)
end = time.perf_counter()
print("Skyline Points:")
for data in result:
    print(data)
    count1 +=1
print(count1)
print((end-start)*1000)




