# This is a function that can be used to remove a list from a text file.
# For example, removing inactive ip addresses from the list of allowed ip addresses
# To use this function, the first parameter is the name of the file, and the second parameter is the list of elements to be removed.
# The function also displays the original file and the updated file. This  can be amended based on the requirements of the user.

def update_file(import_file, remove_list):
    # Open and read the file

    with open(import_file, "r") as file:
        text = file.read()

    # Print original to check if the file is opened properly and compare against updated file (Optional)
    print(f"Original file: \n{text}")

    # Split the string into a list using .split()

    text = text.split()

    # Print text to check if the file is string is split into a list (Optional)
    # print(text)

    # iterate through the list to check for any blocked addresses which maybe allowed

    for ip in text:

        # A conditional statement to check if the ip address matches one in the remove_list
        if ip in remove_list:
            text.remove(ip)

    # The list then needs to be converted back to a string using .join() with "\n" as an argument to make each entry on a new line

    text = "\n".join(text)

    # Write the string onto the original file

    with open(import_file, "w") as file:
        text = file.write(text)

    # Open the file again to read and display the contents

    with open(import_file, "r") as file:
        text = file.read()

    print(f"Updated file: \n{text}")
    return

