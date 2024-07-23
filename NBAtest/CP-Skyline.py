import csv
import time
data = []

with open('all_seasons.csv', newline='') as csvfile:
    # Create CSV dictionary reader, specify column names
    reader = csv.DictReader(csvfile, fieldnames=[
        "index", "player_name", "team_abbreviation", "age", "player_height",
        "player_weight", "college", "country", "draft_year", "draft_round",
        "draft_number", "gp", "pts", "reb", "ast", "net_rating", "oreb_pct",
        "dreb_pct", "usg_pct", "ts_pct", "ast_pct", "season"
    ])

    # Skip the header row (if present)
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Convert each row to a dictionary and add to the list
        data.append(dict(row))

filtered_data = [point for point in data if float(point['pts']) > 15 and float(point['reb']) > 8]


def dominates(point1, point2, attributes):
    # Check if point1 dominates point2 (assuming larger values are better)
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

# Specify the attributes for Skyline query
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
