#!/usr/bin/env python3

"""Inserts a new document using kwargs"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Here's more docs"""
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
