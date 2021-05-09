from uuid import uuid4
import random


# sorter helper function
def sorter(length=7):
    end = random.choice(range(33))
    start = end - length
    if start < 0:
        start, end = sorter()
    return start, end


# function for generating a reset token
def generate_slug():
    slug = uuid4().hex
    start, end = sorter()
    return slug[start:end]
