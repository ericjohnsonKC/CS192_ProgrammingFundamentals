# Create class of Player
class Player():
    def __init__(self, name, phone, jerseyNumber):
        self.name = name,
        self.phone = phone,
        self.jerseyNumber = jerseyNumber

# Create a dict to hold all players on roster
roster = {}

# Functions for each menu option:
def displayTeamRoster(roster):
    for player in roster:
        print('\nName:',roster[player].name)
        print('Phone:',roster[player].phone)
        print('Jersey number:',roster[player].jerseyNumber)
    return roster

def addMember(roster):
    print('\n')
    name = input("Enter the new member's name: ")
    print('\n')
    phone = input("Enter the new member's phone number: ")
    print('\n')
    jerseyNumber = input("Enter the new member's jersey number: ")
    player = Player(name, phone, jerseyNumber)
    roster[name] = player
    return roster

def removeMember(roster):
    print('\n')
    player = input('Enter member name to be removed: ')
    del roster[player]
    return roster

def editMember(roster):
    print('\n')
    oldName = input("Enter the name of the member you want to edit: ")
    print('\n')
    newName = input("Enter the new name of the member: ")
    print('\n')
    newPhone = input("Enter the new phone number of the member: ")
    print('\n')
    newJerseyNum = input("Enter the new jersey number of the member: ")
    player = Player(newName, newPhone, newJerseyNum)
    roster[newName] = player
    del roster[oldName]
    return roster

# A function to display the main menu and retrieve user selection:
def mainMenu():
    print('\n{:=^30}'.format('Main Menu'))
    print("\n1. Display Team Roster.")
    print('\n2. Add Member.')
    print('\n3. Remove Member.')
    print('\n4. Edit Member.')
    print('\n9. Exit Program.')
    print('\n')
    selection = input('Selection> ')
    return selection

print('\nWelcome to the Team Manager')
selection = mainMenu()
while selection != '9':
    if selection == '1':
        displayTeamRoster(roster)
    if selection == '2':
        roster = addMember(roster)
    if selection == '3':
        roster = removeMember(roster)
    if selection == '4':
        roster = editMember(roster)
    selection = mainMenu()

print('\nExiting Program...')

