#!/usr/bin/env python3

"""lists all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Not sure what else to say"""
    documents = list(mongo_collection.find({}))

    return documents
