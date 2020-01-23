# BMI index calculator 
# An exercise for learning modularization

# Initialize a student object as a dict...

student = {'name': '', 
           'height': 0, 
           'weight': 0, 
           'BMI': 0
           }

"""Four function defs for getting height, weight, calculating
    BMI, and displaying the student's BMI profile: """

def getHeight(student):
    print('\n')
    student['height'] = int(input('Please enter student\'s height in inches: '))
    return student

def getWeight(student):
    print('\n')
    student['weight'] = int(input('Please enter student\'s weight in pounds: '))
    return student

def calcBMI(student):
    student['BMI'] = (student['weight'] * 703) / (student['height'] ** 2)
    return student

def displayStudentProfile(student):
    print('\n')
    print(student['name'] + "'s BMI profile: ")
    print('\n')
    print('------------------')
    print('\n')
    print('Height:', student['height'], end=""), print('"')
    print('\n')
    print('Weight:', student['weight'], 'lbs.')
    print('\n')
    print('BMI Index:', '{:.1f}'.format(student['BMI']))
    return

# Begin with welcome message:

print('\n')
print('Welcome to the BMI Index Calculator.')

# Value entered for student name will be used as sentinel for main program loop

print('\n')
student['name'] = input('Please begin by entering the student\'s name, or 0 to quit: ')

while student['name'] != '0':
    getHeight(student)
    getWeight(student)
    calcBMI(student)
    displayStudentProfile(student)
    for value in student:   #...to clear memory in case null student
        value = 0           #   info is entered next iteration...
    print('\n')
    student['name'] = input('Enter next student\'s name or 0 to quit: ')

print('\n')
print('Exiting program...')
    
