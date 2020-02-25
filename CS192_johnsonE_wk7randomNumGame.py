import random

def mainMenu():
    print('\n{:_^40}'.format("MAIN MENU"))
    print("1. Object of the Game")
    print("2. How to Play")
    print("3. Play GUESS THAT NUMBER!")
    print('9. Quit')
    selection = input('Selection > ')
    return selection

def objectOfTheGame():
    print('\n{:_^40}'.format('Object of the Game'))
    print('The object of the game is to guess a')
    print('number from 1 and 100, including')
    print('both 1 and 100.  You get as many guesses')
    print('as you need. Many have tried and failed.')
    print('Well, not really, but you could be the')
    print('first. No pressure.')

def howToPlay():
    print('\n{:_^40}'.format("How to Play"))
    print('Simply enter your guess at the prompt.')
    print('After your guess, you\'ll be given a')
    print('hint to help with your next guess...')
    print('(unless you\'re extremely lucky).')

def guessThatNumber():
    print('\n{:_^40}'.format("GUESS THAT NUMBER!"))
    print('\nI\'m thinking of a number somewhere')
    print('from 1 to 100.  See if you can guess')
    print('what it is in as few guesses as')
    print('possible...')

    theNumber = random.randint(1, 100)
    guess = int(input("Make your best guess: "))
    guesses = 1
    while guess != theNumber:
        if theNumber > guess:
            print('Hint: You guessed too low,')
            guesses += 1
            guess = int(input('try again: '))
        elif theNumber < guess:
            print('Hint: You guessed too high,')
            guesses += 1
            guess = int(input('try again: '))
    if guesses == 1:
        print('\nYou obviously cheated. The')
        print('official GUESS THAT NUMBER')
        print('committee will be investigating')
        print('this to determine if you are')
        print('eating performance enhancing brain')
        print('food or something. Nobody\'s that')
        print('lucky.')
    else:
        print('\nWell it took you', guesses, 'guesses, and ')
        print('granted I\'m a computer, but I could do')
        print('better than that. Try again?')


# The main program loop:
print("\nWelcome to GUESS THAT NUMBER!")

selection = mainMenu()
while selection != '9':
    if selection == '1':
        objectOfTheGame()
    elif selection == '2':
        howToPlay()
    elif selection == '3':
        guessThatNumber()
    else:
        print('Whoops, that\'s not a menu option.')
        print('Please try again...')
    selection = mainMenu()

print("Exiting GUESS THAT NUMBER...")
print("Goodbye.")




