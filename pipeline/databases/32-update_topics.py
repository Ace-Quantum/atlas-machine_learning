#!/usr/bin/env python3

"""changes the topics of a school document"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Good golly this is a lot of files"""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result
