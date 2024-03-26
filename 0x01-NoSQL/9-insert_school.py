#!/usr/bin/env python3
"""A python script that inserts a document into a collection in MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """
        A function that adds a document to collection
        Args: mongo_collection (collection object)
              kwargs(a dictionary)
        Return: the insertion id of the document if successful
    """
    result = mongo_collection.insert_one(kwargs)
    return getattr(result, 'inserted_id', '')
