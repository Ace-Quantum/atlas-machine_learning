#!/usr/bin/env python3

"""provides stats about Nginx logs"""

from pymongo import MongoClient

def nginx_log_stats():
    """gets some stats"""

    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_log_stats()