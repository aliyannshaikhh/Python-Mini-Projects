str = "Hello! I have a cat. My cat has blue eyes. Its color is white."

def word_replacer():
    print(str)
    word_to_replace = input("Which word you want to replace in the above string? ")
    word_replacement = input("Enter your desired replacer: ")
    print(str.replace(word_to_replace, word_replacement))

word_replacer()