import random

while(a):
    stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

word_list = ["alok","abhijeet","anurag","abhishek","uplakshya"]
random_word = random.choice(word_list)
print(random_word)  # for testing

b = len(random_word)
placeholder = ["_"] * b
wrong_guesses = 0
max_wrong = len(stages) - 1

while wrong_guesses < max_wrong and "_" in placeholder:
    print("\nCurrent word:", " ".join(placeholder))
    guess = input("Enter the guess letter: ").lower()

    if guess in random_word:
        for i in range(b):
            if random_word[i] == guess:
                placeholder[i] = guess
    else:
        wrong_guesses += 1
        print(stages[wrong_guesses])

# Game result
if "_" not in placeholder:
    print("\n🎉 You won! The word was:", random_word)
else:
    print("\n💀 You lost! The word was:", random_word)
