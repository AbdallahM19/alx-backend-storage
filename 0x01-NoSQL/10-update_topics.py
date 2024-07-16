#!/usr/bin/env python3
"""task 9 pymongo"""


def update_topics(mongo_collection, name, topics):
    """
    Write a Python function that changes all topics of
    a school document based on the name.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
