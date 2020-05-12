class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return "This apple is {} and it's flavor is {}.".format(self.color, self.flavor)

name = Apple("green", "bitter")
print(name)
