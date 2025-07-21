

# Prompt user for camelCase input
camel_case_input = input("Enter a variable name in camelCase: ")

# Initialize snake_case output
snake_case = ""

# Loop through each character and build the snake_case version
for i in camel_case_input:
    if i.isupper():
        snake_case += "_" + i.lower()
    else:
        snake_case += i

# Print the result
print(f"snake_case: {snake_case}")
