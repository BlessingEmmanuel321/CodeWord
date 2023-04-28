import hashlib
import random
# fix the error in the play_game() function. it continues to say my guess is incorrect when i input a correct guess. for example for cell i input 8 and for letter_guess i input E and the code goes to else and says I'm wrong.
codeword = [
    ["#", "A", "D", "I", "D", "A", "S", "#", "#"],
    ["P", "#", "#", "#", "#", "#", "K", "#", "#"],
    ["U", "#", "#", "#", "#", "#", "E", "#", "#"],
    ["M", "#", "#", "#", "#", "#", "C", "#", "#"],
    ["A", "#", "#", "#", "#", "#", "H", "#", "N"],
    ["#", "#", "#", "#", "#", "#", "E", "#", "I"],
    ["#", "#", "#", "#", "#", "#", "R", "#", "K"],
    ["#", "#", "#", "#", "#", "#", "S", "#", "E"],
    ["R", "E", "E", "B", "O", "K", "#", "#", "#"]

]

player_codeword = [

    ["#", "A", "1", "2", "D", "3", "4", "#", "#"],
    ["5", "#", "#", "#", "#", "#", "6", "#", "#"],
    ["U", "#", "#", "#", "#", "#", "8", "#", "#"],
    ["9", "#", "#", "#", "#", "#", "10", "#", "#"],
    ["3", "#", "#", "#", "#", "#", "H", "#", "12"],
    ["#", "#", "#", "#", "#", "#", "8", "#", "2"],
    ["#", "#", "#", "#", "#", "#", "13", "#", "K"],
    ["#", "#", "#", "#", "#", "#", "4", "#", "8"],
    ["R", "8", "8", "14", "O", "6", "#", "#", "#"]

]

answer_key = [
    ["1", "D"], ["2", "I"], ["3", "A"], ["4", "S"], ["5", "P"], ["6", "K"], ["7", "U"], ["8", "E"], ["9", "M"], ["10", "C"],
    ["11", "H"], ["12", "N"], ["13", "R"], ["14", "B"], ["15", "O"]
]

