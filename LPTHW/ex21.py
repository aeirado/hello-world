def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b



print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."


what = add(age, subtract(height, multiply(weight, divide(iq, 2))))


print "That becomes: ", what, "Can you do it by hand?"

formula = 50 + (200 - (130 * (90 / 3)))

print "\n\n\nThe result of formula [50 + (200 - (130 * (90 / 3)))] is:\n%.2f" \
        % formula

print "\n\n\nLet's print adds = add(30, 20):"
adds = add(30, 20)
print "Let's print subs = subtract(270, 70):"
subs = subtract(270, 70)
print "Let's print mults = multiply(65, 2):"
mults = multiply(65, 2)
print "Let's print divs = divide(270, 3):"
divs = divide(270, 3)

print "\n"

formula_functions = add(adds, subtract(subs, multiply(mults, divide(divs, 3))))

print """The result of formula_functions = formula_functions = add(adds,
        subtract(subs, multiply(mults, divide(divs, 3)))) is %.2f""" \
        % formula_functions
