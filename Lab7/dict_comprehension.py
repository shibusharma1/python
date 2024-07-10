num_entries = int(input("Enter the number of entries you want to add: "))

user_dict = {input(f"Enter key {i+1}: "): input(f"Enter value {i+1}: ") for i in range(num_entries)}

print("Dictionary after adding user input:", user_dict)
