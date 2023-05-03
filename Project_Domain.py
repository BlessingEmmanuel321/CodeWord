# 2 - Project Domain
# This is the final codeword
import hashlib
import random

# login_as is now create_login

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

# This is the codeword shown to the player/s
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

# Final answer key - not displayed to user
answer_key = [
    [1, "D"], [2, "I"], [3, "A"], [4, "S"], [5, "P"], [6, "K"], [7, "U"], [8, "E"], [9, "M"], [10, "C"],
    [11, "H"], [12, "N"], [13, "R"], [14, "B"], [15, "O"]
]

# This is the key that the player/s answers will be entered into
player_key = [
    [1, "D"], [2, "_"], [3, "A"], [4, "_"], [5, "_"], [6, "K"], [7, "U"], [8, "_"], [9, "_"], [10, "_"],
    [11, "H"], [12, "_"], [13, "R"], [14, "_"], [15, "O"]
]
# Used for creating randomised usernames and passwords
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
random_chars = "!?%$"


# username and password creator
def username_password():
    name123 = input("Enter your name?: ")
    name_lst = list(name123)
    popped = name_lst.pop()
    username123 = name_lst[0] + popped + random.choice(name_lst) + random.choice(numbers)
    password123 = random.choice(alphabet) + random.choice(numbers) + random.choice(alphabet) + random.choice(
        random_chars) \
                  + random.choice(alphabet) + random.choice(numbers)
    return name123, hashlib.sha256(username123.encode()).hexdigest(), hashlib.sha256(password123.encode()).hexdigest()


class PersonalDetails:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.health_value = 5


# creating administrator's login info
admin_name, admin_username, admin_password = username_password()
admin_info = PersonalDetails(admin_name, admin_username, admin_password)

# Creates logins for player 1 and player 2
login_as = input("Lets create your login details: ")
name1, username1, password1 = username_password()
player1 = PersonalDetails(name1, username1, password1)

name2, username2, password2 = username_password()
player2 = PersonalDetails(name2, username2, password2)
# Creating player 1 and player 2's details
print(f"\nPlayer one's login info:\nUsername: {player1.username}\nPassword: {player1.password}\n")
print(f"Player two's login info:\nUsername: {player2.username}\nPassword: {player2.password}")


# Encrypts password and username and gives user 3 tries to input correct usernames/passwords
def login(username_encrypted, password_encrypted):
    logged_in = False
    count = 3
    while (not logged_in) and (count > 0):
        username = input("Enter your username: ")
        if username_encrypted == hashlib.sha256(username.encode()).hexdigest():
            password = input("Enter your password: ")
            if password_encrypted == hashlib.sha256(password.encode()).hexdigest():
                logged_in = True
                print(logged_in)
        count -= 1

    return logged_in


# for loop that appends the admins and all the players details into a list
players_details = [[admin_info.name, admin_info.username, admin_info.password]]
for i in range(2):
    name, username, password = username_password()
    player = PersonalDetails(name, username, password)
    players_details.append([player.name, player.username, player.password, player.health_value])

# write a function that creates a file and writes the players stats in it. The function then returns the file using pandas
''' import pandas as pd

def game_statistics(player1, player2):
    # Define the file name and open it with 'w' attribute
    file_name = 'game_stats.csv'
    file = open(file_name, 'w')
    
    # Write the column titles and player stats to the file
    file.write('Name,No: of correct guesses,No: of incorrect guesses,Current health value\n')
    file.write(f'{player1.name},{player1.correct_guesses},{player1.incorrect_guesses},{player1.health_value}\n')
    file.write(f'{player2.name},{player2.correct_guesses},{player2.incorrect_guesses},{player2.health_value}\n')
    
    # Close the file
    file.close()
    
    # Read the CSV file into a Pandas dataframe and return it
    df = pd.read_csv(file_name)
    return df'''

'''def admin_username_password(name):
    name_lst = list(name)
    popped = name_lst.pop()
    username = name_lst[0] + popped + random.choice(name_lst) + random.choice(numbers)
    password = random.choice(alphabet) + random.choice(numbers) + random.choice(alphabet) + random.choice(
        random_chars) + random.choice(alphabet) + random.choice(numbers)
    return username, password'''

def delete_word():
    """
    This function will delete a word from the codeword.
    """
    word = input("Which word do you want to delete: ")
    while word.lower() != "adidas" or word.lower() != "puma" or word.lower() != "skechers" or word.lower() != "nike" or word.lower() != "reebok":
        word = input("Enter a word that's in the codeword")
    if word.lower() == "adidas":
        codeword[0][1], codeword[0][2], codeword[0][3], codeword[0][4], codeword[0][5], codeword[0][6] = "#", "#", "#", "#", "#", "#"
    elif word.lower() == "puma":
        codeword[1][0], codeword[2][0], codeword[3][0], codeword[4][0] = "#", "#", "#", "#"
    elif word.lower() == "skechers":
        codeword[0][6], codeword[1][6], codeword[2][6], codeword[3][6], codeword[4][6], codeword[5][6], codeword[6][6], codeword[7][6] = "#", "#", "#", "#", "#", "#", "#", "#"
    elif word.lower() == "nike":
        codeword[4][8], codeword[5][8], codeword[6][8], codeword[7][8] = "#", "#", "#", "#"
    elif word.lower() == "reebok":
        codeword[8][0], codeword[8][1], codeword[8][2], codeword[8][3], codeword[8][4], codeword[8][5] = "#", "#", "#", "#", "#", "#"


def new_puzzle(codeword, player_codeword, answer_key, player_key):
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
        ["5", "A"], ["9", "B"], ["12", "C"], ["15", "D"], ["21", "E"], ["26", "F"], ["19", "G"], ["14", "H"], ["6", "I"],
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
        ["5", "A"], ["9", "B"], ["12", "C"], ["15", "D"], ["21", "E"], ["26", "F"], ["19", "G"], ["14", "H"], ["6", "I"],
        ["13", "J"], ["23", "K"], ["8", "L"], ["17", "M"], ["3", "N"], ["11", "O"], ["4", "P"], ["22", "Q"],
        ["18", "R"], ["1", "S"], ["24", "T"], ["10", "U"], ["25", "V"], ["16", "W"], ["2", "X"], ["20", "Y"],
        ["7", "Z"],
    ]

def add_word():
    """
    This function adds a new word to the codeword
    """
    new_word = input("Enter what word you want to add to the codeword: ")
    new_word = list(new_word.upper())
    row_location = int(input("What row do you want to put this word?: "))
    col_location = int(input("What column do you want to put this row?: "))
    for row in range(len(codeword)):
        for col in range(len(codeword[row])):
            if codeword[row][col] == codeword[row_location-1][col_location-1]:
                if codeword[row][col] == "#":
                    codeword[row][col] == new_word[0]
                    print(codeword)
                    self.admin_menu
                else:
                    print("There's already a word in this location")
                    self.admin_menu