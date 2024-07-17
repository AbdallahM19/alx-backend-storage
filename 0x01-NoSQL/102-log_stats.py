#!/usr/bin/env python3
"""task 102 pymongo"""

from pymongo import MongoClient


def log_stats_2(collection):
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

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))


def log_stats_ips(collection):
    """
    Improve 12-log_stats.py by adding
    the top 10 of the most present IPs
    in the collection nginx of the database logs.
    """
    top_ips = collection.aggregate([
        {
            "$group": {"_id": "$ip", "count": {"$sum": 1}}
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ])
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log_stats_2(collection)
    log_stats_ips(collection)
