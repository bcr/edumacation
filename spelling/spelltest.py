import random
import subprocess
import time

letter_map = {
	'a' : 'a',
	'b' : 'bee',
	'c' : 'see',
	'd' : 'dee',
	'e' : 'eee',
	'f' : 'eff',
	'g' : 'gee',
	'h' : 'aych',
	'i' : 'eye',
	'j' : 'jay',
	'k' : 'kay',
	'l' : 'ell',
	'm' : 'em',
	'n' : 'enn',
	'o' : 'oh',
	'p' : 'pee',
	'q' : 'cue',
	'r' : 'are',
	's' : 'esss',
	't' : 'tee',
	'u' : 'you',
	'v' : 'vee',
	'w' : 'double you',
	'x' : 'ecks',
	'y' : 'why',
	'z' : 'zee',
	' ' : 'space',
}

def say(str):
	return subprocess.call(['say', str])

def spell(str):
	final_string = str.lower()
	say(reduce(lambda x, y: x + letter_map[y] + ', ', final_string, "")[:-2])

def spelltest(words, name):
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
					say("Let's move on. It's spelled")
					spell(word)
					time.sleep(.5)
					break

				if number_guesses == 1:
					say("Try again")
				elif number_guesses == 2:
					say("One more try")

				time.sleep(0.25)

		if number_guesses > 1:
			wrong_words.append(word)

	total_wrong_words = len(wrong_words)
	if total_wrong_words == 0:
		say("You rock %s! You spelled all of them right! Go get a Diet Coke!" % (name))
	else:
		print("\nAwesome job %s! But you need to work on:" % (name))
		say("Awesome job %s! But you need to work on:" % (name))
		total_words_read = 0
		for word in wrong_words:
			time.sleep(0.5)
			print("  %s" % (word))
			if ((total_words_read > 0) and (total_words_read == (total_wrong_words - 1))):
				say("and %s" % (word))
			else:
				say(word)
			total_words_read += 1
		print("")
