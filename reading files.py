try:
    with open('New Text Document.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("        "
          ""
          ""
          "\nThat file is not found :(")












