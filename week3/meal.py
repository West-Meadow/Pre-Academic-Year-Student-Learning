def main():
    time = input("Enter your current time: ").strip()
    time_float = convert(time)

    if time_float >= 7.00 and time_float <= 8.00:
        print("breakfast time")

    elif time_float >= 12.00 and time_float <= 13.00:
        print("lunch time")

    elif time_float >= 18.00 and time_float <= 19.00:
        print("dinner time")

    return


def convert(time):

    hour, minutes = time.split(":")

    hour =float(hour)
    minutes= float(minutes) * 1 /60

    return hour + minutes

if __name__ == "__main__":
    main()
