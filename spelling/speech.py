import subprocess

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
