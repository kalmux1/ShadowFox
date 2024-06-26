                                # HANGMAN GAME TASK IN INTERMEDIATE Level
#------------------------------------------------------------------------------------------------------------------#

from random_word import RandomWords

r = RandomWords()

def generate_word():
    while True:
        random_word = r.get_random_word()
        if random_word and len(random_word) == 8:
            return random_word

random_word = generate_word()
lives = 7

blanks = []


HANGMANPICS = ["""
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
|       dead
|_____   
""","""
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / \\
|
|_____
""", """
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / 
|
|_____
""","""
 ____
|/   |
|   (_)
|   \\|/
|    |
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|   \\|
|    |
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""","""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",""" 
____
|/   |
|   
|    
|    
|    
|
|_____
"""]


for letters in random_word :
    blanks += '_'

print(" ")
print (" WELCOME TO THE HANGMAN GAME ")
print (" ")
print (" ")
print(blanks)
print (" ")


gameover = False

while not gameover :
    guessed_letter = input("Guess a letter : ")
    for position in range(len(random_word)) :
        letter = random_word[position]
        if letter == guessed_letter :
            blanks[position] = guessed_letter
    print(blanks)

    if guessed_letter not in random_word :
        lives -= 1
        if lives == 0 :
            gameover = True
            print("\nGAMEOVER ! YOU LOOSE :( ")     
            
    if '_' not in blanks :
        gameover = True
        print("\nGAMEOVER ! YOU WIN :) ") 
    
    print(HANGMANPICS[lives])

