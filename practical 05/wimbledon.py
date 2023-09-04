def read_wimbledon_data(filename):
    wimbledon_data = []

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        for line in lines[1:]:
            fields = line.strip().split(',')
            year = int(fields[0])
            champ_country = fields[1]
            champion = fields[2]
            runner_country = fields[3]
            runner_up = fields[4]
            score = ",".join(fields[5:])
            wimbledon_data.append((year, champ_country, champion, runner_country, runner_up, score))

    return wimbledon_data


def count_champions(wimbledon_data):
    champion_counts = {}

    for year, champ_country, champion, _, _, _ in wimbledon_data:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1

    return champion_counts


def list_countries(wimbledon_data):
    countries = set()

    for _, champ_country, _, _, _, _ in wimbledon_data:
        countries.add(champ_country)

    sorted_countries = sorted(countries)
    countries_str = ', '.join(sorted_countries)

    return countries_str


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)

    print("Wimbledon Champions:")
    champion_counts = count_champions(wimbledon_data)
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

    countries_str = list_countries(wimbledon_data)
    print("\nThese", len(countries_str.split(', ')), "countries have won Wimbledon:")
    print(countries_str)


main()
