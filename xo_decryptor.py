print("Use -print to see result!")
decrypted = "Decrypted: "
true = 0

while true == 0:
    enc = input("Import encrypted or use -print: ")

    if enc.lower() == 'ooooo':
        decrypted = (decrypted + "a")

    elif  enc.lower() == 'oooox':
        decrypted = (decrypted + "b")

    elif enc.lower() == 'oooxo':
        decrypted = (decrypted + "c")

    elif enc.lower() == 'oooxx':
        decrypted = (decrypted + "d")

    elif  enc.lower() == 'ooxoo':
        decrypted = (decrypted + "e")

    elif  enc.lower() == 'ooxox':
        decrypted = (decrypted + "f")

    elif  enc.lower() == 'ooxxo':
        decrypted = (decrypted + "g")

    elif  enc.lower() == 'ooxxx':
        decrypted = (decrypted + "h")

    elif  enc.lower() == 'oxooo':
        decrypted = (decrypted + "ch")

    elif  enc.lower() == 'oxoox':
        decrypted = (decrypted + "i")

    elif  enc.lower() == 'oxoxo':
        decrypted = (decrypted + "j")

    elif  enc.lower() == 'oxoxx':
        decrypted = (decrypted + "k")

    elif  enc.lower() == 'oxxoo':
        decrypted = (decrypted + "l")

    elif  enc.lower() == 'oxxox':
        decrypted = (decrypted + "m")

    elif  enc.lower() == 'oxxxo':
        decrypted = (decrypted + "n")

    elif  enc.lower() == 'oxxxx':
        decrypted = (decrypted + "o")

    elif  enc.lower() == 'xoooo':
        decrypted = (decrypted + "p")

    elif  enc.lower() == 'xooox':
        decrypted = (decrypted + "q")

    elif  enc.lower() == 'xooxo':
        decrypted = (decrypted + "r")

    elif  enc.lower() == 'xooxx':
        decrypted = (decrypted + "s")

    elif  enc.lower() == 'xoxoo':
        decrypted = (decrypted + "t")

    elif  enc.lower() == 'xoxox':
        decrypted = (decrypted + "u")

    elif  enc.lower() == 'xoxxo':
        decrypted = (decrypted + "v")

    elif  enc.lower() == 'xoxxx':
        decrypted = (decrypted + "w")

    elif  enc.lower() == 'xxooo':
        decrypted = (decrypted + "x")

    elif  enc.lower() == 'xxoox':
        decrypted = (decrypted + "y")

    elif  enc.lower() == 'xxoxo':
        decrypted = (decrypted + "z")

    elif  enc.lower() == 'xxoxx':
        decrypted = (decrypted + ".")

    elif  enc.lower() == 'xxxoo':
        decrypted = (decrypted + "!")

    elif  enc.lower() == 'xxxox':
        decrypted = (decrypted + "?")

    elif  enc.lower() == 'xxxxo':
        decrypted = (decrypted + " ")

    elif  enc.lower() == 'xxxxx':
        decrypted = (decrypted + ",")

    elif  enc.lower() == '-print':
        print(decrypted)
        decrypted = "Decrypted: "

    else:
        print("Bad import, try again!")