user_input = input("Enter the name of the file: ").lower().strip()

if user_input.endswith(".jpeg"):

    print("image/jpeg")

elif user_input.endswith(".jpg"):

    print("image/jpeg")
elif user_input.endswith(".png"):

    print("image/png")
elif user_input.endswith(".gif"):

    print("image/gif")

elif user_input.endswith(".pdf"):
    print("application/pdf")

elif user_input.endswith(".zip"):
    print("application/zip")
elif user_input.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")