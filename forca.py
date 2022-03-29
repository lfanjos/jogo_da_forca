from random import randint, choice


def choose_option_input(options, prompt, error_prompt):
    opt = input(prompt)
    while opt not in options:
        opt = input(error_prompt)
    return int(opt)


def load_words(opt):
    if opt == 5:
        opt = randint(1, 4)
    with open("palavras_forca.csv") as file:
        lines = [line.strip("\n").split(",") for line in file.readlines()]
        messy_words = [word for word in lines if lines.index(word) != 0]
        words = [x[opt - 1].upper() for x in messy_words]

        return list(filter(None, words))


def show_spaces():
    for space in empty_spaces:
        print(space, end=' ')
    print()


def get_guess():
    letter_guessed = input("Chute uma letra: ").upper()
    while len(letter_guessed) != 1 \
            or letter_guessed.isnumeric() \
            or not letter_guessed.isalnum() \
            or letter_guessed in letters_guessed:
        letter_guessed = input("Chute uma letra válida ou não repetida: ").upper()

    return letter_guessed


def ask_play_again(status):
    if status:
        play_again = input("Que pena, você perdeu :(. Deseja jogar novamente? (s/n) ").upper()
        while play_again not in 'SN':
            play_again = input("Não entendi, deseja jogar novamente? (s/n) ").upper()
        return True if play_again == 'S' else False

    play_again = input("Parábens!!! Você conseguiu. Deseja jogar novamente? (s/n) ").upper()
    while play_again not in 'SN':
        play_again = input("Não entendi, deseja jogar novamente? (s/n) ").upper()
    return True if play_again == 'S' else False


def show_welcome():
    print("**************************")
    print("Bem-vindo ao jogo da Forca")
    print("**************************")
    print("[1] Profissões [2] Corpo Humano [3] Cores [4] Animais [5] Aleatório")


while True:
    show_welcome()

    hangman_pics = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''']
    errors = 0
    hanged = False
    theme = choose_option_input(['1', '2', '3', '4', '5'],
                                "Selecione um tema: ",
                                "Selecione uma opção válida: "
                                )

    available_words = load_words(theme)
    chosen_word = list(choice(available_words))
    empty_spaces = ['_' for x in chosen_word]
    letters_guessed = []

    print(hangman_pics[0])

    while not hanged and '_' in empty_spaces:
        print(*letters_guessed, sep=' ', end='\n') if len(letters_guessed) != 0 else None
        print(*empty_spaces, sep=' ', end='\n')

        guess = get_guess()
        letters_guessed.append(guess)

        for index, letter in enumerate(chosen_word):
            if guess == letter:
                empty_spaces[index] = letter

        if guess not in chosen_word:
            errors += 1

        print(hangman_pics[errors])

        hanged = True if errors == 6 else False

    if '_' not in empty_spaces:
        print(*empty_spaces, sep=' ')

    if not ask_play_again(hanged):
        break
