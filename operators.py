print("Arithmetic and Assignment Operators")
print("Follow the examples and predict each answer.\n")


apples = 12
oranges = 5
print("1. 12 + 5 =", apples + oranges)  # Addition
print("2. 12 - 5 =", apples - oranges)  # Subtraction
print("3. 12 * 2 =", apples * 2)        # Multiplication
print("4. 12 / 2 =", apples / 2)        # Division

score = 10
score += 5
print("5. Score after score += 5:", score)
score -= 3
print("6. Score after score -= 3:", score)
score *= 2
print("7. Score after score *= 2:", score)

print("\nYour turn: change the numbers and run the program again!")








class OperatorActivity:
    def __init__(self):
        # Imagine buying snacks with class money.
        self.money = 20
        self.apple_price = 3
        self.juice_price = 5
        self.apples = 2
        self.juices = 1

    def arithmetic_practice(self):
        print("--- Arithmetic operators ---")
        total_cost = self.apples * self.apple_price + self.juices * self.juice_price
        
        # Addition (+), subtraction (-), multiplication (*), division (/)
        print("Total cost:", total_cost)
        print("Money left:", self.money - total_cost)
        print("Half your money:", self.money / 2)
        
        # Floor division (//) gives a whole number; modulo (%) gives the remainder.
        print("Whole groups of 3 coins:", self.money // 3)
        print("Coins left after groups of 3:", self.money % 3)
        
        # Exponentiation (**) multiplies a number by itself.
        print("Apples squared:", self.apples ** 2)
        
        # TODO: Add 4 to self.money and print the answer.
        self.money += 4
        print("Money after adding 4:", self.money)
        # Reset self.money back to 20 if needed for subsequent logic, or leave updated.
        
        # TODO: Multiply self.apple_price by 2 and print the answer.
        print("Apple price multiplied by 2:", self.apple_price * 2)

    def logical_practice(self):
        print("\n--- Logical operators ---")
        total_cost = self.apples * self.apple_price + self.juices * self.juice_price
        can_buy = total_cost <= self.money
        has_apples = self.apples > 0
        
        # and is true only when both conditions are true.
        print("Can buy everything and has apples:", can_buy and has_apples)
        
        # or is true when at least one condition is true.
        print("Can buy everything or has apples:", can_buy or has_apples)
        
        # not changes True to False, and False to True.
        print("Cannot buy everything:", not can_buy)
        
        # TODO: Make a variable called has_juice that checks self.juices > 0.
        has_juice = self.juices > 0
        
        # TODO: Print whether has_apples and has_juice are both true.
        print("Has both apples and juice:", has_apples and has_juice)

if __name__ == "__main__":
    activity = OperatorActivity()
    activity.arithmetic_practice()
    activity.logical_practice()