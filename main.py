# morse code
morese_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    "5": ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '0': "-----",
    " ":"/",

}

# using a while loop for multiple output's
game = True
while game:
    # enter user input
    data = input('Enter any string to convert into morse code:\n').lower()


    # function to convert normal string into morse code.
    def convert(*args, **kwargs):
        converted_string = ""
        for value in data:
            converted_string += f"{morese_code[value]} "
        print(converted_string)

    # run the function.
    convert(data)

    # ask users if they want to continue or quit the code.
    again = input("Do you want to convert some other text, type yes or no?\n").lower()
    if again == "yes":
        continue
    elif again == "no":
        print("Thanks for using the application, have a good day.")
        game = False
    else:
        print("You did not type yes or no, the program will quit now.")
        print("Thanks for using the application, have a good day.")
        game = False