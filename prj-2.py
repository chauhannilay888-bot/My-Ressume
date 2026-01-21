# Temperature Convertor
try:
    a = (input("Enter the temperature: "))
    temp = float(a)
    b = (input("Want to convert it in celcius or fahreneight(c/f): "))
    option = str(b)
    if option == "c" or "C":
        answer = (f"{temp-32*(5/9)}°C")
    elif option == "f" or "F":
        answer = (f"{temp*(9/5)+32}°F")
        print(answer)
except ValueError:
    print("Invalid")
