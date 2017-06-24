name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = "White"
hair = 'Brown'
height_inches2centimeters = height * 2.54
weight_lbs2kg = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe." % teeth

# this line is tricky, try to get it exactly rihgt
print "If I add %r, %r, and %r I get %r." % (
age, height, weight, age + height + weight)

print "His height is %.2f centimeters." % height_inches2centimeters
print "His weight is %.2f kg." % weight_lbs2kg
