import random
import game_data as data

# =================== Part I: Required Functions - Starts ===================

# Input: N/A
# Output: N/A
# This function initiates the game logic, and displays all the menus
def main_menu():
    # selected value of main menu function
    main_menu_option = 0
    # maintains overall game results of all the games played
    game_result_list = list()
    # result for dice rolls in each game
    dice_result_list = list()

    while (not valid_main_menu_option(main_menu_option)):
        print(data.new_game_string)
        print(data.main_menu_opt_1)
        print(data.main_menu_opt_2)
        print(data.main_menu_opt_3)
        print("\n")

        main_menu_option = int(input(data.main_menu_input))
        if main_menu_option == 3:
            print(data.exit_game_str)
        elif main_menu_option == 2:
            print(data.game_history_str)
            game_history_menu(game_result_list)
        elif main_menu_option == 1:
            print(data.start_game_str)
            game_result_list.append(game_menu())
            print(data.end_game_str)
        else:
            print(data.main_menu_invalid_input)

# Input: N/A
# Output: List - Tuple - int
# This function is the main game mennu
def game_menu():
    number_of_dice = 0
    while (not valid_dice_count(number_of_dice)):
        number_of_dice = int(input(data.game_menu_input_1))
        if valid_dice_count(number_of_dice):
            type_of_dice = 0
            while (not valid_type_of_dice(type_of_dice)):
                type_of_dice = int(input(data.game_menu_input_2))
                if (valid_type_of_dice(type_of_dice)):
                    return game_play(number_of_dice, type_of_dice)
                else:
                    print(data.game_menu_invalid_input_1)
        else:
            print(data.game_menu_invalid_input_2)

# Input: int, int
# Output: Tuple - int
# This function rolls the selected dice type selected number of times
def roll_dice(number_of_dice, type_of_dice):
    outcome = list()
    for x in range(number_of_dice):
        outcome.append(roll_value(type_of_dice))
    display_dice_results(tuple(outcome))
    return tuple(outcome)

# Input: List - Tuple - int
# Output: String
# This function checks if the player has won or lost the game
def check_win_lose(dice_result_list):
    if (len(dice_result_list) < 0):
        return 'not played'

    if (len(dice_result_list) > 10):
        return 'lose'

    game_result = list()
    for game_turn in dice_result_list:
        for outcome in game_turn:
            game_result.append(outcome)

    game_result.sort()
    median = calculate_median(game_result)
    mean = int(sum(game_result)/len(game_result))

    if median == mean:
        return 'win'
    else:
        return 'lose'

# Input: List - Tuple - int
# Output: N/A
# This function displays game history data
def game_history_menu(game_result_list):
    game_history = list()
    for result in game_result_list:
        game_history.append({ "number_of_roll": len(result), "number_of_dice": len(result[0]), "result": check_win_lose(result) })

    display_history(game_history)

# =================== Part I: Required Functions - Ends =====================

# =================== Part II: Addtional Functions - Start ==================

# Input: int, int
# Output: List - Tuple - int
# This method executes main game play logic
def game_play(number_of_dice, type_of_dice):
    print(data.game_menu_opt_1)
    print(data.game_menu_opt_2)
    print(data.game_menu_opt_3)
    print("\n")

    # result for dice rolls in each game
    dice_result_list = list()

    selected_option = 0
    while (not exit_game_option(selected_option)):
        selected_option = int(input())
        if selected_option == 1:
            type_of_dice = change_dice_type(type_of_dice)
            dice_result_list.append(roll_dice(number_of_dice, type_of_dice))
        elif selected_option == 2:
            print(check_win_lose(dice_result_list))
        elif selected_option == 3:
            return dice_result_list

# Input: int
# Output: int
# This method changes the value of dice type if the player opts to change the type of dice
def change_dice_type(type_of_dice):
    change_dice_type = ""
    while (not valid_response(change_dice_type)):
        change_dice_type = input(data.change_dice_type_input)
        if change_dice_type == "yes":
            new_type_of_dice = 0
            while (not valid_type_of_dice(new_type_of_dice)):
                new_type_of_dice = int(input(data.game_menu_input_2))
                if (valid_type_of_dice(new_type_of_dice)):
                    return new_type_of_dice
                else:
                    print(data.change_dice_type_invalid_input_2)
        elif change_dice_type == "no":
            return type_of_dice
        else:
            print(data.change_dice_type_invalid_input_1)

