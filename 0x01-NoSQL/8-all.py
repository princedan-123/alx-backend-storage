#!/usr/bin/env python3
"""A python script that retrieves all documents from a MongoDB collection."""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
        A function that returns a list of documents in a collection.
        Args: mongo_collection (collection object).
        Return: a list of documents from the collection or an empty list
                if the collection is empty
    """
    result = []
    documents = mongo_collection.find()
    for document in documents:
        result.append(document)
    if len(result) == 0:
        return result
    return result
