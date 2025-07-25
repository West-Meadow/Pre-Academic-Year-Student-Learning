# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def starts_with_letters(input):
    if input[:2].isalpha():
        return True

def num_of_characters(input):
    if 2 < len(input) < 7:
        return True

def ends_with_numbers(input):
    for i in range(len(input)):
        if input[i].isdigit() :
            if input[i] == "0":
                return False

            if input[i:].isdigit():
                return True


    return True


def contains_no_punctuation(input):
    if input.isalnum():
        return True




def is_valid(s):
    if (starts_with_letters(s) and
        num_of_characters(s) and
        ends_with_numbers(s) and
        contains_no_punctuation(s)):
        return True
    return False





main()
