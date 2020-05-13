class Apple:
	"""apple class describes flavor and color"""
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return "This apple is {} and it's flavor is {}.".format(self.color, self.flavor)

shubham = Apple("green", "bitter")
print(shubham)
