# Create class of Player
class Player:
    def __init__(self, name, phone, jerseyNumber):
        self.name = name
        self.phone = phone
        self.jerseyNumber = jerseyNumber

# Create a dict to hold all players on roster
roster = {}

# Functions for each menu option:
def saveData(roster):
    fileName = input("Filename to save: ")
    outFile = open('./'+fileName, 'wt')
    print("Saving data...")
    for player in roster.keys():
        name = roster[player].name
        phone = roster[player].phone
        jerseyNumber = roster[player].jerseyNumber
        outFile.write(name+","+phone+","+jerseyNumber+"\n")
    outFile.close()
    print("Data saved.")
    return roster

def loadData(roster):
    fileName = input("Filename to load: ")
    inFile = open('./'+fileName, 'rt')
    print("Loading data...")
    while True:
        inLine = inFile.readline()
        if not inLine:
            break
        inLine = inLine[:-1]
        name, phone, jerseyNumber = inLine.split(',')
        roster[name] = Player(name, phone, jerseyNumber)
    inFile.close()
    print("Data Loaded Successfully.")
    return roster

def displayTeamRoster(roster):
    if len(roster) > 0:
        for player in roster:
            print('\n', 'Name: '+ roster[player].name)
            print('\n', 'Phone: '+roster[player].phone)
            print('\n', 'Jersey Number: '+roster[player].jerseyNumber)
    else:
        print("No current members in memory.")
    return roster

def addMember(roster):
    print('\n')
    name = input("Enter new member's name: ")
    print('\n')
    phone = input("Contact phone number: ")
    print('\n')
    jerseyNumber = input("Jersey number: ")
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
    print('\n5. Save Data.')
    print('\n6. Load Data.')
    print('\n9. Exit Program.')
    print('\n')
    selection = input('Selection> ')
    return selection

# The main program loop:

print('\nWelcome to the Team Manager')
selection = mainMenu()
while selection != '9':
    if selection == '1':
        displayTeamRoster(roster)
    elif selection == '2':
        roster = addMember(roster)
    elif selection == '3':
        roster = removeMember(roster)
    elif selection == '4':
        roster = editMember(roster)
    elif selection == '5':
        saveData(roster)
    elif selection == '6':
        loadData(roster)
    selection = mainMenu()

print('\nExiting Program...')