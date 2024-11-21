#!/usr/bin/env python3
"""I can't remember but I think this is where documentation goes
https://pages.github.rpi.edu/kuruzj/website_introml_rpi/notebooks/08-intro-nlp/03-scikit-learn-text.html
Props to that person for making a tutorial"""

from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words(sentences, vocab=None):
    """Sentences - list of sentences to organize
    Vocab - words to use for analysis
    
    returns embeddings (# of sentences, # of features analyzed)
    features - a list of features used for embeddings"""

    # Who even knows how this actually works
    # Fail fast fail often
    # Until you're mentally broken
    vectorizer = CountVectorizer()

    # I *think* this is just fitting an already made model, yeah?
    #   Oh it is definitely not that.
    #   Pretty sure at least
    #       Idk what to do with vocab yet.
    vectorizer.fit(raw_documents=sentences)
    
    # Wtf does this do
    # Where the hecky becky am I supposed to use the vocab parameter
    # Seriously where
    #   Hey Ace
    #   This is one of those fun little things
    #   That would print something in a notebook
    #   But not in a basic python script
    print(vectorizer.vocabulary_)

    # Just try it Ace
    # Stop overthinking it
    #   We're going to the playground

    print(vectorizer)
    return(None, None)


    
