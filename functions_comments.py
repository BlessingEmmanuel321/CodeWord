# Functions needed

def start_program():#
    """Function that will call display and login functions. If login is unsuccessful it will exit here"""


def display_menu(): #
    """This function will display to the user the menu, whether they want to log in as an administrator, player or
    exit the system"""


def administrator_login(): #
    """This function will take in the users username and password and check if it is correct. They get 3 tries to
    insert a correct password and username"""


def player_login(player1, player2): #
    """This function will do the same as the administrator_login() function, checking for the correct login details.
    The two arguments 'player1' and 'player2' to see if both players are logged in correctly"""


def player_menu(): #
    """This function will display the players' menu, much shorter than the administrators. Menu includes playing the
    game, showing game statistics etc."""


def admin_menu(): #
    """This function, once the administrator has logged in, will display the admin menu. This includes wanting to see
    the final codeword and changing anything"""

def Player_Check(player, health_value): #
    """This function, once players state they want to play will check if they both have >=2 health value. If they both
    do then they can play the game. If not it will skip the player who does not have enough health points. If both
    don't then game doesn't play and goes back to menu"""

def Start_Game(players): #
    """This function plays the game, taking turns for each player. It will continuously loop and and call function
    Play_Game to check if the players both want to still continue playing and if they have enough health value to
    play the game"""

def stats():
    """This function will be called from the menu. It will display the stats of the game like number of incorrect and
    correct guesses by each player etc."""