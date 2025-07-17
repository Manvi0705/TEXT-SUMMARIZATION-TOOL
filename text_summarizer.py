"""
Text Summarization Tool - CODTECH Internship Task 1
Author: Manvi Sharma
Description: This Python script summarizes lengthy articles using Natural Language Processing techniques.
Deliverable: A Python script showcasing input text and concise summaries.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download NLTK data files (only first time)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, summary_ratio=0.3):
    """
    Summarizes the given text using a frequency-based approach.
    :param text: (str) The input lengthy article or paragraph.
    :param summary_ratio: (float) Percentage of sentences to keep in summary.
    :return: (str) Concise summarized text.
    """
    
    # Tokenize words & sentences
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)

    word_frequencies = {}
    for word in words:
        word = word.lower()
        if word not in stop_words and word not in punctuation:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Find maximum frequency for normalization
    max_frequency = max(word_frequencies.values())

    # Normalize frequencies
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_frequency

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Select top sentences for the summary
    select_length = max(1, int(len(sentences) * summary_ratio))
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:select_length]

    # Return the summary
    return ' '.join(summarized_sentences)


if __name__ == "__main__":
    print("\n==== TEXT SUMMARIZATION TOOL ====")
    input_text = input("\nEnter the article or text to summarize:\n")
    summary = summarize_text(input_text)
    print("\n==== GENERATED SUMMARY ====")
    print(summary)
    print("\nTask Completed Successfully ✅")
