import math
import string
import sys

import numpy as np
from sympy import Matrix


# Shows the list of functions that can be run, and the user chooses one of them.
def option_menu():
    while True:
        print("---- HILL CIPHER (EXERCISE 3.2) " + "-"*200)
        print("List of available functions:")
        print("1) Encryption.")
        print("2) Decryption.")
        print("3) Known Plaintext Attack.")
        print("4) Exit.\n")
        try:
            chosen_function = int(input("\U0000270F Select the number of the function to run: "))
            if 1 <= chosen_function <= 4:
                return chosen_function
            else:
                print("\nYou must enter a number from 1 to 4\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 4\n")
        input("Press Enter to continue.\n")


# Creates a dictionary, letters of the English alphabet to numbers, and returns it.
def get_from_letters_to_numbers():
    alphabet = {}
    for character in string.ascii_uppercase:
        alphabet[character] = string.ascii_uppercase.index(character)
    return alphabet


# Creates a dictionary, numbers to letters of the English alphabet, and returns it.
def get_from_numbers_to_letters():
    alphabet = get_from_letters_to_numbers()
    reverse_alphabet = {}
    for key, value in alphabet.items():
        reverse_alphabet[value] = key
    return reverse_alphabet


# Gets input from the user and checks if respects the alphabet.
def get_text_input(message, alphabet):
    while True:
        text = input(message)
        text = text.upper()

        # Checks that all characters in the text are letters.
        if all(keys in alphabet for keys in text):
            return text
        else:
            print("\nThe text must contain only characters from the english alphabet ([A to Z] or [a to z]), "
                  "without spaces and numbers.")


# Checks if the key is a square in length.
def is_square(key):
    key_length = len(key)
    if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
        return True
    else:
        return False


# Creates the matrix k for the key.
def get_key_matrix(key, alphabet):
    k = list(key)
    m = int(math.sqrt(len(k)))
    for (i, character) in enumerate(k):
        k[i] = alphabet[character]

    # Reshape method transforms a one-dimensional array into a multi-dimensional matrix.
    return np.reshape(k, (m, m))


# Creates the matrix of m-grams of a text, if needed, complete the last m-gram with the last letter of the alphabet.
def get_text_matrix(text, m, alphabet):
    matrix = list(text)
    remainder = len(text) % m
    for (i, character) in enumerate(matrix):
        matrix[i] = alphabet[character]
    if remainder != 0:
        for i in range(m - remainder):
            # Adds 25 to the list because it corresponds to the letter Z.
            matrix.append(25)

    # Reshapes method transforms a one-dimensional array into a multi-dimensional matrix.
    return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()


# Encrypts a Message and returns the ciphertext matrix.
def encrypt(key, plaintext, alphabet):
    # Takes the number of rows of the key.
    m = key.shape[0]

    # Takes the number of columns of the plaintext, which corresponds to the number of m-grams
    # into which the plaintext is divided.
    m_grams = plaintext.shape[1]

    # Encrypts the plaintext with the key provided k, calculate matrix c of ciphertext.
    ciphertext = np.zeros((m, m_grams)).astype(int)
    for i in range(m_grams):
        ciphertext[:, i] = np.reshape(np.dot(key, plaintext[:, i]) % len(alphabet), m)
    return ciphertext


# Transforms a matrix to a text, according to the alphabet.
def from_matrix_to_text(matrix, order, alphabet):
    # The plaintext and ciphertext matrices are read by columns.
    if order == 't':
        # The ravel() with order='F' transforms the matrix into an array by reading it by columns.
        text_array = np.ravel(matrix, order='F')

    # The key matrix is read by rows.
    else:
        # The ravel() method (by default order = C) transforms the matrix into an array by reading it by rows.
        text_array = np.ravel(matrix)
    text = ""
    for i in range(len(text_array)):
        text = text + alphabet[text_array[i]]
    return text


# Checks if the key is invertible and in that case returns the inverse of the matrix.
def get_inverse_matrix(matrix, alphabet):
    alphabet_len = len(alphabet)
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix = Matrix(matrix)
        return np.matrix(matrix.inv_mod(alphabet_len))
    else:
        return None


# Decrypts a Message and returns the plaintext matrix.
def decrypt(key_inverse, ciphertext, alphabet):
    return encrypt(key_inverse, ciphertext, alphabet)


# Returns the value of m, inserted in input by the user during the known plaintext attack.
def get_m():
    while True:
        try:
            m = int(input("\U0000270F Insert the length of the grams (m): "))
            if m >= 2:
                return m
            else:
                print("\nYou must enter a number m >= 2\n")
        except ValueError:
            print("\nYou must enter a number m >= 2\n")


# Known Plaintext Attack
def known_plaintext_attack(ciphertext, plaintext_inverse, alphabet):
    return encrypt(ciphertext, plaintext_inverse, alphabet)


