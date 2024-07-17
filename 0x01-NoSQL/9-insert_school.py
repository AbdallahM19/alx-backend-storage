#!/usr/bin/env python3
"""task 9 pymongo"""


def insert_school(mongo_collection, **kwargs):
    """
    a Python function that
    inserts a new document
    in a collection based on kwargs
    """
    list_collection = mongo_collection.insert_one(kwargs)
    return list_collection.inserted_id
