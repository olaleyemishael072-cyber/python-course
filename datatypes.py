"""Examples of Python data types and basic operations."""

# String operations
text = "Hello"
print("String:", text, "Type:", type(text).__name__)
print("String operations:", text + " Python", text.upper(), len(text))

# Integer operations
number = 12
print("Integer:", number, "Type:", type(number).__name__)
print("Integer operations:", number + 3, number * 2, number // 5)

# Boolean operations
is_ready = True
print("Boolean:", is_ready, "Type:", type(is_ready).__name__)
print("Boolean operations:", is_ready and False, not is_ready)

# Float operations
price = 4.5
print("Float:", price, "Type:", type(price).__name__)
print("Float operations:", price + 1.5, price * 2, round(price / 3, 2))

# Boolean operations
is_ready = True
print("Boolean:", is_ready, "Type:", type(is_ready).__name__)
print("Boolean operations:", is_ready and False, not is_ready)

# Float operations
price = 4.5
print("Float:", price, "Type:", type(price).__name__)
print("Float operations:", price + 1.5, price * 2, round(price / 3, 2))

# Python uses None for a null value
empty_value = None
print("Null value:", empty_value, "Type:", type(empty_value).__name__)
print("Null check:", empty_value is None)