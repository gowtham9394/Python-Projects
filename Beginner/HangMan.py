import random
name = input('what is your Name ')
print('All the best', name)

words = ['rainbow', 'computer', 'scicene', 'monitor', 'laptop', 'keyboard', 'mobile']
word = random.choice(words)
print('Guess the characters')
guess = ''
turn = 12
while turn > 0:
    failed == 0
    for char in word:
        if char in guess:
            print(char)
        else:
            print('_')
    if failed == 0:
         print('you win')
         print('Word is: ', word)
         break
    guess = input('Guess the characters')
    # every input character will be stored in guesses
    guesses += guess
    # check input with the character in word
    if guess not in word:
        turn -= 1
        print('wrong')
        print('you have' + turns, 'more guesses')
        if turn == 0:
            print('You lose')
