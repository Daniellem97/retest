import re

# A regular expression pattern that matches a sequence of digits
pattern = r'\d+'

# Some sample text to match against
text = 'The answer is 42.'

# Use the search function from the re module to find the first match
match = re.search(pattern, text)

# Print the matched string
print(match.group())
