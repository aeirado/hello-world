from sys import argv
from os.path import exists

if len(argv) == 3:
    SCRIPT, FROM_FILE, TO_FILE = argv
else:
    raise ValueError("not enough values to unpack (expected 3, got 2)")

print(f"Copying from {FROM_FILE} to {TO_FILE}")

IN_FILE = open(FROM_FILE).read()

print(f"The input file is {len(IN_FILE)} bytes long.")

print(f"Does the output file exist? {exists(TO_FILE)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

OUT_FILE = open(TO_FILE, 'w').write(IN_FILE)

# kind_of_OUT_FILE = str(type(OUT_FILE))
# kind_of_IN_FILE = str(type(IN_FILE))

# print(f'Type of OUT_FILE is: {kind_of_OUT_FILE}\n\
# Type of IN_FILE is: {kind_of_IN_FILE}')

print("\nAlright, all done.")

# IN_FILE.close()
# OUT_FILE.close()
