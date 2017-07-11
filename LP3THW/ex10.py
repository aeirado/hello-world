tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(blackslash_cat)
print(fat_cat)
print("\t* \N{cat}")

# \\ = blackslash
# \' = single quote
# \" = double quote
# \a = ASCII bell (BEL)
# \b = ASCII backspace (BS)
# \f = ASCII formfeed (FF)
# \n = ASCII linefeed (LF)
# \N{name} = Character named name in the Unicode database (Unicode Only)
# \r = Carriage Return (CR)
# \t = Horisontal Tab (TAB)
# \uxxxx = Character with 16-bit hex value xxxx
# \Uxxxxxxxx = Character with 32-bit hex value xxxxxxxx
# \v = Vertical tab (VT)
# \ooo = Character with octal value ooo
# \xhh = Cuatavter with hex value hh
