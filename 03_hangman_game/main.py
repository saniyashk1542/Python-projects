import random
import word_file
import hangman_stages

lives=6

chosen_word=random.choice(word_file.words)
# print(chosen_word)

display=[]

for i in range(len(chosen_word)):
    display+='_'
print(display)

game_over=False

while not game_over:
    guessed_letter=input("guess a letter!\n").lower()
    for position in range(len(chosen_word)):
        letter=guessed_letter
        if letter==chosen_word[position]:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose!")
    if '_' not in display:
        game_over=True
        print("you win!!")
    print(hangman_stages.hangman[lives])



