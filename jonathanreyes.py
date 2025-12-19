import os
import time  # For the exit countdown

# Defines the index position of letters in the alphabet
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Vigenere Cipher
# Encryption Function
def vigenere_en(phrase, keyword):
    encrypted = ""
    key_In = 0  # Tracks position in keyword
    for char in phrase:
        # Checks if character is uppercase
        if char in UPPER_ALPHABET:
            letter = UPPER_ALPHABET.index(char)
            # Locates index of keyword letter in UPPER_ALPHABET
            rot = LOWER_ALPHABET.index(keyword[key_In % len(keyword)].lower())
            # Cycles through keyword letters to match the length of the phrase (.lower => turns keyword to lowercase)
            new_letter = (letter + rot) % 26
            # Wraps around the alphabet using modulo 26
            encrypted += UPPER_ALPHABET[new_letter]
            # Encrypts and moves to the next letter
            key_In += 1
        # CHecks if character is lowercase
        elif char in LOWER_ALPHABET:
            letter = LOWER_ALPHABET.index(char)
            # Locates index of keyword letter in LOWER_ALPHABET
            rot = LOWER_ALPHABET.index(keyword[key_In % len(keyword)].lower())
            # Cycles through keyword letters to match the length of the phrase (.lower => turns keyword to lowercase)
            new_letter = (letter + rot) % 26
            # Wraps around the alphabet using modulo 26
            encrypted += LOWER_ALPHABET[new_letter]
            key_In += 1  # Move to next keyword letter
        else:
            # Characters not included in the alphabet remain unchanged
            encrypted += char
    return encrypted


# Decryption Function
def vigenere_de(phrase, keyword):
    decrypted = ""
    key_In = 0  # Tracks position in keyword
    for char in phrase:
        if char in UPPER_ALPHABET:
            letter = UPPER_ALPHABET.index(char)
            # Locates index of keyword letter in UPPER_ALPHABET
            rot = LOWER_ALPHABET.index(keyword[key_In % len(keyword)].lower())
            # Cycles through keyword letters to match the length of the phrase (.lower => turns keyword to lowercase)
            new_letter = (letter - rot) % 26
            # Subtracts the rotation to reverse the encryption to decrypt
            decrypted += UPPER_ALPHABET[new_letter]
            key_In += 1
        elif char in LOWER_ALPHABET:
            letter = LOWER_ALPHABET.index(char)
            # Locates index of keyword letter in LOWER_ALPHABET
            rot = LOWER_ALPHABET.index(keyword[key_In % len(keyword)].lower())
            # Cycles through keyword letters to match the length of the phrase (.lower => turns keyword to lowercase)
            new_letter = (letter - rot) % 26
            # Subtracts the rotation to reverse the encryption to decrypt
            decrypted += LOWER_ALPHABET[new_letter]
            key_In += 1  # Move to next keyword letter
        else:
            # Characters not included in the alphabet remain unchanged
            decrypted += char
    return decrypted


# Created to ensure the keyword is valid and avoid crashes
def valid_keyword():
    while True:
        keyword = input("Enter Keyword: ")
        if keyword.isalpha():  # Checks if input characters are letters only
            return keyword
        else:
            print("Invalid keyword. Please use letters only.")


# Menu Function
def menu():
    # Phrase is stored here
    file_path = "cipher_file.txt"
    # Keyword is stored here
    key_path = "keyword_file.txt"
    # Keeps the menu running until user selects exit
    while True:
        print("\n[-] 0. Exit\n"
              "[-] 1. Encrypt Content\n"
              "[-] 2. Decrypt Content\n"
              "[-] 3. View File")

        try:
            # Users inputs Number value to perform action
            selection = int(input("[-] Please Select an Option: "))
        except ValueError:
            # If User enters a letter/symbol instead of a number, it runs this error instead of crashing
            print("Invalid input. Please enter a number to the menu options.")
            continue
            # Returns to the start of the loop

        # Exit the program
        if selection == 0:
            print("Initiating Self Destruct Sequence...")
            for i in range(3, 0, -1):  # Countdown from 3 to 1
                print(f"Self destruct in... {i}")
                time.sleep(1)  # 1 second pause
            print("BOOM")
            exit()

        # Encryption Menu
        elif selection == 1:
            phrase = input("Enter Content: ")
            keyword = valid_keyword()
            encrypted = vigenere_en(phrase, keyword)
            # w - overwrite content in file
            with open(file_path, 'w') as file:
                file.write(encrypted)
            print(f"Encrypted content written to {file_path}")
            with open(key_path, 'w') as file:
                file.write(keyword)
            print(f"Keyword written to {key_path}")
        # Decryption Menu
        elif selection == 2:
            keyword = valid_keyword()
            try:
                # Pulls the keyword from the file to confirm correctness
                with open(key_path, 'r') as file:
                    keyword_file = file.read().strip()

                if keyword != keyword_file:
                    print("Incorrect keyword. Cannot decrypt the file.")
                    continue

                # Keyword Is Correct, Continues with decryption
                # r - Read File
                with open(file_path, 'r') as file:
                    contents = file.read()
                decrypted = vigenere_de(contents, keyword)
                # w - overwrite content in file
                with open(file_path, 'w') as file:
                    file.write(decrypted)
                print(f"Decrypted content written to {file_path}")
            except FileNotFoundError:
                print("No file found to decrypt.")

        # View File Menu
        elif selection == 3:
            try:
                # r - Read File
                with open(file_path, 'r') as file:
                    print("\nFile contents:\n")
                    print(file.read())
            except FileNotFoundError:
                print("No file found to view.")

        else:
            print("Invalid selection.")


def main():
    menu()


# Launches the main() function when script runs
if __name__ == "__main__":
    main()