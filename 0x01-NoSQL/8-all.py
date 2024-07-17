#!/usr/bin/env python3
"""task 8 pymongo"""


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    list_collection = [i for i in mongo_collection.find()]
    return list_collection
