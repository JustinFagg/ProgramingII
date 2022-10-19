"""
Word Occurrences
Estimate: 40 minutes
Actual:   51 minutes
"""


FILE_NAME = "test.csv"


def main():
    file_data = get_data()
    champion_countries, win_counts = scalp_data(file_data)
    print_data(champion_countries, win_counts)


def print_data(champion_countries, win_counts):
    print("Wimbledon Champions:")
    for champion in win_counts:
        print(f"{champion} {win_counts[champion]}")
    print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
    print(f", ".join(sorted(champion_countries)))


def scalp_data(file_data):
    win_counts = {}
    champion_countries = set()
    for data in file_data:
        champion_countries.add(data[1])
        try:
            win_counts[data[2]] = win_counts[data[2]] + 1
        except KeyError:
            win_counts[data[2]] = 1
    return champion_countries, win_counts


def get_data():
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        file_data = []
        next(in_file)
        for line in in_file:
            file_data.append(line.split(","))
    return file_data


main()
