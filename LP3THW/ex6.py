# Assign the integer 10 to a variable named types_of_people
types_of_people = 10
# Assign to variable x a f-string where is inserted the variable above
x = f"There are {types_of_people} types of people."

# Assign the value "bynary" to a variable named binary
binary = "binary"
# Assign the value "don't" to a variable named do_not
do_not = "don't"
# Assign another f-string to the variable y
y = f"Those who know {binary} and those who {do_not}."

# Prints the x variable f-string to stdout
print(x)
# Prints the y variable f-string to stdout
print(y)

# Prints the x variable inserted in another f-string
print(f"I said: {x}")
# Prints the y variable inserted in another f-string
print(f"I said: '{y}'")

# Assign False to the variable hilarious
hilarious = False

# Assign to a variable nemed joke_evaluation a string with 2 curly braces '{}'
# to mark the place where to insert a value or a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the joke_evaluation variable with the variable hilarious inserted in it
print(joke_evaluation.format(hilarious))

# Bellow a string is assign to the variable w
w = "This is the left side of..."
# Bellow a string is assign to the variable e
e = "a string with a right side."

# Prints the variables w and e concatenated by the operator +
print(w + e)
