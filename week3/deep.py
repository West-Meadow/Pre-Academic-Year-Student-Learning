user_input = input("Answer to the Great Question of Life, the Universe and Everything: "). strip().lower()

if user_input in ["42", "forty-two", "forty two"]:
    print("Yes")

else :
    print("No")