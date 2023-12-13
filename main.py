from string import ascii_letters


alphabet = list(ascii_letters)
word = input("Input your word: ")
key_word = input("Input your key word: ")
key_message = (key_word * 10)[:len(word)]
new_word = ""
for i in range(len(word)):
    letter_index_message = alphabet.index(word[i])
    letter_index_key = alphabet.index(key_message[i])
    letter_index = letter_index_message + letter_index_key

    if letter_index > len(alphabet):
        letter_index -= len(alphabet)

    new_word += alphabet[letter_index]

print(f"Зашифрованное сообщение: {new_word}")










