def get_num_syllables(doc: Doc, min_syllables: int = 1):
    import syllapy
    """Return number of words in the document.
    Filters punctuation and words that start with apostrophe (aka contractions)
    """
    text = (word for word in doc if not word.is_punct and "'" not in word.text)
    syllables_per_word = tuple(syllapy.count(word.text) for word in text)
    return sum(c for c in syllables_per_word if c >= min_syllables)