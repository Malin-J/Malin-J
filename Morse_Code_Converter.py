#Prompt the user to choose to translate to Morse Code or translate from Morse Code
choose=input('Type the letter M to translate to Morse Code or type the letter T to translate from Morse Code: ')

#This list/dictionary will be used to translate Morse code into english letters and arabic numbers using a slash "/" to act as a space between words.
morsedict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '
}
#The second dictionary, "mydict" translates letters and numbers into Morse Code for the user
mydict ={65: ".- ", 97: ".- ",
            66: "-... ", 98: "-... ",
            67: "-.-. ", 99: "-.-. ",
            68: "-.. ", 100: "-.. ",
            69: ". ", 101: ". ",
            70: "..-. ", 102: "..-. ",
            71: "--. ", 103: "--. ",
            72: ".... ", 104: ".... ",
            73: ".. ", 105: ".. ",
            74: ".--- ", 106: ".--- ",
            75: "-.- ", 107: "-.- ",
            76: ".-.. ", 108: ".-.. ",
            77: "-- ", 109: "-- ",
            78: "-. ", 110: "-. ",
            79: "--- ", 111: "--- ",
            80: ".--. ", 112: ".--. ",
            81: "--.- ", 113: "--.- ",
            82: ".-. ", 114: ".-. ",
            83: "... ", 115: "... ",
            84: "- ", 116: "- ",
            85: "..- ", 117: "..- ",
            86: "...- ", 118: "...- ",
            87: ".-- ", 119: ".-- ",
            88: "-..- ", 120: "-..- ",
            89: "-.-- ", 121: "-.-- ",
            90: "--.. ", 122: "--.. ",
            48: "----- ",
            49: ".---- ",
            50: "..--- ",
            51: "...-- ",
            52: "....- ",
            53: "..... ",
            54: "-.... ",
            55: "--... ",
            56: "---.. ",
            57: "----. "
        } 
#If the user choose "M" they will translate to Morse Code
if choose =='M':
 #The prompt a user will see, the user will type in a message they want to convert to Morse Code.
    code=input('What would you like to translate to Morse Code?\n')
    print(code.translate(mydict))
#If the user chooses "T" they will translate from Morse Code
elif choose == 'T':
    morse = input('Please provide the Morse Code you need converted and use a "/" as a space if needed.\n') #The dictionary at the top of the script that isn't nested will look for the Morse Code and translate it to plain text
    words = morse.split('   ') #splits the morsedict into a list 
    decoded_message = [] #Grabs the input from the user and acts as a list to store the "decoded" message.
    for word in words: #word is the vaule here, and is used to tell the script what to identify the letters as that are being converted.
        characters = word.split(' ') #This tells the script to list only the letters that are submitted to the input.
        decoded_word = ''.join(morsedict.get(char, '') for char in characters) #This tells the script to "decode" the Morse code input based on what "characters" are submitted by looking at the morsedict list
        decoded_message.append(decoded_word) #Each "character" that is submitted by the user is added to the decoded_message list using the .append function
    print(' '.join(decoded_message)) #Prints the output by "joining" the user input with the "decoded_message" list to translate from Morse code to english

#If the user chooses an option not available (including lowercase m and t) this error will appear.
else:
    print('Not an option!')
 
#Created by Malin-J  
#Creator note: This is my first python script and I managed to do it without looking up a guide on how to make this type of script.
#Python forums and websites were enough to carry me about 70% of the way through until I had to phone a friend to ask for help on the remaining 30%
#With no background in scripting, I'm proud of myself with this project!