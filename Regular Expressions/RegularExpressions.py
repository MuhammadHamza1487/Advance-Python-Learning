import re
from re import split 

# Example:
# This Python code uses regular expressions to search for the word “portal” in the given string and then prints the start and end indices of the matched word within the string.
  
s = 'GeeksforGeeks: A computer science portal for geeks'
  
match = re.search(r'portal', s) 
  
print('Start Index:', match.start()) 
print('End Index:', match.end())

# 1. \ – Backslash_________________________________________________________________________________________________

# The first search (re.search(r'.', s)) matches any character, not just the period, while the second search (re.search(r'\.', s)) specifically looks for and matches the period character.

s = 'geeks.forgeeks'
  
# without using \ 
match = re.search(r'.', s) 
print(match) 
  
# using \ 
match = re.search(r'\.', s) 
print(match) 

# 2. [] – Square Brackets_________________________________________________________________________________________________

# In this code, you’re using regular expressions to find all the characters in the string that fall within the range of ‘a’ to ‘m’. The re.findall() function returns a list of all such characters. In the given string, the characters that match this pattern are: ‘c’, ‘k’, ‘b’, ‘f’, ‘j’, ‘e’, ‘h’, ‘l’, ‘d’, ‘g’.

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string) 
  
print(result)

# 3. ^ – Caret_________________________________________________________________________________________________

# This code uses regular expressions to check if a list of strings starts with “The”. If a string begins with “The,” it’s marked as “Matched” otherwise, it’s labeled as “Not matched”.

regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox'] 
for string in strings: 
    if re.match(regex, string): 
        print(f'Matched: {string}') 
    else: 
        print(f'Not matched: {string}') 

# 4. $ – Dollar_________________________________________________________________________________________________

# This code uses a regular expression to check if the string ends with “World!”. If a match is found, it prints “Match found!” otherwise, it prints “Match not found”.
  
string = "Hello World!"
pattern = r"World!$"
  
match = re.search(pattern, string) 
if match: 
    print("Match found!") 
else: 
    print("Match not found.") 

# 5. . – Dot_________________________________________________________________________________________________

# This code uses a regular expression to search for the pattern “brown.fox” within the string. The dot (.) in the pattern represents any character. If a match is found, it prints “Match found!” otherwise, it prints “Match not found”.


import re 
  
string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"
  
match = re.search(pattern, string) 
if match: 
    print("Match found!") 
else: 
    print("Match not found.") 

# 6 to 11_________________________________________________________________________________________________

# 6. | – Or
# Or symbol works as the or operator meaning it checks whether the pattern before or after the or symbol is present in the string or not. For example –  
# a|b will match any string that contains a or b such as acd, bcd, abcd, etc.

# ***********************

# 7. ? – Question Mark
# The question mark (?) is a quantifier in regular expressions that indicates that the preceding element should be matched zero or one time. It allows you to specify that the element is optional, meaning it may occur once or not at all. For example,
# ab?c will be matched for the string ac, acb, dabc but will not be matched for abbc because there are two b. Similarly, it will not be matched for abdc because b is not followed by c.

# ***********************

# 8.* – Star
# Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol. For example –  
# ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched for abdc because b is not followed by c.

# ***********************

# 9. + – Plus
# Plus (+) symbol matches one or more occurrences of the regex preceding the + symbol. For example –  
# ab+c will be matched for the string abc, abbc, dabc, but will not be matched for ac, abdc, because there is no b in ac and b, is not followed by c in abdc.

# ***********************

# 10. {m, n} – Braces
# Braces match any repetitions preceding regex from m to n both inclusive. For example –  
# a{2, 4} will be matched for the string aaab, baaaac, gaad, but will not be matched for strings like abc, bc because there is only one a or no a in both the cases.

# ***********************

# 11. (<regex>) – Group
# Group symbol is used to group sub-patterns. For example –  
# (a|b)cd will match for strings like acd, abcd, gacd, etc.

# _________________________________________________________________________________________________

# \A : Matches if the string begins with the given character.
# \b : Matches if the word begins or ends with the given character. \b(string) will check for the beginning of the word and (string)\b will check for the ending of the word.
# \B : It is the opposite of the \b i.e. the string should not start or end with the given regex.
# \d : Matches any decimal digit, this is equivalent to the set class [0-9].
# \D : Matches any non-digit character, this is equivalent to the set class [^0-9].
# \s : Matches any whitespace character.
# \S : Matches any non-whitespace character.
# \w : Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
# \W : Matches any non-alphanumeric character.
# \Z : Matches if the string ends with the given regex.



# 1. re.findall()_________________________________________________________________________________________________

# This code uses a regular expression (\d+) to find all the sequences of one or more digits in the given string. It searches for numeric values and stores them in a list. In this example, it finds and prints the numbers “123456789” and “987654321” from the input string.

string = """Hello my Number is 123456789 and 
            my friend's number is 987654321"""
regex = '\d+'
  
match = re.findall(regex, string) 
print(match) 

# 2. re.compile()_________________________________________________________________________________________________

