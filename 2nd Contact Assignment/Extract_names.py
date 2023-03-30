# Open the file and read the contents
with open('my_name.txt', 'r') as file:
    full_name = file.read().replace('\n', '')

# Split the full name into its components
name_list = full_name.split()

# Determine the number of name components
name_len = len(name_list)

# Extract the first name
first_name = name_list[0]

# Extract the last name
last_name = name_list[-1]

# Extract the middle name (if applicable)
if name_len == 3:
    middle_name = name_list[1]
else:
    middle_name = None

# Print the results
print('Full Name:', full_name)
print('First Name:', first_name)
print('Last Name:', last_name)

if middle_name:
    print('Middle Name:', middle_name)
