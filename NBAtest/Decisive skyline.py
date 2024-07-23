import csv
import time
from itertools import combinations
data = []

# Open CSV file
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
result = find_skyline(data, attributes_to_compare)

all_subsets = [list(subset) for subset_size in range(1, len(attributes_to_compare) + 1)
               for subset in combinations(attributes_to_compare, subset_size)]

# Output all subsets
for i, subset in enumerate(all_subsets):
    print(f'skyline in a[{i}] = {subset}')
    skyline = find_skyline(result, all_subsets[i])
    for j in skyline:
        print(j)
end = time.perf_counter()
print((end - start) * 1000)
