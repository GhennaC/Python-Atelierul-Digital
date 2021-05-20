from random import randint

wordList = ["abecedar", "concatenare", "digital"]
attempts = 7
word = wordList[randint(0, 2)]
listWord = list(word)
listObscureWord = ['_'] * len(listWord)
figure_output = [" o \n", " o \n |\n", " o \n/|\n", " o \n/|\\\n", " o \n/|\\\n/ \n",
                 " o \n/|\\\n/ \\\n", " o \n/|\\\n/ \\\n***\n"]


def validate_input(letter):
    if len(letter) == 1 and letter.isalpha():
        if letter not in listObscureWord:
            return True
        else:
            print("This letter is already opened in our word.\n")
    else:
        print("Input invalid\n")
    return False


def get_letter():
    print("Letter: ")
    letter = input()
    return letter


def update_word(letter):
    for i, v in enumerate(listWord):
        if v == letter:
            listObscureWord[i] = letter
    return


def main():
    global attempts
    update_word(listWord[0])
    update_word(listWord[-1])

    print(''.join(listObscureWord))

    while attempts > 0 and '_' in listObscureWord:

        letter = get_letter()
        while not validate_input(letter):
            letter = get_letter()

        if letter in listWord:
            update_word(letter)
            print(''.join(listObscureWord))
        else:
            print(figure_output[7 - attempts])
            attempts -= 1
            print("Try again. " + str(attempts) + "you have more attempts")

    if attempts == 0:
        print("You lost The Game")
    else:
        print("You won The Game")


if __name__ == "__main__":
    main()
