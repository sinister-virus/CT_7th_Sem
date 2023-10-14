#Caesar_Cipher
def ceasar_cipher_encryption():
    print("Ceasar Cipher Encryption")
    x=input("Enter Plain Text: ")
    key=int(input("Enter Key: "))

    y = x.split(" ", len(x))

    cipher_word_list = []

    for z in range(len(y)):
        word = y[z]


        s_word = list(word)


        new_word = []  # empty list for new word
        cipher_text = ""  # empty list for cipher text

        for r in range(len(s_word)):
            char = s_word[r]


            # char to ascii

            char_a = int(ord(char))


            # char ascii + key = new char ascii

            new_char_a = char_a + key


            # new char ascii to new char

            new_char = chr(new_char_a)


            # new char to new word
            new_word.append(new_char)


            # new_word list merge



            if len(new_word) == len(s_word):

                # join all the strings in list without spaces
                strValue = ''.join(new_word)



                # append cipher word to list
                cipher_word_list.append(strValue)



                # cipher word to string

                for j in cipher_word_list:
                    cipher_text = str(' '.join(cipher_word_list))

                if len(x)==len(cipher_text):
                    print("Cipher Text = ",cipher_text)
                    print()



def ceasar_cipher_decryption():
    print("Ceasar Cipher Decryption")
    x=input("Enter Cipher Text: ")
    k=int(input("Enter Key: "))
    key=k*-1

    y = x.split(" ", len(x))

    cipher_word_list = []

    for z in range(len(y)):
        word = y[z]


        s_word = list(word)


        new_word = []  # empty list for new word
        cipher_text = ""  # empty list for cipher text

        for r in range(len(s_word)):
            char = s_word[r]


            # char to ascii

            char_a = int(ord(char))


            # char ascii + key = new char ascii

            new_char_a = char_a + key


            # new char ascii to new char

            new_char = chr(new_char_a)


            # new char to new word
            new_word.append(new_char)


            # new_word list merge



            if len(new_word) == len(s_word):

                # join all the strings in list without spaces
                strValue = ''.join(new_word)



                # append cipher word to list
                cipher_word_list.append(strValue)



                # cipher word to string

                for j in cipher_word_list:
                    cipher_text = str(' '.join(cipher_word_list))

                if len(x)==len(cipher_text):
                    print("Plain Text = ",cipher_text)
                    print()

ceasar_cipher_encryption()

ceasar_cipher_decryption()





