#!/usr/bin/python3
def text_indentation(text):
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	for i in range(len(text)):
		if text[i] in ('.', '?', ':'):
			print("{}\n\n".format(text[i]), end = "")
		elif text[i] == ' ' and text[i - 1] in ('.', '?', ':'):
			print(end="")
		else:
			print(text[i], end="")
