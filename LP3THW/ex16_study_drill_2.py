from sys import argv

script, filename = argv

print("I'm going to read the file created in ex16.py")
print("Reading...")

with open(filename, 'r') as file_2_read:
    text_in_file = file_2_read.read()

print("Now I'm going to print it to stout...")
print(text_in_file)