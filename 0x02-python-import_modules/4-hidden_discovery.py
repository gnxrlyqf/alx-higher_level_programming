#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
	names = hidden_4.names
	for item in sorted(name for name in names if not name.startswith('__')):
		print(item)