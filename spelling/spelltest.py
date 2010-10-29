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

encouragements = [
	'Good job!',
	'Way to go!',
	'Nice one!',
	'Awesome!',
	'Good work!',
	'Keep it up!',
	'Excellent!',
	'Spell-tacular!',
	]

def encourage():
	say(random.choice(encouragements))

rewards = [
	'Go get a Diet Coke!',
	'Go play Halo Reach!',
	'Now go take out the recycling!',
	]

def reward():
	say(random.choice(rewards))

def spelltest(words, name):
	random.shuffle(words)

	wrong_words = []

	last_word_wrong = False
	for word in words:
		number_guesses = 0
		while True:
			if last_word_wrong:
				say("Now spell %s" % (word))
				last_word_wrong = False
			else:
				say(word)
			guess = raw_input("Spell it now (just hit return to say it again): ")
			if (len(guess) > 0):
				number_guesses += 1

				if (guess.lower() == word.lower()):
					encourage()
					time.sleep(.25)
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

		last_word_wrong = number_guesses > 1
		if last_word_wrong:
			wrong_words.append(word)

	total_wrong_words = len(wrong_words)
	if total_wrong_words == 0:
		say("You rock %s! You spelled all of them right!" % (name))
		reward()
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
