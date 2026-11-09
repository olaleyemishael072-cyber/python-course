def demonstrate_dictionary_operations():
	# 1. Create a dictionary (keys are unique; values can be any type).
	scores = {"Ava": 88, "Ben": 74, "Chen": 95}
	empty_dictionary = {}
	print("Starting scores:", scores)

	# 2. Read values: square brackets raise KeyError for a missing key;
	#    get() safely returns a default instead.
	print("Ava's score:", scores["Ava"])
	print("Missing student:", scores.get("Dina", "not found"))

	# 3. Add a key or change the value for an existing key.
	scores["Dina"] = 81
	scores["Ben"] = 79
	scores.update({"Eli": 90, "Ava": 91})
	print("After adding/updating:", scores)

	# 4. Check membership and get the number of entries.
	print("Is Chen in the class?", "Chen" in scores)  # checks keys
	print("Number of students:", len(scores))

	# 5. Loop over keys, values, or key-value pairs.
	for student in scores:
		print(student, "has", scores[student])
	print("All names:", list(scores.keys()))
	print("All scores:", list(scores.values()))
	print("All pairs:", list(scores.items()))

	# 6. Remove entries. pop() returns the removed value; del removes by key.
	removed_score = scores.pop("Eli")
	del scores["Dina"]
	print("Removed Eli's score:", removed_score)
	print("After removals:", scores)

	# popitem() removes and returns the most recently inserted pair.
	removed_pair = scores.popitem()
	print("Removed pair:", removed_pair)

	# 7. Copying, default values, and combining dictionaries.
	backup = scores.copy()  # a shallow copy
	scores.setdefault("Frank", 0)  # only adds the key if it is missing
	more_scores = {"Gita": 84}
	scores.update(more_scores)  # also works to combine/update dictionaries
	combined = backup | more_scores  # Python 3.9+: creates a new dictionary
	print("Updated scores:", scores)
	print("Combined copy:", combined)

	# 8. Dictionary comprehension: build a dictionary from existing data.
	passed = {name: score for name, score in scores.items() if score >= 60}
	print("Passing students:", passed)

	# 9. Nested dictionaries store related information for each student.
	class_records = {
		"Ava": {"score": 91, "club": "Robotics"},
		"Chen": {"score": 95, "club": "Art"},
	}
	print("Ava's club:", class_records["Ava"]["club"])
	class_records["Ava"]["score"] = 93
	print("Updated records:", class_records)

	# clear() empties a dictionary. Use it only when you no longer need its data.
	temporary = {"example": 1}
	temporary.clear()
	print("After clear():", temporary, "(empty dictionary:", empty_dictionary, ")")


def class_challenges():
	"""Complete these challenges in your own code, using a dictionary."""
def demonstrate_dictionary_operations():
	
	scores = {"Ava": 88, "Ben": 74, "Chen": 95}
	empty_dictionary = {}
	print("Starting scores:", scores)

	
	print("Ava's score:", scores["Ava"])
	print("Missing student:", scores.get("Dina", "not found"))

	scores["Dina"] = 81
	scores["Ben"] = 79
	scores.update({"Eli": 90, "Ava": 91})
	print("After adding/updating:", scores)

	
	print("Is Chen in the class?", "Chen" in scores)  # checks keys
	print("Number of students:", len(scores))

	
	for student in scores:
		print(student, "has", scores[student])
	print("All names:", list(scores.keys()))
	print("All scores:", list(scores.values()))
	print("All pairs:", list(scores.items()))

	
	removed_score = scores.pop("Eli")
	del scores["Dina"]
	print("Removed Eli's score:", removed_score)
	print("After removals:", scores)

	
	removed_pair = scores.popitem()
	print("Removed pair:", removed_pair)

	
	backup = scores.copy()  # a shallow copy
	scores.setdefault("Frank", 0)  # only adds the key if it is missing
	more_scores = {"Gita": 84}
	scores.update(more_scores)  # also works to combine/update dictionaries
	combined = backup | more_scores  # Python 3.9+: creates a new dictionary
	print("Updated scores:", scores)
	print("Combined copy:", combined)

	
	passed = {name: score for name, score in scores.items() if score >= 60}
	print("Passing students:", passed)

	
	class_records = {
		"Ava": {"score": 91, "club": "Robotics"},
		"Chen": {"score": 95, "club": "Art"},
	}
	print("Ava's club:", class_records["Ava"]["club"])
	class_records["Ava"]["score"] = 93
	print("Updated records:", class_records)

	# clear() empties a dictionary. Use it only when you no longer need its data.
	temporary = {"example": 1}
	temporary.clear()
	print("After clear():", temporary, "(empty dictionary:", empty_dictionary, ")")


def class_challenges():
	"""Complete these challenges in your own code, using a dictionary."""
	# 1. Create a dictionary of at least four subjects and their scores.
	# 2. Print one score, safely look up a missing subject with get(), and
	#    check whether a subject is a key using `in`.
	# 3. Add a subject and update an existing score; print the dictionary length.
	# 4. Use a loop over items() to print each subject and score.
	# 5. Remove one subject with pop() and another with del.
	# 6. Make a copy, use setdefault(), then combine it with another dictionary
	#    using update() or |. Explain which keys/values are kept on duplicates.
	# 7. Use a dictionary comprehension to make a dictionary of scores >= 80.
	# 8. Store a nested dictionary for a student with at least two details.
	# 9. Try keys(), values(), items(), popitem(), and clear() on a temporary
	#    dictionary. Describe what each method returns or changes.
	pass


if __name__ == "__main__":
	demonstrate_dictionary_operations()
	class_challenges()
	pass


if __name__ == "__main__":
	demonstrate_dictionary_operations()
	class_challenges()