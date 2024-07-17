#!/usr/bin/env python3
"""task 101 pymongo"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    line_code = [
        {
            '$project': {
                'name': 1,  # (1) mean if name true
                'topics': 1,  # (1) mean if topics true
                'averageScore': {'$avg': '$topics.score'}
                # update and set avg
            }
        },
        {
            '$sort': {'averageScore': -1}
            # sorts the documents in descending order
        }
    ]
    return list(mongo_collection.aggregate(line_code))