# Exposes all the functions for the various choices.
def main():
    while True:

        # Asks the user what function wants to run.
        choice = option_menu()

        # Gets two dictionaries, english alphabet to numbers and numbers to english alphabet.
        alphabet = get_from_letters_to_numbers()
        reverse_alphabet = get_from_numbers_to_letters()

        # Run the function selected by the user
        if choice == 1:

            # Asks the user the plaintext and the key for the encryption and checks the input.
            plaintext = get_text_input("\n\U0000270F Insert the plaintext: ", alphabet)
            key = get_text_input("\U0000270F Insert the key for encryption: ", alphabet)

            if is_square(key):

                # Gets the key matrix k.
                k = get_key_matrix(key, alphabet)
                print("\n\U00002022 Key Matrix:\n", k)

                # Gets the m-grams matrix p of the plaintext.
                p = get_text_matrix(plaintext, k.shape[0], alphabet)
                print("\U00002022 Plaintext Matrix:\n", p)

                # Encrypts the plaintext.
                c = encrypt(k, p, alphabet)

                # Transforms the ciphertext matrix to a text of the alphabet.
                ciphertext = from_matrix_to_text(c, "t", reverse_alphabet)


                print("\U00002022 Ciphertext: ", ciphertext, "\n")
            else:
                print("\nThe length of the key must be a square and >= 2.\n")

        elif choice == 2:

            # Asks the user the ciphertext and the key for the encryption and checks the input.
            ciphertext = get_text_input("\n\U0000270F Insert the ciphertext: ", alphabet)
            key = get_text_input("\U0000270F Insert the key for decryption: ", alphabet)

            if is_square(key):

                # Gets the key matrix k.
                k = get_key_matrix(key, alphabet)

                # Checks if the key is invertible and in that case returns the inverse of the matrix.
                k_inverse = get_inverse_matrix(k, alphabet)

                if k_inverse is not None:

                    # Gets the m-grams matrix c of the ciphertext.
                    c = get_text_matrix(ciphertext, k_inverse.shape[0], alphabet)

                    print("\n\U00002022 Key Matrix:\n", k)
                    print("\U00002022 Ciphertext Matrix:\n", c)

                    # Decrypts the ciphertext.
                    p = decrypt(k_inverse, c, alphabet)

                    # Transforms the plaintext matrix to a text of the alphabet.
                    plaintext = from_matrix_to_text(p, "t", reverse_alphabet)

                    print("\nThe message has been decrypted.\n")
                    print("\U00002022 Generated Plaintext Matrix:\n", p)
                    print("\U00002022 Generated Plaintext: ", plaintext, "\n")
                else:
                    print("\nThe matrix of the key provided is not invertible.\n")
            else:
                print("\nThe key must be a square and size >= 2.\n")

        elif choice == 3:

            # Asks the user the text and the ciphertext to use them for the plaintext attack.
            plaintext = get_text_input("\n\U0000270F Insert the plaintext for the attack: ", alphabet)
            ciphertext = get_text_input("\U0000270F Insert the ciphertext of the plaintext for the attack: ", alphabet)

            # Asks the user the length of the grams
            m = get_m()

            if len(plaintext) / m >= m:

                # Gets the m-grams matrix p of the plaintext and takes the firsts m.
                p = get_text_matrix(plaintext, m, alphabet)
                # Takes all rows and only the first m columns.
                p = p[:, 0:m]

                # Checks if the matrix of the plaintext is invertible and in that case returns the inverse of the
                # matrix.
                p_inverse = get_inverse_matrix(p, alphabet)

                if p_inverse is not None:

                    # Gets the m-grams matrix c of the ciphertext.
                    c = get_text_matrix(ciphertext, m, alphabet)
                    # Takes all rows and only the first m columns.
                    c = c[:, 0:m]

                    if c.shape[1] == p.shape[0]:
                        print("\n\U00002022 Ciphertext Matrix C*:\n", c)
                        print("\U00002022 Plaintext Matrix P*:\n", p)

                        # Forces the ciphertext provided.
                        k = known_plaintext_attack(c, p_inverse, alphabet)

                        # Transforms the key matrix to a text of the alphabet.
                        key = from_matrix_to_text(k, "k", reverse_alphabet)

                        print("\nThe key has been found.\n")
                        print("\U00002022 Generated Key Matrix:\n", k)
                        print("\U00002022 Generated Key: ", key, "\n")

                    else:
                        print("\nThe number of m-grams for plaintext and ciphertext are different.\n")
                else:
                    print("\nThe matrix of the plaintext provided is not invertible.\n")
            else:
                print("\nThe length of the plaintext must be compatible with the length of the grams (m).\n")

        elif choice == 4:
            sys.exit(0)
        input("Press Enter to return to the selection menu.\n")


if __name__ == '__main__':
    main()