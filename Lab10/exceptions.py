def handle_exceptions():
    try:
        # Attemptin9559g to divide by zero
        result = 10 / 0
        print("Result of division:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    try:
        # Attempting to access an undefined variable
        print("undefined_variable")

    except NameError:
        print("Error: Variable is not defined.")

    try:
        # Attempting to open a file that doesn't exist
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    try:
        # Attempting to access an index that doesn't exist
        lst = [1, 2, 3]
        print(lst[5])

    except IndexError:
        print("Error: List index out of range.")

    try:
        # Attempting to convert an invalid string to an integer
        number = int("not_a_number")
        print("Converted number:", number)

    except ValueError:
        print("Error: Invalid literal for int() with base 10.")

    finally:
        print("Execution completed.")

# Call the function to handle exceptions
handle_exceptions()
