#!/usr/bin/env python3
"""task 12 pymongo"""

from pymongo import MongoClient


def log_stats(collection):
    """
    a Python script that provides
    some stats about Nginx
    logs stored in MongoDB.
    """
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log_stats(collection)
