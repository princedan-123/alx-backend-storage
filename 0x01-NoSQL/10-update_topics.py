#!/usr/bin/env python3
"""A python script that updates a document in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """ 
        A function that changes all topics of a school
        document based on the name
        Args: mongo_collection (collection object)
              name (string) school name to update
              topic (list) list of topics approached in the school
        Return: None
    """
    filter_object = {'name': name}
    update_field = {'$set': {'topics': topics}}
    mongo_collection.update_many(filter_object, update_field)