# Example 2: The code uses a regular expression pattern [a-e] to find and list all lowercase letters from ‘a’ to ‘e’ in the input string “Aye, said Mr. Gibenson Stark”. The output will be ['e', 'a', 'd', 'b', 'e'], which are the matching characters.

p = re.compile('[a-e]') 
  
print(p.findall("Rigrex is in lahore")) 


# Example 2: Set class [\s,.] will match any whitespace character,  ‘,’,  or, ‘.’ . 
# The code uses regular expressions to find and list all single digits and sequences of digits in the given input strings. It finds single digits with \d and sequences of digits with \d+.

p = re.compile('\d') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
  
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 


# Example 3:
# The code uses regular expressions to find and list word characters, sequences of word characters, and non-word characters in input strings. It provides lists of the matched characters or sequences.
  
p = re.compile('\w') 
print(p.findall("He said * in some_lang.")) 
  
p = re.compile('\w+') 
print(p.findall("I went to him at 11 A.M., he said *** in some_language.")) 
  
p = re.compile('\W') 
print(p.findall("he said *** in some_language.")) 


# Example 4:
# The code uses a regular expression pattern ‘ab*’ to find and list all occurrences of ‘ab’ followed by zero or more ‘b’ characters in the input string “ababbaabbb”. It returns the following list of matches: [‘ab’, ‘abb’, ‘abbb’].

p = re.compile('ab*') 
print(p.findall("ababbaabbb")) 

# 3. re.split() _________________________________________________________________________________________________

# Example 1:
# Splits a string using non-word characters and spaces as delimiters, returning words: ['Words', 'words', 'Words']. Considers apostrophes as non-word characters: ['Word', 's', 'words', 'Words']. Splits using non-word characters and digits: ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']. Splits using digits as the delimiter: ['On ', 'th Jan ', ', at ', ':', ' AM'].
  
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 


# Example 2:
# First statement splits the string at the first occurrence of one or more digits: ['On ', 'th Jan 2016, at 11:02 AM']. second splits the string using lowercase letters a to f as delimiters, case-insensitive: ['', 'y, ', 'oy oh ', 'oy, ', 'ome here']. Third splits the string using lowercase letters a to f as delimiters, case-sensitive: ['', 'ey, Boy oh ', 'oy, ', 'ome here'].

print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE)) 
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here')) 

# 4. re.sub() _________________________________________________________________________________________________

# Example 1:
# First statement replaces all occurrences of ‘ub’ with ‘~*’ (case-insensitive): 'S~*ject has ~*er booked already'.
# Second statement replaces all occurrences of ‘ub’ with ‘~*’ (case-sensitive): 'S~*ject has Uber booked already'.
# Third statement replaces the first occurrence of ‘ub’ with ‘~*’ (case-insensitive): 'S~*ject has Uber booked already'.
# Fourth replaces ‘AND’ with ‘ & ‘ (case-insensitive): 'Baked Beans & Spam'.

import re 
print(re.sub('ub', '~*', 'Subject has Uber booked already',  
             flags=re.IGNORECASE)) 
print(re.sub('ub', '~*', 'Subject has Uber booked already')) 
print(re.sub('ub', '~*', 'Subject has Uber booked already', 
             count=1, flags=re.IGNORECASE)) 
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',  
             flags=re.IGNORECASE)) 


# 5. re.subn() _________________________________________________________________________________________________

# subn() is similar to sub() in all ways, except in its way of providing output. It returns a tuple with a count of the total of replacement and the new string rather than just the string. 

# Example:
# re.subn() replaces all occurrences of a pattern in a string and returns a tuple with the modified string and the count of substitutions made. It’s useful for both case-sensitive and case-insensitive substitutions.

print(re.subn('ub', '~*', 'Subject has Uber booked already')) 
  
t = re.subn('ub', '~*', 'Subject has Uber booked already', 
            flags=re.IGNORECASE) 
print(t) 
print(len(t)) 
print(t[0]) 

# 6. re.escape() _________________________________________________________________________________________________

# re.escape() is used to escape special characters in a string, making it safe to be used as a pattern in regular expressions. It ensures that any characters with special meanings in regular expressions are treated as literal characters.

print(re.escape("This is Awesome even 1 AM")) 
print(re.escape("I Asked what is this [a-9], he said \t ^WoW")) 

# 7. re.search()  _________________________________________________________________________________________________

# Example: Searching for an occurrence of the pattern
# This code uses a regular expression to search for a pattern in the given string. If a match is found, it extracts and prints the matched portions of the string.
# In this specific example, it searches for a pattern that consists of a month (letters) followed by a day (digits) in the input string “I was born on June 24”. If a match is found, it prints the full match, the month, and the day.

regex = r"([a-zA-Z]+) (\d+)"
  
match = re.search(regex, "I was born on June 24") 
if match != None: 
    print ("Match at index %s, %s" % (match.start(), match.end())) 
    print ("Full match: %s" % (match.group(0))) 
    print ("Month: %s" % (match.group(1))) 
    print ("Day: %s" % (match.group(2))) 
  
else: 
    print ("The regex pattern does not match.") 

#  _________________________________________________________________________________________________