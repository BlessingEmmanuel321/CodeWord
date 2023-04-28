# Basic Program Logic

# 3.2 - Player's logic

def play_game(player):
    print(f"It's now {player} turn to play")
    print(player_codeword)
    print(f"\n\n{player_key}")

    cell = input("What number do you want to fill in?: ")
    if cell not in range(0, 16):
        print("Number not found")
    guess = input("What letter do you want to put here?: ")

    for x in range(len(player_codeword)):
        for y in range(len(player_codeword[x])):
            if player_codeword[x][y] == cell:
                original_codeword_value = player_codeword[x][y]
                player_codeword[x][y] = guess
                for i in range(len(player_key)):
                    for a in range(len(player_key[i])):
                        if player_key[i][a] == cell:
                            original_key_value = player_key[i][a]
                            player_key[i][a] = guess
                            print(player_codeword, player_key)

                            if player_codeword == original_codeword_value and player_key == original_key_value:
                                health_value += 2
                                if player_codeword == codeword and player_key == answer_key:
                                    print(f"Congratulations {player}! You have won the game!")
                                else:
                                    continue
                                if player == PersonalDetails(name1):
                                    play_game(PersonalDetails(name2))
                                elif player == PersonalDetails(name2):
                                    play_game(PersonalDetails(name1))
                                return

                            else:
                                player_codeword[x][y] = original_codeword_value
                                player_key[i][a] = original_key_value
                                print(f"{Player}, your answer is incorrect")
                                health_value -= 2
                                if player == player1.name1:
                                    play_game(player2.name2)
                                elif player == player2.name2:
                                    play_game(player1.name1)
                return


# Function that checks if both of them want to play and if they have enough lives
def player_check(health1, health2):
    player1_answer = input("Player 1, do you want to continue playing? (y/n): ")
    player2_answer = input("Player 2, do you want to continue playing? (y/n): ")

    if player1_answer.lower() == 'y' and player2_answer.lower() == 'y':
        if health1 >= 2 and health2 >= 2:
            print("Both players can continue playing.")
        else:
            print("You don't have enough lives.")
    else:
        print("Game ended.")

def player_menu():
    print("1: Play the Game")
    print("2: Display the statistics")
    choice = input("Choose an option: ")
    if choice in range(1, 3):
        return

def admin_menu():
    print("1: Display codeword")
    print("2: Display incomplete codeword")
    print("3: Display key grid")
    print("4: Display incomplete key grid")
    print("5: Add a different word to the puzzle")
    print("6: Delete a word from the puzzle")
    print("7: ")
    print("8: ")
    print("9: ")
    menu_choice = input("Choose an option: ")
    if menu_choice in range(1, 10):
        return

def start_program():
    print("1: Administrator")
    print("2: Player")
    print("3: Exit the system")
    choices = input("Choose an option: ")
    if choices in range(1, 4):
        return

def administrator_login():

    correct_guesses = 0
    incorrect_guesses = 0
    for row in range(9):
        for col in range(9):
            if player_codeword[row][col] == answer_key[row][1]:
                correct_guesses += 1
            elif player_codeword[row][col] != player_key[row][1]:
                incorrect_guesses += 1

    health_value = 5 - (incorrect_guesses // 3)

    if player_num == 1:
        player1.health_value = health_value

        def play_game():
            print(player_codeword)
            print(player_key)
            player_num = int(input("Enter your player number (1 or 2): "))
            player_name = ""
            for player in players_details[1:]:
                if player_num == 1 and player[0] == player1.name:
                    player_name = player1.name
                    break
                elif player_num == 2 and player[0] == player2.name:
                    player_name = player2.name
                    break

            cell = input("What number do you want to fill in: ")
            if cell not in range(1, 16):
                print("Number not found")
            else:
                letter_guess = input("What letter do you want to put here: ")

def play_game():
    cell = int(input("Enter what number you want to input for: "))
    while cell not in range(1, 16):
        cell = int(input("Enter a number from 1-15: "))
    letter_guess = input("Enter the letter you want to place here: ")
    correct_guesses = 0
    incorrect_guesses = 0
    for x in range(len(player_codeword)):
        for y in range(len(player_codeword)):
            if player_codeword[x][y] == cell:
                original_codeword = player_codeword[x][y]
                player_codeword[x][y] = letter_guess
                for i in range(len(player_key)):
                    for n in range(len(player_key)):
                        if player_key[i][n] == cell:
                            original_key = player_key[i][n]
                            player_key[i][n] = letter_guess
                            for row in player_codeword:
                                for column in row:
                                    print(column, end=" ")
                                print(" ")
                            for key in player_key:
                                for num in key:
                                    print(num, end=" ")
                                print(" ")

                            if player_codeword[x][y] == codeword[x][y] and player_key[i][n] == answer_key[i][n]:
                                correct_guesses += 1
                                if player_codeword == codeword and player_key == answer_key:
                                    print(f"Congratulations, you have won the game!")
                                    break
                            else:
                                print(f"Your answer is incorrect, therefore you lose 2 health points")
                                player_codeword[x][y], player_key[i][n] = original_codeword, original_key
                                incorrect_guesses += 1

    def play_game():

        correct_guesses = 0
        incorrect_guesses = 0

        while correct_guesses < 15:
            player_num = int(input("Enter your player number (1 or 2): "))
            player_name = ""
            for player in players_details[1:]:
                if player_num == 1 and player[0] == player1.name:
                    player_name = player1.name
                    break
                elif player_num == 2 and player[0] == player2.name:
                    player_name = player2.name
                    break

            cell = input("Enter the number you want to guess for: ")
            while int(cell) not in range(1, 16):
                print(cell)
            letter_guess = input("Enter the letter that you want to guess for: ")
            matched_cells = []
            for row in range(len(player_codeword)):
                for col in range(len(player_codeword[row])):
                    if str(cell) in str(player_codeword[row][col]):
                        player_codeword[row][col] = letter_guess
                        matched_cells.append((row, col))
            for x in player_codeword:
                for y in x:
                    print(y, end=" ")
                print(" ")
            if player_codeword == codeword:
                print(f"{player_name}, has successfully won the game")
            elif letter_guess in codeword:
                print("Correct answer")
                correct_guesses += 1
            else:
                print(f"{player_name}, your guess was incorrect therefore you lose 2 health points")
                for row, col in matched_cells:
                    player_codeword[row][col] = str(cell)
                incorrect_guesses += 1