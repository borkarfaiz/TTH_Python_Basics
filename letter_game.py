import random

# make a list of words

words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

while True:
    start = input("Press enter/ return to start or press 'q' to quit   ")
    if start.lower == 'q':
        break
    
    
    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        
        
    
        # draw spaces
        # draw guessed letters and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end ='')
            else:
                print('_', end = '')

        print('')
        print('Strike: {}/7'.format(len(bad_guesses))
        print('')
              
    # take guess
        guess = input("Guess a letter:   ").lower()

        if len(guess) ! = 1:
            print("You can guess a single letter only")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("you already guess it")
        elif not guess.isalpha():
            print("You van only guess letters! ")
            continue
     
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You Won")
        else:
            bad_guesses.append(guess)
                  
    # print out win/lose



