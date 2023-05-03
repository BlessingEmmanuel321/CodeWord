import hashlib
import pandas as pd
import random

codeword = [
    # Sports brand inspired crossword with the words: Adidas, Puma, Skechers, Nike, Reekbok
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
    ["1", "D"], ["2", "I"], ["3", "A"], ["4", "S"], ["5", "P"], ["6", "K"], ["7", "U"], ["8", "E"], ["9", "M"],
    ["10", "C"],
    ["11", "H"], ["12", "N"], ["13", "R"], ["14", "B"], ["15", "O"]
]

player_key = [
    ["1", "D"], ["2", "_"], ["3", "A"], ["4", "_"], ["5", "_"], ["6", "K"], ["7", "U"], ["8", "_"], ["9", "_"],
    ["10", "_"],
    ["11", "H"], ["12", "_"], ["13", "R"], ["14", "_"], ["15", "O"]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
random_chars = "!?%$@"


def admin_username_password(name):
    """
    This function is created just to create the admins username and password. The admin username/password is already
    created. They do not have the choice to create their own.
    """
    name_lst = list(name)
    popped = name_lst.pop()
    username = name_lst[0] + popped + random.choice(name_lst) + random.choice(numbers)
    password = random.choice(alphabet) + random.choice(numbers) + random.choice(alphabet) + random.choice(
        random_chars) + random.choice(alphabet) + random.choice(numbers)
    return username, password


def player_username_password(name):
    """
    This username/password creator is solely for the players. It allows them to create their own username and
    password. However, the password has to follow the criteria or else it loops.
    """
    username = input("Make a username: ")
    print("\nNow lets make you a password.\nIt must contain:")
    print("At least 2 numbers (0-9)")
    print("A capital letter (A-Z)")
    print("A lowercase letter (a-z)")
    print("A special character (!?%$@)")
    while True:
        password = input("\nPlease enter a password: ")
        if not (any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(not c.isalnum() for c in password)):
            print("Your password must meet the criteria above\n")
        else:
            return username, password


class PersonalDetails:
    """
    This class creates 4 instances of self. username/password_encrypted are used to encrypt the usernames and passwords.
    """

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.health_value = 5

    def username_encrypted(self):
        return hashlib.sha256(self.username.encode()).hexdigest()

    def password_encrypted(self):
        return hashlib.sha256(self.password.encode()).hexdigest()


class CodeWordGame:
    def __init__(self) -> None:

        self.admin_name = "Blessing"
        self.admin_username, self.admin_password = admin_username_password(self.admin_name)
        self.admin_info = PersonalDetails(self.admin_name, self.admin_username, self.admin_password)
        print(self.admin_username, self.admin_password)

        print("Lets create your login details.")
        self.name1 = input("\nEnter player one's name: ")
        self.username1, self.password1 = player_username_password(self.name1)
        self.player1 = PersonalDetails(self.name1, self.username1, self.password1)

        self.name2 = input("\nEnter player two's name: ")
        self.username2, self.password2 = player_username_password(self.name2)
        self.player2 = PersonalDetails(self.name2, self.username2, self.password2)

        self.players_details = [
            # List of all login info for admin and players
            [self.admin_info.name, self.admin_info.username_encrypted(), self.admin_info.password_encrypted()],
            [self.player1.name, self.player1.username_encrypted(), self.player1.password_encrypted(),
             self.player1.health_value],
            [self.player2.name, self.player2.username_encrypted(), self.player2.password_encrypted(),
             self.player2.health_value]]

    def start_program(self):
        print("\n\nMain Menu")
        print("\n1: Administrator")
        print("2: Player")
        print("3: Exit the system")
        choice = int(input("\nChoose an option: "))
        if choice == 1:
            if self.login(self.admin_info.username_encrypted(), self.admin_info.password_encrypted()):
                print("You have successfully logged in as the administrator.")
                self.admin_menu()
            else:
                print("Incorrect username or password")
        elif choice == 2:
            for i in range(2):
                name = input("Enter your name: ")
                for player_detail in self.players_details[1:]:
                    if name == player_detail[0]:
                        if self.login(player_detail[1], player_detail[2]):
                            print(f"{name} has successfully logged in")
                            break
                        else:
                            print("Incorrect username or password")
                            break
                else:
                    print("\nNo player found with that name\n")
            self.player_menu()
        elif choice == 3:
            exit()
        else:
            print("Invalid choice")

    def login(self, username_encrypted, password_encrypted):
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

    def admin_menu(self):
        print("\n1: Display codeword")
        print("2: Display incomplete codeword")
        print("3: Display key grid")
        print("4: Display incomplete key grid")
        print("5: Add a different word to the puzzle")
        print("6: Delete a word from the puzzle")
        print("7: Use alphabet puzzle")
        print("8: Show newly changed grids")
        menu_choice = int(input("\nChoose an option: "))
        while menu_choice not in range(1, 9):
            menu_choice = int(input("\nChoose a valid option: "))
        if menu_choice == 1:
            self.display_codeword()
        elif menu_choice == 2:
            self.display_player_codeword()
        elif menu_choice == 3:
            self.display_answer_key()
        elif menu_choice == 4:
            self.display_player_key()
        elif menu_choice == 5:
            self.add_word(codeword)
        elif menu_choice == 6:
            self.delete_word()
        elif menu_choice == 7:
            self.new_puzzle(codeword, answer_key, player_codeword, player_key)
        elif menu_choice == 8:
            for row in codeword:
                for column in row:
                    print(column, end=" ")
                print(" ")
            for row in answer_key:
                for column in row:
                    print(column, end=" ")
                print(" \n")
            for row in player_codeword:
                for column in row:
                    print(column, end=" ")
                print(" ")
            for row in player_key:
                for column in row:
                    print(column, end=" ")
                print(" \n")

    def display_codeword(self):
        for row in codeword:
            for column in row:
                print(column, end=" ")
            print(" ")
        self.admin_menu()

    def display_player_codeword(self):
        for row in player_codeword:
            for column in row:
                print(column, end=" ")
            print(" ")
        self.admin_menu()

    def display_answer_key(self):
        for row in answer_key:
            for column in row:
                print(column, end=" ")
            print(" \n")
        self.admin_menu()

    def display_player_key(self):
        for row in player_key:
            for column in row:
                print(column, end=" ")
            print(" \n")
        self.admin_menu()

    def add_word(self, codeword):
        """
        This function adds a new word to the codeword
        """
        new_word = input("Enter what word you want to add to the codeword: ")
        row_location = int(input("What row do you want to put this word?: "))
        col_location = int(input("What column do you want to put this row?: "))
        direction = input("What direction do you want this word the go in: "
                          "1: left to right"
                          "2: top to bottom: (enter 1 or 2): ")
        if codeword[row_location - 1][col_location - 1] == "#":
            if direction == 1:
                for i, letter in enumerate(new_word.upper()):
                    codeword[row_location - 1][col_location - 1 + i] = letter
            elif direction == 2:
                for i, letter in enumerate(new_word.upper()):
                    codeword[row_location - 1 + i][col_location - 1] = letter
            else:
                print("Please choose option 1 or 2: ")
            self.add_word(codeword)
        else:
            print("\nThere's already a word in this location\n")
        self.admin_menu()

    def delete_word(self):
        """
        This function will delete a word from the codeword.
        """
        print("\nThe words in the codeword are: adidas, puma, skechers, nike and reebok\n")
        word = input("Which word do you want to delete: ")

        if word.lower() == "adidas":
            codeword[0][1], codeword[0][2], codeword[0][3], codeword[0][4], codeword[0][5], codeword[0][
                6] = "#", "#", "#", "#", "#", "#"
        elif word.lower() == "puma":
            codeword[1][0], codeword[2][0], codeword[3][0], codeword[4][0] = "#", "#", "#", "#"
        elif word.lower() == "skechers":
            codeword[0][6], codeword[1][6], codeword[2][6], codeword[3][6], codeword[4][6], codeword[5][6], codeword[6][
                6], codeword[7][6] = "#", "#", "#", "#", "#", "#", "#", "#"
        elif word.lower() == "nike":
            codeword[4][8], codeword[5][8], codeword[6][8], codeword[7][8] = "#", "#", "#", "#"
        elif word.lower() == "reebok":
            codeword[8][0], codeword[8][1], codeword[8][2], codeword[8][3], codeword[8][4], codeword[8][
                5] = "#", "#", "#", "#", "#", "#"
        else:
            print("This word is not in the codeword\n")

        self.admin_menu()

    def new_puzzle(self, codeword, answer_key, player_codeword, player_key):
        codeword = [
            # Random 7 words - crossword contains all 26 letter of the alphabet
            # words = abducting, squawkers, blackjack, conjugate, jackknife, equinoxes, whizzbang
            ["A", "B", "D", "U", "C", "T", "I", "N", "G"],
            ["S", "Q", "U", "A", "W", "K", "E", "R", "S"],
            ["B", "L", "A", "C", "K", "J", "A", "C", "K"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["C", "O", "N", "J", "U", "G", "A", "T", "E"],
            ["J", "A", "C", "K", "K", "N", "I", "F", "E"],
            ["E", "Q", "U", "I", "N", "O", "X", "E", "S"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["W", "H", "I", "Z", "Z", "B", "A", "N", "G"]
        ]

        answer_key = [
            # contains all letters in alphabet
            ["5", "A"], ["9", "B"], ["12", "C"], ["15", "D"], ["21", "E"], ["26", "F"], ["19", "G"], ["14", "H"],
            ["6", "I"],
            ["13", "J"], ["23", "K"], ["8", "L"], ["17", "M"], ["3", "N"], ["11", "O"], ["4", "P"], ["22", "Q"],
            ["18", "R"], ["1", "S"], ["24", "T"], ["10", "U"], ["25", "V"], ["16", "W"], ["2", "X"], ["20", "Y"],
            ["7", "Z"],
        ]

        player_codeword = [
            # words = abducting, squawkers, blackjack, conjugate, jackknife, equinoxes, whizzbang
            ["5", "B", "D", "U", "12", "24", "6", " 3", "19"],
            ["S", "Q", "U", "5", " W", "23", "21", "18", "S"],
            ["B", "L", "5", "12", "23", "J", "5", "12", "23"],
            ["#", "#", "#", "#", " #", " #", "#", " #", " #"],
            ["12", "O", "3", "J", "U", "19", "5", "24", "21"],
            ["J", "5", "12", "K", "23", "3", "6", " F", "21"],
            ["21", "Q", "U", "6", "3", " O", "2", " E", " S"],
            ["#", " #", "#", "#", "#", " #", "#", " #", " #"],
            ["W", " H", "6", "Z", "7", " B", "5", " 3", "19"]
        ]

        player_key = [
            # contains all letters in alphabet
            ["_", "A"], ["9", "B"], ["_", "C"], ["15", "D"], ["_", "E"], ["26", "F"], ["_", "G"], ["14", "H"],
            ["_", "I"],
            ["13", "J"], ["_", "K"], ["8", "L"], ["_", "M"], ["3", "N"], ["_", "O"], ["4", "P"], ["_", "Q"],
            ["18", "R"], ["_", "S"], ["24", "T"], ["_", "U"], ["25", "V"], ["_", "W"], ["2", "X"], ["_", "Y"],
            ["_", "Z"],
        ]
        print(f"\nHere is the new codeword that uses all of the letters in the alphabet: ")

        for row in codeword:
            for column in row:
                print(column, end=" ")
            print(" ")

        self.admin_menu()

    def player_menu(self):
        print("1: Play the Game")
        print("2: Display the statistics")
        choice = int(input("Choose an option: "))
        if choice == 1:
            self.health1 = self.player1.health_value
            self.health2 = self.player2.health_value
            self.game_rules()
        elif choice == 2:
            self.game_statistics()

    def game_rules(self):
        print("\nWelcome to Codeword Games!")
        print("\nHere are the rules:")
        print("1. You must guess the letters in the codeword.")
        print("2. You have 5 chances to guess correctly.")
        print("3. For each incorrect guess, you will lose 2 health values.")
        print("4. If you lose all of your health values, the game is over.")
        print("5. The first player to guess the entire codeword wins the game.")
        print("\nLet's begin!")
        print("\nHere is the Codeword:\n")
        for word in player_codeword:
            for column in word:
                print(column, end=" ")
            print(" ")
        print("\nHere is the Key:\n")
        for key in player_key:
            for keys in key:
                print(keys, end=" ")
            print(" ")
        self.play_game()

    def play_game(self):

        good_remarks = ["Excellent!!", "Well Done!", "You're on fire!!", "Now THAT was impressive!", "Bravo",
                        "Exceptional", "IMPRESSIVE", "Keep it up!"]

        bad_comments = ["Better luck next time", "Nice Try", "You'll get her next time ;)", "Your throwing it away!!"
                        "You're on the right track, but not there yet", "Wrong answer"]

        self.correct_guesses_p1 = 0
        self.correct_guesses_p2 = 0
        self.incorrect_guesses_p1 = 0
        self.incorrect_guesses_p2 = 0
        player_num_flag = False

        while self.correct_guesses_p1 < 15 and self.correct_guesses_p2 < 15 and self.health1 > 2 and self.health2 > 2:
            player_name = ""

            player1_answer = input("Player 1, do you want to continue playing? (y/n): ")
            player2_answer = input("Player 2, do you want to continue playing? (y/n): \n")
            if player1_answer.lower() == "y" and player2_answer.lower() == "y":

                if player_num_flag == False:
                    player_name = self.player1.name
                    print(f"""Player 1 ({player_name})....
                    YOUR UP!....
                        """)
                elif player_num_flag == True:
                    player_name = self.player2.name
                    print(f"""Player 2 ({player_name})....
                    IT'S YOUR TURN!....
                        """)
                for player in self.players_details[1:]:
                    cell = input("Enter the number you want to guess for: ")
                    while int(cell) not in range(1, 16):
                        print(cell)
                    letter_guess = input("Enter the letter that you want to guess for: ")
                    codeword_matched_cells = []
                    key_matched_cells = []
                    for row in range(len(player_codeword)):
                        for col in range(len(player_codeword[row])):
                            if str(cell) == str(player_codeword[row][col]):
                                player_codeword[row][col] = letter_guess.upper()
                                codeword_matched_cells.append((row, col))
                                for word in player_codeword:
                                    for column in word:
                                        print(column, end=" ")
                                    print(" ")
                                for i in range(len(player_key)):
                                    for x in range(len(player_key[i])):
                                        if str(cell) == str(player_key[i][x]):
                                            player_key[i][x + 1] = letter_guess.upper()
                                            key_matched_cells.append((i, x))
                                            for key in player_key:
                                                for keys in key:
                                                    print(keys, end=" ")
                                                print(" ")

                    for key in player_key:
                        for keys in key:
                            print(keys, end=" ")
                        print(" ")

                    if codeword[codeword_matched_cells[0][0]][codeword_matched_cells[0][1]] == letter_guess.upper():

                        if player_num_flag == False:
                            self.correct_guesses_p1 += 1
                            self.health1 += 2
                            print(f"""\n{random.choice(good_remarks)} Player 1 ({player_name})!!""")
                        else:
                            self.correct_guesses_p2 += 1
                            self.health2 += 2
                            print(f"""\n{random.choice(good_remarks)} Player 2 ({player_name})!!""")
                        if codeword == player_codeword:
                            print(f"{player_name}, has successfully won!!")
                            self.game_statistics()
                            exit()
                    else:
                        print(f"{player_name}, your guess was incorrect therefore you lose 2 health points")
                        for row, col in codeword_matched_cells:
                            player_codeword[row][col] = str(cell)
                        for i, x in key_matched_cells:
                            player_key[i][x + 1] = str(cell)
                        if player_num_flag == False:
                            self.incorrect_guesses_p1 += 1
                            self.health1 -= 2
                            player_num_flag = True
                            print(f"""{random.choice(bad_comments)}...
                            Time to switch it up!\n""")
                        else:
                            self.incorrect_guesses_p2 += 1
                            self.health2 -= 2
                            player_num_flag = False
                            print(f"""{random.choice(bad_comments)}...
                            Need to try harder!\n""")

            else:
                print("\nExiting game")
                self.game_statistics()

        else:
            print("\nNot enough lives to play game")
            self.player_menu()

    def game_statistics(self):
        file_name = 'game_stats.csv'
        file = open(file_name, 'w')

        file.write('Name,No: of correct guesses,No: of incorrect guesses,Current health value\n')
        file.write(
            f'{self.player1.name},{self.correct_guesses_p1},{self.incorrect_guesses_p1},{self.health1}\n')
        file.write(
            f'{self.player2.name},{self.correct_guesses_p2},{self.incorrect_guesses_p2},{self.health2}\n')

        file.close()

        df = pd.read_csv(file_name)
        print(f"\n{df}\n")
        self.player_menu()


if __name__ == '__main__':
    game = CodeWordGame()
    game.start_program()
