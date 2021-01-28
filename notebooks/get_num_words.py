def get_num_words(doc: Doc):
    """Return number of words in the document.
    Filters punctuation and words that start with apostrophe (aka contractions)
    """
    filtered_words = [
        word for word in doc if not word.is_punct and "'" not in word.text
    ]
    return len(filtered_words)