sentence = "the sky is blue and the grass is green"
words = sentence.split()
unique_words = set(words)
has_duplicates = len(words) != len(unique_words)
print("Has duplicates:", has_duplicates)
