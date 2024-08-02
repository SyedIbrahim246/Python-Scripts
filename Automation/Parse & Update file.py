#A script which opens a text file with all the ip addresses allowed to access the network and removes the ones that are to be blocked.
#Import the file that will be read and updated.

import_file = 'allow_list.txt'

#List of blocked ip address to remove

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

#Open and read the file

with open(import_file, "r") as file:
    text = file.read()

# Print original to check if the file is opened properly and compare against updated file (Optional)
print(f"Original file: \n{text}")

# Split the string into a list using .split()

text = text.split()

# Print text to check if the file is string is split into a list (Optional)
#print(text)

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