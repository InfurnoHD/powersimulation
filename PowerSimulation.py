# This program calculates a value based on user input temperature.
def main():
    # Assigning initial values to variables.
    a = 4736.09815
    b = -82.55861
    num = 99

    # A loop that continues until the temperature entered is within the valid range of -10 to 20 degrees Celsius.
    while num > 20 or num < -10:
        # Asking the user to input temperature.
        tmp = input('Enter temperature:')

        # Replacing any commas with periods in the user's input.
        tmp = tmp.replace(',', '.')

        # Checking if the input is a numeric value or a valid negative/positive float value.
        if tmp.isnumeric() or \
                (tmp[0] == '-' and tmp[1:].isdigit()) or \
                ('.' in tmp and tmp.replace('.', '', 1).isdigit()) or \
                (tmp[0] == '-' and '.' in tmp and tmp[1:].replace('.', '', 1).isdigit()):
            num = float(tmp)
            if num > 20 or num < -10:
                print('It is only valid for temperature between -10 and 20 degrees Celsius')
        else:
            # If the user input is not numeric, an error message will be displayed.
            print('Please enter an integer')

    return a + b * num


if __name__ == '__main__':
    # Calling the main() function and printing the result.
    print(main())