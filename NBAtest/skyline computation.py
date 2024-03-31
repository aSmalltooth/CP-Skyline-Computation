import csv
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

# 输出转换后的数据
for row_dict in data:
    print(row_dict),
print(type(data))
print(data[0]['gp'])

