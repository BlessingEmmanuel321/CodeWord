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
    
class CodeWordGame:
    def __init__(self) -> None:
        


        self.admin_name = "Blessing"
        self.admin_username, self.admin_password = username_password(self.admin_name)
        self.admin_info = PersonalDetails(self.admin_name, self.admin_username, self.admin_password)

        print("Lets create your login details.")
        self.name1 = input("\nEnter player one's name: ")
        self.username1, self.password1 = username_password(self.name1)
        self.player1 = PersonalDetails(self.name1, self.username1, self.password1)

        self.name2 = input("Enter player two's name: ")
        self.username2, self.password2 = username_password(self.name2)
        self.player2 = PersonalDetails(self.name2, self.username2, self.password2)

        print(f"\n{self.player1.name}'s login info:\nUsername: {self.player1.username}\nPassword: {self.player1.password}\n")
        print(f"{self.player2.name}'s login info:\nUsername: {self.player2.username}\nPassword: {self.player2.password}")

        self.players_details = [[self.admin_info.name, self.admin_info.username_encrypted(), self.admin_info.password_encrypted()],
                        [self.player1.name, self.player1.username_encrypted(), self.player1.password_encrypted(), self.player1.health_value],
                        [self.player2.name, self.player2.username_encrypted(), self.player2.password_encrypted(), self.player2.health_value]]


    def start_program(self):
        print("\n\nMain Menu")
        print("\n1: Administrator")
        print("2: Player")
        print("3: Exit the system")
        choice = int(input("\nChoose an option: "))
        if choice == 1:
            if self.login(self.admin_info.username_encrypted(), self.admin_info.password_encrypted()):
                print("You have successfully logged in as the administrator.")
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
            self.display_codeword()
        elif menu_choice == 2:
            self.display_player_codeword()
        elif menu_choice == 3:
            self.display_answer_key()
        elif menu_choice == 4:
            self.display_player_key()


    def display_codeword(self):
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


    def player_menu(self):
        print("1: Play the Game")
        print("2: Display the statistics")
        choice = int(input("Choose an option: "))
        if choice == 1:
            self.health1 = self.player1.health_value
            self.health2 = self.player2.health_value
            self.player_check()


    def player_check(self):
        player1_answer = input("Player 1, do you want to continue playing? (y/n): ")
        player2_answer = input("Player 2, do you want to continue playing? (y/n): ")

        if player1_answer.lower() == 'y' and player2_answer.lower() == 'y':
            if self.health1 >= 2 and self.health2 >= 2:
                print("Both players can continue playing.")
                self.game_rules()
            else:
                print("You don't have enough lives.")
        else:
            print("Game ended.")


    def game_rules(self):
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
        self.play_game()


    def play_game(self):

        self.correct_guesses_p1 = 0
        self.correct_guesses_p2 = 0
        self.incorrect_guesses_p1 = 0
        self.incorrect_guesses_p2 = 0
        player_num_flag  = False
        while self.correct_guesses_p1 < 15 and self.correct_guesses_p2 < 15 and self.health1> 2 and self.health2 > 2:
            # player_num = int(input("Enter your player number (1 or 2): "))
            player_name = ""
            
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
                matched_cells = []
                for row in range(len(player_codeword)):
                    for col in range(len(player_codeword[row])):
                        if str(cell) == str(player_codeword[row][col]):
                            player_codeword[row][col] = letter_guess
                            matched_cells.append((row, col))
                for x in player_codeword:
                    for y in x:
                        print(y, end=" ")
                    print(" ")
                
                if codeword[matched_cells[0][0]][matched_cells[0][1]] == letter_guess: 
                # if letter_guess in codeword:
                    # print("Correct answer!")
                    if player_num_flag == False:
                        self.correct_guesses_p1 += 1
                        self.health1 += 2
                        print(f""" Well done Player 1 ({player_name} !!""")
                    else:
                        self.correct_guesses_p2 += 1
                        self.health2 += 2
                        print(f""" Excellent Player 2 ({player_name} !!""")
                    if codeword == player_codeword:
                        print(f"{player_name}, has successfully won")
                else:
                    print(f"{player_name}, your guess was incorrect therefore you lose 2 health points")
                    for row, col in matched_cells:
                        player_codeword[row][col] = str(cell)
                    if player_num_flag == False:
                        self.incorrect_guesses_p1 += 1
                        self.health1 -= 2
                        player_num_flag = True
                        print("""Better luck next time...
                        Time to switch it up!""")
                    else:
                        self.incorrect_guesses_p2 += 1
                        self.health2 -= 2
                        player_num_flag = False
                        print("""Your throwing it away...
                        Need to try harder!""")


                    # if player_num == 1 and player[0] == self.player1.name:
                    #     player_name = self.player1.name
                    #     # health1 = player1.health_value
                    #     self.health1 -= (incorrect_guesses*2)
                    #     self.health1 += (correct_guesses*2)
                    #     break
                    # elif player_num == 2 and player[0] == self.player2.name:
                    #     player_name = self.player2.name
                    #     # health2 = player2.health_value
                    #     self.health2 -= (incorrect_guesses*2)
                    #     self.health2 += (correct_guesses*2)
                    #     break


if __name__ == '__main__':
    game = CodeWordGame()
    game.start_program()

    
