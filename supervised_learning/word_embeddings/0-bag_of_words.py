#!/usr/bin/env python3
"""I can't remember but I think this is where documentation goes
https://pages.github.rpi.edu/kuruzj/website_introml_rpi/notebooks/08-intro-nlp/03-scikit-learn-text.html
Props to that person for making a tutorial"""

from sklearn.feature_extraction.text import CountVectorizer as vectorizer

def bag_of_words(sentences, vocab=None):
    """Sentences - list of sentences to organize
    Vocab - words to use for analysis
    
    returns embeddings (# of sentences, # of features analyzed)
    features - a list of features used for embeddings"""

    # I *think* this is just fitting an already made model, yeah?
    vectorizer.fit(raw_documents=sentences)

    

    print(vectorizer)

    
