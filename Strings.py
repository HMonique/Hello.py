word = input("Enter a word: ")  
print("Length of word:", len(word))
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())

letter = input("Enter a letter: ")
print(f"'{letter}' appears {word.count(letter)} times in '{word}'")

substring = input("Enter a substring: ")
print(f"'{substring}' appears {word.count(substring)} times in '{word}'")

reverse_word = word[::-1]
print("Reverse:", reverse_word)

start_index = int(input("Enter a starting index: "))
end_index = int(input("Enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word:", sliced_word)

char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter a replacement character: ")
new_word = word.replace(char_to_replace, replacement_char)
print("Replaced:", new_word)

second_word = input("Enter a second word: ")
concatenated_word = word + second_word
print("Concatenated:", concatenated_word)

is_palindrome = word == reverse_word
is_valid_identifier = word.isidentifier()

print("Is palindrome:", is_palindrome)
print("Is valid Python identifier?", is_valid_identifier)