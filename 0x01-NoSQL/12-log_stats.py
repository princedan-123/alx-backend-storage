#!/usr/bin/env python3
"""A python script that provides some stats from the log in MongoDB."""
from pymongo import MongoClient


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
print(
        f"{total_log} logs\nMethods:\n\tmethod GET: {doc_with_get}\
        \n\tmethod POST: {doc_with_post}\n\tmethod PUT: {doc_with_put}\
        \n\tmethod PATCH: {doc_with_patch}\n\tmethod DELETE: {doc_with_del}\
        \n{doc_with_status} status check\
        "
        )