# Input: int
# Output: int
# This function returns the value after the roll of a dice
def roll_value(type_of_dice):
    if type_of_dice == 6:
        return random.randint(1, 6)
    elif type_of_dice == 8:
        return random.choice([2,2,3,3,4,8])
    elif type_of_dice == 9:
        return random.choice([1,1,1,1,5,9])

# Input: List
# Output: int
# This function calculates the median of the of the game
def calculate_median(list_of_numbers):
    size_is_even = ((len(list_of_numbers)/2) % 2) == 0
    middle_of_list = int(len(list_of_numbers)/2)
    if size_is_even:
        return int((list_of_numbers[middle_of_list] + list_of_numbers[middle_of_list + 1])/2)
    else:
        return int(list_of_numbers[middle_of_list])

# Input: List
# Output: N/A
# This function displays the result of selected number of dices after each roll
def display_dice_results(game_turn):
    rows = []
    for outcome in game_turn:
        rows.append(dice(outcome))
    display_dice(rows)

# Input: int
# Output: 2-D Array
# This function returns the display of dice based of number generated after a roll in 2-D Array
def dice(outcome):
    display = []
    if outcome == 1:
        display.append(
        "-------"
        "|     |"
        "|  O  |"
        "|     |"
        "-------")
    elif outcome == 2:
        display.append(
        "-------"
        "|     |"
        "|O   O|"
        "|     |"
        "-------")
    elif outcome == 3:
        display.append(
        "-------"
        "|O    |"
        "|  O  |"
        "|    O|"
        "-------")
    elif outcome == 4:
        display.append(
        "-------"
        "|O   O|"
        "|     |"
        "|O   O|"
        "-------")
    elif outcome == 5:
        display.append(
        "-------"
        "|O   O|"
        "|  O  |"
        "|O   O|"
        "-------")
    elif outcome == 6:
        display.append(
        "-------"
        "|O O O|"
        "|     |"
        "|O O O|"
        "-------")
    elif outcome == 8:
        display.append(
        "-------"
        "|O O O|"
        "|O   O|"
        "|O O O|"
        "-------")
    elif outcome == 9:
        display.append(
        "-------"
        "|O O O|"
        "|O O O|"
        "|O O O|"
        "-------")
    return display[0]

# Input: 2-D Array
# Output: N/A
# This function prints the final result
def display_dice(rows):
    for rx in range(5):
       for ry in rows:
          print(ry[rx*7:(rx+1)*7], end='          ')
       print()

# Input: List - Dictionary
# Output: N/A
# This method display game history in string format
def display_history(game_history):
    game_history = sorted(game_history, key=lambda i: i['number_of_roll'])
    result_display_string = ""
    for game in game_history:
        result_display_string += "Dice rolling times: " + str(game['number_of_roll']) + ", Number of dice: " + str(game['number_of_dice']) + ", Result: " + game['result'] + "\n"
    print(result_display_string)

# =================== Part II: Addtional Functions - Ends ===================

# =================== Part III: Validation Functions Starts =================

# Input: int
# Output: boolean
# This method checks if the player wants to exit the game
def exit_game_option(selected_option):
    return (selected_option == 3)

# Input: int
# Output: boolean
# This function checks validity of main menu options
def valid_main_menu_option(main_menu_option):
    return (main_menu_option == 3)

# Input: int
# Output: boolean
# This function checks validity of dice count
def valid_dice_count(number_of_dice):
    return (number_of_dice >= 2 and number_of_dice <= 6)

# Input: int
# Output: boolean
# This function checks validity of dice type
def valid_type_of_dice(type_of_dice):
    return (type_of_dice == 6 or type_of_dice == 8 or type_of_dice == 9)

# Input: String
# Output: boolean
# This function checks validity of response
def valid_response(response):
    return (response == "yes" or response == "no")

# =================== Part III: Validation Functions Ends ===================

# =================== Part IV: Main Program Starts ==========================

print(data.start_of_program)
print()
main_menu()
print()
print(data.end_of_program)

# =================== Part IV: Main Program End =============================
