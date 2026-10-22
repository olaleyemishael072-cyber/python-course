# Create a list
fruits = ["apple", "banana", "cherry", "date", "strawberry"]
print("Starting list:", fruits)

# Add items to a list
fruits.append("watermelon")
fruits.insert(1, "pear")
print("After adding items:", fruits)

# Create a list of numbers using range()
numbers = list(range(1,6))
print("Numbers from 1 to 5:",numbers)

print("First fruit:", fruits [0])
print("Last fruit:", fruits[-1])

fruits.sort()
print("Fruits in the alphabetical order:", fruits)

# Try it: add another fruit, print fruits[2], then sort in reverse order
# with fruits.sort(reverse=True)

fruits.append("jackfruit")
print("Third fruit:", fruits[2])
fruits.sort(reverse=True)