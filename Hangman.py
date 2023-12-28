### Mamadou Cellou Diallo.    UCID: 30191307

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \ /
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
import random
## 1: random selection of a word that contains at least 4 letters from the lexicon

# This line will read the file in reading mode.
inf = open("data\\cpsc231-lexicon.txt", "r")
words = []  # This is an empty list of words

lines = inf.readlines()  # List of words where each word ends at \n
inf.close()


for k in lines:
     # Our word to guess has to be longer than 4 letters.
     if len(k.rstrip()) >  4:
          words.append(k.rstrip()) # we need to remove \n from each words so we use rstrip
# Note: the file has 4000 words. If you display all 4000 words, it may not display 4000 lines

# Our word will be randomly chosen from the words list
game_word = random.choice(words).upper()

# This step is for the number of guesses remaining
number_Of_guesses = 6

# Now our player will be prompted to guess letters of a word until the game is over
my_guesses = []
incorrect_guesses = []
# This is our loop control.
def loopcontrol(game_word,my_guesses):
     """

     :param game_word: this is our secret word.
     :param my_guesses: this is our right guesses.
     :return: if there's a word in our game_word that isn't guessed yet, the function will return false.
     else it will return "True" meaning that we found our word. Once it's true, it means that we found the word.
     """
     for i in game_word:
          if i.upper() not in my_guesses:
               return False
     return True

while number_Of_guesses >0:
     # We will check if the word is complete. If it is, then we will break out of the loop
     check = loopcontrol(game_word, my_guesses)
     if check == True: break
     print(display_hangman(number_Of_guesses))
     ## This part will show how our game_word looks like but will be hiding the letters with dashes
     print("")
     print("The word looks like:")
     for i in game_word:
     # this will display how the word looks like. in our first iteration, my_guesses is empty
     # so our word's letters will be hidden with dashes. whenever a guess happens to be in our
     # gameword's letters, we will display that guess.
          if i.upper() in my_guesses:
               print(i, end="")
          else:
               print("_", end="")

     # This will show our bad guesses as the game goes on.
     if len(incorrect_guesses) >0:
          print("\nyour bad guesses so far: \n", incorrect_guesses)

     # Let us display our remaining number of guesses.
     print("")
     print("You have", number_Of_guesses, "remaining!")

     # Our player will guess letters in a randomly chosen word
     player_guess = input("What is your next guess? ").upper()
     # This code will tell the player if he already guessed a letter before.
     if player_guess in incorrect_guesses or player_guess in my_guesses:
          print("You already guessed",player_guess,". Please try again.")
     # if our player's guess is correct, we will display "nice guess" and add the guess to our
     # list (my_guesses)
     elif player_guess in game_word:
          print("Nice guess!")
          my_guesses.append(player_guess.upper())
     else:
          incorrect_guesses.append(player_guess)
          number_Of_guesses -= 1
          print("Sorry,",player_guess,"is not part of the word.")


# Now we will display the outcome of the game
print("")
if check :
     print("congrats, you found the word. It was:",game_word)
else:
     print("Sorry you lost. The word was:",game_word)