import string
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    index_list=[]
    for i in range(len(doc_list)):
        doc = doc_list[i]
        translator = str.maketrans('', '', string.punctuation)
        cleaned_doc = doc.translate(translator)
        words = cleaned_doc.lower().split()
        if keyword in words:
            index_list.append(i)
    return index_list
