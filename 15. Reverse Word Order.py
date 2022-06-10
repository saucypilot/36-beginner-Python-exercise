userInput = input("Please enter a sentence or a long string of multiple words.\n")
sentence = userInput.split(" ")
reverse_sentence = " ".join(reversed(sentence))
print(reverse_sentence)
