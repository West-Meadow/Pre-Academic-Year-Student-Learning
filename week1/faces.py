def convert(string):
    string =string.replace(":(","🙁")
    string =string.replace(":)","🙂")

    return string

def main():
    user_promt = input("enter your input here: ")
    value = convert(user_promt)
    print(value)


main()