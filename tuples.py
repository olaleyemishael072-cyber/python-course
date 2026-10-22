print("TUPLE ACTIVITY")

# 1. Create tuples. A one-item tuple needs a trailing comma.
empty = ()
foods = ("pizza", "tacos", "apples")
single_item = ("pasta",)
also_foods = "pizza", "tacos", "apples"  # Parentheses are optional.
print("Foods:", foods)
print("One item:", single_item)

# 2. Access items with indexing. The first index is 0; negative indexes
# count backward from the end.
print("First food:", foods[0])
print("Last food:", foods[-1])

# 3. Get part of a tuple with slicing: [start:stop:step]. Stop is not included.
print("First two:", foods[:2])
print("From the second item:", foods[1:])
print("Every other item:", foods[::2])

# 4. Join tuples with + and repeat a tuple with *.
more_foods = ("rice", "beans")
all_foods = foods + more_foods
echo = ("yum",) * 3
print("Joined:", all_foods)
print("Repeated:", echo)

# 5. Check membership and find the tuple's length.
print("Is tacos in foods?", "tacos" in foods)
print("Is soup absent?", "soup" not in foods)
print("Number of foods:", len(foods))

# 6. Tuple methods: count() tells how many times a value occurs;
# index() gives the position of its first occurrence.
numbers = (4, 7, 4, 9, 4)
print("Count of 4:", numbers.count(4))
print("First position of 9:", numbers.index(9))

# 7. Iterate over a tuple with a for loop.
for food in foods:
	print("I like", food)

# 8. Unpack a tuple into variables. The number of variables must match items.
person = ("Jordan", 13, "Grade 8")
name, age, grade = person
print(name, "is", age, "and is in", grade)

# 9. Tuples cannot be changed in place. This would raise a TypeError:
# foods[0] = "soup"
# Instead, make a new tuple using slicing and +.
updated_foods = ("soup",) + foods[1:]
print("New tuple:", updated_foods)

# 10. Built-in functions that work with numeric tuples.
print("Smallest:", min(numbers))
print("Largest:", max(numbers))
print("Sum:", sum(numbers))
print("Sorted values:", sorted(numbers))  # sorted() returns a list.

# 11. Nested tuples and conversions.
seating = (("Ava", "Ben"), ("Mia", "Leo"))
print("First person in row two:", seating[1][0])
food_list = list(foods)       # tuple to list
food_tuple = tuple(food_list) # list to tuple
print("Converted back:", food_tuple)

# You can delete a whole tuple variable with del, but not one item in a tuple.
temporary = (1, 2)
del temporary

# CHALLENGES
# 1. Create a tuple of three favorite games. Print its first and last items.
# 2. Create a tuple of five numbers. Print its length, minimum, maximum, and sum.
# 3. Use count() and index() with a tuple of your own.
# 4. Join two tuples, then loop through the combined tuple.

games=("fortnite", "minecraft", "roblox")

print("First game:", games[0])
print("Last game:", games[-1])

numbers = (5, 10, 15, 20, 25)
print("Length of numbers:", len(numbers))
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of numbers:", sum(numbers))

letters = ("a", "b", "c", "a", "d")
print("Count of 'a':", letters.count("a"))
print("Index of first 'a':", letters.index("a"))

tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
combined_tuple = tuple1 + tuple2
print("Combined tuple:", combined_tuple)
for item in combined_tuple:
    print("Item:", item)