def handle_errors():
    try:
        # Example of ValueError
        num = int(input("Enter a number: "))
        
        # Example of IndexError
        my_list = [1, 2, 3]
        index = int(input("Enter an index to access the list: "))
        print(f"Element at index {index}: {my_list[index]}")

    except ValueError:
        print("Error: Invalid input! Please enter a valid number.")
    
    except IndexError:
        print("Error: Index out of range! Please enter a valid index.")

# Call the function
handle_errors()