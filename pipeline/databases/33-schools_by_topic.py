#!/usr/bin/env python3

"""returns list of school having specific topic"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """This is taking a literal hour of set up"""
    query = {"topics": {"$in": [topic]}}

    schools = list(mongo_collection.find(query))

    return schools
