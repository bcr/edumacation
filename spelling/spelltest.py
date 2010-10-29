import random
import subprocess
import time

def say(str):
	return subprocess.call(['say', str])

def spelltest(words):
	random.shuffle(words)

	wrong_words = []

	for word in words:
		number_guesses = 0
		while True:
			say(word)
			guess = raw_input("Spell it now (just hit return to say it again): ")
			if (len(guess) > 0):
				number_guesses += 1

				if (guess.lower() == word.lower()):
					break

				if (number_guesses >= 3):
					say("Let's move on. Look how it's spelled")
					print "\nThe correct spelling is %s\n" % (word)
					time.sleep(3)
					break

				if number_guesses == 1:
					say("Try again")
				elif number_guesses == 2:
					say("One more try")

				time.sleep(0.25)

		if number_guesses > 1:
			wrong_words.append(word)

	if len(wrong_words) == 0:
		print "You rock! That's all of them right!"
	else:
		print "\nGood work -- you missed %d:" % (len(wrong_words))
		for word in wrong_words:
			print "  %s" % (word)
