import string
word = input("Enter a word to see if it is a palindrome: ")

# using a for loop
n_word = (word.replace(" ", "")).lower()
for c in string.punctuation:
    n_word = n_word.replace(c, "")

start_index = 0 # change here!
end_index = -1
pal = 0

for letter in n_word:
    if n_word[start_index] != n_word[end_index]:
        pal = 0
        break
    else:
        pal = 1
    start_index += 1
    end_index -= 1

if pal == 1:
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))

# using slice
if n_word == n_word[::-1]:
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))