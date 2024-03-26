#!/usr/bin/env python3
"""A python script that computes the average score of students in MongoDB."""


def top_students(mongo_collection):
    """A function that computes the average of student documents within
        a collection.
        Args: mongo_collection (collection object)
        Returns: modified documents with average score field
    """
    result = mongo_collection.aggregation(
            [
                {
                    "$group": {
                        "_id": "$name",
                        "averageScore": {"$avg": "$score"}
                        }
                    }
                ]
            )
    return result
