# one.py

# All code at indentation level 0, meaning no indentation at all, closest to the number line code margin runs

# print('hello')

# built in variable name, obvious because its got double _

# __name__ = "__main__"


# SOOO Back to one.py

def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
	# same as RUN THE SCRIPT
	print('One.py is being run directly!')
else:
	print('One.py has been imported!')
