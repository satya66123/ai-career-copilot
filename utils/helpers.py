import re

def validate_input(text):
    if not text:
        return False

    if len(text) > 10000:
        return False

    # block dangerous patterns
    blacklist = ["DROP", "DELETE", "--", ";"]

    for word in blacklist:
        if word.lower() in text.lower():
            return False

    return True