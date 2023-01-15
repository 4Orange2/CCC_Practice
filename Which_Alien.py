def alien_identify():
    print("You have spotted an alien.")
    print("How many antennae?")
    antenna = int(input())
    print("How many eyes?")
    eyes = int(input())
    alien = ""
    if antenna >= 3 and eyes <= 4:
        alien += "TroyMartian \n"
    if antenna <= 6 and eyes >= 2:
        alien += "VladSaturnian \n"
    if antenna <= 2 and eyes <= 3:
        print("hi")
        alien += "GraemeMercurian \n"
    return alien

print(alien_identify())