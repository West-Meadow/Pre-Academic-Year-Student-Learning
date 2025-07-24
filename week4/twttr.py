user_str = input("Enter your string: ")
vowels = "aeiouAEIOU"

for x in vowels:
    user_str =user_str.replace(x,"")

print(user_str)