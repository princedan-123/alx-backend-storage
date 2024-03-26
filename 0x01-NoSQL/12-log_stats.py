#!/usr/bin/env python3
"""A python script that provides some stats from the log in MongoDB."""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    total_log = client.logs.nginx.count_documents({})
    doc_with_get = client.logs.nginx.count_documents({"method": "GET"})
    doc_with_post = client.logs.nginx.count_documents({"method": "POST"})
    doc_with_put = client.logs.nginx.count_documents({"method": "PUT"})
    doc_with_patch = client.logs.nginx.count_documents({"method": "PATCH"})
    doc_with_del = client.logs.nginx.count_documents({"method": "DELETE"})
    doc_with_status = client.logs.nginx.count_documents({
        "method": "GET", "path": "/status"
        })
    print(f"{total_log} logs")
    print("Methods:")
    print(f"\tmethod GET: {doc_with_get}")
    print(f"\tmethod POST: {doc_with_post}")
    print(f"\tmethod PUT: {doc_with_put}")
    print(f"\tmethod PATCH: {doc_with_patch}")
    print(f"\tmethod DELETE: {doc_with_del}")
    print(f"{doc_with_status} status check")
    client.close()
