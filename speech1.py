# Uses the espeak package as a speech synthesizer
# Simply a command-line interface, requires espeak to be installed

import os

def speechify(text):
	# Non-blocking has issues with successive calls
	#os.system('espeak -p50 -s120 '{}' >/dev/null 2> /dev/null &".format(text))
	os.system("espeak -p50 -s120 '{}' >/dev/null 2> /dev/null ".format(text))
