# Python Type Casting Guide
# Type casting = converting a value from one data type to another

# ─────────────────────────────────────────────
# 1. int() — Convert to integer
# ─────────────────────────────────────────────
print("=== int() ===")
print(int(3.9))        # float  → int  : 3  (truncates, does NOT round)
print(int("42"))       # string → int  : 42
print(int(True))       # bool   → int  : 1
print(int(False))      # bool   → int  : 0

# ─────────────────────────────────────────────
# 2. float() — Convert to float
# ─────────────────────────────────────────────
print("\n=== float() ===")
print(float(7))        # int    → float : 7.0
print(float("3.14"))   # string → float : 3.14
print(float(True))     # bool   → float : 1.0

# ─────────────────────────────────────────────
# 3. str() — Convert to string
# ─────────────────────────────────────────────
print("\n=== str() ===")
print(str(100))        # int   → string : "100"
print(str(9.99))       # float → string : "9.99"
print(str(True))       # bool  → string : "True"

# ─────────────────────────────────────────────
# 4. bool() — Convert to boolean
# ─────────────────────────────────────────────
print("\n=== bool() ===")
print(bool(0))         # int    → bool : False  (0 is falsy)
print(bool(42))        # int    → bool : True   (non-zero is truthy)
print(bool(""))        # string → bool : False  (empty string is falsy)
print(bool("hello"))   # string → bool : True   (non-empty is truthy)
print(bool(None))      # None   → bool : False

# ─────────────────────────────────────────────
# 5. list(), tuple(), set() — Collection casting
# ─────────────────────────────────────────────
print("\n=== Collection casting ===")
text = "hello"
print(list(text))      # string → list  : ['h', 'e', 'l', 'l', 'o']
print(tuple(text))     # string → tuple : ('h', 'e', 'l', 'l', 'o')
print(set(text))       # string → set   : unique chars (order varies)

nums = [1, 2, 2, 3, 3]
print(set(nums))       # list   → set   : {1, 2, 3}  (removes duplicates)
print(list(set(nums))) # set    → list  : back to list

# ─────────────────────────────────────────────
# 6. Common pitfall — invalid conversions raise ValueError
# ─────────────────────────────────────────────
print("\n=== Safe casting with try/except ===")
user_input = "abc"
try:
    number = int(user_input)
except ValueError:
    print(f'Cannot convert "{user_input}" to int — not a valid number')

# ─────────────────────────────────────────────
# 7. Practical example — adding user input to a number
# ─────────────────────────────────────────────
print("\n=== Practical example ===")
# input() always returns a string, so we must cast before arithmetic
raw = "25"                  # simulates user input
age = int(raw)              # cast string → int
print(f"In 5 years you will be {age + 5}")  # works because age is now int

price = float("19.99")     # cast string → float
tax = price * 0.08
print(f"Price: ${price:.2f}, Tax: ${tax:.2f}, Total: ${price + tax:.2f}")

# ─────────────────────────────────────────────
# 8. User input with explicit type casting
# ─────────────────────────────────────────────
print("\n=== User input with explicit type casting ===")

# Modify the line below
name = str(input('What is your name? '))

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
age = int(input('What is your age? '))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input('What is your height in meters? '))

print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty = bool(input('Are you part of our loyalty program? '))

print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
