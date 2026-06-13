name = "deepak"
print(len(name))

print(name.endswith("pak"))
print(name.startswith("dee"))
print(name.capitalize())
# Some of the most commonly used string functions (methods) in Python are:

# Method	Description	Example
# lower()	Converts string to lowercase	"HELLO".lower() → 'hello'
# upper()	Converts string to uppercase	"hello".upper() → 'HELLO'
# strip()	Removes leading/trailing spaces	" hello ".strip() → 'hello'
# replace()	Replaces part of a string	"hello".replace("h", "j") → 'jello'
# split()	Splits string into a list	"a,b,c".split(",") → ['a','b','c']
# join()	Joins list items into a string	"-".join(['a','b']) → 'a-b'
# find()	Finds the position of a substring	"hello".find("e") → 1
# startswith()	Checks if string starts with text	"hello".startswith("he") → True
# endswith()	Checks if string ends with text	"hello".endswith("lo") → True
# count()	Counts occurrences of a substring	"hello".count("l") → 2
# isalpha()	Checks if all characters are letters	"Hello".isalpha() → True
# isdigit()	Checks if all characters are digits	"123".isdigit() → True
# title()	Converts first letter of each word to uppercase	"hello world".title() → 'Hello World'
# capitalize()	Capitalizes first character	"hello".capitalize() → 'Hello'