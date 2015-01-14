
class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_path(self, name, room):
		self.paths[name] = room

	def remove_path(self, name):
		del self.paths[name]
