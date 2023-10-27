#defining function to remove white spaces and replace with underscore
def noWhiteSpace(text):
    print(text.title().replace(' ','_'))

#Getting string from user
text = input('What text do you wanna remove the white spaces from')
#calling function that has the user text as a parameter
output = noWhiteSpace(text)

#printing result
print(output)



####################################
####################################
####################################



# This function adds two numbers
def add(a, b):
    return a + b

# This function subtracts two numbers
def sub(a, b):
    return a - b

# This function divides two numbers
def div(a, b):
    return a / b

# This function multiplies two numbers
def mul(a, b):
    return a * b

# Get the first number from the user
x = float(input('Enter the first number: '))

# Get the second number from the user
y = float(input('Enter the second number: '))


# Ask the user which operation to perform
operator = input('Would you like to add, subtract, multiply, or divide? ')

# Perform the selected operation and round the result to 2 decimal places
# if operator == 'add':
#    result = round(add(x, y))
# elif operator == 'subtract':
#    result = round(sub(x, y))
# elif operator == 'multiply':
#    result = round(mul(x, y))
# elif operator == 'divide':
#    result = round(div(x, y))
# else:
#     result = 'Invalid operator. Please enter a valid operator.'

match operator:
    case 'add':
      result = round(add(x, y))
    case 'subtract':
        result = round(sub(x, y))
    case 'multiply':
        result = round(mul(x, y))
    case 'divide':
        result = round(div(x, y))
    case _:
        result = 'Invalid operator. Please enter a valid operator.'


# Print the result
print(result)
