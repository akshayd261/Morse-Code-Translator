'''
KEY VARIABLES
cipher -> stores the morse translated form of the english string
decipher -> stores the english translated form of the morse string
citext -> stores morse code of a single character
i -> keeps count of the spaces between morse characters
txt -> stores the string to be encoded or decoded
'''

#Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


#Function to encrypt the string
def encrypt(text):
    cipher = ''
    for letter in text:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            #1 space indicates different characters and 2 indicates a new word
            cipher += ' '

    return cipher


#Function to decrypt the string
def decrypt(text):
    #extra space added at the end to access the last morse code
    text += ' '

    decipher = ''
    citext = ''
    for letter in text:

        #check for space
        if (letter != ' '):

            #counter for number of spaces
            i = 0

            #store morse code (single character)
            citext += letter

        #in case of space
        else:
            #if i = 1 that indicates a new character
            i += 1

            #if i = 2 that indicates a new word
            if i == 2:

                #add a space to separate words
                decipher += ' '
            else:

                #accessing the keys using their values
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher


#Driver function
def main():
    choice = input("Would you like to encrypt or decrypt your message? (e/d) " + "\n")
    if(choice == 'e'):
        txt = input("Enter text: \n")
        result = encrypt(txt.upper())
        print(result)
    elif(choice == 'd'):
        txt = input("Enter morse code text: \n")
        result = decrypt(txt)
        print(result)


#Execution
if __name__ == '__main__':
    main()