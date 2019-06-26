from constants import PLAYERS, TEAMS
from typing import List
from copy import deepcopy


def clean_the_data() -> List:

    data_dictionary = deepcopy(PLAYERS)

    cleaned_data = []

    for player in data_dictionary:
        try:
            player["height"] = int(player["height"][:2])
        except ValueError as err:
            print("invalid data from file {}".format(err))
            quit()

        if player["experience"] == "YES":
            player["experience"] = True
        elif player["experience"] == "NO":
            player["experience"] = False

        cleaned_data.append(player["name"])

    return cleaned_data


def balance_on_players(data: List):

    team_build = []

    teams = deepcopy(TEAMS)

    team_size = int(len(data) / len(teams))

    for t in teams:

        sample = data[0:team_size]

        team_build.append((t, sample))

        del data[0:team_size]

    return team_build


def create_teams():

    clean_data = clean_the_data()

    the_teams = balance_on_players(clean_data)

    return the_teams


def display_menu():

    menu = '''
    *****   MENU    *****\n
    Here are your choices:\n
    1) Display team stats \n
    2) Quit\n
    '''
    print(menu)


def display_team_options():

    teams = deepcopy(TEAMS)

    for index, t in enumerate(teams, start=1):
        print("{}: {} ".format(index, t))


def display_stats(chosen_team: int, the_teams: List):

    stats = """
    Team: {} Stats \n
    -------------------- \n
    Total Players: {} \n \n

    Players on Team: \n
    {} 
    """

    selected_team = the_teams[chosen_team - 1]
    team_name = selected_team[0]
    total_players = len(selected_team[1])
    list_of_players = selected_team[1]

    print(stats.format(team_name, total_players, ", ".join(list_of_players)))


def users_main_menu_choice():
    valid_option = False
    menu_option = ""

    while not valid_option:
        menu_option = input(display_menu())

        if menu_option not in ("1", "2"):
            print("You must type 1 or 2 ")
        else:
            valid_option = True

    return menu_option


def users_team_choice():
    valid_option = False

    selection = 0

    # number of teams from the length of teams plus 1 to be inclusive
    range_max = len(TEAMS) + 1

    while not valid_option:
        try:
            selection = int(input(display_team_options()))

            if selection not in range(1, range_max):
                print("\nYou picked {}. Please pick a number from 1 to {}. ".format(selection, len(TEAMS)))
            else:
                valid_option = True
        except ValueError:
            print("\nPlease type a valid number from the list!\n")
    return selection


if __name__ == '__main__':
    # create a team
    created_teams = create_teams()

    print("BASKETBALL TEAM STATS TOOL")

    # get user choice of main menu
    option = users_main_menu_choice()

    while option is "1":
        # user picks team
        print("\nPlease Select A Team (1, 2, 3) \n")
        team = users_team_choice()

        # display stats for team
        display_stats(int(team), created_teams)

        # see if user wants to continue
        option = users_main_menu_choice()

    else:
        quit()
