# Q09. Functions with Default Parameters
#
# Write the following two functions:
#
#   greet(name, greeting="Hello")
#       Returns the string: "{greeting}, {name}!"
#
#   power(base, exp=2)
#       Returns base raised to exp.
#
# Then in the main block below, call and print:
#   greet("Alice")          → "Hello, Alice!"
#   greet("Bob", "Hi")      → "Hi, Bob!"
#   power(5)                → 25
#   power(2, 10)            → 1024


def greet(name, greeting="Hello"):
    # --- YOUR CODE HERE ---
    print(f"{greeting}, {name}!")
    pass


def power(base, exp=2):
    # --- YOUR CODE HERE ---
    return base**exp
    pass


if __name__ == "__main__":
    # Call the functions and print results
    # --- YOUR CODE HERE ---
    greet("Nandini")
    greet("Tony Stark","Hey")
    print(power(3))
    print(power(3,7))
    pass
