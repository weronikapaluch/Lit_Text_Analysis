# First let's import math

import math

doc = open("Melanctha.txt")

# Tokenize the documents and create a vocubulary
def tokenize(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return[word.strip(punctuation) for word in text.lower().split()]


vocabulary = sorted({word for word in tokenize(doc)})

def calculate_tf(document, vocabulary):
    tokens = tokenize(document)
    tf_vector = [tokens.count(word)/len(tokens) for word in vocabulary]
    return tf_vector

def calculate_idf(document, vocabulary):
    num_documents = len(document)
    idf_vector = []
    for word in vocabulary:
        doc_count = sum(1 for word in document if word in tokenize(doc))
        idf = math.log(num_documents/doc_count)
        idf_vector.append(idf)
    return idf_vector