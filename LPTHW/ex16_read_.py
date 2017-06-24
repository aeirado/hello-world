from sys import argv

script, filename = argv
txt = open(filename)

print "Welcome to the world of %r!" % script
print "Now I'm going to read the file %r." % filename
text = txt.read()

print "And, now I will print the content of the file to STDOUT:"
print text
txt.close()
