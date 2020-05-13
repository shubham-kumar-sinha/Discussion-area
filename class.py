
class Fruit:
	"""Fruit class describes flavor and color"""
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return "This apple is {} and it's flavor is {}.".format(self.color, self.flavor)

def function(number):
	sums = 0
	for i in range(number):
		sums += i
	return sums
hgu = int(input())
print(function(hgu))
