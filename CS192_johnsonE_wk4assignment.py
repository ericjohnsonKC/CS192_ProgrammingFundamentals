# This function displays the main menu:
def mainMenu():
    print('\n')
    print('{:=^30}'.format('Main Menu'))
    menuOptions = ['Display Team Roster.',
               'Add Member.',
               'Remove Member.',
               'Edit Member.']
    i = 1
    
    for option in menuOptions:
        print('\n')
        print(i, end = '')
        print('.', option)
        i += 1           
    print('\n')
    print('9. Exit Program.')
    print('\n')
    selection = int(input('Selection> '))
    return selection

# initialize a roster of players:
roster = []

# Below are the function definitions for each menu selection:

def printCurrentRoster(roster):
    for player in roster:
        print('\n')
        print(player)
    return roster

def addNewPlayer(roster):
    print('\n')
    roster.append(input('Enter new member\'s name: '))
    return roster

def removePlayer(roster):
    print('\n')
    roster.remove(input('Enter member name to be removed: ' ))
    return roster

def editPlayer(roster):
    print('\n')
    oldName = input('Enter the name of the member you want to edit: ')
    print('\n')
    newName = input('Enter the new name of the member: ')
    roster[roster.index(oldName)] = newName
    return roster

# Welcome message to start main program:
print('\n')
print('Welcome to the Team Manager')

# Main program loop:
selection = mainMenu()
while selection != 9 :
    if selection == 1 :
        printCurrentRoster(roster)
        selection = mainMenu()
    elif selection == 2 :
        addNewPlayer(roster)
        selection = mainMenu()
    elif selection == 3 :
        removePlayer(roster)
        selection = mainMenu()
    elif selection == 4 :
        editPlayer(roster)
        selection = mainMenu()
        
print('\n')
print('Exiting Program...')




    