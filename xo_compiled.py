switch = 0

while(True):
    while switch == 0:
        print("\033[34mDecrypt mode enabled. Use -help to see all commands!")
        decrypted = "Decrypted: "

        while switch == 0:
            enc = input("\033[36mImport encrypted or use -help: ")

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
                print("\033[32m" ,decrypted,)
                decrypted = "decrypted: "

            elif  enc.lower() == '-help':
                print("\033[32mUse -print (show results), -clear (clear all previous imputs), -supported (show supported imputs), -switch (switch to another mode (decrypt to encrypt))")

            elif  enc.lower() == '-clear':
                print("\033[32mCleared!")
                decrypted = "Decrypted: "  

            elif  enc.lower() == '-supported':
                print("\033[32mSupported format: 5 - digits, x and o format.")

            elif  enc.lower() == '-switch':
                print("\033[32mSwitched!")
                switch = 1

            else:
                print("\033[31mBad import, try again!")


    while switch == 1:
            
        print("\033[34mEncrypt mode enabled. Use -help to see all commands!")
        encrypted = "Encrypted: "

        while switch == 1:
            enc = input("\033[36mImport letter after letter or use -help: ")

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
                print("\033[32mUse -print (show results), -clear (clear all previous imputs), -supported (show supported imputs), -switch (switch to another mode (encrypt to decrypt))")

            elif  enc.lower() == '-clear':
                print("\033[32mCleared!")
                encrypted = "Encrypted: "  

            elif  enc.lower() == '-supported':
                print("\033[32mThese are supported: abcdefghchijklmnopqrstuvwxxz.!? ,")

            elif  enc.lower() == '-switch':
                print("\033[32mSwitched!")
                switch = 0

            else:
                print("\033[31mBad import, try again!")