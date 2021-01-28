def get_num_sentences(doc: Doc):
    """Return number of sentences in the document
    """
    return len(list(doc.sents))