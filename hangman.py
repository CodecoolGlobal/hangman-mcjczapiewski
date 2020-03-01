from random import choice


def pick_capital():
    """
    Picks a random European capital

    Returns:
    str: The name of European capital
    """
    capitals = [
        'TIRANA', 'ANDORRA LA VELLA', 'YEREVAN', 'VIENNA',
        'BAKU', 'MINSK', 'BRUSSELS', 'SARAJEVO', 'SOFIA',
        'ZAGREB', 'NICOSIA', 'PRAGUE', 'COPENHAGEN', 'TALLINN',
        'HELSINKI', 'PARIS', 'TBILISI', 'BERLIN', 'ATHENS',
        'BUDAPEST', 'REYKJAVIK', 'DUBLIN', 'ROME', 'NUR-SULTAN',
        'PRISTINA', 'RIGA', 'VADUZ', 'VILNIUS', 'LUXEMBOURG',
        'VALLETTA', 'CHISINAU', 'MONACO', 'PODGORICA', 'AMSTERDAM',
        'SKOPJE', 'OSLO', 'WARSAW', 'LISBON', 'BUCHAREST', 'MOSCOW',
        'SAN MARINO', 'BELGRADE', 'BRATISLAVA', 'LJUBLJANA', 'MADRID',
        'STOCKHOLM', 'BERN', 'ANKARA', 'KYIV', 'LONDON', 'VATICAN CITY'
    ]
    return choice(capitals)


def get_hashed(word):
    """
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.

    Args:
    str: The word to hash

    Returns:
    str: The hashed password
    """
    hashed_word = ""
    for c in word:
        if ord(c) in range(ord("A"), ord("Z") + 1):
            hashed_word += "_"
        else:
            hashed_word += c
    return hashed_word


def uncover(hashed_password, password, letter):
    """
    Uncovers all occurrences of the given letter in the hashed
    password based on the password

    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover

    Returns:
    str: The hashed password with uncovered letter
    """
    updated_hashed = ""
    i = 0
    for c in password:
        if letter == c:
            updated_hashed += letter
        else:
            updated_hashed += hashed_password[i]
        i += 1
    return updated_hashed


def update(used_letters, letter):
    """
    Appends the letter to used_letters if it doesn't occur

    Args:
    list: The list of already used letters
    str: The letter to append

    Returns:
    list: The updated list of already used letters
    """
    return used_letters + letter


def is_win(hashed_password, password):
    """
    Checks if the hashed password is fully uncovered

    Args:
    str: The hashed password
    str: The password

    Returns:
    bool:
    """
    if hashed_password == password:
        return True
    return False


def is_loose(life_points):
    """
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    """
    if life_points == 0:
        return True
    return False


def get_input(already_used):
    """
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    """
    user_letters = ""
    correct = False
    while not correct:
        user_letters = input(
            "\033[34mYou have 2 options:\n\
\033[37m1. \033[34mGive me a single letter to check if it is in given word.\n\
   The letter must not be already used.\n\
\033[37m2. \033[34mGuess the whole word at once.\n\
Any other variation will be interpreted as \033[31merror!\n\033[37m: "
        ).upper()
        if user_letters in already_used:
            print("\033[31mThis letter is in already used once. Pick another.")
        elif any(
            ord(c) not in range(ord("A"), ord("Z") + 1) and c != " "
            for c in user_letters
        ):
            print("\033[31mThis input contains invalid character.\n\
Please do it again.")
        else:
            correct = True
    return user_letters


def main():
    word_to_dash = pick_capital()
    used_letters = ""
    lives = 10
    hashed = get_hashed(word_to_dash)
    print("\033[34mHere's how long the word to guess is:\033[37m", len(hashed))
    print(hashed)
    print(
        "\033[34mYou have\033[37m",
        lives,
        "\033[34mlives at the start. Good luck!\n",
    )
    while not is_win(hashed, word_to_dash) and not is_loose(lives):
        user_guess = get_input(used_letters)
        if user_guess == word_to_dash:
            hashed = user_guess
            continue
        else:
            if len(user_guess) > 1:
                lives -= 1
                print(
                    "\033[31mGiven word was incorrect, you have\033[37m",
                    lives,
                    "\033[31mlives left.",
                )
            else:
                new_hashed = uncover(hashed, word_to_dash, user_guess)
                if hashed == new_hashed:
                    used_letters = update(used_letters, user_guess)
                    lives -= 1
                    print(
                        "\n\033[31mSorry, this letter doesn't occur \
in the word to guess.\n\033[34mYou have\033[37m",
                        lives,
                        "\033[34mlives left.\n\
These are the already used letters:\033[37m",
                    )
                    print(list(used_letters))
                    print("\033[34mThe letters you've guessed:\033[37m")
                    print(hashed)
                else:
                    hashed = new_hashed
                    print(
                        "\n\033[32mYou guessed new letter!\n\
Now the word looks like this:\033[37m"
                    )
                    print(hashed)
    if is_loose(lives):
        print("\n\033[31mSorry mate, you've lost.")
    elif is_win(hashed, word_to_dash):
        print("\n\033[32mYOU WON!")


if __name__ == "__main__":
    main()
