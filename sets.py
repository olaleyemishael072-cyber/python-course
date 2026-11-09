class SetsActivity:
	def __init__(self):
		# Students who like soccer and students who like art
		self.soccer = {"Pheona", "Abass", "Tristan", "Hamza"}
		self.art = {"Holly", "Carah", "Blake"}

	def run(self):
		print("CLASS SURVEY: SOCCER AND ART")
		print("Soccer:", self.soccer)
		print("Art:", self.art)

		# Union: everyone who likes soccer or art
		print("\nSoccer or art (union):", self.soccer | self.art)

		# Intersection: students who like both
		print("Both soccer and art (intersection):", self.soccer & self.art)

		# Difference: students in one set but not the other
		print("Soccer but not art (difference):", self.soccer - self.art)
		print("Art but not soccer (difference):", self.art - self.soccer)

		# Symmetric difference: students who like exactly one activity
		print("Exactly one activity (symmetric difference):", self.soccer ^ self.art)

		# Membership checks
		print("\nIs Ava in the soccer set?", "Ava" in self.soccer)
		print("Is Eli in the soccer set?", "Eli" in self.soccer)

		# Set comparisons
		soccer_fans = {"Ava", "Ben"}
		print("Are soccer_fans a subset of soccer?", soccer_fans <= self.soccer)
		print("Is soccer a superset of soccer_fans?", self.soccer >= soccer_fans)
		print("Are soccer and art disjoint?", self.soccer.isdisjoint(self.art))

		# Sets have no positions, so sort the names into a list before indexing.
		names = sorted(self.soccer | self.art)
		print("\nClass list (index and name):")
		for index in range(len(names)):
			print(index, names[index])


if __name__ == "__main__":
	SetsActivity().run()

        
