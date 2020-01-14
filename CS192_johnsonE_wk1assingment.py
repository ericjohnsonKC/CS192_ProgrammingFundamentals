# Get five prices from the user
print('\n')
print("Welcome to the Express Lane!", '\n')

prices = []
adjectives = ['first', 'second', 'third', 'fourth', 'final']

for i in adjectives:
    prices.append(
        input("Enter the " + i + " price: ")
                  )
    print('\n')


# Perform calculations

# Currency values will be stored as integers of cents to avoid using floats
subtotal = 0
salesTax = 0
total = subtotal + salesTax

for i in prices:
    price = int(
        float(i) * 100
    )
    subtotal += price

# Format for printing
print('subtotal: ', '{:.2f}'.format(subtotal/100)
      )
print('\n')

# Calculate tax
taxRate = .06

salesTax = subtotal * taxRate
print('salesTax: ', '{:.2f}'.format(salesTax/100)
      )
print('\n')
print('---------------', '\n')

# Calculate total
total =  subtotal + salesTax
print(
    'total: ', '{:.2f}'.format(total/100)
)


