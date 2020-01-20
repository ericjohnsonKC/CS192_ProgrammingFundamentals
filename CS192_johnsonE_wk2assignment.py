# Professor Lusby, I noticed the example output only had pay info
# displayed to one decimal place.  I'm duplicating that here, but
# I want to note that I would have used '{:.2f}'.format(payInfo)
# if you required two decimals.

#start with function solely for calculating overtime pay
def calc_overtime_pay(hours_worked, pay_rate,):
    if hours_worked <= 40:
        return 0
    else:
        return (hours_worked - 40) * (1.5 * pay_rate)

#a function for calculating gross pay, including overtime
def calc_pay(overtime_pay, hours_worked, pay_rate):
    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate
    else:
        gross_pay = (40 * pay_rate) + overtime_pay
    return gross_pay

#this function will display name, gross pay, and overtime pay as required
def display_pay(name, overtime_pay, gross_pay):
    print('Employee Name: ' + name)
    if overtime_pay == 0:
        print('Gross Pay: ' + '{:.1f}'.format(gross_pay))
    else:
        print('Gross Pay: ' + '{:.1f}'.format(gross_pay))
        print('(overtime pay: ' + '{:.1f}'.format(overtime_pay))
    return

# Initialize a time card that will be used for each employee
time_card = {'Name': 0, 'Hours_worked': 0, 'Pay_rate': 0}
#-----------------------------------------------------------------
# Begin with the specified welcome message
print('ABC Inc., Gross Pay Calculator!')

# Initial prompt with exit option
time_card['Name'] = input('Enter employee\'s name or 0 to quit: ')

while time_card['Name'] != '0':
    time_card['Hours_worked'] = float(input('Enter hours worked: '))
    time_card['Pay_rate'] = float(input('Enter employee\'s pay rate: '))
    overtime_pay = calc_overtime_pay(time_card['Hours_worked'], time_card['Pay_rate'])
    gross_pay = calc_pay(overtime_pay, time_card['Hours_worked'], time_card['Pay_rate'])
    display_pay(time_card['Name'], overtime_pay, gross_pay)
    time_card = {'Name': 0, 'Hours_worked': 0, 'Pay_rate': 0}  # clear memory for security
    time_card['Name'] = input('Enter employee\'s name or 0 to quit: ')


