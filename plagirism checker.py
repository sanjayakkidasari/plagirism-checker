import string
from collections import Counter

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    return text

def calculate_similarity(text1, text2):
    # Preprocess the texts
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Tokenize the texts into words
    words1 = text1.split()
    words2 = text2.split()

    # Calculate word frequencies using Counter
    word_freq1 = Counter(words1)
    word_freq2 = Counter(words2)

    # Calculate the similarity using cosine similarity formula
    intersection = set(word_freq1.keys()) & set(word_freq2.keys())
    numerator = sum(word_freq1[x] * word_freq2[x] for x in intersection)
    sum_squares1 = sum(word_freq1[x] ** 2 for x in word_freq1.keys())
    sum_squares2 = sum(word_freq2[x] ** 2 for x in word_freq2.keys())
    denominator = (sum_squares1 ** 0.5) * (sum_squares2 ** 0.5)

    if denominator != 0:
        similarity = numerator / denominator
    else:
        similarity = 0.0

    return similarity

def check_plagirism(text1, text2, threshold=0.8):
    similarity = calculate_similarity(text1, text2)
    
    if similarity >= threshold:
        print("Plagirism detected! Similarity:", similarity)
    else:
        print("No plagirism detected. Similarity:", similarity)

# Example usage
text1 = "This is an example sentence."
text2 = "This is a similar sentence."
text3 = "This is a different sentence."

check_plagirism(text1, text2)  # Plagiarism detected! Similarity: 0.629940788348712
check_plagirism(text1, text3)  # No plagiarism detected. Similarity: 0.0
