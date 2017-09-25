# Assign a string to formater (the string is composed of four replacement
# fields delimited by curly braces {})
formater = "{} {} {} {}"

# Prints a string made up by str.format() function and by four integer values
print(formater.format(1, 2, 3, 4))
print(formater.format("one", "two", "three", "four"))
print(True, False, False, True)
print(formater.format(formater, formater, formater, formater))
print(formater.format(
    "Try your",
    "Own text here",
    "May be a poem",
    "Or a song about fear"
))
