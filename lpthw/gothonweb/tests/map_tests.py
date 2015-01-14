
from nose.tools import *
from gothonweb.map import Room

def test_room():
	gold = Room("Gold", "There is a lot of gold in this room")
	assert_equal(gold.name, "Gold")
	assert_equal(gold.paths, {})

def test_paths():
	left = Room("Left", "Room on the left")
	right = Room("Right", "Room on the right")
	centre = Room("Centre", "Room on the centre")

	left.add_path("left", left)
	left.add_path("centre", centre)

	right.add_path("right", right)
	right.add_path("centre", centre)

	centre.add_path("centre", centre)
	centre.add_path("left", left)
	centre.add_path("right", right)

	assert_equal(left.go("right"), None)
	assert_equal(left.go("centre"), centre)

	assert_equal(right.go("left"), None)
	assert_equal(right.go("centre"), centre)

	assert_equal(centre.go("left"), left)
	assert_equal(centre.go("right"), right)