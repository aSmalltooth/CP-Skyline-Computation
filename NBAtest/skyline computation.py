import csv
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

# Output the converted data
for row_dict in data:
    print(row_dict),
print(type(data))
print(data[0]['gp'])
