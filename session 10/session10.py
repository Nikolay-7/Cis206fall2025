import re

#1.checks if string contains only a-z, A-Z, 0-9
print("1:", bool(re.match(r'^[a-zA-Z0-9]+$', "ABCDEFabcdef123450")))
print("1:", bool(re.match(r'^[a-zA-Z0-9]+$', "*&%@#!}{")))

#2.matches "a" followed by zero or more b's
print("\n2:", bool(re.match(r'^ab*$', "ab")))
print("2:", bool(re.match(r'^ab*$', "abc")))
print("2:", bool(re.match(r'^ab*$', "a")))
print("2:", bool(re.match(r'^ab*$', "abb")))

#3.matches "a" followed by one or more b's
print("\n3:", bool(re.match(r'^ab+$', "ab")))
print("3:", bool(re.match(r'^ab+$', "abc")))
print("3:", bool(re.match(r'^ab+$', "a")))
print("3:", bool(re.match(r'^ab+$', "abb")))

#4.finds sequences of lowercase letters joined by an underscore
print("\n4:", re.findall(r'[a-z]+_[a-z]+', "aab_cbbbc"))
print("4:", re.findall(r'[a-z]+_[a-z]+', "aab_Abbbc"))
print("4:", re.findall(r'[a-z]+_[a-z]+', "Aaab_abbbc"))

#5.matches word at beginning of string
print("\n5:", re.match(r'^\w+', "The quick brown fox jumps over the lazy dog.").group())
print("5:", re.match(r'^\w+', " The quick brown fox jumps over the lazy dog."))

#6.matches word containing "z"
print("\n6:", re.findall(r'\w*z\w*', "The quick brown fox jumps over the lazy dog."))
print("6:", re.findall(r'\w*z\w*', "Python Exercises."))

#7.removev leading zeros from IP address
print("\n7:", re.sub(r'\b0+(\d)', r'\1', "216.08.094.196"))

#8.searches for literal strings within a string
text = 'The quick brown fox jumps over the lazy dog.'
print("\n8:", ['fox' if re.search('fox', text) else None,
              'dog' if re.search('dog', text) else None,
              'horse' if re.search('horse', text) else None])

#9.finds literal string in a string and its location
match = re.search('fox', 'The quick brown fox jumps over the lazy dog.')
print("\n9: Found at", match.start(), "-", match.end())

#10.replaces whitespaces with underscore and vice versa
print("\n10:", re.sub(r'\s', '_', "Regular Expressions"))
print("10:", re.sub(r'_', ' ', "Code_Examples"))

#11.extracts year, month, and date from URL
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
print("\n11: Year:", match.group(1), "Month:", match.group(2), "Date:", match.group(3))

#12.finds all words starting with "a" or "e" in string
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print("\n12:", re.findall(r'\b[ae]\w*', text, re.IGNORECASE))

#13.replaces space, comma, or dot with a colon
print("\n13:", re.sub(r'[ ,.]', ':', 'Python Exercises, PHP exercises.'))

#14.finds all words starting with "a" or "e" in a string
print("\n14:", re.findall(r'\b[ae]\w*', text, re.IGNORECASE))

#15.removes multiple spaces from a string
print("\n15:", re.sub(r'\s+', ' ', 'Python      Exercises'))
