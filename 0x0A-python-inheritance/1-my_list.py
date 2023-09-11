#!/usr/bin/python3
"""defines a class that inherits from a list"""


class MyList(list):
	"""add sorted printing"""

	def print_sorted(self):
		"""print sorted list"""
		print(sorted(self))
