from operator import attrgetter
import numpy

print('Welcome to the basketball simulator.')


class Team:
    def __init__(self):
        self.location = input('Where is the team located? ')
        self.mascot = input('What is the team mascot? ')
        self.wins = input('How many wins did the team have? ')

    def __repr__(self):
        return self.mascot

    def team_info(self):
        return f"{self.location} {self.mascot} | {self.wins} wins"


def determine_homecourt(teams):
    return max(teams, key=lambda obj: getattr(obj, 'wins'))


print('TEAM 1 ATTRIBUTES')
team_one = Team()
print(f"Team 1: {team_one.team_info()}")

print('TEAM 2 ATTRIBUTES')
team_two = Team()
print(team_two.team_info())

print(
    f"The two teams playing in this series are:\n{team_one.location} {team_one.mascot}\n{team_two.location} {team_two.mascot}.")

teams = [team_one, team_two]

home_team = determine_homecourt(teams)
print(f"The {home_team} will be the home team.")

team_one_wins = 0
team_two_wins = 0
next_game = 1

while True:
    if team_one_wins == 4:
        print(f"The {team_one.location} {team_one.mascot} win the series {team_one_wins} games to {team_two_wins}.")
        break
    elif team_two_wins == 4:
        print(f"The {team_two.location} {team_two.mascot} win the series {team_two_wins} games to {team_one_wins}.")
        break
    else:
        print(f"{team_one.location}: {team_one_wins}\n{team_two.location}: {team_two_wins}")
        pass
    team_one_score = numpy.random.choice([70, 80, 90, 100, 110, 120], p=[0.1, 0.2, 0.3, 0.15, 0.15, 0.1])
    team_two_score = numpy.random.choice([70, 80, 90, 100, 110, 120], p=[0.1, 0.2, 0.3, 0.15, 0.15, 0.1])
    print(f"Game {next_game} is starting!")
    print(f"Final score:\n{team_one.location} {team_one_score}\n{team_two.location} {team_two_score}")
    if team_one_score > team_two_score:
        print(f"{team_one.location} wins.")
        team_one_wins += 1
        next_game += 1
    elif team_two_score > team_one_score:
        print(f"{team_two.location} wins.")
        team_two_wins += 1
        next_game += 1
    else:
        print('Redo...')
        continue


