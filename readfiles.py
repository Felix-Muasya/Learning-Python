try:
    with open('Facts and Figures - 2021.pdf') as file:
        print(file.read())
except FileNotFoundError:
    print("        "
          ""
          ""
          "\nThat file is not found :(")


