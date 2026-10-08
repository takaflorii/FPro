import random                      # we cover random numbers in the modules chapter
number = random.randrange(1, 1000) # get a random number between (1 and 1000).

guesses = 0     # the "counter" with the number of guesses
message = ""    # the "accumulated" message

while True:
  guess = int(input(message + "\nGuess my number between 1 and 1000: "))
  guesses += 1  # one more guess
  if guess > number:
    print("Value", guess, "is greater than the number")   # TODO: add a line to the message
  elif guess < number:
    print("Value", guess, "is smaller than the number")   # TODO: add a line to the message
  else:
    print("Value", guess, "is the number")   
    print("\nGreat, you got it in " + str(guesses) + " guesses!\n")# TODO: leave the cycle immediately

