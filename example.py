import sys
from tp import *

def group():
	"""
	X is a thing that we want to know stuff about.
	"""
	with does("X look right?") as question:
		x = 5
		# x.blarf = stub("sniz")
		yield answer(x > 0, "X should be bigger than zero")

	with can("X look right?") as question:
		x = 5
		yield answer(x > 0, "X should be bigger than zero")

	with does("XYZ fail?") as question:
		x = 5
		yield answer(x == 6, "X should equal 5")

	with does("XYZ fail?") as question:
		x = 5
		yield answer(True, "X should equal 5")

def group2():

	with does("XYZ fail?") as question:
		x = 5
		yield answer(x == 6, "X should equal 5")

	with does("XYZ fail?") as question:
		x = 5
		yield answer(True, "X should equal 5")



	# with scenario("XYZ fail?") as given:
	# 	x = 5
	# 	yield x == 6, "X should equal 5"


