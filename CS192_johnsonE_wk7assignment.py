import math

def mainMenu():
    print('\n{:_^40}'.format("MAIN MENU"))
    print("1. Object of the Game")
    print("2. How to Play")
    print("3. Player stats")
    print("4. Grab your club and WHACK-A-MOLE!")
    print('9. Quit')
    selection = input('Selection > ')
    return selection

def objectOfTheGame():
    print('\n{:_^40}'.format('Object of the Game'))
    print('The game begins with 16 imaginary holes')
    print('aligned in a 4 x 4 square, with a mole')
    print('that pops up out of one of the holes')
    print('every time you swing your imaginary')
    print('club at one of the holes.  The object')
    print('of the game is to whack the mole by')
    print('picking the correct hole.  The trouble')
    print('is, the mole can move by one hole\'s')
    print('distance every time you miss in any')
    print('direction - up, down, left, right, even')
    print('diagonally, or just pop up from the same')
    print('hole again.')

def howToPlay():
    print('\n{:_^40}'.format("How to Play"))
    print("There is a 4 x 4 grid of holes.")
    print("The horizontal rows are lettered")
    print("a through d, and the vertical")
    print("columns are numbered 1 through 4.")
    print("At the prompt, indicate the hole")
    print("that you want to club as the letter")
    print("then the number, such as \"b3\" or")
    print("\"c4\", etc, and press enter to")
    print("swing your club.")

# The main program loop:
print("\nWelcome to WHACK-A-MOLE!")

selection = mainMenu()
while selection != '9':
    if selection == '1':
        objectOfTheGame()
    elif selection == '2':
        howToPlay()
    elif selection == '3':
        print('selected 3')
    elif selection == '4':
        print('selected 4')
    else:
        print('Whoops, that\'s not a menu option.')
        print('Please try again...')
    selection = mainMenu()

print("Exiting WHACK-A-MOLE...")
print("Goodbye.")




