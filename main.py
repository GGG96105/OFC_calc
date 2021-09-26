import numpy as np


# player base
while True:
    # Takes a number of players (either 2 or 3).
    while True:
        try:
            number_of_players = int(input('Chose a number of players: '))
        except ValueError:
            number_of_players = 0
        if number_of_players in range(2, 4):
            break
        else:
            print('The number of players is supposed to be either 2 or 3.')

    # requests player names to store in a dictionary
    player_name = {}
    for i in range(number_of_players):
        player_name[i] = input(f"Give a name to player{i + 1}: ")

    # prints list of players and asks for confirmation
    for player, name in player_name.items():
        print(f"Player {player + 1} will be called {name}. ")
    confirmation = input("Are you happy with your selection of names (y/n): ")
    if confirmation.casefold() == 'y':
        break


final_score = [0, 0, 0]



starting_score_conf = input("Do you want to insert a starting score (y/n): ")
while True:
  if starting_score_conf == 'y':
    try:
      for x in range(number_of_players):
        final_score[x] = int(input(f"Enter the starting points of player {x+1}: "))
      break
    except ValueError:
      print('Please enter valid numbers')
  else:
    break
    

# main program
hand_number = 1
points = {}
points[0] = [0, 0, 0]
row_inter_1_2 = 0
row_inter_2_3 = 0
row_inter_1_3 = 0

for_zip = []
while True:
    print(f"This is hand {hand_number}...")
    h_r = [0, 0, 0]    # hand royalties
    hand_points = [0, 0, 0]
    while True:
        try:
            for i in range(number_of_players):
                h_r[i] = int(input(f"Enter the royaltie points of {player_name[i]} from hand {hand_number}: "))

            if number_of_players == 2:
                row_inter_1_2 = int(input(f'Enter the row points between {player_name[0]} and {player_name[1]}: '))
            else:
                row_inter_1_2 = int(input(f'Enter the row points between {player_name[0]} and {player_name[1]}: '))
                row_inter_2_3 = int(input(f'Enter the row points between {player_name[1]} and {player_name[2]}: '))
                row_inter_1_3 = int(input(f'Enter the row points between {player_name[0]} and {player_name[2]}: '))
            break
        except ValueError:
            print("Please enter legitimate values!")
    if number_of_players == 3:
        hand_points[0] = (h_r[0] - h_r[1])+(h_r[0] - h_r[2]) + row_inter_1_3 + row_inter_1_2
        hand_points[1] = (h_r[1] - h_r[0])+(h_r[1] - h_r[2]) + row_inter_2_3 - row_inter_1_2
        hand_points[2] = (h_r[2] - h_r[0])+(h_r[2] - h_r[1]) - row_inter_2_3 - row_inter_1_3

        print(f"{player_name[0]}: {hand_points[0]}, {player_name[1]}: {hand_points[1]}, {player_name[2]}: "
              f"{hand_points[2]}")
    else:
        hand_points[0] = (h_r[0] - h_r[1]) + row_inter_1_2
        hand_points[1] = - hand_points[0]
        print(f"{player_name[0]}: {hand_points[0]}   {player_name[1]}: {hand_points[1]}")

    points[hand_number] = hand_points

    points_check = input('Are those the correct amo1unt of points from this hand (y/n): ')
    if points_check != 'n':

        for_zip = points.values()
        final_score += sum(map(np.array, for_zip))

        final_score_view = input("Do you want to take a look at the current score (y/n): ")

        if final_score_view == 'y':
            print(final_score)

        check_next_hand = input('Continue to next hand(y/n): ')
        if check_next_hand != 'n':
            hand_number += 1
        else:
            break

print(f"The final score is {player_name[0]}: {final_score[0]}, {player_name[1]}: {final_score[1]}, {player_name[2]}"
      f": {final_score[2]}.")
input('Enter')
