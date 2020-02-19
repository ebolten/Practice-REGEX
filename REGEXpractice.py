import re
# --------------------------------------- NOTES ON REGEX ----------------------------------------------------------------------------------------------------
# REGEX FUNCTIONS
# findall --> returns a list containing all matches
# search --> returns a Match object if there is a match anywhere in the string
# split --> returns a list where the string has been split at each match
# sub --> replaces one or many matches with a string

# REGEX METACHARACTERS
# [] --> A set of characters ("[a-m]")	
# \ --> Signals a special sequence (can also be used to escape special characters) ("\d")
# . --> Any character (except newline character) ("he..o")
# ^ --> Starts with ("^hello")
# $ --> Ends with ("world$")
# * --> Zero or more occurrences ("aix*")
# + --> One or more occurrences ("aix+")
# {} --> Exactly the specified number of occurrences ("al{2}")
# | --> Either or ("falls|stays")

# REGEX SPECIAL SEQUENCES
# \A --> returns a match if the specified characters are at the beginning of the string ("\AThe")
# \b --> returns a match where the specified characters are at the beginning or at the end of a word (r"\bain")  (r"ain\b")
# \B --> returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (r"\Bain")  (r"ain\B")
# \d --> returns a match where the string contains digits (numbers from 0-9) ("\d")
# \D --> returns a match where the string DOES NOT contain digits ("\D")
# \s --> returns a match where the string contains a white space character ("\s")
# \S --> returns a match where the string DOES NOT contain a white space character ("\S")
# \w --> returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) ("\w")
# \W --> returns a match where the string DOES NOT contain any word characters ("\W")
# \Z --> returns a match if the specified characters are at the end of the string ("Spain\Z")

# REGEX SETS
# [arn] --> returns a match where one of the specified characters (a, r, or n) are present	
# [a-n] --> returns a match for any lower case character, alphabetically between a and n	
# [^arn] --> returns a match for any character EXCEPT a, r, and n	
# [0123] --> returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9] --> returns a match for any digit between 0 and 9	
# [0-5][0-9] --> returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z] --> returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+] --> in sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# --------------------------------------- NOTES ON REGEX ----------------------------------------------------------------------------------------------------
print("\n")
# begin regex practices
# using the findall() method
# line = "Your hair is winter fire / January embers / My heart burns there, too."
# all_matches = re.findall("er", line) # finding the number of matches ("ai") in string, returns list
# print("Original Line: " + line + "\nThere are " + str(len(all_matches)) + " matches: " + str(all_matches) + "\n")


# using the sub() method
line = "John makes pancakes, he always makes pancakes on Monday."
replacement = re.sub("pancakes","soup",line) # replacing any instance of the match (pancakes)
print("Original Line: " + line + "\nNew Line: " + replacement + "\n")


# splitting and joining strings and arrays
line = "milk, coffee, apples, pepper, cereal"
split_line = re.split(", ", line) # returns a list where the string has been split at each match (", ")
print("Originial List: " + line + "\nNew List: " + str(split_line) + "\n")


# removing digits from a string
line = "h3el1lo w0orl6d"
str_line = re.sub(r'[0-9]+',"",line) # removing any digits form the string and replacing with ""
print("Original Line: " + line + "\nNew Line: " + str_line + "\n")


# finding if a line starts and ends with specified characters
line = "The rain in Spain"
the_spain = re.search("^The.*Spain$",line) # will search for strings at beginning ("^The") and end ("Spain$")
if the_spain: # if match is valid
    print("The line \"" + line + "\" begins with \"The\" and ends with \"Spain.\"\n")
else:
    print("The line \"" + line + "\" does not begin with \"The\" and does not end with \"Spain.\"\n")
# end regex practices
print("\n\n")







