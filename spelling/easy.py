import spelltest

raw_words = """
dog
cat
mouse
"""

words = raw_words.split('\n')[1:-1]

spelltest.spelltest(words, "Ben")
