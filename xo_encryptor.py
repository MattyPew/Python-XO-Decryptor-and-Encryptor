print("Use -help to see all commands!")
encrypted = "Encrypted: "
true = 0

while true == 0:
    enc = input("Import letter after letter or use -help: ")

    if enc.lower() == 'a':
        encrypted = (encrypted + "ooooo ")

    elif  enc.lower() == 'b':
        encrypted = (encrypted + "oooox ")

    elif enc.lower() == 'c':
        encrypted = (encrypted + "oooxo ")

    elif enc.lower() == 'd':
        encrypted = (encrypted + "oooxx ")

    elif  enc.lower() == 'e':
        encrypted = (encrypted + "ooxoo ")

    elif  enc.lower() == 'f':
        encrypted = (encrypted + "ooxox ")

    elif  enc.lower() == 'g':
        encrypted = (encrypted + "ooxxo ")

    elif  enc.lower() == 'h':
        encrypted = (encrypted + "ooxxx ")

    elif  enc.lower() == 'ch':
        encrypted = (encrypted + "oxooo ")

    elif  enc.lower() == 'i':
        encrypted = (encrypted + "oxoox ")

    elif  enc.lower() == 'j':
        encrypted = (encrypted + "oxoxo ")

    elif  enc.lower() == 'k':
        encrypted = (encrypted + "oxoxx ")

    elif  enc.lower() == 'l':
        encrypted = (encrypted + "oxxoo ")

    elif  enc.lower() == 'm':
        encrypted = (encrypted + "oxxox ")

    elif  enc.lower() == 'n':
        encrypted = (encrypted + "oxxxo ")

    elif  enc.lower() == 'o':
        encrypted = (encrypted + "oxxxx ")

    elif  enc.lower() == 'p':
        encrypted = (encrypted + "xoooo ")

    elif  enc.lower() == 'q':
        encrypted = (encrypted + "xooox ")

    elif  enc.lower() == 'r':
        encrypted = (encrypted + "xooxo ")

    elif  enc.lower() == 's':
        encrypted = (encrypted + "xooxx ")

    elif  enc.lower() == 't':
        encrypted = (encrypted + "xoxoo ")

    elif  enc.lower() == 'u':
        encrypted = (encrypted + "xoxox ")

    elif  enc.lower() == 'v':
        encrypted = (encrypted + "xoxxo ")

    elif  enc.lower() == 'w':
        encrypted = (encrypted + "xoxxx ")

    elif  enc.lower() == 'x':
        encrypted = (encrypted + "xxooo ")

    elif  enc.lower() == 'y':
        encrypted = (encrypted + "xxoox ")

    elif  enc.lower() == 'z':
        encrypted = (encrypted + "xxoxo ")

    elif  enc.lower() == '.':
        encrypted = (encrypted + "xxoxx ")

    elif  enc.lower() == '!':
        encrypted = (encrypted + "xxxoo ")

    elif  enc.lower() == '?':
        encrypted = (encrypted + "xxxox ")

    elif  enc.lower() == ' ':
        encrypted = (encrypted + "xxxxo ")

    elif  enc.lower() == ',':
        encrypted = (encrypted + "xxxxx ")

    elif  enc.lower() == '-print':
        print(encrypted)
        encrypted = "Encrypted: "

    elif  enc.lower() == '-help':
        print("Use -print (show results), -clear (clear all previous imputs)")

    elif  enc.lower() == '-clear':
        print("Cleared!")
        encrypted = "Encrypted: "  

    else:
        print("Bad import, try again!")