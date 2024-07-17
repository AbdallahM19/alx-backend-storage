#!/usr/bin/env python3
"""task 11 pymongo"""


def schools_by_topic(mongo_collection, topic):
    """
    a Python function that returns
    the list of school having
    a specific topic.
    """
    list_doc = []
    for i in mongo_collection.find({"topics": topic}):
        list_doc.append(i)
    return list_doc
