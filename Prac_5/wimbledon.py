FILE_NAME = "test.csv"

win_counts = {}
champion_countries = set()

with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
    file_data = []
    next(in_file)
    for line in in_file:
        file_data.append(line.split(","))


for data in file_data:
    champion_countries.add(data[1])
    try:
        win_counts[data[2]] = win_counts[data[2]] + 1
    except KeyError:
        win_counts[data[2]] = 1

print("Wimbledon Champions:")
for champion in win_counts:
    print(f"{champion} {win_counts[champion]}")
print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
print(f", ".join(sorted(champion_countries)))