player_key = [
    ["1", "D"], ["2", "_"], ["3", "A"], ["4", "_"], ["5", "_"], ["6", "K"], ["7", "U"], ["8", "_"], ["9", "_"], ["10", "_"],
    ["11", "H"], ["12", "_"], ["13", "R"], ["14", "_"], ["15", "O"]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
random_chars = "!?%$"


def username_password(name):
    name_lst = list(name)
    popped = name_lst.pop()
    username = name_lst[0] + popped + random.choice(name_lst) + random.choice(numbers)
    password = random.choice(alphabet) + random.choice(numbers) + random.choice(alphabet) + random.choice(
        random_chars) + random.choice(alphabet) + random.choice(numbers)
    return username, password


class PersonalDetails:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.health_value = 5

    def username_encrypted(self):
        return hashlib.sha256(self.username.encode()).hexdigest()

    def password_encrypted(self):
        return hashlib.sha256(self.password.encode()).hexdigest()


admin_name = "Blessing"
admin_username, admin_password = username_password(admin_name)
admin_info = PersonalDetails(admin_name, admin_username, admin_password)

print("Lets create your login details.")
name1 = input("\nEnter player one's name: ")
username1, password1 = username_password(name1)
player1 = PersonalDetails(name1, username1, password1)

name2 = input("Enter player two's name: ")
username2, password2 = username_password(name2)
player2 = PersonalDetails(name2, username2, password2)

print(f"\n{player1.name}'s login info:\nUsername: {player1.username}\nPassword: {player1.password}\n")
print(f"{player2.name}'s login info:\nUsername: {player2.username}\nPassword: {player2.password}")

players_details = [[admin_info.name, admin_info.username_encrypted(), admin_info.password_encrypted()],
                   [player1.name, player1.username_encrypted(), player1.password_encrypted(), player1.health_value],
                   [player2.name, player2.username_encrypted(), player2.password_encrypted(), player2.health_value]]


def start_program():
    print("\n\nMain Menu")
    print("\n1: Administrator")
    print("2: Player")
    print("3: Exit the system")
    choice = int(input("\nChoose an option: "))
    if choice == 1:
        if login(admin_info.username_encrypted(), admin_info.password_encrypted()):
            print("You have successfully logged in as the administrator.")
        else:
            print("Incorrect username or password")
    elif choice == 2:
        for i in range(2):
            name = input("Enter your name: ")
            for PLAYER_DETAILS in players_details[1:]:
                if name == PLAYER_DETAILS[0]:
                    if login(PLAYER_DETAILS[1], PLAYER_DETAILS[2]):
                        print(f"{name} has successfully logged in")
                        break
                    else:
                        print("Incorrect username or password")
                        break
            else:
                print("\nNo player found with that name\n")
        player_menu()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")


def login(username_encrypted, password_encrypted):
    logged_in = False
    count = 3
    while (not logged_in) and (count > 0):
        username_attempt = input("Enter your username: ")
        if username_encrypted == hashlib.sha256(username_attempt.encode()).hexdigest():
            password_attempt = input("Enter your password: ")
            if password_encrypted == hashlib.sha256(password_attempt.encode()).hexdigest():
                logged_in = True
                break
            else:
                print("Incorrect password. Try again")
        else:
            print("Incorrect username. Try again")
        count -= 1

    return logged_in


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
    if menu_choice not in range(1, 10):
        print(menu_choice)
    if menu_choice == 1:
        display_codeword()
    elif menu_choice == 2:
        display_player_codeword()
    elif menu_choice == 3:
        display_answer_key()
    elif menu_choice == 4:
        display_player_key()


def display_codeword():
    for row in codeword:
        for column in row:
            print(column, end=" ")
        print(" ")


def display_player_codeword():
    for row in player_codeword:
        for column in row:
            print(column, end=" ")
        print(" ")


def display_answer_key():
    for row in answer_key:
        for column in row:
            print(column, end=" ")
        print(" ")


def display_player_key():
    for row in player_key:
        for column in row:
            print(column, end=" ")
        print(" ")


def player_menu():
    print("1: Play the Game")
    print("2: Display the statistics")
    choice = int(input("Choose an option: "))
    if choice == 1:
        player_check(player1.health_value, player2.health_value)


def player_check(health1, health2):
    player1_answer = input("Player 1, do you want to continue playing? (y/n): ")
    player2_answer = input("Player 2, do you want to continue playing? (y/n): ")

    if player1_answer.lower() == 'y' and player2_answer.lower() == 'y':
        if health1 >= 2 and health2 >= 2:
            print("Both players can continue playing.")
            game_rules()
        else:
            print("You don't have enough lives.")
    else:
        print("Game ended.")


def game_rules():
    print("\nWelcome to Codeword Games!")
    print("\nHere are the rules:")
    print("1. You must guess the letters in the codeword.")
    print("2. You have 5 chances to guess correctly.")
    print("3. For each incorrect guess, you will lose 2 health values.")
    print("4. If you lose all of your health values, the game is over.")
    print("5. The first player to guess the entire codeword wins the game.")
    print("\nLet's begin!")
    print("\nHere is the Codeword:")
    for row in player_codeword:
        for column in row:
            print(column, end=" ")
        print(" ")
    for key in player_key:
        for num in key:
            print(num, end=" ")
        print(" ")
    play_game()


def play_game():

    correct_guesses = 0
    incorrect_guesses = 0

    while correct_guesses < 15:
        player_check(health1, health2)
        player_num = int(input("Enter your player number (1 or 2): "))
        player_name = ""
        for player in players_details[1:]:
            if player_num == 1 and player[0] == player1.name:
                player_name = player1.name
                health1 = player1.health_value
                health1 -= (incorrect_guesses*2)
                health1 += (correct_guesses*2)
                break
            elif player_num == 2 and player[0] == player2.name:
                player_name = player2.name
                health2 = player2.health_value
                health2 -= (incorrect_guesses*2)
                health2 += (correct_guesses*2)
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
        if letter_guess in codeword:
            print("Correct answer!")
            correct_guesses += 1
            if codeword == player_codeword:
                print(f"{player_name}, has successfully won")
        else:
            print(f"{player_name}, your guess was incorrect therefore you lose 2 health points")
            for row, col in matched_cells:
                player_codeword[row][col] = str(cell)
            incorrect_guesses += 1


start_program()
