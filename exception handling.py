try:
    numerator= int(input("Enter a number the number to be divided "))
    denominator= int(input("Enter the divider "))
    result=numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
#
except ValueError as e:
    print(e)
    print("Enter only numbers please")

except Exception as e:
    print(e)
    print("Something went wrong")

else:
    print(result)

finally:
    print("this will always execute")




