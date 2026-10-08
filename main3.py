from classes1 import Team, Driver


def main():
    teams = []
    teams_by_name = {}
    try:
        with open("f1_points.csv", encoding="utf-8") as data_file:
            next(data_file)
            for line in data_file:
                driver_name, team_name, points = line.strip().split(",")
                if team_name not in teams_by_name:
                    team = Team(team_name)
                    teams_by_name[team_name] = team
                    teams.append(team)

                driver = Driver(driver_name, int(points))
                teams_by_name[team_name].add_driver(driver)
    except FileNotFoundError:
        print("Error: f1_points.csv file not found.")
        return
    except ValueError:
        print("Error: Invalid points data in f1_points.csv.")
        return

    for team in sorted(teams):
        print(team)


main()