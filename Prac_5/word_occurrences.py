"""
Word Occurrences
Estimate: 20 minutes
Actual:   16 minutes
"""

word_counts = {}

text = input("Text: ").lower()
text_words = text.split()
for word in text_words:
    try:
        word_counts[word] = word_counts[word] + 1
    except KeyError:
        word_counts[word] = 1
for word in sorted(word_counts):
    print(f"{word:{13}} : {word_counts[word]}")
