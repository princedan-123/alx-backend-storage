#!/usr/bin/env python3
"""A python script that list schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
        A function that returns the list of school having a specific topic
        Args: mongo_collection(collection object) pymongo collection object
              topic(string) will be topic searched
        Return: A list of schools having the specified topic.
    """
    return list(mongo_collection.find({'topics': topic}))
