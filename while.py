num = 10
to_guess=True
while to_guess:
	guess = int(input("Guess the number: "))
	if guess== num:
		print("You guessed it right!")
		to_guess=False
	elif guess <num:
	    print("Your guess is less than the secret no.")
	else:
	    print("Your guess is larger than the secret no.")    	