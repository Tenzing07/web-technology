def welcome():
    #prints the welcome message to the user
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def main():
    welcome()
    #continuously prompt the user for valid answer whether to encrypt or decrypt
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
        if mode == "e" or mode == "d":
            break
        else:
            print("Invalid Mode")
            # Get message and shift number from user
    message = input("What message would you like to {}: ".format(mode))
    shift = int(input("What is the shift number: "))
    # Encrypt or decrypt message depending on user's choice
    if mode == "e":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)
        # Print result
    print(result)
    # Continuously prompt user for valid choice (continue or exit)
    while True:
        choice = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if choice == "y" or choice == "n":
            break
        else:
            print("Invalid Choice")
    if choice == "n":
        # Exit program
        print("Thanks for using the program, goodbye!")
        return
    # Restart program
    main()

def encrypt(message, shift):
    result = ""
    # Loop through each character in the message
    for char in message:
        if char.isalpha():
            # Get the ASCII code of the character
            char_code = ord(char)
            # Add the shift to the ASCII code
            char_code += shift
            # Check if character is uppercase or lowercase
            if char.isupper():
                # Check if ASCII code is greater than 'Z'
                if char_code > ord('Z'):
                    char_code -= 26
                result += chr(char_code)
            else:
                # Check if ASCII code is greater than 'z'
                if char_code > ord('z'):
                    char_code -= 26
                result += chr(char_code)
        else:
            # If character is not a letter, add it to the result as is
            result += char
    return result.upper()

def decrypt(message, shift):
    result = ""
    # Loop through each character in the message
    for char in message:
        if char.isalpha():
            # Get the ASCII code of the character
            char_code = ord(char)
            # Subtract the shift from the ASCII code
            char_code -= shift
            # Check if character is uppercase or lowercase
            if char.isupper():
                # Check if ASCII code is less than 'A'
                if char_code < ord('A'):
                    char_code += 26
                result += chr(char_code)
            else:
                # Check if ASCII code is less than 'a'
                if char_code < ord('a'):
                    char_code += 26
                result += chr(char_code)
        else:
            # If character is not a letter, add it to the result as is
            result += char
    return result.upper()

main()