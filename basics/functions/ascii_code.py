print("Program Started!")

print("Please enter a standard character:")
character = input()

if len(character) == 1:
    print(f"The ASCII code of {character} is {ord(character)}")
else:
    print("A single character was expected.")

print("program ended!")