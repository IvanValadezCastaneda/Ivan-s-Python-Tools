import random

# Set the number of entries
num_entries = 7
Num_against = 7

# Create a list of entries
entries = []
for i in range(1, num_entries+1):
    # Get the value of the entry from the user
    entry_value = input("Enter the value for entry {}: ".format(i))
    # Add the entry to the list
    entries.append(entry_value)


contry_entries = []
for i in range(1, Num_against+1):
    # Get the value of the entry from the user
    entry_value_against = input("Enter the value for entry aginst {}: ".format(i))
    # Add the entry to the list
    contry_entries.append(entry_value_against)

# Shuffle the entries
random.shuffle(entries)
random.shuffle(contry_entries)

# Create a new array to hold the mixed arrays
mixed_arrays = []

# Mix the arrays together intercalated between both arrays
for i in range(len(entries)):
    mixed_arrays.append(entries[i])
    mixed_arrays.append(contry_entries[i])

# Print the mixed arrays
print(mixed_arrays)


